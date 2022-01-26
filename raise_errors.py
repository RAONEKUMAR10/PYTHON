# RAISE ERRORS////////////////////////////////

# def sum(a,b):
#    if type(a) and type(b)== int:
#       return a+b

# print(sum(1,2))
# OUTPUT-
# 3

# BUT IF WE DO 
# print('2','9')
# OUTPUT-
# 29

# NOW WE WANT IF OUR USER  PASS WRONG DATA TYPE THEN WE GET AN ERROR ---------------------

# def add(a,b):
#    if (type(a) is int) and (type(b) is int):
      # return a+b
   # raise TypeError("oops you are passing wrong data type")

# raise   it is use to define errors or raise errors
# TypeError is raise when we pass awrong data type in our function/programm

# print(add(7,8.9))
# OUTPUT-
# TypeError: oops you are passing wrong data type

# print(add(3,6))
# OUTPUT-
# 9


# NOTIMPLEMENTED ERRORS////////////////////
# NOW WE WANT THAT IF ANY SUBCLASS INHERIT PARENT CLASS AND RUN ITS FUNCTION THEN AN ERROR IS RAISE 
# AND SAY TO DEFINE A FUNCTION IN SUBCLASS

# class Animals:
#    def __init__(self,name):
#       self.name=name
   
#    def sound(self):
#       raise NotImplementedError("YOU HAVE TO DEFINE THIS METHOD IN EVERY SUBCLASS")

# class Dod(Animals):
#    def __init__(self,name,breed):
#       super().__init__(name)
#       self.breed=breed

# class Cat(Animals):
#    def __init__(self,name,breed):
#       super().__init__(name)
#       self.breed=breed
# kitty=Cat("jigli",'russian')
# dogy=Dod("browny","petbull")
# print(dogy.sound())
# OUTPUT-
   #  raise NotImplementedError("YOU HAVE TO DEFINE THIS METHOD IN EVERY SUBCLASS")


# NotImplementedError: YOU HAVE TO DEFINE THIS METHOD IN EVERY SUBCLASS

# NOW THE CLASS IS ----------

# class Animals:
#    def __init__(self,name):
#       self.name=name
   
#    def sound(self):
#       raise NotImplementedError("YOU HAVE TO DEFINE THIS METHOD IN EVERY SUBCLASS")

# class Dod(Animals):
#    def __init__(self,name,breed):
#       super().__init__(name)
#       self.breed=breed
   
#    def sound(self):           #NotImplemantedError  IS ALSO KNOWN AS ABSTRACT METHOD.IN THIS METHOD WE DID'NT DEFINE ANY THING.
#       return "bhow bhow"      #THIS METHOD IS COME IN JAVA LANGUAGE

# class Cat(Animals):
#    def __init__(self,name,breed):
#       super().__init__(name)
#       self.breed=breed
 
#    def sound(self):
#       return "meow meow"


# kitty=Cat("jigli",'russian')
# dogy=Dod("browny","petbull")
# print(dogy.sound())
# # OUTPUT-
# # bhow bhow
# print(kitty.sound())
# # OUTPUT-
# # meow meow




# class Mobile:
#    def __init__(self,name):
#       self.name=name

# class MobileStore:
#    def __init__(self):
#       self.mobile=[]
   
#    def add_mobile(self,new_mobile):
#       self.mobile.append(new_mobile)

# P1=Mobile ("NOKIA")
# samsung='it has a hang problem'
# mobostore=MobileStore()
# print(mobostore.mobile)
# OUTPUT-
# []
# mobostore.add_mobile(samsung)
# print(mobostore.mobile)
# OUTPUT-
# ['it has a hang problem']  

# BUT WE DON'T WANT IT WE WANT ONLY THOSE OBJECT ADD WHICH IS IN MOBILE CLASS STORE IN MOBOSTORE
# SO THE CLASS IS ----
# EXG-

# class Mobile:
#    def __init__(self,name):
#       self.name=name
 
# class MobileStore:
#    def __init__(self):
#       self.mobiles=[]
   
#    def add_mobile(self,new_mobile):
#       if isinstance(new_mobile,Mobile):
#          self.mobiles.append(new_mobile)
#       else:
#          raise TypeError('NEW MOBILE SHOULD BE OBJECT OF MOBILE CLASS')

# P1=Mobile("NOKIA")
# samsung='it has a hang problem'
# mobostore=MobileStore()
# mobostore.add_mobile(P1)
# print(mobostore.mobiles)


# EXCEPTION HANDLING//////////////////////////////////////////////////////////////////////

# EXCEPTIONS ARE THOSE ERRORS WHO RAISE AT A TIME OF PROGRAMM EXECUTION

# age = int(input("enter yor age:")) # HERE WE HAVE TO GAVE INPUT AS A INTEGER(21) BUT IF WE GAVE STRING(TWENTYONE) THEN EXECPTION ERROR IS RAISE 

# if age < 18:
#    print("you can't play this game")
# else:
#    print("you can play this game")
# TO OVER COME THIS ERROR WE USE [TRY, EXCEPT,ELSE,FINALLY] BLOCK
 
# TRY BLOCK ////////////////////////
# WE USE IT IN OUR PROGRAM WHERE WE THOUGHT THAT ERROR AN OCCUR IN THIS LINE OF CODE
# IN TRY CAN USE MANY BLOCKS OR WE CAN DEFINE MANY BLOCKS IN SINGLE TRY BLOCK


# try:
#    age = int(input("enter your age:"))   # HERE WE HAVE TO GAVE INPUT AS A INTEGER(21) BUT IF WE GAVE STRING(TWENTYONE) THEN EXECPTION ERROR IS RAISE 
# except:
#    print("invalid input")

# if age < 18:
#    print("you can't play this game")
# else:
#    print("you can play this game")

# IF WE GIVE INPUT AS A STRING THEN WE GET A ERROR (NAME ERROR)

# OUTPUT-
# enter your age:ten
# invalid input
# Traceback (most recent call last):
#   File "raise_errors.py", line 164, in <module>
#     if age < 18:
# NameError: name 'age' is not defined

# OUTPUT-
# enter your age:20
# you can play this game

# NOW WE WANT THAT OUR LOOP WILL CONTINUOS WHILE OUR INPUT IS TRUE

# while True:
#    try:
#       age = int(input("enter yor age:"))   # HERE WE HAVE TO GAVE INPUT AS A INTEGER(21) BUT IF WE GAVE STRING(TWENTYONE) THEN EXECPTION ERROR IS RAISE 
#       break
#    except ValueError:  #BCOS HERE WE KNOW THAT VALUE ERROR WILL OCCUR
#       print(f"may be input is integer insted of string, try again")
#    except:          # WE USE THIS BLOCK BCOS MAY BE OTHER ERROR WILL OCCUR
#       print("invalid input")


# if age < 18:
#    print("you can't play this game")
# else:
#    print("you can play this game")



# ELSE  and FINALLY BLOCK-------------------------------

# ELSE BLOCK EXECUTE USER GAVE CORRECT INPUT


# while True:
#    try:
#       number=int(input("please enter a number :- "))
#    except ValueError:
#       print("please typw integer :-")
#    except:
#       print("unexpected error")
#    else:
#       print(f"user input= {number}")
#       break
#    finally :  #FINALLY BLAOCK ALWASY EXECUTE .NO MATTER ERROR OCCUR OR NOT.THIS METHOD EXECUTE BEFORE THE EXECUTION OF BREAK OF ELSE METHOD
#       print("finally I done it.....")


# EXG-
# def divide(a,b):
#    return a/b
# print(divide(4,0))
# OUTPUT-
# ZeroDivisionError: division by zero

# TO OVER COME THIS ERROR WE DO--
# def divide(a,b):
#    try:
#       return a/b
#    except ZeroDivisionError:
#       print("please enter the valid input")
#    except TypeError as TE:     #WE USE THIS TO PRINT DEFAULT MSG OF ERROR
#       print(TE)
#    except:     #IF ANY OTHER ERROR OCCUR INSTED OF ZeroDivisionError AND TypeError. THEN WE OVER COME THESE ERROR BY USING --
#       print("UNEXPETED ERROR") 
   

# print(divide(6,0))
# OUTPUT-
# please enter the valid input
# None

# print(divide('6',0))
# OUTPUT-
# unsupported operand type(s) for /: 'str' and 'int'
# None



# CUSTOM EXCEPTIONS/////////////////////////////////////////////////

# WE CAN MAKE OUR EXCEPTIONS TO IMPROVE READIABLE OF OUR PROGRAMM

# SYNTAX--
# class errorwhatwewanttomake(inhert type of error like ValueError)
# pass
# and use it as we want

# class NameTooShortError(ValueError):  #HERE WE CREATE A CLASS THAT'S NAME IS OUR ERROR WHICH WE WANT TO GAVE DURING WRONG INPUT
#    pass                                #AND IN IT WE GACE A STRING OR WHAT EVER WE WANT TO PRINT

# def name(n):
#    if len(n)<8:
#       raise NameTooShortError("name is too short")             #JUST LIKE THIS

# username=input("enter your name  :- ")
# name(username)
# print(f'hello{name}')

# OUTPUT-
# enter your name  :- RITIK KUMAR
# hello<function name at 0x000001BF65DA5160>


# IF WE DO-

# OUTPUT-
# enter your name  :- RITIK
# Traceback (most recent call last):
#   File "raise_errors.py", line 276, in <module>
#     name(username)
#   File "raise_errors.py", line 273, in name
#     raise NameTooShortError("name is too short")             #JUST LIKE THIS
# __main__.NameTooShortError: name is too short