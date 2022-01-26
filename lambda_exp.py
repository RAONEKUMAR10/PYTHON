
# LAMBDA EXPRESSION OR ANONYMOUS FUNCTION

# THESE FUNCTIONS DON'T HAVE ANY NAME BUT IT ONLY KNOWN AS LAMBDA IN PYTHON
# IT SHOWS ASS A MEMORY LOCATION IN SYSTEM
# IN LAMBDA EXPRESSION WE CAN'T USE for loop OR while loop


# SYNTAX--------------------

# variable = lambda inputs(many values int,float,str,etc.) : operation(add,divide,reverse str multiply,etc.) #return

add =lambda a,b,c:a*b*c
print(add(2,3,4))
print(add)

# OUTPUT-
# 24
# <function <lambda> at 0x00000214541B9C10>      

reverse = lambda s1: s1[::1]
print(reverse('ritik become a devloper'))
print(reverse)

# OUTPUT-
# ritik become a devloper
# <function <lambda> at 0x00000241B2C99CA0>


#  LAMBDA EXPRESSION USING if-else //////////////////////////////////////////////////

# SYNTAX--------------------------

# var = lambda input : operation1 if(condition) else operation2

even = lambda a: 'even' if a%2==0 else  'odd'
print(even(3))

# OUTPUT-
# odd

# OR IF WE DO----------------------------

even = lambda a:a%2==0
print(even(3))

# OUTPUT-
# False    #THIS IS THE BOOLEAN VALUE IF CONDITION IS TRUE THEN WE GET 'True' OR IF CONDTION IS FALSE THEN WE GET 'False'

length = lambda list : 'TRUE' if (len(list)>3 and len(list)<10) else 'FALSE'
list=[i for i in range(1,12)]    #WE CNA CREATE LIST USING L.C
print(length(list))

# OUTPUT-
# FALSE 

list=[5,6,7,8,9]                 #WE CAN CREATE LIST SIMPLY
print(length(list))

# OUTPUT-
# TRUE 

