import random
#using python 3 syntax
filename = input("Filename to be encrypted > ")+".txt"

#read and load file
file = open(filename,"r")
message = file.readline()
print ("the unencrypted version is:"+message)

#encrytion begins
str_array = []
for letters in message:
    str_array.insert(len(str_array),letters)
print ("The array:"+str(str_array))

#declaring temp variables to be used later
decryptKey = [] #holds the decryption keys, the difference between the actuall value and the real value
a = 0

for letters in str_array:
    shift = random.randrange(127)
    print (shift)
    break
