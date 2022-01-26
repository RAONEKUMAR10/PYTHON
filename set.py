#  SET DATA TYPE
# It is a unordered collection of unique items
# in this there is no KEY-VALUE pair 
# We can't  store list , dictionary & tuple in SET
# SET is create by using '{}' CURLEY BRACKETS.
# In SET we can store int,float,string etc.

from builtins import set

set1={1,1.0,2,3,5.64,'hiii'}
print(set1)

# OUTPUT-
# {1, 2, 3, 5.64, 'hiii'}

# Duplicate values are not in output and order can be change of output.
# 1,1.0==1

# SET IS ALSO A FUNCTION set() FUNCTION///////////////////////////////////////
# It is use to change list,tuple,dictionary into set

l=[1,2,3,5,3,4,6,7,2,6,'hii','hello','heyy','hii']
s=set(l)
print(s)

# OUTPUT-
# {1, 2, 3, 4, 5, 6, 7, 'hii', 'hello', 'heyy'}

s=list(set(l))
print(s)

# OUTPUT-
# [1, 2, 3, 4, 5, 6, 7, 'hello', 'heyy', 'hii']

user={'name':'ritik',
'age':20,                      
'course':'b,tech'
}

s=set(user)
print(s)
print(type(s))

# OUTPUT-
# {'course', 'name', 'age'}
# <class 'set'>


tuple1=(1,2,3,4.5,'hii','hello')
s=set(tuple1)
print(s)
print(type(s))

# OUTPUT-
# {1, 2, 3, 4.5, 'hello', 'hii'}
# <class 'set'>


#  .add() METHOD///////////////////////////
# it is use to add elements in set

s={1,2,3,5}
s.add(4)
print(s)

# OUTPUT-
# {1, 2, 3, 4, 5}


# .remove() METHOD
# It is use to remove elements from set

s={1,2,3,5}
s.remove(3)
print(s)

# OUTPUT-
# {1, 2, 5}

# s.remove(6)
# print(s)

# OUTPUT-
# KeyError: 6

#  .discard() METHOD
# To avoid  KEYERROR in .remove() method

s={1,2,3,4,5}
s.discard(3)
print(s) 

# OUTPUT-
# {1, 2, 4, 5}

s.discard(9)
print(s)

# OUTPUT-
# {1, 2, 3, 4, 5}


#   .clear() METHOD
# It is use to clear set

a={1,2,3,4,5,6}
a.clear()
print(a)

# OUTPUT-
# set()


#  .copy() METHOD
# It is used to copy one set in another set

s={1,2,3,4,5,6,7,87}
s1=s.copy()
print(s1)

# OUTPUT-
# {1, 2, 3, 4, 5, 6, 7, 87}



#  'in' KEYWORD in SET/////////////////////////////
# It is use to check that the element is present in set or not

s={'a',1,2,3,4}

if 'a' in s:
   print('yes')
else:
   print('no')

# OUTPUT-
# yes

# 'in' KEYWORD USING LOOP/////////////////////////////////////

s={1,2,3,4}

for i in s:
   print(i)

# OUTPUT-
# 1
# 2
# 3
# 4


#  SET MATHS//////////////////////////////////

# UNION/////////////
# It is use to combine two sets and remove duplicates.
# It is define by '|' PIPE

s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
set= s1|s2
print(set)

# OUTPUT-
# {1, 2, 3, 4, 5, 6, 7, 8, 9}


# INTERSECTION//////////////////////////
# It is use to print common elements between two sets.
# It is define by '&' END.

s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
set= s1&s2
print(set)

# OUTPUT-
# {4, 5}