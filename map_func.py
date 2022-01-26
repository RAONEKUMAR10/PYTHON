#     MAP() FUNCTION /////////

# WHEN WE USE MAP() FUNCTION IN OUR FUNCTION WE THEN MAP() FUNCTION GAVE US A MAP OBJECT THAT OBJECT WE CAN CHANGESTORE IN "LIST","SET,
# "TUPLE".WE CAN'T STORE IT IN "DICTIONARY" OR "STRING".
# MAP() FUNCTION ARE ITERALE THAT MEANS WE CAN USE LOOP IN IT BUT ONLY ONCE
# BUT IF WE CHANGE IN "LIST","TUPLE","SET" THEN WE USE LOOP MULTIPLE TIMES

# SYNTAX---------------------------
# map(function,itterable)

# function== that function which we define or built in function which we use
# itterabe== name or variable of our data in which our data is assing 


#Q- Find the length of elements present in list

lst=['ritik','ujwal','arjun singh']
a=map(len,lst)     # HERE len is a length function which is BUILT-IN FUNCTION
print(a)
print(type(a))

# OUTPUT-
# <map object at 0x000001F628462C70>     #WE GET MAP OBJECT IT WILL CHANGE EVERY TIME
# <class 'map'>    #DATATYPE OF MAP() FUNCTION

# OR IF WE DO

print(list(map(len,lst)))
print(set(map(len,lst)))
print(tuple(map(len,lst)))

# OUTPUT-
# [5, 5, 11]         #LIST
# {11, 5}            #SET
# (5, 5, 11)         #TUPLE


# LAMDA EXPRESSION IN MAP() FUNCTION ////////////////////////////////////////////////////

# SYNTAX-----------------------------
# map(lambda inputs:operation ,itterable)

lst=['ritik','ujwal','arjun singh']
print(map(lambda a:len(a),lst))

# OUTPUT-
# <map object at 0x0000018ABCCA2250>

# OR IF WE DO 

s=set(map(lambda a:len(a),lst))
print(s)
print(type(s))

# OUTPUT-
# {11, 5}
# <class 'set'>  #BECAUSE WE USE "SET" TO STORE MAP OBJECT 

# Q- PRINT SQUARE OF ELEMENTS PRESENT IN "LIST" AND RETURN IN "SET"

lst=[2,3,4,5]
def sqr(a):
   return a**2
num= set(map(sqr,lst))
print(num)

# OUTPUT-
# {16, 9, 4, 25}   # UNORDERED COLLECTION OF DATA 

#  OR IF WE DO

lst=[2,3,4,5]
def sqr(a):
   return a**2
num= set(map(lambda a:a**2,lst))
print(num)

# OUTPUT-
# {16, 9, 4, 25}