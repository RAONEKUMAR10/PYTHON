# SET COMPREHENSION 

# It is rarely use 
# It gave unordered data
# SYNTAX---------------------
# variable = {a(whatwewant) loop}

# Q- PRINT SQUARE OF NUMBERS
square={i**2 for i in range(1,6)}
print(square)

# OUTPUT-
# {1, 4, 9, 16, 25}

# Q- PRINT FIRST CHARACTERS OF NAME STORED IN A SET

set1={'ritik','avantika','harsh','paras'}
set2={i[0] for i in set1}
print(set2)

# OUTPUT-
# {'r', 'a', 'p', 'h'}      #UNORDERED DATA
