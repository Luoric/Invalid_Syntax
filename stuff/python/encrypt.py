

working = True

def printMenu():
    print('''+-------------------+''')
    print('''+Type "e" to encrypt+''')
    print('''+Type "d" to decrypt+''')
    print('''+Type "q" to quit   +''')
    print('''+-------------------+''')

def int_input(input):
    user_input = raw_input(input)
    return int(user_input)

def cipher(message, mode, key):
    if mode == "d":
        key = - key
    output =""
    for char in message:
        output += chr((ord(char) + key) % 128)
    return output

while working == True:
    printMenu()
    mode = raw_input("Please enter your choice: ")
    if mode == "q":
        working = False
    elif mode == "e":
        message = raw_input("Message: ")
        key = int_input("key: ")
        print(cipher(message, "e", key))
    elif mode == "d":
        message = raw_input("Message: ")
        key = int_input("key: ")
        print(cipher(message, "d", key))
