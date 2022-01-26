
def func1():
   print("hello world")  #if we use print insted of return then we dont have need to call function in print.

print(func1())

# OUTPUT-     
# hello world
# None     #just because of func1 have no any parameters.

# OR IF WE DO-

print(func1)

# OUTPUT-
# <function func1 at 0x00000212A7845160>

# SO THE RIGHT WAY IS -
# JUST CALL THE FUNCTION NAME  LIKE THIS.

func1()

# OUTPUT-
# hello world


# RETURN FUNCTION/////////////////////////


def func2():
   return "hello.world"

func2()

# OUTPUT-
# BLANK SCREEN

# if we use REURN FUNCTION then we to print it.

print(func2)

# OUTPUT-
# <function func1 at 0x7f5d6dcb9e18>

# SO THE RIGHT WAY IS 

print(func2())

# OUTPUT-
# hello.world



# SWAPING WITHOUT USING ANOTHER VARIABLE
def swap(a,b):
   a,b=b,a
   return a,b
a= int(input("ENTER a: "))
b= int(input("ENTER b: "))
print(f"Number before swaping {a,b}")
print(f"Number after swaping {swap(a,b)}")

# OUTPUT-
# ENTER a: 23
# ENTER b: 12
# Number before swaping (23, 12)
# Number after swaping (12, 23)



# SWAPING USING THIRD VARIABLE
def swap(a,b):      
   c=a
   a=b
   b=c
   return a,b
a= int(input("ENTER a: "))
b= int(input("ENTER b: "))
print(f"Number before swaping {a,b}")
print(f"Number after swaping {swap(a,b)}")

# OUTPUT-
# ENTER a: 65
# ENTER b: 23
# Number before swaping (65, 23)
# Number after swaping (23, 65)



def add(a,b):
   return a+b

def sum(a,b,c):
   d=add(a,b)
   return add(d,c)

a= int(input("ENTER a: "))
b= int(input("ENTER b: "))
c= int(input("ENTER c: "))
print(f"The Sum Of {a},{b},{c} Is {sum(a,b,c)}")

# OUTPUT-
# ENTER a: 76
# ENTER b: 78
# ENTER c: 90
# The Sum Of 76,78,90 Is 244



def factorial(n):
   i=1
   fact=1
   while i <= n:
      fact = fact*i
      i=i+1
   return fact

print(factorial(6))

# OUTPUT-
# 720



def fibonacci(n):
   a=0
   b=1
   if n==1:
      print (a)
   elif n==2:
      print (a,b)
   else:
      print(a,b, end=" ")
      for i in range(n-2):
         c=a+b
         a=b
         b=c
         print(b,end=" ")
fibonacci(10)

# OUTPUT-
# 0 1 1 2 3 5 8 13 21 34



def great(a,b):
   if a>b:
      return a
   return b
def greatest(a,b,c):
   big=great(a,b)
   return great(big,c)

print(greatest(42,52,822))

# OUTPUT-
# 822



def big(num1,num2):
   if num1>num2:
      return "num1 is bigger"
   return"num2 is bigger"
print(big(2,9))


# OUTPUT-
# num2 is bigger




def last_char(name):
   return name[-1]
print(last_char("ritik kumar"))
print(last_char("fellos"))

# OUTPUT-
# r
# s




def odd_even(num):
   if num%2==0:
      return"even"
   else:
      return"odd"
print(odd_even(90077689))      

# OUTPUT-
# odd




def odd_even(num):
   if num%2==0:
      return"even"
   return"odd"      
print(odd_even(12343454))

# OUTPUT-
# even


# FUNCTION WITH DEFAULT PARAMETER ////////////////////////////////////////////////

# IT IS USE ALSO A TYPE OF A FUNCTION WHICH WE GAVE A VALUE TO OUR PEREMETERS IF THE USER DIDN'T PASS AN ARGUMENT IN A FUNCTION

def data (name='unknown',age=20):
   print(name)
   print(age)

data()  #IF WE DO EMPTY OUR ARGUMENTS THEN WE GET DEFAULT VALUES WHICH IS GIVEN IN PARAMETER

# OUTPUT-
# unknown
# 20

# OR 

data('ritik') #IF WE PASS ONLY FIRST ARGUMENT THEN WE GET UPDATED ARGUMENT OF FIRST PARAMETER AND DEFAULT ARGUMENTS OF OTHER PARAMETERS 

# OUTPUT-
# ritik
# 20

# OR 

data('ritik',22) #IF WE GAVE ALL UPDATE ARGUMENTS OF ALL PARAMETER THEN WE GET UPDATED ARGUMENTS OF ALL PARAMETERS

# OUTPUT-
# ritik
# 22



