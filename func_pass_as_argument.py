#  THIS METHOD IS USE TO CALL ONE FUNCTION IN OTHER FUNCTION 
# AND CALL MANY TIMES WE JAUST HAVE TO DEFINE ONE FUNCTION IN OTHER FUNCTION

# METHOD-FIRST///////////////////////////////

# NORMAL METHOD----------------------------

def square(n):      #first function 
   return n**2
def map(func,l):    #second function
   newlist=[]
   for i in l:
      newlist.append(func(i))   
   return newlist
l=[2,3,4,5,6]
print(map(square,l))   #first function call in second function

# OUTPUT-
# [4, 9, 16, 25, 36]


# METHOD-SECOND///////////////////////////////////////////

# USING LAMBDA FUNCTION---------------------

l=[4,5,6,7,8]
def map(func,l):    #first function 
   newlist=[]
   for i in l:
      newlist.append(func(i))
   return newlist
print(map(lambda a:a**2,l))    #second (lambda function) function call in first function 

# OUTPUT-
# [16, 25, 36, 49, 64]

       
# METHOD-THIRD///////////////////////////////////////////

# USING LIST COMPREHENSION-------------------------------

def cube(n):                    #first function 
   return n**3
def num(func,l):                #second function
   return [func(i) for i in l]

l=[2,3,4,5]
print(num(cube,l))              #first function call in second function

# OUTPUT-
# [8, 27, 64, 125]
 