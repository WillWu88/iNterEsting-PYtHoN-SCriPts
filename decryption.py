#decrypting file
#takes two files, a decrp
import math
import decryptionKey
import encrypted

decrypted = ""

for num in range(len(decryptionKey.key)):
    decrypted += chr(decryptionKey.key[num]+ord(encrypted.key[num]))

print(decrypted)
#print(shift_key)