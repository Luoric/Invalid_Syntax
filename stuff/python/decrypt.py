message = raw_input("Please enter the message: ")
import random
output = ""
key = range (10)


for i in key:
    output = ""
    for char in message:
        num = int(ord(char) - key[i])
        char = str(chr(num))
        output = output + char
    print(output)
