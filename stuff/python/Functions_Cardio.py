import random
def int_input(input):
    user_input = raw_input(input)
    return int(user_input)

def longest_word(string1, string2, string3):
    maxSoFar = 0
    longestWord = ''
    while len(string2) > maxSoFar or len(string3) > maxSoFar or len(string1) > maxSoFar:
        if len(string2) > maxSoFar:
            maxSoFar = len(string2)
            longestWord = string2
        if len(string3) > maxSoFar:
            maxSoFar = len(string3)
            longestWord = string3
        if len(string1) > maxSoFar:
            maxSoFar = len(string1)
            longestWord = string1
        return longestWord

def reverse_string(string):
    output = ''
    for char in string:
        output = char + output
    return output

def sum_to_n(number):
    if number%2 == 0:
        answer = (1 + number) * (number/2)
    else:
        answer = (1 + (number -1)) * ((number-1)/2) + number
    return answer

#number = int_input("enter number: ")
#print sum_to_n(number)

def is_triangle(s1,s2,s3):
    if((s1 + s2)> s3 and (s1 + s3) > s2 and (s2 + s3) > s1):
        answer = True
    else:
        answer = False
    return answer

#s1 = int_input("enter number: ")
#s2 = int_input("enter number: ")
#s3 = int_input("enter number: ")

def roll_dice(number):
    dices = range(number)
    answer = 0
    for i in dices:
        answer = answer + random.randint(1,6)
    return answer

#number = int_input("number of time to roll dice: ")
#print(roll_dice(number))

def isPrime(number):
    if number%2 == 0 or number%3 ==0 or number%7 == 0:
        if number ==2 or number ==3 or number ==5 or number ==7:
            result = True
        else: result = False
    else:
        result = True
    return result
#number = int_input("enter number: ")
#print(isPrime(number))

def snake_case(camelCase):
    camelCase =camelCase.replace('A',"_a")
    camelCase =camelCase.replace('B',"_b")
    camelCase =camelCase.replace('C',"_c")
    camelCase =camelCase.replace('D',"_d")
    camelCase =camelCase.replace('E',"_e")
    camelCase =camelCase.replace('F',"_f")
    camelCase =camelCase.replace('G',"_g")
    camelCase =camelCase.replace('H',"_h")
    camelCase =camelCase.replace('I',"_i")
    camelCase =camelCase.replace('J',"_j")
    camelCase =camelCase.replace('K',"_k")
    camelCase =camelCase.replace('L',"_l")
    camelCase =camelCase.replace('M',"_m")
    camelCase =camelCase.replace('N',"_n")
    camelCase =camelCase.replace('O',"_o")
    camelCase =camelCase.replace('P',"_p")
    camelCase =camelCase.replace('Q',"_q")
    camelCase =camelCase.replace('R',"_r")
    camelCase =camelCase.replace('S',"_s")
    camelCase =camelCase.replace('T',"_t")
    camelCase =camelCase.replace('U',"_u")
    camelCase =camelCase.replace('V',"_v")
    camelCase =camelCase.replace('W',"_w")
    camelCase =camelCase.replace('X',"_x")
    camelCase =camelCase.replace('Y',"_y")
    camelCase =camelCase.replace('Z',"_z")
    return camelCase

#user_input = raw_input("Enter in camel case: ")
#print(snake_case(user_input))


def get_number_input(user_input):
    stuff = raw_input("Enter in a number: ")
