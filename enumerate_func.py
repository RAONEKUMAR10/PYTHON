# ENUMERATE FUNCTION //////////////////

# IT IS USE WITH for LOOP TO TRACK POSITION OF OUR ITEM IN ITERABLE

# SYNTAX---------------------------
# for var(position),var(loping) in enumerate(var)(#data):

# Q- PRINTA LIST WITH SOME STRING AND PRINT IT POSITION ALSO 
name=['ritik','avantika','paras']                    #WE CAN WRITE THIS PROGRMA WITHOUT USING ENUMERATE FUNCTION
for pos , i in enumerate(name):                      #  name=['ritik','avantika','paras']
   print(f"{pos} ====>> {i}")                        #  pos=0
                                                     #  for i in name:
# OUTPUT-                                            #     print(f"{pos} ====>> {i}")                                                   
# 0 ====>> ritik                                     #     pos+=1
# 1 ====>> avantika                                  
# 2 ====>> paras                                     # OUTPUT-
                                                     #   0======ritik
                                                     #   1======avantika
                                                     #   2======paras                 


l={'name':'ritik','class':'b.tech','clg':'rggi'}
pos=1
for pos,i in enumerate(l.items()):
   pos+=1
   print(f'{pos}=={i}')
print(type(l))
print(type(pos))
print(type(i))

# OUTPUT-
# 1==('name', 'ritik')
# 2==('class', 'b.tech')
# 3==('clg', 'rggi')
# <class 'dict'>
# <class 'int'>
# <class 'tuple'>



l={'name':'ritik','class':'b.tech','clg':'rggi'}
for pos,i in enumerate(l.items()):
   print(f'{pos}=={i}')
print(type(l))
print(type(pos))
print(type(i))

# OUTPUT-
# 0==('name', 'ritik')
# 1==('class', 'b.tech')
# 2==('clg', 'rggi')
# <class 'dict'>
# <class 'int'>
# <class 'tuple'>