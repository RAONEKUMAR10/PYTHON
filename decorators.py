# DECORATORS/////////////////////////////////////////////////

# DECORATORS ARE USE TO ENHANCE THE FUNCTIONALITY OF OTHER FUNCTION WITH OUT CHANGING OF FUNCTION'S CODE.
# WE CAN USE 2 MORE THEN 2 DECORATORS TO ENHANCE OUR FUNCTION'S FUNCNALITY 
# BUT IF THE ORDER OF DECORATORS ARE  CHANGE THEN THE OUTPUT WILL BE CHANGE OF OUR FUNCTION.
# '@' THIS IS CALLED SYNTAX SUGAR .IT IS USE TO DEFINE DECORATOR IN FUNCTION.

# SYNATX-
# def decorator(func):
#    def wrap():
#       print("any thing you want")
#       return func()
#    return wrap

# @decorator()
# def sum(a,b):
#    return a+b



def deco_func(any_function):
   def wrap_function():
      print("hello world")
      any_function()
   return wrap_function

def func1():
   print ("meet our new friend")

func1 = deco_func(func1)
func1()

# OUTPUT-
# hello world
# meet our new friend

# OTHER WAY TO USE DECORATORS-------------

# IN THIS FIRST WE HAVE TO DEFINE DECORATOR FUNCTION AND 
@deco_func
def func3():
   print("my name is xyz")

func3()

# OUTPUT-
# hello world
# my name is xyz


# IF WE WANTS TO PRINT TWO OR MORE THE TWO VALUES OF FUNCTION THEN WE HAVE TO USE THIS SYNTAX/FORMAT ------------
def deco_func(any_func):
   def wrap_func(*args,**kwargs):
      print("hello")
      return any_func(*args,**kwargs)
   return wrap_func

@deco_func
def func1(a,b):
   return a+b

print(func1(3,2))

# OUTPUT-
# hello
# 5


# IF WE WNATS TO PRINT DOCS OF OUR FUNCTION AND NAME OF OUR FUNCTION THEN WE HAVE TO SOME MODULES AND OTHER FORMAT/SYNTAX //////////////
# THIS IS THE RIGHT WAY TO PRINT DOCS AND OUT OF MANY ARGUMENTS AND PARAMMETER-----------


from functools import wraps
def deco_func(any_func):
   @wraps(any_func)
   def wrap_func(*args,**kwargs):
      """this is wrap function"""
      print("this is good sum")
      return any_func(*args,**kwargs)
   return wrap_func

@deco_func
def add(a,b):
   """this is add function"""
   return a+b
# print(wrap_func.__doc__)
print(add.__doc__)
print(add.__name__)
print(add(2,3))
print(deco_func.__doc__)

# OUTPUT-
# this is add function
# add
# this is good sum
# 5
# None


# PRINT DOC AND NAME OF FUNCTION AND PRINT SUM OF TWO NUMBERS USING DECORATORS-----

from functools import wraps

def sum_func(any_func):
   @wraps(any_func)
   def wrap_func(*args,**kwargs):
      print(f"you are calling {any_func.__name__} function")
      print(f"{any_func.__doc__}")
      return any_func(*args,**kwargs)
   return wrap_func

@sum_func
def add(a,b):
   """this function takes two arguments and return their sum"""
   return a+b

print(add(7,5))

# OUTPUT-
# you are calling add
# this function takes two arguments and return their sum
# 12




from functools import wraps
import time
def calculate_time(func):                          
   @wraps(func)
   def wrap_func(*args,**kwargs):
      print("this is ritik kumar")
      print("this is ritik kumar")
      print("this is ritik kumar")
      print("this is ritik kumar")
      print("this is ritik kumar")
      print("this is ritik kumar")
      print("this is ritik kumar")
      print("this is ritik kumar")
      t1=time.time()
      returned_value=func(*args,**kwargs)
      t2=time.time()
      total_time=t2 - t1
      print(f"time take by this function-----  {total_time}")
      return returned_value
   return wrap_func

@calculate_time
def square(n):
   return [i*2 for i in range(1,n+1)]

print(square(8)) 

# OUTPUT-
# this is ritik kumar
# this is ritik kumar
# this is ritik kumar
# this is ritik kumar
# this is ritik kumar
# this is ritik kumar
# this is ritik kumar
# this is ritik kumar
# time take by this function-----  0.0009996891021728516
# [2, 4, 6, 8, 10, 12, 14, 16]



def calculate_time(anyf1):                 #EXAMPLE WITH OUT IMPORT FUNCTOOLS FROM 
    def wf1(*args,**kwargs):
        import time
        t1 = time.time()
        print(anyf1(*args,**kwargs))
        t2 = time.time()
        return(f'this function took_'+ str(t2-t1) +'_secs to run')
    return(wf1)

@calculate_time
def func123(a,b):
    print(f'this func took {a},{b} as arguments')
    print(f'this func took {a},{b} as arguments')
    print(f'this func took {a},{b} as arguments')
    print(f'this func took {a},{b} as arguments')
    print(f'this func took {a},{b} as arguments')
    print(f'this func took {a},{b} as arguments')
    print(f'this func took {a},{b} as arguments')
print(func123(2,4))

# OUTPUT-
# this func took 2,4 as arguments
# this func took 2,4 as arguments
# this func took 2,4 as arguments
# this func took 2,4 as arguments
# this func took 2,4 as arguments
# this func took 2,4 as arguments
# this func took 2,4 as arguments
# None
# this function took_0.0026025772094726562_secs to run

from functools import wraps
def int_allow(function):
   @wraps(function)
   def wraper(*args,**kwargs):
      data_types=[]
      for arg in args:
         data_types.append(type(arg)== int)
      if all(data_types):
         return function(*args,**kwargs)
      return "invalid argument"
   return wraper

@int_allow
def data(*args):
   total=[]
   for i in args:
      total+=i
   return total

print(data(2,3,4,5,65,7))


# OUTPUT-
# 86

# BUT IF WE DO-

print(data(3,4,5,6,7,'hii',1,5,6))

# OUTPUT-
# invalid argument 


# DECORATORS USING ARGUMENTS/////////////////////////////////

# WE CAN USE ARGUMENTS TO PRINT MANY VALUES OR SPECIFIC VALUE DEPEND ON DATA TYPE.

from functools import wraps
def func(data_types):
   def decorator(function):
      @wraps(function)
      def wraper(*args,**kwargs):
         for arg in args:
            if all([type(arg)==data_types]):   #using 'all function()'
               return function(*args,**kwargs)
         print("invalid argument")
      return wraper
   return decorator

@func(str) 
def data(*args):
   var=''
   for i in args:
      var+=i
   return var

print(data("ritik","kumar"))


# OUTPUT-
# ritikkumar


from functools import wraps
def func(data_types):
   def decorator(function):
      @wraps(function)
      def wraper(*args,**kwargs):
         if all([type(arg)==data_types for arg in args]):  #using list comprehensive 
            return function(*args,**kwargs)
         print("invalid argument")
      return wraper
   return decorator

@func(str) 
def data(*args):
   var=''
   for i in args:
      var+=i
   return var

print(data("ritik","kumar"))


# OUTPUT-
# ritikkumar

