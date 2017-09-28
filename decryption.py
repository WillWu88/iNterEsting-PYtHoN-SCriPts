#decrypting file
#takes two files, a decrp
filename = "encrypted.txt"
file_to_decry = open(filename, "r")

filename2 = "decryptionKey.txt"
keyFile = open(filename2, "r")

encrypted_File = []
shift_key = []

for chars in file_to_decry:
    encrypted_File.insert(len(encrypted_File), chars)

#"decomma" the string from key file for the type inversion

#work on this tmr, still buggy
pointer = 0
while True:
    char = keyFile.read(1)
    if not char:
        break
    elif (char==','):
        pointer+=1
    else:
        shift_key.insert(pointer, int(char))

print(shift_key)