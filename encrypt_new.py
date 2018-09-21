#file name is default: messsage.txt

try:
    file_name = 'message.txt'
    file = open(file_name, "r")
    message = file.readline()
except:
    message = ''
    print('no file found')

encrypted = []

def constant_shift(shift):
    for char in message:
        encrypted.append(chr(ord(char) + shift))
