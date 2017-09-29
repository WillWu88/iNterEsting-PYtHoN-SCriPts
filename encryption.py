import random
#using python 3 syntax
filename = input("Filename to be encrypted > ")+".txt"

#read and load file
file = open(filename, "r")
message = file.readline()
print("the unencrypted version is:"+message)

#encrytion begins
# temp arry holds message
str_array = []
for letters in message:
    str_array.insert(len(str_array), letters)
#print ("The array:"+str(str_array))

#holds encrypted message
encrypted_array = []

#declaring temp variables to be used later
decryptKey = []
'''holds the decryption keys, the difference between the actuall
value and the real value'''

for chars in str_array:
    a = random.randint(0, ord(chars))
    b = ord(chars) - a
    encrypted_array.insert(len(encrypted_array), chr(b))
    decryptKey.insert(len(decryptKey), a)

with open("encrypted.py", "w+") as output_file:
    output_file.write("key="+str(encrypted_array))

with open("decryptionKey.py", "w+") as output_file:
    output_file.write("key="+str(decryptKey))

