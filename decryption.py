#decrypting file
#takes two files, a decrp
filename = "encrypted.txt"
file_to_decry = open(filename, "r")

filename = "decryptionKey.txt"
keyFile = open(filename, "r")

encrypted_File = []
shift_key = []

for chars in file_to_decry:
    encrypted_File.insert(len(encrypted_File), chars)

for chars in keyFile:
    shift_key.insert(len(shift_key), chars)

