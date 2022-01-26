import random
winning_number =random.randint(1,100)
n = int(input("ENTER YOUR NUMBER : "))
guess=1
game_over=False
while not game_over:
   if n==winning_number:
      print(f"****YOU_WIN**** \nYOU TAKE {guess} CHANCES")
      game_over= True
   else:
      if n<winning_number:
         print("TOO_LOW") 
      else:
         if n>winning_number:
            print("TOO_HIGH")

      n=int(input("GUESS-AGAIN : "))
      guess +=1