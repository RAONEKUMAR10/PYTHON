n= int(input("enter the number  "))
fact=1
i=1
while i <n:
   fact += fact*i
   i +=1
print(f"THE FACTORIAL OF {n} IS {fact}")

# OUTPUT-
# enter the number  12
# THE FACTORIAL OF 12 IS 479001600


n= input('enter your name= ')
var=""
i=0
while i<len(n):
   var= var+n[i]
   print(var)
   i=i+1

# OUTPUT-
# enter your name= ritik kumar
# r
# ri        
# rit       
# riti      
# ritik     
# ritik     
# ritik k   
# ritik ku  
# ritik kum 
# ritik kuma
# ritik kumar





import datetime
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())

NAME = input("ENTER YOUR NAME HERE :- ")
temp_var=""
i=0
while i<len(NAME):
    if NAME[i] not in temp_var:
        temp_var += NAME[i]
        print(f"{NAME[i]} :  {NAME.count(NAME[i])}")
    i+=1

# OUTPUT-
# 2021-05-12
# 16:36:51.478590
# ENTER YOUR NAME HERE :- ritik kumar
# r :  2
# i :  2
# t :  1
# k :  2
#   :  1
# u :  1
# m :  1
# a :  1






number= int(input())

print(number)

i=1
while i<=10:
   print(i)
   i +=1

# OUTPUT-
# 1
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 10   




i=0
str= "javatpoint"
while i<len(str):
   if str[i]=='o':
      i +=1
      break
   print(str[i])
   i +=1

# OUTPUT- 
# j
# a
# v
# a
# t
# p




i=0
str= "javapoint"
while i < len(str):
   if str[i]=='a' or str[i]=='t':
      i +=1
      continue
   print(str[i])
   i +=1

# OOUTPUT-
# j
# v
# p
# o
# i
# n