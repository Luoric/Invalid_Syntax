yearBorn = int(raw_input("Please enter the year your were born: "))
monthBorn = int(raw_input("Please enter the month your were born: "))
dayBorn = int(raw_input("Please enter the day your were born: "))

if monthBorn == 1:
    monthInDays = 31
elif monthBorn == 2:
    monthInDays = 28 + 31
elif monthBorn == 3:
    monthInDays = 31 + 31 + 28
elif monthBorn == 4:
    monthInDays = 31 + 31 + 28 + 30
elif monthBorn == 5:
    monthInDays = 31 + 31 + 28 + 30 + 31
elif monthBorn == 6:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30
elif monthBorn == 7:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30 + 31
elif monthBorn == 8:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30 + 31 + 31
elif monthBorn == 9:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30 + 31 + 31 + 30
elif monthBorn == 10:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30 + 31 + 31 + 30 + 31
elif monthBorn == 11:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
elif monthBorn == 12:
    monthInDays = 31 + 31 + 28 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31

timeNow = 6 * 30 + 10
timeToBirthday = (timeNow - (monthInDays + dayBorn))
birthday = monthInDays + dayBorn
if birthday > timeNow :
    print(str(timeToBirthday) + " days to birthday")
elif birthday < timeNow :
    timeToBirthday = (365 - timeNow) + (birthday)
    print(str(timeToBirthday) + " days to birthday")
