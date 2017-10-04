#decrypting file
#takes two files, a decrp
import decryptionKey
import encrypted

decrypted = ""

for num in range(len(decryptionKey.key)):
    decrypted += chr(decryptionKey.key[num]+ord(encrypted.key[num]))

print(decrypted)

#remember to go back to rewrite the previous version