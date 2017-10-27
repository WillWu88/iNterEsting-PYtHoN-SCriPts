def ImportMessage(encrypted_File_Name):
    '''pull the chars out from the encrypted file'''
    char_List = []
    with open(encrypted_File_Name,'r') as encrypted_message:
        char_List = encrypted_message.readline()
        char_List = [x.strip() for x in char_List]
    return char_List

def ImportKey(decryption_Key_File):
    key_list = []
    with open(decryption_Key_File, 'r') as decryption_key:
        key_list = decryption_key.readline()
        key_list = [x.remove(',') for ]

#print("The unencrypted message is"+str(ImportMessage('encrypted.txt')))
