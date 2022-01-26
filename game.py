import time
startTime = time.time()


import datetime
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())

import random
WINNING_NUMBER = random.randint(1,5)
N = int(input("ENTER YOUR NUMBER BETWEEN 1 TO 5 :- "))
if N==random.randint(1,5):
    print("****YOU WIN**** !!!! ")
else:
        if N<=random.randint(1,5):
            print("YOUR NUMBER IS TOO LOW BETTER LUCK NEXT TIME \n YOU HAVE LAST CHANCES")
            N= int(input("ENTER YOUR NUMBER AGAIN :- "))
            if N==random.randint(1,5):
                print("****YOU WIN**** !!!! ")
            else:
                if N<=random.randint(1,5):
                    print("YOUR NUMBER IS TOO LOW ")
                    print("****GAME OVER****")
                else: 
                        print("YOUR NUMBER IS TOO BIG")
                        print("****GAME OVER****")
        else:
            print("YOUR NUMBER IS TOO BIG BETTER LUCK NEXT TIME ")
            print("YOU HAVE LAST CHANCE")
            N= int(input("ENTER YOUR NUMBER AGAIN :- "))
            if N==random.randint(1,5):
                print("****YOU WIN****")
            else:
                if N<=random.randint(1,5):
                    print("YOUR NUMBER IS TOO LOW ")
                    print("****GAME OVER****")
                else: 
                        print("YOUR NUMBER IS TOO BIG")
                        print("****GAME OVER****")


endTime = time.time()
totalTime = endTime - startTime


print("Total time required to execute code is= ", totalTime)