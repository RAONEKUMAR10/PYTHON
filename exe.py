import json
import requests
request=requests.get("https://data.nasdaq.com/api/v3/datasets/WIKI/AAPL.csv") 
request_text=request.text
data=json.loads(request_text)
print(data)

# print(dir(json))
# OUTPUT--['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_default_decoder', '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']


# Python provides a dump() function to transmit(encode) data in JSON format. It accepts two positional arguments, first is the data object to be serialized and second is the file-like object to which the bytes needs to be written.

# PYTHON dump() FUNCTION
  
# student  = {  
# "Name" : "Peter",  
# "Roll_no" : "0090014",  
# "Grade" : "A",  
# "Age": 20,  
#     "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]  
# }  
# # with open ("data.json","w")as write_file:
# #     json.dump(student,write_file)
# print(type(student))
# print(student['name'])
# b=json.dumps(student)
# print(b)
# print(type(b))
# print(b['name'])
# # print(student)

# student  = {  
# "Name" : "Peter",  
# "Roll_no" : "0090014",  
# "Grade" : "A",  
# "Age": 20  
# }  
# b = json.dumps(student)  
  
# print(b) 
# OUTPUT--{"Name": "Peter", "Roll_no": "0090014", "Grade": "A", "Age": 20}
###########################################################################################
# def arguments(self, arguments: list):
#         """
#         Parameters
#         ----------
#         arguments : list
#             Command arguments.
#         """
#         self._arguments = arguments


# print(arguments(arguments[1,2,3,4,5,]))

# from django.db import models
# class Reporter(models.Model):
#    full_name=models.CharField(max_length=70)
#    def __str__(self);
#    return self.full_name

# class Article(models.Model): 
#    pub_date=models.DateField()
#    headline=models.CharField(max_length=200)
#    content=models.TexiField()
#    reporter models.ForeignKey(Reporter ,on_delete=models.CASCADE)
#    def __str__(self):
#       rerurn self.headline












# def ret():
#    return(10,20)

# print(ret())

# user={'name':'ritik',
# 'age':20,
# 'course':'b,tech',
# '["hii"]':"ritik_kumar"}
# print(user['["hii"]','age'])
 



# user={'name':'ritik',
# 'age':20,                      
# 'course':'b,tech'}
# for i in user.keys():
#    print(user[i])




# h=[i for i in range(2,8) ]
# print(h)
# def decorator(func):
#    def wrap(*args,**kwargs):
#       print("any thing you want")
#       func()
#    return wrap

# @decorator 
# def sum(a,b):
#    return a+b

# print(sum(3,4))



# def calculate_time(anyf1):                 #EXAMPLE
#     def wf1(*args,**kwargs):
#         import time
#         t1 = time.time()
#         print(anyf1(*args,**kwargs))
#         t2 = time.time()
#         return(f'this function took_'+ str(t2-t1) +'_secs to run')
#     return(wf1)

# @calculate_time
# def func123(a,b):
#     print(f'this func took {a},{b} as arguments')
#     print(f'this func took {a},{b} as arguments')
#     print(f'this func took {a},{b} as arguments')
#     print(f'this func took {a},{b} as arguments')
#     print(f'this func took {a},{b} as arguments')
#     print(f'this func took {a},{b} as arguments')
#     print(f'this func took {a},{b} as arguments')
# print(func123(2,4))


# from functools import wraps
# import time
# def calculate_time(func):                          #THERE IS SOME BUG IN THIS PROGRAMM BCOS IT DOES NOT SHOW THE TIME
#    @wraps(func)
#    def wrap_func(*args,**kwargs):
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       print("this is ritik kumar")
#       t1=time.time()
#       returned_value=func(*args,**kwargs)
#       t2=time.time()
#       total_time=t2 - t1
#       print(f"time take by this function-----  {total_time}")
#       return returned_value
#    return wrap_func

# @calculate_time
# def square(n):
#    return [i*2 for i in range(1,n+1)]

# print(square(8)) 





# from functools import wraps
# def func(data_types):
#    def decorator(function):
#       @wraps(function)
#       def wraper(*args,**kwargs):
#          for arg in args:
#             if all([type(arg)==data_types]):
#                return function(*args,**kwargs)
#          print("invalid argument")
#       return wraper
#    return decorator

# @func(str) 
# def data(*args):
#    var=''
#    for i in args:
#       var+=i
#    return var

# print(data("ritik","kumar"))

# if all([type(arg)==data_types for arg in args]):

# from functools import wraps
# import time
# def calculate_time(func):
#    @wraps(func)
#    def wrap_func(*args,**kwargs):
#       print("this is ritik kumar")
#       t1=time.time()
#       returned_value=func(*args,**kwargs)
#       t2=time.time()
#       total_time=t2 - t1
#       print(f"time take by this function-----  {total_time}")
#       return returned_value
#    return wrap_func

# @calculate_time
# def square(n):
#    return [i*2 for i in range(1,n+1)]

# print(square(8)) 

# import time
# t1=time.time()
# print("MY NAME IS RITIK KUMAR")
# print("I AM AN ENGINEER")
# t2=time.time()
# t= t2-t1
# print(f"time taken by this function   {t}")


# from functools import wraps
# import time

# def function(func):
   
#    @wraps(func)
#    def wrap(*args,**kwargs):
#       t1=time.time()
#       print("hello world")
#       return func(*args,**kwargs)
#       t2=time.time()
#       total=t2-t1
#       print(f"total time is {total}")
#    return wrap



# @function
# def square(n):
#    return n**2

# print(square(5))








# from functools import wraps

# def sum_func(any_func):
#    @wraps(any_func)
#    def wrap_func(*args,**kwargs):
#       print(f"you are calling {any_func.__name__}")
#       print(f"{any_func.__doc__}")
#       return any_func(*args,**kwargs)
#    return wrap_func

# @sum_func
# def add(a,b):
#    """this function takes two arguments and return their sum"""
#    return a+b

# print(add(7,5))


# def outter_func():
#    def inner_func():
#       return ("inside inner fucn") #HERE WE CAN'T USE "RETURN".WE HAVE TO USE "PRINT" OTHERWISE WE GET A BLANK SCREEN(NO OUTPUT) AFTER RUN THE PGM. 
#    return inner_func

# var = outter_func()
# var()

# def hii():
#    print("hello my world")
#    print("earth")
#    return "ritik"
#    return "ujjwal"

# print(hii())
#    if all(num%i!=0 for i in range(2,num)):
#       print(num)

# def prime(*a):
#    return [a%i!=0 for i in range *a]

# print(prime(1,2,3,4,5,6,7,8,9))
# n=int(input("enter the terms"))
# a=0
# b=1
# for i in range(n):
#    print(a,end=" ")
#    c=a+b
#    a=b
#    b=c
#    i+=1

# s=input("enter the string").split()
# s.sort()
# print(s)


# t=int(input("enter the terms:- "))
# a,b =0,1
# for i in range(t):
   
#    print(a,end=" ")
#    c=a+b
#    a,b=b,c

#    i+=1



# l=[10,9,8,7,6,5,4,3,2,1]
# nl=[]
# for i in l:
#    nl.append(l.pop(-1)) 
# print(nl)  


    









# def add(*args):
#    if all([(type(num)==int or float) for num in args]):
#       total=0
#       for i in args:
#          total+=i
#       return total
#    else:
#       return "wrong input"   
# print(add(2,1,5,3,4,8,7.3))
# bikes=[
#    {'model':'apache','price':8400},
#    {'model':'pulsar','price':50000},
#    {'model':'hero','price':35000},
#    {'model':'yamaha','price':45000}
# ]

# print(sorted(bikes,key=lambda b:b['price']))


# def add_it_up(n):
#    try:
#       sum(range(n+1))
#    except TypeError:
#       0
#    return 

# print(add_it_up(5))


# n=5
# s="hiiu"
# print(n*2)


# def add_it_up(n):
#    return sum(range(n+1))
# print(add_it_up(3))


# r=lambda a:a*2
# s=lambda b:b*3
# x=3
# x=r(x)
# x=s(x)
# x=r(x)
# print(x)

# reverse = lambda s1: s1[::1]
# reverse('ritik become a devloper')
# print(reverse)



# print(help(sorted))




# bikes=[
#    {'model':'apache','price':8400},
#    {'model':'pulsar','price':50000},
#    {'model':'hero','price':35000},
#    {'model':'yamaha','price':45000}
# ]

# print(sorted(bikes,key=lambda b:b.keys('apache'),reverse=True))


# lst=['arjun','anju','aarti','bunty','babli','brijesh','budh','ekta']
# A=[]
# B=[]
# E=[]
# for n in lst:
#    if n[0]=='a':
#       A.append(n)
#    if n[0]=='b':
#       B.append(n)
#    if n[0]=='e':
#       E.append(n)
# print(A)
# print(B)
# print(E)



# students ={
#    'harshit' : {'score':90,'age':24},
#    'mohit' : {'score':75,'age':19},
#    'rohit' : {'score':76,'age':23}
# }

# print(max(students,key = lambda item:item.values('score'))['name'])

# list1=['ritik','anamika','thakurraj']
# print(max(list1))

# OUTPUT-
# thakurraj

# def max_name(*args):      #we can use here list, items any thing we want
#    return len(*args)

# list1=['ritik ','anamika','ramcharan']
# print(max(*list1,key=max_name))

# OUTPUT-
# ramcharan

# lst=['ritik kumar ','anamika','ramcharan']
# print(max(lst,key=lambda item:len(item)))

# OUTPUT-
# ritik kumar

# def add(*args):
#    if all([(type(num)==int or type(num)==float) for num in args]):
#       total=0
#       for i in args:
#          total+=i
#       return total
#    else:
#       return "wrong input"
# print(add(2,1,5,3,'RITIK',4,8,7.3))







# import turtle



# numbers=[2,1,4,3,5,6,7]
# even=[True if num%2==0 else False for num in numbers]
# print(even)

# for pos,num in enumerate(numbers):
#    print(f"{pos} == {num}")

# L=[(1,2),(3,4),(5,6)]
# L1,L2=zip(*L)
# print(L2)
# print(L1)

# def add(*args):
#    tot=[]
#    tot.append(sum(args))
#    return tot


# print(add(3,4,5,2,6))

# def avg(*args):
#    average=[]
#    for pair in zip(*args):
#       average.append(sum(pair)/len(pair))
#    return average

# print(avg([1,2,3,4],[8,9,7,9]))



# def avg(l1,l2):
#    return ()


# L=[(1,2),(8,4),(5,6)]
# for pos,pair in enumerate(L):
#    print(f"{pos}  {pair}")

# L1=[2,4,8,5]
# L2=[3,6,1,7]
# MX=[]
# MN=[]
# print(list(zip(L1,L2)))
# for pair in zip(L1,L2):
#    MX.append(max(pair))
#    MN.append(min(pair))
# print(MX)
# print(MN)

# L1=[(8,4),(7,9),(2,8)]
# L2=[(3,10),(5,9),(3,7)]
# MX=[]
# MN=[]
# for pair in zip(L1,L2):
#    print(list(zip(L1,L2)))
#    MX.append(max(pair))
#    MN.append(min(pair))
# print(MX)
# print(MN)


# L=[(1,2),(3,4),(5,6)]
# MX=[]
# MN=[]
# for pos,i in enumerate(L):
#    print(f"{pos}  :  {i}")
# for i in L:
#    MX.append(max(i))
#    MN.append(min(i))
# print(f"MAX NUMBER IS PAIR {MX}")
# print(f"SMALL NUMBER IS PAIR {MN}")





# L=[(1,2),(3,4),(5,6)]
# for pos,i in L:
#    print(list(zip(*L)))

# l=[1,2,3,4,5,6]
# for pos,i in enumerate(l):
#    print(f"{pos} = {i}")


# L=[(1,2),(4,3),(8,6)]
# L1,L2=zip(*L)
# M=[]
# for i in L:
#    M.append(max(i))
# print(M)
# print(f"L1 == {L1}")
# print(f"L2 == {L2}")


# L=[('A',2),('B',4,)]
# N=(5,6)
# S={'A','B'}
# F=[32.3,76.9]
# print(list(zip(L,N,S,F)))


# user_id=['user1','user2']
# name=['ritik','ujjwal']
# print(list(zip(user_id,name)))
# def sqr(l):
#    return l%2==0

# a=[2,3,1,4,8,6]
# even=filter(lambda a:a%2==0,a)
# print(even)


# def num(l):
#    if l%2==0:
#       return l



# a=[1,2,1,3,4,5,2,5]
# b = list(map(num,a))
# for i in b:
#    print(i)
# for i in b:
#    print(i)


# def sqr(a):
#    return a%2==0

# l=['ritik','ujjwal','arjun']
# print(set(filter(lambda n:n[-1],l)))
# print(set(map(lambda n:n[-1],l)))


# lst=[2,3,4]
# def sqr(a):
#    for i in lst:
#       print(a**2)

# list(map(sqr,lst))
# # lst=['absc','def','ghji']
# print(list(map(lambda a:len(a),lst)))
                                        
# l={'name':'ritik','class':'b.tech','clg':'rggi'}
# for pos,i in enumerate(l.items()):
#    print(f'{pos}=={i}')
# print(type(l))
# print(type(pos))
# print(type(i))
   
# l=[i**2 for i in range(2,6)]
# print(l)


# list=[2,3,4]
# def sqr(list):
#    l=[]
#    for i in list:
#       l.append(i**2)
#    return l
# print(sqr(list))


# name=['ritik','avantika','paras']
# pos=0
# for i in name:
#    print(f"{pos}======{i}")
#    pos+=1



# def func(l,target):
#    for pos , i in enumerate(l):   
#       if i==target:
#          return f"{pos} == {i}"
#    return -1

# l=['ritik','paras','avantika','harsh']
# print(func(l,'avantika'))

# length = lambda list : 'TRUE' if len(list)>3  else 'FALSE'
# list=[i for i in range(0,2)]    #WE CNA CREATE LIST USING L.C
# print(length(list))




# length = lambda l : 'TRUE' if len([i for i in range(4,19)]) and len([i for i in range(4,19)]) else 'FALSE'
# print(length(list))



# even_odd = lambda l :l [I for I in range(1,11)]

# print(even_odd(l))



# rev = lambda a: 'true' if len(a)<3 else 'false' 
# a=(i for i in range (0,1))
# print(rev('avantika'))


# even = lambda a: 'even' if a%2==0 else  'odd'

# print(even(3))

# even = lambda a:a%2==0
# print(even(3))

# is_even=lambda a,b,c: a%2==0,b%2==0,c%2==0
# print(is_even(2,5,4))
# multiply=lambda a,b : a*b
# multiply(2,3)
# print(multiply)



# def func(l,**kwargs):
# #    return [(i[::-1].title() if kwargs.get('reverse_string')==True else i.title()) for i in l]
   
   
#    if kwargs.get('reverse_str')==True:
#       return [i[::-1].title() for i in l]
#    else:
#       return [i.title() for i in l]

# l=['ritik','paras','avantika']
# print(func(l,reverse_str=True))


# def func(name, **kwrags):
#     if kwargs.get('reverse')==True:
#         return [name[::-1].title() for i in name]
#     else:
#         return [name.title() for i in name]

# name=['ritik','avantika']
        
# print(func(name))

# def rev(l,**kwargs):
#     if kwargs.get('reverse_str')==True:
#        return [l[::-1] for i in l]
#     else:
#        return [l for i in l]

# l=['ritik','avantika']
# print(rev(l,reverse_str=True))

# def myFun(name,*agrs,course='b.tech',**kwargs):
#         print(myFun)
 
# # Driver code
# myFun('ritik kumar','ECE',course='b.tech')   



# def myFun(arg1, *argv):
#     print ("First argument :", arg1)
#     for arg in argv:
#         print("Next argument through argv :", arg)
 
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')







# erse_str=True))


# def name(*args):
#    l1=args.title()
#    return l1
# args=(['ritik','arjun','ujjawal'])
# print(name(args))


# def func(name,*args,last_name='unknown',**kwargs):
#    print(name)
#    print(args)
#    print(last_name)
#    print(kwargs)

# func('ritik',1,2,3,4,'kumar',a=319.8)


# def data (name='unknown',age=20):
#    print(name)
#    print(age)

# data('ritik',22)



# def power(num1,*args):
#    print(num1)
#    print(args)
#    if args:
#       return [i**num1 for i in args]
#    else:
#       return 'ENTER THE ARGS'

# print(power(2,(3,4,5,6)))









# l1=[[i for i in range (1,4)]  for j in range (1,4)]
# print(l1)







# def data(name,*args,last_name='unknown',**kwargs):
#    print(name)
#    print(args)
#    print(last_name)
#    print(kwargs)
# data('ritik',1,2,3,a=319.8)







# def func(**kwargs):
#    for k,v in kwargs.items():
#       print(f"{k} : {v}")
# d={'first_name':'ritik','last_name':'kumar'}
# func(**d)




# def power(n1,*args):
#    if args:
#       return[i**n1 for i in args]
#    else:
#       return 'plss enter args'
# l1=[2,3,4,5]

# print(power(*l1))



# def power(n1,sum,*args):
#    if args:
#       return[i**n1 for i in args]
#    else:
#       return 'plss enter args'
# print(power(2,*(6,7,8),*[4,5,7]))



# n=(1,2,3,4,5)
# if n:
#    print('not empty')
# else:
#    print('empty')



# def cubic(n1,*args):
#    if args:
#       return [i**n1 for i in args ]
#    else:                                                                      
#       return 'enter the args'vv
# lst=[2,2,3,4,5,6]
# print(cubic(*lst))





# def sum(*args):
#    multiply=1
#    for i in args:
#       multiply*=i
#    return multiply 
# l1=(1,2,3,4)
# print(sum(l1))



# def sum(n1,n2,*nums):
#    print(type(n1))
#    print(type(n2))
#    print(n1,n2)
#    print(nums)
#    print(type(nums))
#    total=0
#    for i in nums:
#       total= total+i
#    return total

# print(sum('a',3.2,3,4,5,6,7,8,9,0))


# var={'ritik','harshit','paras'}
# first={i[0] for i in var}
# print(first)



# nums={i:([] if i%2==0 else []) for i in range (1,11)}
# for j,k in nums.items():
#    print(j,k)




# char_count={char:'ritik'.count(char) for char in 'ritik'}
# print(char_count)




# square={i: i**2 for i in range(1,3)}
# print(square)
# for j,k in square.items():






# l1=[[[i for i in range(0,5)],[j for j in range(5,10)],[k for k in range(10,15)]]  for l in range(0,1)]
# print(l1)





# l1=[[i for i in range(1,3)] for j in range(1,4)]
# print(l1)



# def nums(l1):
#    return [str(i) for i in l1 if (type(i)==int or type(i)==float)]
# l1=[1,2,3,'hii',6.7,9.2]
# print(nums(l1))



# l1=[i for i in range(1,11) if i%2==0]
# print(l1)


# square=[-i for i in range(1,6)]
# print(square)


# s={1,2,3,4}

# if 1 in s:
#    print('yes')
# else:
#    print('no')




# USER={}
# USER['NAME']=input("ENTER YOUR NAME ")
# USER['AGE']=int(input("ENTER YOUR AGE "))
# USER['COURSE']=input("ENTER YOUR COURSE")
# s=set(user)
# print(s)






# user= dict_fromkeys(
#    ['name','age','course'],'unmnown'
# )
# print(user)





# user={'name':'ritik',
# 'age':20,                      
# 'course':'b,tech'
# }

# s=set(user)
# print(s)
# print(type(s))

# OUTPUT-
# {'course', 'name', 'age'}
# <class 'set'>
# print(user.clear())

# # user_data={'subject':{'1st year':10,'2nd year':12,'3rd year':12,'final year':7},     #dictionary
# # 'fav-movies':['ra.one','avengers','iron man'],                            #list
# # 'fav:songs':('aviki','soulchef','el shaddai'),                            #tuple
# # 'blood group': 'a'
# # }
# print(user)
# user.update()
# print(user)


# user={'name':'ritik',
# 'age':20,
# 'course':'b,tech'}
# for i,j in user.items():
#    print(i)
   
# print(type(i))
  


# OUTPUT-
# dict_items([('name', 'ritik'), ('age', 20), ('course', 'b,tech')])



#  user={'name':'ritik',
# 'age':20,
# 'course':'b.tech',
# 'subject':{'1st year':10,'2nd year':12,'3rd year':12,'final year':7},
# 'fav-movies':['ra.one','avengers','iron man'],
# 'fav:songs':('aviki','soulchef','el shaddai'),
# 'blood group': 'a'
# }

# print(user)
# print(type(user))
# print(user['name'])
# print(user['age'])
# print(user['course'])
# print(user['subject'])
# print(user['fav-movies'])
# print(user['fav:songs'])
# print(user['blood group'])


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

# s = {1,2,3}
# s1={5,7,6}
# s=s1.copy()
# print(s)
# # s=set(l)
# print(s)
# s=list(set(l))
# print(s)

# user = {}

# user['name'] = input("enter your name ")
# user['age']= input("enter your age ")
# user['course']=input("enter your course ")
# user['branch']=input("enter your branch ")

# for key,value in user.items():
#    print(key,value)



# def char_counter(name):
#    count={}
#    for i in name:
#       count[i] = name.count(i)
#    return count

# print(char_counter('ritik'))





# def cube(n):
#    cubic_values={}
#    for i in range(1,n+1):
#       cubic_values[i]=i**3
#    return cubic_values

# print(cube(3))





# d= dict.fromkeys(
#    ['name','age'],['ubnkmon','unknoum']
# )
# print(d.get('names','it\'s not'))
 
# user = {'name' : 'ritik',
#    'age' : 20,
#    'school':'RGGI',
#    'branch':'E.C.E',
#    'roll_no':1706931006,
#    'profession' : 'ENGINEER',
# }
# # user['mob'] = 8193045571
# # user['add']='meerut'
# # print(user)
# a=user.popitem()
# print(a)
# print(type(a))
# print(user)
   

# for i in user.items():
#    print(i)
#    print(type(i))

# for i in user:
#    print(user[i])
# print(user.keys())
# # user=user.values()
# print(user.values())


# i=0
# while i <user.values():
#    print(i)
#    i =i+1



# user={}
# user['name']='ritik'
# user['age']=20
# print(user)

# mixed= (1,2,3,'hello',[4,5,6],9.8)
# i=0
# while i <len(mixed):
#    print(type(mixed[i]),type(mixed))
   
#    i+=1




# num=str(list((1, 2, 3, 4, 5,'hello', 6, 7, 8, 9, 10)))
# print(num)
# print(type(num))


# def func(a,b):
#    add= a+b
#    multiply=a*b
#    return add, multiply
   
# add,multiply= func(3,5)
# print(f"add is {add}")
# print(f"multiply is {multiply}")
# one= ('two')
# print(type(one))

# tuple=('hii ritik','how','are','you')
# print(tuple)
# print(tuple[:-1:-1])
# print(tuple[::-1])

 



# def difference_list(list):
#    difference=max(list)-min(list)
#    return difference,min(list),max(list)
# list= [27,83,62,5,10]
# print(difference_list(list))


# data = ['harshit','24']
# print(' '.join(data))

# def reversed_list(l):
#    reverse=[]
#    for i in  range(len(l)):
#       r=reversed_list.pop(i)
#       reverse.append(r)

# #       reverse.append(i[::-1])
#    return reverse
# l=['abc','def','ghi','jkl']
# print(reversed_list(l))


# def common_list(list1,list2,list3):
#    common_nums=[]
#    for i in list1:
#       if i in list2 and list3:
#          common_nums.append(i)
#    return common_nums

# list1=[2,3,1,3,5,6]
# list2=[3,5,4,1,7]
# list3=[1,3,2,5,7]
# print(common_list(list1,list2,list3))


# def filter_list(list):
#    odd_nums=[]
#    even_nums=[]
#    for i in list:
#       if i%2==0:
#          even_nums.append(i)
#       else:odd_nums.append(i)
      
#    return [odd_nums]+[even_nums]

# list=[1,2,3,4,5,6,7,8,9]
# print(filter_list(list))


# def reverse_list(list):
#    reverse=[]
#    for i in list:
#       reverse.append(-i)
#    return reverse

# list=['abc','cde','efg']

# print(reverse_list(list))




# def reverse_list(list):
#    reverse=[]
#    for i in range(len(list)):
#       poped_item=list.pop()
#       reverse.append(poped_item)
#    return reverse

# list=[1,2,3,4,5,6,7,8,9,]
# print(reverse_list(list))



# def square(list):
#    e=[]
#    for i in list:
#       e.append(i**90)
#    return e

# list=[2]
# print(square(list))




# def neg_list(l):
#    neg=[]
#    for i in l:
#       neg.append(-i)
#    return neg

# a=[1,2,3,4,5]

# print(neg_list(a))

# n=list(list(range(1,5),range(2,8)))
# print(n)



# a=[1,2,3,[4,5,6]]
# print(type(a))
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix[0][2]
# for submatrix in matrix:
#    for i in submatrix:
#       print(i)
# print(type(matrix))




# a=["apple",8.7,2,4,8,'kiwi']
# for i in a:
#    print(i,end=" ")
# i=0
# while i < len(a):
#    print(a[i])
#    i+=1



# s= "string"
# t=s.title()
# a=s[3]
# print(s)
# print(s[3])
# print(t)
# print(s)



# a=[2,3,4,5,7]
# b=[3,4,8,0,2]
# print(a==b)
# for i in range(0,5):
#     for j in range(5,i,-1):
#         print(j,end='')
#     print("")


# for i in range(0,6):
#    for j in range(6,i,-1):
#       print("*",end=" ")
#    print("")
# for i in range(1,7):
#    for j in range (1,i+1): 
#       print("*",end=" ")
#    print('')



# n= int(input('enter the number : '))

# for i in range(n,0):
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print("")
#    for j in range(1,n):
#       print(j,end=" ")
#    print("")
# for i in range(n,0):
#    for j in range(n,0):
#       print(end=" ")
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print("")

 








# num=[2,3,4,5,1,2,3,6,7]
# num.clear()
# print(num)

# OUTPUT-
# []




# num=[2,3,4,5,1,2,3,6,7]
# SUM= num.copy()
# print(SUM)

# OUTPUT-
# [2, 3, 4, 5, 1, 2, 3, 6, 7]


# num=[2,3,4,5,1,2,3,6,7]
# print(sorted(num))

# OUTPUT-
# [1, 2, 2, 3, 3, 4, 5, 6, 7]

# num=[2,3,4,5,1,2,3,6,7]
# print(num.count(3))

# OUTPUT-
# 2

# NUM= [2,3,5,1]
# NUM.sort()
# print(NUM)
    
# # OUTPUT-
# # [1, 2, 3, 5]


# CHAR= ['BANANA','MANGO','APPLE','KIWI']
# CHAR.sort()
# print(CHAR)

# # OUTPUT-
# # ['APPLE', 'BANANA', 'KIWI', 'MANGO']

# import turtle
# turtle.bgcolor('black')
# star= turtle.Turtle()
# star.pensize(10)
# star.color('red','black')
# star.begin_fill()
# star.left(65)
# star.forward(200)
# star.right(125)
# star.forward(200)
# star.right(145)
# star.forward(240)
# star.right(155)
# star.forward(240)
# star.right(152)
# star.forward(232)
# star.end_fill()
# star.hideturtle()
# turtle.done()







# import turtle
# turtle.bgcolor('black')

# piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200),
#          (-170, 100), (-160, 40), (-170, 10), (-150, -10),
#          (-140, 10), (-40, -20), (0, -20)],
#         [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10),
#          (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
#          (40, 120), (0, 120)]]

# piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0),
#          (-186, -30), (-186, -40), (-120, -170), (-110, -210),
#          (-80, -230), (-64, -210), (0, -210)],
#         [(0, -210), (64, -210),
#          (80, -230), (110, -210), (120, -170), (186, -40), (186, -30),
#          (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]

# piece3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280),
#          (-60, -260), (-30, -260), (-20, -250), (0, -250)],
#         [(0, -250), (20, -250),
#          (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240),
#          (60, -220), (0, -220)]]

# piece1goto = (0,120)
# piece2goto = (0,-30)
# piece3goto = (0,-220)

# def draw_piece(piece,piecegoto):
#     turtle.penup()
#     turtle.goto(piecegoto)
#     turtle.pendown()
#     turtle.color('red')
#     turtle.begin_fill()
#     for i in range(len(piece[0])):
#         x,y =piece[0][i]
#         turtle.goto(x,y)

#     for i in range(len(piece[1])):
#         x,y=piece[1][i]
#         turtle.goto(x,y)

#     turtle.end_fill()

# draw_piece(piece1,piece1goto)
# draw_piece(piece2,piece2goto)
# draw_piece(piece3,piece3goto)

# turtle.hideturtle()
# turtle.done()



# n= ['ritik',8,'ramesh',7.89,6,1]
# n[1:]=['three','four']
# print(n)




# x=5
# def func():
#    global x
#    x=7
#    return x

# print(x)
# print(func())
 



# def fact(n):
#    i=1
#    fact=1
#    while i <= n:
#       fact = fact*i
#       i=i+1
#    return fact

# print(fact(8))



# n=int(input("enter your number"))

# a=0
# b=1
# i=0
# while i<n:
#    print(a,end=" ")
#    count=a+b
#    a=b
#    b=count
#    i=i+1p


# avg=lambda *args:sum(pair)/len(pair) zip(*args) for pair in zip:
# print(avg([2,3,4],[6,4,3]))