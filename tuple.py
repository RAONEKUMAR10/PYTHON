# Tuple are data structure.Tuple can store any data type .
# Most important tuple are immutable  .Once tuple is created we can't update dat inside tuple.
# Tuple are usedwhere we know that data are never changed.
# Tuple are faster then list.
# We define tupls in '()' paranthesis.

from builtins import sum

tuple = ('hello', 'ritik',1,2,3)
# print(tuple)

# OUTPUT-
# ('hello', 'ritik', 1, 2, 3)

print(tuple[1])

# OUTPUT-
# ritik

# In tuple we can use .count() Method , .index() Method , len() Function , Slicing.

#  .index() Method  ////////////////////

tple= ('ritik kumar','hello',23,87.9,3,5)
print(tple.index(23))
print(type(tple))

# OUTPUT-
# 2
# <class 'tuple'>


#  len() Function  ///////////////////

tple= ('ritik kumar','hello',23,87.9,3,5)
print(len(tple))
print(type(tple))

# OUTPUT-
# 6
# <class 'tuple'>


#  Slicing  ////////////////////

tple= ('ritik kumar','hello',23,87.9,3,5)
print(tple[::-1])
print(type(tple))

# OUTPUT-
# (5, 3, 87.9, 23, 'hello', 'ritik kumar')
# <class 'tuple'>


# if we wan't to create a tuple who has only one element then we have to use ',' comma. 
# Then the data type of output is typle,either the type is int ,string etc.


t=1,
print(t)

# OUTPUT-
# (1,)

t=(1,)
print(t)

# OUTPUT-
# (1,)

t=1
print(t)
print(type(t))

# OUTPUT-
# 1
# <class 'int'>

t='hello',
print(t)
print(type(t))

# OUTPUT-
# ('hello',)
# <class 'tuple'>

# We can define tuple without using paranthesis 

# LOOPING in TUPLE////////////////////////

# While Loop  //////////////////////

# mixed = 1,2,3,4,5,'hello','hii'
# i=0
# while i < len(mixed):
#    print(mixed[i],end=" ")
#    i +=1

# OUTPUT-
# 1 2 3 4 5 hello hii

# For Loop  /////////////////////

mixed = 1,2,3,4,5,'hello','hii'
for i in mixed:
   print(i,end=" ")

# OUTPUT-
# 1 2 3 4 5 hello hii


# TUPLE UNPACKING///////////////////

fruits = 'apple','mango','kiwi','banana'
print(fruits)
# OUTPUT-('apple', 'mango', 'kiwi', 'banana')

fruit1,fruit2,fruit3,fruit4=fruits

print(fruit1)
print(fruit2)
print(fruit3)
print(fruit4)
print(fruits)

# OUTPUT-
# apple
# mango
# kiwi
# banana
# ('apple', 'mango', 'kiwi', 'banana')


# This is known as Tuple Unpacking ,one thing is remember that the number of variable is euqals to the number of elements 
# present in tuple,either we got an error (ValueError).


# LIST IN SIDE TUPLE//////////////////////////////

# We know that we can't change tuple but if a list inside a tuple than we can change the data  which is store in list
# and also use as  .pop() Method, .extend() Method, .append() Method.


#  .pop() Method  //////////////////////////

mixed=1,2,3,[6,4,'hiii',2]
mixed[3].pop()
print(mixed)

# OUTPUT-
# (1, 2, 3, [6, 4, 'hiii'])

mixed=1,2,3,[6,4,'hiii',2]
mixed[3].pop(1)
print(mixed)

# OUTPUT-
# (1, 2, 3, [6, 'hiii', 2])


#  .extend() Method  /////////////////////////

mixed=1,2,3,[6,4,'hiii',2]
a=[1,2,3,4,5,'hello']
mixed[3].extend(a)
print(mixed)

# OUTPUT-
# (1, 2, 3, [6, 4, 'hiii', 2, 1, 2, 3, 4, 5, 'hello'])


#  .append() Method  ///////////////////////////

mixed=1,2,3,[6,4,'hiii',2]
mixed[3].append(9)
print(mixed)

# OUTPUT-
# (1, 2, 3, [6, 4, 'hiii', 2, 9])


# We can change Tuple into List,Tuple into String///////////////

# use  '(())' duble-paranthesis to change tuple into string or list. 


# Tuple into List  /////////////////////

mixed=list((1,2,3,[6,4,'hiii',2]))
print(mixed)
print(type(mixed))

#  OUTPUT-
# [1, 2, 3, [6, 4, 'hiii', 2]]
# <class 'list'>


# Tuple into String  ////////////////////////

mixed=str((1,2,3,[6,4,'hiii',2]))
print(mixed)
print(type(mixed))

# OUTPUT-
# (1, 2, 3, [6, 4, 'hiii', 2])
# <class 'str'>



# FUNCTIONS use in Tuple/////////////

#  min() Function  //////////////////////

# it is used to find minimum value in tuple

mixed=1,2,3,3,4,5,6,7
print(min(mixed))
print(type(mixed))

# OUTPUT-
# 1
# <class 'tuple'>


#  max() Fuction  ////////////////////

# it is used to find mamimum value in tuple

mixed=1,2,3,3,4,5,6,7
print(max(mixed))
print(type(mixed))

# OUTPUT-
# 7
# <class 'tuple'>


#  sum() Function  //////////////////

# it use to add of numbers present in tuple

mixed=(1,2,3,3,4,5,6,7)
print(sum(mixed))
print(type(mixed))

# OUTPUT-
# 31
# <class 'tuple'>



# Function Return Values in Tuple/////////////////

# A function can return two or more then two values then the values are return in tuple.

def math(a,b):
   add=a+b
   div=a-b

   return add,div

print(math(8,6))
print(type(math))

# OUTPUT-
# (14, 2)
# <class 'function'>

sum,divide=math(9,5)
print(sum)
print(type(sum))
print(divide)
print(type(divide))

# OUTPUT-
# 14
# <class 'int'>
# 4
# <class 'int'>

print(sum,divide)

# OUTPUT-
# 14 4
