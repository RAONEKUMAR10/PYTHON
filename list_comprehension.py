# LIST COMPREHENSION///////////////////////
# This is also a part of LIST
# It is use to create list in one line 
# SYNTAX------
#  variable = [whatwewant loop/condition]
import numbers

square =[i**2 for i in range (1,11)]
print(square)

# OUTPUT-
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# OR 
print([i**2 for i in range (1,11)])

# OUTPUT-
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


negative_numbers=[-i for i in range (1,9)]
print(negative_numbers)

# OUTPUT-
# [-1, -2, -3, -4, -5, -6, -7, -8]

# LIST COMPREHENSION WITH if //////////////////////////////////////////

# SYNTAX-------------

# variable= [whatwewant loop(for outer range of list) condition(if conditions)]

# Q- print even numbers in list using LC(LIST COMPREHENSION)
L2=[1,2,3,4,5,6,7,8,9,10]
L1=[i for i in L2 if i%2==0]
print(L1)

# OUTPUT-
# [2, 4, 6, 8, 10]

# Q- print [1,2.6,3,'hii',6,7.5,'heyy'] only string and float elements
L1=  [1,2.6,3,'hii',6,7.5,'heyy']
L2 = [I for I in L1 if (type(I)==int or type(I)==str)]
print(L2)

# OUTPUT-
# [1, 3, 'hii', 6, 'heyy']


# Q- print int and float numbers of a list in string
L1=[1,2.6,3,'hii',6,7.5,'heyy']
L2=[str(i) for i in L1 if (type(i)==int or type(i)==float)]
print(L2)

# OUTPUT-
# ['1', '2.6', '3', '6', '7.5']


# LIST COMPREHENSION WITH if-else ///////////////////////////////////////////////////

# SYNTAX --------------
# variable = [whatwewant if(conditions) else(conditions #not necessory) whatwewant loop(for outer range)]

# Q- if the number is odd then print it as a negative number or if number is even then print it as a square
L1=[i**2 if i%2==0 else -i for i in range(1,21)]
print(L1)

# OUTPUT-
# [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100, -11, 144, -13, 196, -15, 256, -17, 324, -19, 400]


# LIST COMPREHENSION WITH NESTED LIST //////////////////////////////////////

# SYNTAX----------------
# variable =[[whatwewant with loop and conditions] loop(for outer range)]

# we can create list into list using LC

# Q- print [[1,2],[3,4],[5,6]]
L1=[[[i for i in range(1,3)],[i for i in range(3,5)],[i for i in range(5,7)]] for i in range(1,2)]
print(L1) 

# OUTPUT-
# [[[1, 2], [3, 4], [5, 6]]]


# LIST COMPREHENSION USING FUNCTION //////////////////////////////////////////////

#Q- PRINT THE SQUARE  OF ANY NUMBERS

def square(n):
   return [i**2 for i in range(1,n+1)]
print(square(5))

# OUTPUT-
# [1, 4, 9, 16, 25]

# Q- TAKE A LIST OF SOME STRINGS AND PRINT FIRST CHARACTER OF EACH STRING

def reverse(list):
   return [list[-i] for i in list]
print(reverse(['abc','def','ghi']))

# OUTPUT-
# ['a', 'd', 'g']

