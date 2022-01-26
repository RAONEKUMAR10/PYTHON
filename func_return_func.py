#  WE CAN USE A FUNCTION IN A RETURN OF ANOTHER FUNCTION ////
# ONE FUNCTION RETURN OTHER FUNCTION 

# SYNTAX------------------

# def func1(n):
#     def func2():
#        print("hiii")
#     return func2
# var=func1()
# var()

# WE CAN USE MANY FUNCTIONS IN A FUNCTION.


def outter_func():
   def inner_func():
      print("inside inner fucn") #HERE WE CAN'T USE "RETURN".WE HAVE TO USE "PRINT" OTHERWISE WE GET A BLANK SCREEN(NO OUTPUT) AFTER RUN THE PGM. 
   return inner_func

var = outter_func()
var()

# OUTPUT-
# inside inner fucn

def func1():
   def func2():
      return ("inside inner fucn") 
var = func1()
var()

# OUTPUT-
# BLANK SCREEN


def outter_func():
   def inner_func():
      print("inside inner fucn")
   return inner_func

print(outter_func())


# OUTPUT-
# <function outter_func.<locals>.inner_func at 0x000001C0F7AF9DC0>

# IF WE DO-------------------

print(outter_func)

# OUTOUT-
# <function outter_func at 0x00000249BF7C5160>

# WE CAN USE PARAMETERS IN FUNCTION RETURN FUNCTION.

def outer_func(n):
   def inner_func():
      print(f"multiplication is {n**3}")
   return inner_func
   
var=outer_func(2)
var()

# OUTPUT-
# multiplication is 8


def outer_func(msg):
   def inner_func():
      print(f"the truth  is {msg}")
   return inner_func
   
var=outer_func("i am IRON MAN ")
var()

# OUTPUT-
# the truth  is i am IRON MAN 