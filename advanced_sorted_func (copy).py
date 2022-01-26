# ADVANCED SORTED() FUNCTION 

# SORT.() METHOD IS USED IN LIST BECAUSE WE CAN CHANGE IN LIST
# BUT IN SET,TUPLE WE USE SORTED() FUNCTION IT CAN'T CHANGE THE ORIGINAL BUT SET OR TUPLE BUT IT TAKES THE ELEMENTS AND SORT IT AND
# GAVE US A LIST BUT THE ORIGINAL SET OR TUPLE IS STILL SAME.

# ADVANCED SORT() FUNCTION IS USED TO SORT DICTIONARY AND DATA STRUCTURES

bikes=[
   {'model':'apache','price':8400},
   {'model':'pulsar','price':50000},
   {'model':'hero','price':35000},
   {'model':'yamaha','price':45000}
]

print(sorted(bikes,key=lambda b:b.get('model')))

# OUTPUT-
# [{'model': 'apache', 'price': 8400}, {'model': 'hero', 'price': 35000}, {'model': 'pulsar', 'price': 50000}, {'model': 'yamaha', 'price': 45000}]

# IF WE DO-

print(sorted(bikes,key=lambda b:b['model']))

# OUTPUT-
# [{'model': 'apache', 'price': 8400}, {'model': 'hero', 'price': 35000}, {'model': 'pulsar', 'price': 50000}, {'model': 'yamaha', 'price': 45000}]


# IF WE DO-

print(sorted(bikes,key=lambda b:b.get('price')))

# OUTPUT-
# [{'model': 'apache', 'price': 8400}, {'model': 'hero', 'price': 35000}, {'model': 'yamaha', 'price': 45000}, {'model': 'pulsar', 'price': 50000}]

# IF WE DO-

print(sorted(bikes,key=lambda b:b['price']))

# OUTPUT-
# [{'model': 'apache', 'price': 8400}, {'model': 'hero', 'price': 35000}, {'model': 'yamaha', 'price': 45000}, {'model': 'pulsar', 'price': 50000}]

# IF WE USE REVERSE CONDITION THEN WE GET OUR OUTPUT IN REVERSE------------------------------------

bikes=[
   {'model':'apache','price':8400},
   {'model':'pulsar','price':50000},
   {'model':'hero','price':35000},
   {'model':'yamaha','price':45000}
]

print(sorted(bikes,key=lambda b:b['price'],reverse=True))

# OUTPUT-
# [{'model': 'pulsar', 'price': 50000}, {'model': 'yamaha', 'price': 45000}, {'model': 'hero', 'price': 35000}, {'model': 'apache', 'price': 8400}]


# HELP() FUNCTION ////////////////////////////////////////////////////////////////////

# IT IS USE TO LEARN WHAT THIS FUNCTION DO.

# SYNTAX-------------

# print(help(function_name))

print(help(sorted))