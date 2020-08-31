# swift-to-kafka

Ingests swift messages from files in a directory and publishes them to a kafka server

# Usage
`python swift-to-kafka.py --host sasserver.demo.sas.com --inputdir pathToDirectory`

## Arguments

    --host The hostname, or IP, of the kafka server. Defaults to localhost

    --port | -p The port of the kafka server to send the messages to. Defaults to 9092 (Is this the correct default?)

    --inputdir | -i The directory to process files from

    --outputdir | -o The directory to move processed files to. Defaults to "processed" within the inputdir

    --loglevel | -l The verbosity of the log messages. Defaults to INFO

    --logfile | -f The file to write log messages to. Defaults to stdout

# Getting Started
This script can be run from any host that can connect to the kafka server.
To manage prerequisites, use pipenv to establish a virtual environment and install the necessary dependencies

    # install pipenv, if you don't already have it
    pip install pipenv

    # establish the virtual environment, with the required python packages
    pipenv install

    # enter the virtual environment
    pipenv shell

# Accessing Kafka Consumer
Linux command line prompt:

`/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server sasserver.demo.sas.com:9092 --topic nameOfTopic --from-beginning`