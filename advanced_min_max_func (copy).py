# ADVANCED MAX() FUNCTION & ADVANCED MIN() FUNCTION

# ADVANCED MAX() FUNCTION///////////////////////////////////////////////////////////////////

name='a','b','c','d'
print(max(name))

# OUTPUT-
# d 

list1=['ritik','anamika','thakurraj']
print(max(list1))

# OUTPUT-
# thakurraj

def max_name(*args):      #we can use here list, items any thing we want
   return len(*args)

list1=['ritik ','anamika','ramcharan']
print(max(*list1,key=max_name))

# OUTPUT-
# ramcharan

lst=['ritik kumar ','anamika','ramcharan']
print(max(lst,key=lambda item:len(item)))

# OUTPUT-
# ritik kumar 

students =[
   {'name':'harshit','score':78,'age':24},
   {'name':'mohit','score':88,'age':19},
   {'name':'rohit','score':76,'age':23}
]

print(max(students,key=lambda items:items.get('age')))

# OUTPUT-
# {'name': 'harshit', 'score': 90, 'age': 24}

# IF WE DO -----------

print(max(students,key=lambda items:items.get('score')))

# OUTPUT-
# {'name': 'mohit', 'score': 88, 'age': 19}

students =[
   {'name':'harshit','score':78,'age':24},
   {'name':'mohit','score':88,'age':19},
   {'name':'rohit','score':76,'age':23}
]

print(max(students,key=lambda items:items.get('score'))['name'])

# OUTPUT-
# mohit

# IF WE DO------

print(max(students,key=lambda items:items.get('age'))['name'])

# OUTPUT-
# harshit

# IF WE DO------------

print(max(students,key=lambda items:items.get('name'))['age'])

# OUTPUT-
# 23


students ={
   'harshit' : {'score':90,'age':24},
   'mohit' : {'score':75,'age':19},
   'rohit' : {'score':76,'age':28}
}

print(max(students,key=lambda item:students[item]['age']))

# OUTPUT-
# rohit

# IF WE DO-

print(max(students,key=lambda item:students[item]['score']))

# OUTPUT-
# harshit



# ADVANCED MIN() FUNCTION ////////////////////////////////////////////////////////

name='a','b','c','d'
print(min(name))

# OUTPUT-
# a 

list1=['ritik','anamika','thakurraj']
print(min(list1))

# OUTPUT-
# anamika

def min_name(*args):      #we can use here list, items any thing we want
   return len(*args)

list1=['ritik ','anamika','ramcharan']
print(min(*list1,key=min_name))

# OUTPUT-
# ritik 

lst=['ritik kumar ','anamika','ramcharan']
print(min(lst,key=lambda item:len(item)))

# OUTPUT-
# anamika

students =[
   {'name':'harshit','score':78,'age':24},
   {'name':'mohit','score':88,'age':19},
   {'name':'rohit','score':76,'age':23}
]

print(min(students,key=lambda items:items.get('age')))

# OUTPUT-
# {'name': 'mohit', 'score': 88, 'age': 19}

# IF WE DO-

print(min(students,key=lambda items:items.get('score')))

# OUTPUT-
# {'name': 'rohit', 'score': 76, 'age': 23}


students =[
   {'name':'harshit','score':78,'age':24},
   {'name':'mohit','score':88,'age':19},
   {'name':'rohit','score':76,'age':23}
]

print(min(students,key=lambda items:items.get('score'))['name'])

# OUTPUT-
# rohit 

# IF WE DO-

print(min(students,key=lambda items:items.get('age'))['name'])
 
# OUTPUT-
# mohit 

# IF WE DO-

print(min(students,key=lambda items:items.get('name'))['age'])

# OUTPUT-
# 24 


students ={
   'harshit' : {'score':90,'age':24},
   'mohit' : {'score':75,'age':19},
   'rohit' : {'score':76,'age':28}
}

print(min(students,key=lambda item:students[item]['age']))

# OUTPUT-
# mohit 

# IF WE DO-

print(min(students,key=lambda item:students[item]['score']))

# OUTPUT-
# mohit 