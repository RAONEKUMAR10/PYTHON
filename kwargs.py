# **kwargs (KEYWORD ARGUMENT ) or **kwargs (DUBLE STAR ARGUMENT)

# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. 
# We use the name kwargs with the double star. 
# The reason is because the double star allows us to pass through keyword arguments (and any number of them).

# IT IS USE TO PRINT DICTIONARY OR WORK IN A DICTIONARY LIKE *args IS USE FOR LIST
# IT GAVE OUTPUT AS A DICTIONARY
# IT TAKES INPUT IN A KEY:VALUE PAIR


# **kwargs AS A PARAMETER /////////////////////////////

def func(**kwargs):
   print(kwargs)

func(first_name='ritik',last_name='kumar')

# OUTPUT-
# {'first_name': 'ritik', 'last_name': 'kumar'}


# LOOP IN **kwargs /////////////////////////////////////

def sum(**kwargs):
   for j,k in kwargs.items():
      print(j,k)
sum(hii='ritik',love='avantika')

# OUTPUT-
# hii ritik
# love avantika


# WE CAN USE f STRING IN **kwargs ///////////////////

def sum(**kwargs):
   for j,k in kwargs.items():
      print(f"{j} : {k}")
sum(hii='ritik',love='avantika')

# OUTPUT-
# hii : ritik
# love : avantika


# WE CAN GAVE A PARAMETER IN FUNCTION BEFORE **kwargs ////////////////////////////////////////

# SYNTAX------------
# function (parameter,**kwargs):

def func(num1,**kwargs):
   for j,k in kwargs.items():
      print(f"{j} : {k}")
func('destiny',love='avantika',lover='ritik')

# OUTPUT-
# love : avantika
# lover : ritik


# IF WE PASS A PARAMETER IN A FUNCTION AND DIDN'T PASS A ARGUMENT FOR THAT THEN WE GET AN ERROR 

def func(num1,**kwargs):
   for j,k in kwargs.items():
      print(f"{j} : {k}")
func(love='avantika',lover='ritik')  #HERE WE DIDN'T PASS ARGUMENT FOR PARAMETER WHICH WE PASS IN FUNCTION

# OUTPUT-
# TypeError: func() missing 1 required positional argument: 'num1'


#  DICTIONARY UNPACKING IN **kwargs /////////////////////////////////////////////

def func(**kwargs):
   for j,k in kwargs.items():
      print(f"{j} : {k}")
d={'name':'ritik','crush':'avantika'}  #BCOS DICTIONARY CREATED IN '{}'
func(**d)  # PUT TWO STARS '**' BEFORE VARIABLE EITHER WE GET AN ERROR

# OUTPUT-
# name : ritik
# crush : avantika


# OR IF WE DO -------

def func(**kwargs):
   for j,k in kwargs.items():
      print(f"{j} : {k}")
d={'name':'ritik','crush':'avantika'}
func(d)

# OUTPUT-
# TypeError: func() takes 0 positional arguments but 1 was given



# Q- WRITE A PROGRAM IF USE WRITE REVERSE_STR= TRUE THEN STRING WILL LE REVERSE AND LAST CHAR WILL BE CAPITAL,
# BUT IF USER DID NOT WRITE WRITE REVERSE_STR= TRUE THEN PRINT STRING AND FIRST CHAR WILL BE CAPITAL OF EVERY ELEMENT IN THE LIST
# USING **KWARGS 

def func(l,**kwargs):
   if kwargs.get('reverse_str')==True:
      return [i[::-1].title() for i in l]
   else:
      return [i.title() for i in l]

l=['ritik','paras','avantika']
print(func(l))

# OUTPUT-
# ['Ritik', 'Paras', 'Avantika']

# OR

print(func(l,reverse_str=True))

# OUTPUT-
# ['Kitir', 'Sarap', 'Akitnava']