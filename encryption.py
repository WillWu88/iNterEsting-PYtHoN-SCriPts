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
    a = random.randint(0, 127)
    encrypted_array.insert(len(encrypted_array), chr(a))
    b = ord(chars) - a
    decryptKey.insert(len(decryptKey), b)

with open("encrypted.txt", "w+") as output_file:
    for chars in encrypted_array:
        output_file.write(chars)

with open("decryptionKey.txt", "w+") as output_file:
    output_file.write(str(decryptKey))
