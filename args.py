# *args or STAR OPERATOR

# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. 
# It is used to pass a non-key worded, variable-length argument list. 
# The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
# What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args,
#  any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
# For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. 
# It can be done using *args.
# Using the *,the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it,
#  run some higher-order functions such as map and filter, etc.
 

# IT IS USE TO TAKE MANY INPUTS IN FUNCTION
# IT TAKES INPUT AS A TUPLE

# def sum(a,b):
#    return a+b
# print(sum(5,4,8))

# OUTPUT-
# TypeError

# TO OVERCOME THESE ERROT WE USE *args 
# THE MAIN THING IS * NOT args we can rewrite args as a ritik,sum,fruit etc.
# BUT 99% PROGRAMMERS USE *args .

# def sum(*args):
#    total=0
#    for i in args:
#       total+=i
#    return total

# print(sum(2,3,4,5,6,7))


# OUTPUT-
# 27


# print(sum())          # IF WE DON'T PASS ANY VALUE IN *args THEN WE GET EMPTY TUPLE

# OUTPUT-
# 0



# *args WITH NORMAL PARAMETER /////////////////////////////////////////////////

# SYNTAX---------
# function (normal parameter,*args):

# NUMBER ON NORMAL PARAMETER ARE PASS IN FUNCTION THEN NUMBER OF ELEMENTS ARE COVER IN TUPLE

# def sum(num1,num2,num3,*args):
#    print(num1,num2,num3)
#    print(args)
#    total=0
#    for i in args:
#       total+=i
#    return total

# print(sum(2,3))

# OUTPUT-
# TypeError: sum() missing 1 required positional argument: 'num3'    #BCOS NORMAL PARAMETER IN FUNCTION IS 3 AND WE GAVE ONLY 2

# print(sum(2,3,6))

# OUTPUT-
# 2 3 6
# ()  #BCOS WE PASS 3 PARAMETER IN FUNCTION AND GAVE THREE ARGUMENT BUT WE DON'T PASS ANY ARGUMENT FOR *args
# 0  #BCOS IN FIRST WE ASSIGN 0 IN total 



# print(sum(3,2,4,5,6,7))

# OUTPUT-
#3 2 4   #NORMAL PARAMETER
# (5, 6, 7)  # *args
# 18   #SUM FUNCTION OUTPUT


# *args AS AN ARGUMENT ////////////////////////////////////

# WE CAN USE *args IA ARGUMENT TA UNPACK ALL ELEMENTS OF LIST AND TUPLE

def num(*args):
   multiply=1
   for i in args:
      multiply*=i
   return multiply

l1=[1,2,3,4]
print(num(l1))

# OUTPUT-
# [1, 2, 3, 4]   #NOW l1 IS CONSIDER A SINGLE ELEMENT OF TUPLE THATS WHY 1*[1,2,3,4]

# OR 
def num(*args):
   multiply=1
   for i in args:
      multiply*=i
   return multiply

l1=[1,2,3,4]
print(num(*l1))  # *args as a ARGUMENT

# OUTPUT-
# 24  #NOW EVERY ELEMENT OF LIST IS CONSIDER AS A SEPRATE ELEMENT OF TUPLE AND MULTIPLY WITH 1*1*2*3*4


#  *args WITH if-else STATEMENT ////////////////////////////////////

# SYNTAX------------------------

# funftion (parameter,*args):
#     if args:
#        return ---
#     else:
#        return ---


# Q WRITE A PROGRAMM TO RAKE A PARAMETER AND *ARGS VAKUE OF PARAMETER IS THE POWER OF *ARGS AND RETURN IN LIST IF WE DIDN'T GIVE *ARGS
# THEN RETURN 'ENTER THE ARGS'

def power(num1,*args):
   print(num1)
   print(args)
   if args:
      return [i**num1 for i in args]
   else:
      return 'ENTER THE ARGS'

print(power(2,7,3,4,5,6))

# OUTPUT-
# 2                         #num1
# (7, 3, 4, 5, 6)           #args
# [49, 9, 16, 25, 36]       #output


# OR WE CAN DO-------

def power(num1,*args):
   print(num1)
   print(args)
   if args:
      return [i**num1 for i in args]
   else:
      return 'ENTER THE ARGS'

print(power(2,*(3,4,5,6)))

# OUTPUT-
# 2                      #num1
# (3, 4, 5, 6)           #args
# [9, 16, 25, 36]        #output


# OR IF WE DO-----

def power(num1,*args):
   print(num1)
   print(args)
   if args:
      return [i**num1 for i in args]
   else:
      return 'ENTER THE ARGS'

print(power(2,(3,4,5,6)))    #BCOS WE DIDN'T WRITE "*" IN ARGUMENT

# OUTPUT-
# TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'



