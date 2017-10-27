import random
# using python 3 syntax
file_name = input("Filename to be encrypted > ") + ".txt"

# read and load file
file = open(file_name, "r")
message = file.readline()
print("the unencrypted version is: " + message)

# encrytion begins
# temp arry holds message
str_array = []
for letters in message:
    str_array.insert(len(str_array), letters)
#print ("The array:"+str(str_array))

# holds encrypted message
encrypted_array = []

# declaring temp variables to be used later
decryptKey = []
'''holds the decryption keys, the difference between the actuall
value and the real value'''

# generate a random number, plug the number into the decryption key
# a is always less than the ascii num of char
# the encrypted message is the differnece a and char
for chars in str_array:
    a = random.randint(0, ord(chars))
    b = ord(chars) - a
    test = b != 10
    if test:
        encrypted_array.insert(len(encrypted_array), chr(b))
        decryptKey.append(a)
    else:
        encrypted_array.insert(len(encrypted_array), chr(b + 1))
        decryptKey.append(a + 1)

with open("encrypted.txt", "w+") as output_file:
    for chars in encrypted_array:
        output_file.write(chars)

with open("decryptionKey.txt", "w+") as output_file:
    for nums in decryptKey:
        output_file.write(str(nums) + ",")
