#PROGRAM 1

YEAR = int(input("ENTER ANY YEAR :- "))
if (YEAR%100==0 and YEAR%400==0) or (YEAR%100==0 and YEAR%4==0):
    print("THIS IS A LEAP YEAR ")
else:
    print("{} IS NOT A LEAP YEAR".format(YEAR))


#PROGRAM 2

YEAR= int(input("ENTER ANY YEAR :- "))
if YEAR%100==0:
    if YEAR%400==0:
        print("THIS YEAR IS A LEAP YEAR")
    else:
        print("THIS YEAR IS NOT A LEAP YEAR")
else:
    if YEAR%4==0:
        print("THIS YEAR IS A LEAP YEAR")
    else:
        print("THIS YEAR IS NOT A LEAP YEAR")