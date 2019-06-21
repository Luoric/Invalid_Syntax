quiz = float(raw_input("Please enter the score of Quiz: "))
project = float(raw_input("Please enter the score of Project: "))
final = float(raw_input("Please enter the score of Final: "))

average = (quiz + project + final)/3.
print (average)

average_2 = average - int(average)
if average_2 > 0.5:
    averageRounded = int(average) + 1
else: averageRounded = int(average)

print(averageRounded)

if final < 60:
    print ("You Failed")
else :
    if averageRounded >= 90:
        print ("You Scored an A")
    elif averageRounded >= 80:
        print ("You Scored an B")
    elif averageRounded >= 70:
        print ("You Scored an C")
    elif averageRounded >= 60:
        print ("You Scored an D")
    elif averageRounded < 60:
        print ("You Failed")
