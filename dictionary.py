# We use Dictionary because of limitations of List ,
# List are not enough to represent real data
# Dictionaries are UNORDERD COLLECTION of data in KEY:VALUE pair
# in pythton to create Dictionary we use CURLEY BRAKETS '{}'.

user={'name':'ritik','age':20,'course':'b,tech'}
print(user)
print(type(user))

# # OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}
# <class 'dict'>

# Another way to create dictionary///////////////

user=dict(name='ritik',age=20,course='b.tech')
print(user)
print(type(user))

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b.tech'}
# <class 'dict'>

# In this method we don't use curley brackets insted we use paranthesis'()' and '='operator to assign Value in Key.
# but the output is same in both methods

# In dictionary we can't use indexing or slicing to acces our data
# we use KEY to access data in dictionary

user={'name':'ritik',
'age':20,
'course':'b,tech'}
print(user['name'])

# OUTPUT-
# ritik

user=dict(name='ritik',age=20,course='b.tech')
print(user['age'])

# OUTPUT-
# 20


# In dictionary we can store dictionary inside dictionary,string inside dictionary,list inside dictionary,tuple inside dictionary,
# number inside dictionary,character inside dictionary,tuple inside dictionary


user={'name':'ritik',                                                     #string
'age':20,                                                                 #integer
'course':'b.tech',                                                        
'subject':{'1st year':10,'2nd year':12,'3rd year':12,'final year':7},     #dictionary
'fav-movies':['ra.one','avengers','iron man'],                            #list
'fav:songs':('aviki','soulchef','el shaddai'),                            #tuple
'blood group': 'a'                                                        #character
}

print(user)
print(type(user))
print(user['name'])
print(user['age'])
print(user['course'])
print(user['subject'])
print(user['fav-movies'])
print(user['fav:songs'])
print(user['blood group'])


# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b.tech', 'subject': {'1st year': 10, '2nd year': 12, '3rd year': 12, 'final year': 7}, 'fav-movies': ['ra.one', 'avengers', 'iron man'], 'fav:songs': ('aviki', 'soulchef', 'el shaddai'), 'blood group': 'a'}
# <class 'dict'>
# ritik
# 20
# b.tech
# {'1st year': 10, '2nd year': 12, '3rd year': 12, 'final year': 7}
# ['ra.one', 'avengers', 'iron man']
# ('aviki', 'soulchef', 'el shaddai')
# a




# Add data in DICTIONARY/EMPTY DICTIONARY//////////////////////////////// 

# Newly add data will be add in the last of dictionary.

# ADD DATA IN DICTIONARY////////////////////////
user={'name':'ritik',
'age':20,
'course':'b,tech'}

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}

user['blood group']='O+'
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech', 'blood group': 'O+'}


# ADD DATA IN EMPTY DICTIONARY///////////////


user={}
print(user)

# OUTPUT-
# {}


user['name']='ritik'
user['age']=21
user['course']='b.tech'

print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 21, 'course': 'b.tech'}


#  .values() Method/////////////////////////
# It is use to print VALUE of dictionary
# 'dict:values' is the data type of  .values() Method
# If we want to print or check that key is in dictionary or not then we have to use  .values() Method.

user={'name':'ritik',
'age':20,
'course':'b,tech'}
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 21, 'course': 'b.tech'}

user={'name':'ritik',
'age':20,
'course':'b,tech'}
print(user.values())

# OUTPUT-
# dict_values(['ritik', 20, 'b,tech'])



#  'in' KEYWORD IN DICTIONARY///////////////////
# We can use 'in' KEYWORD to find 'KEY' and 'VALUE' in a dictionary

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
if 'name' in user:                        #TO CHECK KEY PRESENT IN DICTIONARY OR NOT
   print("prsesnt")
else:
   print("not present")

# OUTPUT-
# prsesnt

user={'name':'ritik',
'age':20,
'course':'b,tech'}

if 20 in user.values():                    #TO CHECk VALUE PRESENT IN DICTIONARY OR NOT
   print("present")
else:print('absent')

# OUTPUT-
# present


# LOOPING IN DICTIONARY/////////////////////////////

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

for i in user:                  #TO PRINT ONLY 'KEY' OF DICTIONARY
   print(i)

# OUTPUT-
# name
# age
# course


user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

for i in user.values():        #TO PRINT ONLY 'VALUES' OF DICTIONARY
   print(i)

# OUTPUT-
# ritik
# 20
# b,tech


#  .keys() METHOD/////////////////////////////
#It is use to print KEYS of DICTIONARY.
#  'dict_keys' is the data type of  .keys() Method

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

print(user.keys())

# OUTPUT-
# dict_keys(['name', 'age', 'course'])


user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
for i in user.keys():
   print(i)

# OUTPUT-
# name
# age
# course


# Q- Print the values of dictionary using keys//////////////////////

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
for i in user.keys():
   print(user[i])

# OUTPUT-
# ritik
# 20
# b,tech


user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
for i in user:
   print(user[i])

# OUTPUT-
# ritik
# 20
# b,tech


#  .items() METHOD//////////////////////////////
# it is use to print our dictionary as a tuple

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
print(user.items())

# OUTPUT
# dict_items([('name', 'ritik'), ('age', 20), ('course', 'b,tech')])


user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
for i in user.items():
   print(i)
print(type(i))

# OUTPUT-
# ('name', 'ritik')
# ('age', 20)
# ('course', 'b,tech')
# <class 'tuple'>


user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
for i,j in user.items():
   print(i,j)
   print(type(i))
   print(type(j))

# OUTPUT-
# name ritik
# <class 'str'>
# <class 'str'>
# age 20
# <class 'str'>
# <class 'int'>
# course b,tech
# <class 'str'>
# <class 'str'>



#  .pop() METHOD///////////////////////
# In this .pop() method we gave an argument to .pop() method that is 'KEY' which we want to pop 
# we can print the value which is poped

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
print(user)
print(user.pop('age'))
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}
# 20                                 POPED ITEM
# {'name': 'ritik', 'course': 'b,tech'}



# .popitem() METHOD/////////////////////////
# It use when we want to remove ramdomly any one KEY-VALUE pair of our dictionary

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
print(user)
print(user.popitem())
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}
# ('course', 'b,tech')           #RANDOMLY REMOVED KEY-VALUE PAIR
# {'name': 'ritik', 'age': 20}


#  .update() METHOD///////////////////////
# It is used to add data in dictionary or add dictionary in another dictionary .
# and also use to check that is our dictionary have a update or not.

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

user_data={'subject':{'1st year':10,'2nd year':12,'3rd year':12,'final year':7},     #dictionary
'fav-movies':['ra.one','avengers','iron man'],                            #list
'fav:songs':('aviki','soulchef','el shaddai'),                            #tuple
'blood group': 'a'
}
print(user)
user.update(user_data)
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}
# {'name': 'ritik', 'age': 20, 'course': 'b,tech', 'subject': {'1st year': 10, '2nd year': 12, '3rd year': 12, 'final year': 7}, 'fav-movies': ['ra.one', 'avengers', 'iron man'], 'fav:songs': ('aviki', 'soulchef', 'el shaddai'), 'blood group': 'a'}


user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

print(user)
user.update()
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}       #THERE IS NO UPDATE IN DICTIONARY SO NO UPDATE DICTIONARY AS SAME AS BEFORE
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}

# If we hava a KEY in dictionary with VALUE and the same KEY is in new data which we want to add then  key has update and the new data will 
# be store in dictionary

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}
print(user['age'])

# OUTPUT-20

user_data = {'age':21,
'roll_no': 1706931006,
}

user.update(user_data)
print(user)
print(user['age'])

# OUTPUT-
# {'name': 'ritik', 'age': 21, 'course': 'b,tech', 'roll_no': 1706931006}
# 21


#  .fromkeys() METHOD
# it is used to create dictionary

user= dict.fromkeys(
   ['name','age','course'],'unknown'
)
print(user)

# OUTPUT-
# {'name': 'unmnown', 'age': 'unmnown', 'course': 'unmnown'}

# We can use tuple,list to make KEY-VALUE pair.
# but if we use 'STRING' as a KEY then all character  become a seprate KEY.

user = dict.fromkeys('name','unknown')
print(user)

# OUTPUT-
# {'n': 'unknown', 'a': 'unknown', 'm': 'unknown', 'e': 'unknown'}



#   .get() METHOD////////////////////////////////////////////////////
# it is use to access the key of dictionary

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

print(user.get('age'))

# OUTPUT-
# 20

# If we pass a argument that is not available in dictionary then we get "NONE".
# But we can replace it-------
print(user.get('branch'))

# OUTPUT-
# None

print(user.get('branch','wrong key'))

# OUTPUT-
# wrong key


#   .clear() METHOD////////////////////////////////////////////////////
# it is used to clear our dictionary

user={'name':'ritik',
'age':20,                      
'course':'b,tech'}

print(user)
user.clear()
print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech'}
# {}


#  .copy() METHOD
# It is use to copy one dictionary into other dictionary

user={'name':'ritik',
'age':20,                      
'course':'b,tech',
'branch':'E.C.E',
}

user2= user.copy()
print(user2)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech', 'branch': 'E.C.E'}

#  user and user2 are two different with same data we can't use these as a seprate dictionary
# if we delete something in user then it also delete from user2.



# Q- What happen if we have two same key in a dictionary but different values

user={'name':'ritik',
'age':22,                      
'course':'b,tech',
'branch':'E.C.E',
'age':20,
'branch':'C.S'
}

print(user)

# OUTPUT-
# {'name': 'ritik', 'age': 20, 'course': 'b,tech', 'branch': 'C.S'}

# it will over write by the second key .output always be second key or the last value of key.


# Q- Define a function to print a cube of a number and return in a dictionary

def cube(n):
   cubic={}
   for i in range(1,n+1):
      cubic[i]=i**3
   return cubic

print(cube(4))

# OUTPUT-
# {1: 1, 2: 8, 3: 27, 4: 64}


# Q- Write a programm to print a character of any string in dictionary

def char(string):
   count={}
   for i in string:
      count[i]=string.count(i)
   return count

print(char('ritik'))

# OUTPUT-
# {'r': 1, 'i': 2, 't': 1, 'k': 1}


# Q- Write a programm to take input from user and print it as a dictionary

user ={}
name=input("enter you name ")
age=int(input("enter your age "))
course=input("enter your course ")

user['name']=name
user['age']=age
user['course']=course

for i,j in user.items():
   print(f"{i} : {j}")

# OUTPUT-
# enter you name ritik
# enter your age 21
# enter your course b.tech
# name : ritik
# age : 21
# course : b.tech



# ANOTHER WAY TO DO THIS PROGRAMM

USER={}
USER['NAME']=input("ENTER YOUR NAME ")
USER['AGE']=int(input("ENTER YOUR AGE "))
USER['COURSE']=input("ENTER YOUR COURSE")
for I,J in USER.items():
   print(I,J)

# OUTPUT-
# ENTER YOUR NAME RITIK KUMAR
# ENTER YOUR AGE 21
# ENTER YOUR COURSEB.TECH
# NAME RITIK KUMAR
# AGE 21
# COURSE B.TECH




                                                               