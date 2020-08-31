# Python code to
# demonstrate readlines()

# file1 = open(r'C:\Users\ssajpa\Documents\SAS Technology\Customer\SWIIFT\swift-to-kafka-master\samples\mt101\mt101_1.txt', 'r', encoding="utf-8")

file1 = open(r'C:\Users\ssajpa\Documents\SAS Technology\Customer\SWIIFT\xx.dat', 'r', encoding="utf-8")

Lines = file1.readlines()

# Splitting at ':'
#Message = Lines.replace(r"\n", "\t")

#print(Lines.split('$'))
for line in Lines:

# print( str(Lines)[2:-2] )
    print(line)

file1.close()

