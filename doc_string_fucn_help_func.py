# DOC STRING 

# WE CAN USE TO GIVE A MSG TO FROM USER ABOUT OUR PROGRAMM IS KNOWN AS """DOC STRING"""
# IT IS DEFINE IN '''XYZXYZ''' TRIPLE SINGLE QUOTES OD TRIPLE DOUBLE """XYZXYZ""" 

def add(a,b):
   """this function takes 2 numbers and return there sum"""
   return a+b

print(add(5,4))

# OUTPUT-
# 9


# IF WE WANT TO SEE DOC STRING THEN WE HAVE TO FOLLOW THIS SYNTAX//////////////////

# SYNTAX////////////////

# print(function.__doc__)  

# AFTER "FUNCTION NAME" PLACE A DOT "." AND TWO UNDER SCORES "__"  AND WRITE DOC AND THEN TWO UNDER SCORE "__"


def MUL(a,b):
   """this function takes 2 numbers and return there MULTIPLICATION """
   return a*b

print(MUL(5,4))
print(MUL.__doc__)

# OUTPUT-
# 20
# this function takes 2 numbers and return there MULTIPLICATION

# SOME BUILT-IN FUNCTIONS LIKE len(),sum(),max(),min(),sorted() have a doc strings 
#If we wants to wnat to print it then 

print(len.__doc__)

# OUTPUT-
# Return the number of items in a container.

print(sum.__doc__)

# OUTPUT-
# Return the sum of a 'start' value (default: 0) plus an iterable of numbers
# When the iterable is empty, return the start value.
# This function is intended specifically for use with numeric values and may
# reject non-numeric types.


# HELP() FUNCTION ////////////////////////////////////////////////////////////////////

# IT IS USE TO LEARN WHAT THIS FUNCTION DO.

# SYNTAX-------------
# print(help(function_name))

print(help(sorted))

# OUTPUT-
# Help on built-in function sorted in module builtins:

# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.

#     A custom key function can be supplied to customize the sort order, and the
#     reverse flag can be set to request the result in descending order.

# None