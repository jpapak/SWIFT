# Python program to count the

file1 = open(r'C:\Users\ssajpa\Documents\SAS Technology\Customer\SWIIFT\xx.dat', 'r', encoding="utf-8")
#file1 = open(r'C:\Users\ssajpa\Documents\SAS Technology\Customer\SWIIFT\5m.dat', 'r', encoding="utf-8")

# Reading from file
Content = file1.read()                  # Read the file contents
content1 = Content.replace("\n", "")    # Read the file contents
cSwiftMessages = content1.split("$")    # Read the file contents
Counter= 0
for i in cSwiftMessages:
    if i:
        print(i)
        Counter +=1
print(Counter)
