#  DICTIONARY COMPREHENSION
# IT IS USE TO PRINT DICTIONARY IN A VERY EASY METH0D
# SYNTAX-------------
#  variable={key:value loop/condition}

# Q- print key is the square of its value

square={i:i**i for i in range(1,6)}
print(square)

# OUTPUT-
# {1: 1, 2: 4, 3: 27, 4: 256, 5: 3125}

# WE CAN USE STRING FORMATING IN DICTIONARY COMPREHENSION //////////////////////

square={f"square of {i}" : i**2 for i in range (1,6)}
print(square)

# OUTPUT-
# {'square of 1': 1, 'square of 2': 4, 'square of 3': 9, 'square of 4': 16, 'square of 5': 25}

square={i:i**2 for i in range(1,6)}
for j,k in square.items():
   print(f"{j} : {k}")

# OUTPUT-
# 1 : 1
# 2 : 4
# 3 : 9
# 4 : 16
# 5 : 25


# Q- write a programm to count a character of any string
name='ritik'
d1={i:name.count(i) for i in name }
print(d1)

# OUTPUT-
# {'r': 1, 'i': 2, 't': 1, 'k': 1}

# OR 

name='ritik'
d1={i:name.count(i) for i in name }
for j,k in d1.items():
   print(j,k)

# OUTPUT-
# r 1
# i 2
# t 1
# k 1

# OR 

count={i:'ritik'.count(i) for i in 'ritik'}
print(count)

# OUTPUT-
# {'r': 1, 'i': 2, 't': 1, 'k': 1}


# DICTIONARY COMPREHENSION WITH if-else ////////////////////////////////////////

# SYNTAX-------------------

# variable={key:(value if(condition) else(condition #not necessary) value ) loop(outer loop)}

# Q- FIND EVEN AND ODD NUMBER IN A DICTIONARY

nums={i:'even' if i%2==0 else 'odd' for i in range(1,11)}
print(nums)

# OUTPUT-
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}

