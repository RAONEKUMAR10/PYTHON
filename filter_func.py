#  FILTER() FUNCTION

# SYNTAX-
#  filter(function,iterable)
# function== that function which we define or built in function which we use
# itterabe== name or variable of our data in which our data is assing 

def sqr(a):
   return a%2==0

a=[2,5,4,9,7,8,6]
print(filter(sqr,a))

# OUTPUT-
# <filter object at 0x0000022BB7A07E50>

# BUT IF WE DO

print(list(filter(sqr,a)))

# OUTPUT-
# [2, 4, 8, 6]

# IT'S PROPERTIES SAME AS A MAP() FUNCTION .BUT THESE BOTH ARE DIFFERENT FUNCTIONS WITH DIFFERENT WORKING

# WHEN WE USE FILTER() FUNCTION IN OUR FUNCTION WE THEN FILTER() FUNCTION GAVE US A MAP OBJECT THAT OBJECT WE CAN CHANGESTORE IN "LIST",
# "SET",TUPLE".WE CAN'T STORE IT IN "DICTIONARY" OR "STRING".


def sqr(a):
   return a%2==0

l=['ritik','ujjwal','arjun']
print(set(filter(lambda n:n[-1],l)))
print(str(filter(lambda n:n[-1],l)))

# OUTPUT-
# {'ritik', 'arjun', 'ujjwal'}
#<filter object at 0x0000022140CD7E50>   #IN STRING OR DICTIONARY WE GET OBJECT

# FILTER() FUNCTION ARE ITERALE THAT MEANS WE CAN USE LOOP IN IT BUT ONLY ONCE

def num(l):
   return l%2==0

a=[1,2,1,3,4,5,2,5]
b = filter(num,a)
for i in b:
   print(i)
for i in b:
   print(i)

# OUTPUT-
# 2
# 4
# 2


#  BUT IF WE CHANGE IN "LIST","TUPLE","SET" THEN WE USE LOOP MULTIPLE TIMES

def num(l):
   return l%2==0

a=[1,2,1,3,4,5,2,5]
b = list(filter(num,a))
for i in b:
   print(i)
for i in b:
   print(i)

# OUTPUT-
# 2
# 4
# 2
# 2
# 4
# 2


# LAMBDA FUNCTION IN FILTER() FUNCTION/////////////////////////////////////////////////////////

def sqr(l):
   return l%2==0

a=[2,3,1,4,8,6]
even=filter(lambda a:a%2==0,a)
print(even)

# OUTPUT-
# <filter object at 0x000002438DB678E0>


# BUT IF WE DO--------

def sqr(l):
   return l%2==0

a=[2,3,1,4,8,6]
even=set(filter(lambda a:a%2==0,a))
print(even)

# OUTPUT-
# {8,2,4,6}

