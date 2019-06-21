def int_input(input):
    user_input = raw_input(input)
    return int(user_input)


word = raw_input("enter stuff: ")
amount = int_input("enter number: ")

if amount == 1:
    print(str(amount)+ " " + word)
elif amount >1:
    if word[-3:] == "ife":
        word = word[:-3] + "ives"
        print(str(amount)+ " " + word )
    elif word[-2:] == "sh" or word[-2:] == "ch":
        word = word + "es"
        print(str(amount)+ " " + word )
    elif word[-2:] == "us":
        word = word[:-2] + "i"
        print(str(amount)+ " " + word )
    elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
        word = word + "s"
        print(str(amount)+ " " + word )
    elif word[-1:] == "y":
        word = word[:-1] + "ies"
        print(str(amount)+ " " + word )
    else :
        word = word + "s"
        print(str(amount)+ " " + word )
