import time
startTime = time.time()
import datetime
print(f"TIME = {datetime.datetime.now().time()}")
print(f"DATE = {datetime.datetime.now().date()}")
import random
print(" FIND THE NUMBER BETWEEN 1-100"'\n'"IF YOU FIND IT YOU WON ")
WINNING_NUMBER = random.randint(1,100)
N = int(input("ENTER YOUR NUMBER :- "))
GUESS =1
GAME_OVER= False
while not GAME_OVER:
   if N==WINNING_NUMBER:
      print(f"****YOU WIN**** \n YOU TAKE {GUESS} CHANCES ")
      print(WINNING_NUMBER)
      GAME_OVER=True
   else:
      if N<WINNING_NUMBER:
         print("TOO LOW")
      else:
         if N>WINNING_NUMBER:
            print("TOO HIGH")

      GUESS+=1
      N = int(input("GUESS AGAIN :- "))
endTime= time.time()
totalTime= endTime-startTime
print(f"TIME TAKE TO EXECUTE PROGRAMM {totalTime}")
      
            