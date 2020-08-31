from confluent_kafka import Producer
from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic
import time
import os
import shutil
import sys
import argparse
from pathlib import Path
import logging

DELAY = 0.3 # Delays for 0.3 seconds
logger = logging.getLogger(__name__)

def parse_arguments():
    """
    The function parse_argument parses argument from command line.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=False, default="localhost")
    parser.add_argument("-p", "--port", required=False, default="9092")
    parser.add_argument("-i", "--inputdir", required=True, type=Path)
    parser.add_argument("-o", "--outputdir", required=False, type=Path, default="processed")
    parser.add_argument("-t", "--topic", required=False, default="messages")
    parser.add_argument("-l", "--loglevel", required=False, default="INFO")
    parser.add_argument("-f", "--logfile", required=False, default="")
    
    args = parser.parse_args()
    return args

def delivery_report(err, msg):
    """
    Called once for each message produced to indicate delivery results.
    Triggered by poll() or flush().
    """
    if err is not None:
        logging.error('Message delivery failed: {}'.format(err))
    else: 
        logging.info('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

###########################################################

if __name__ == "__main__":
    # print out the standard commands to be run
    print('The delay is: ', DELAY, 'seconds')
    print(' ')
    print('Please be paitent while your data is being loaded to Kafka.')
    print('Run the Kafka Consumer in another session if you want to watch the data being loaded.')
    print('Check logfile for logging report.')
    print('Press CTRL+C to stop processing messages in directory.')
    print(' ')

    args = parse_arguments()
    bootstrap_servers = args.host + ':' + args.port

    LOGLEVEL = os.environ.get('LOGLEVEL', args.loglevel).upper()
    logging.basicConfig(filename=args.logfile, filemode='w', level= LOGLEVEL, format='%(name)s - %(levelname)s - %(message)s')

    p = Producer({'bootstrap.servers': bootstrap_servers })
    while True:
        if args.inputdir.exists():
            for filename in os.listdir(args.inputdir):
                # try to process files as they are dropped into directory, otherwise process on second pass
                try:
                    with open(os.path.join(args.inputdir, filename), 'r') as f:
                        p.poll(0)
                        logging.info("Producing message(s): " + filename)

                        Content = f.read()                      # Read the file contents
                        content1 = Content.replace("\n", "")    # Replace all the newlines in the file
                        cSwiftMessages = content1.split("$")    # Split the content into individual messages

                        for i in cSwiftMessages:
                            if i:
                                p.produce(args.topic, i, callback=delivery_report)

                        time.sleep(DELAY)

                    f.close()
                    # Create 'processed' directory and move processed files to this directory
                    if not os.path.exists('processed'):
                        logging.info("Created 'processed' folder.")
                        os.makedirs('processed')
                    dest = shutil.move(os.path.join(args.inputdir, filename), os.path.join(os.getcwd(), 'processed'))
                    logging.info("Moved file " + filename + " to 'processed' folder.")
                except:
                    logging.warning("Unable to process file on first pass: " + filename)
                    if not os.path.isfile(os.path.join(args.inputdir, filename)):
                        dest = shutil.move(os.path.join(args.inputdir, filename), os.path.join(os.getcwd(), 'processed'))
                        logging.info("Moved directory " + filename + " to 'processed' folder.")
                    continue
        p.flush()

def Extract Message():
