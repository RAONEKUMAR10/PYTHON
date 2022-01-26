n= ['hii',1,1,2,3,4,5,23.987,'hello']
m= [2,3,4,5,6,7,8,9,0]

#  LIST IS A DATA STRUCTURE THAR IS COLLECTION OF ITEMS. WE CAN STORE int,float,string,word in LIST
#  WE CAN CREATE LIST USING SQUARE BRACKETS []

# ADD TWO OR MORE STRINGS

# THERE ARE THREE METHODS 
# 1 .append() METHOD   #{add every element in the last of list}
# 2 .insert() METHOD   #{add any element on any location on list}
# 3 .extend() METHOD   #{it is use add any element/second list after the just end of any element/first list}


# 1  .append() METHOD 

n.append(m)
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello', [2, 3, 4, 5, 6, 7, 8, 9, 0]]

# OR

n.append(2656436)  
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello', 2656436]

# 2 .insert() METHOD

print(m)    
# # [2, 3, 4, 5, 6, 7, 8, 9, 0]
m.insert(8,n)
print(m)

# OUTPUT-
# [2, 3, 4, 5, 6, 7, 8, 9, ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello', 2656436], 0]

# # OR 

m.insert(4,"banana")
print(m)

# OUTPUT-
# [2, 3, 4, 5, 'banana', 6, 7, 8, 9, 0]

# 3 .extend() METHOD

print(n)
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello']
print(m)
# [2, 3, 4, 5, 6, 7, 8, 9, 0]

n.extend(m)
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello', 2, 3, 4, 5, 6, 7, 8, 9, 0]

# OR 

n.extend('ritik')
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello', 'r', 'i', 't', 'i', 'k']

n.extend(['ritik','ujjwal'])
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello', 'ritik', 'ujjwal']



# THERE ARE THREE METHODS TO REMOVE/OPERATOR DATA FROM LIST 

# 1 .pop() METHOD     #{if we do not pass any argument in .pop() method then it defaultly delete last element of list either delete the location which we paas in the argument os .pop() method}
# 2 .del OPERATOR     #{in this we can use STRING SLICING (start indexing,stop indexing,step indexing) }
# 3 .remove() METHOD  #{it is use to delete the first items in between two same elements }


# 1 .pop() METHOD 

print(n)
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello']

n.pop()
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 5, 23.987]

# OR
n.pop(3)
print(n)

# OUTPUT-
# ['hii', 1, 1, 3, 4, 5, 23.987, 'hello']


# 2 .del OPERATOR

print(m)
# [2, 3, 4, 5, 6, 7, 8, 9, 0]

del m[4]
print(m)

# OUTPUT-
# [2, 3, 4, 5, 7, 8, 9, 0]

# OR

del m[2:6:2]
print(m)

# OUTPUT-
# [2, 3, 5, 7, 8, 9, 0]


# 3 .remove() METHOD 

print(n)
# ['hii', 1, 1, 2, 3, 4, 5, 23.987, 'hello']

n.remove(5)
print(n)

# OUTPUT-
# ['hii', 1, 1, 2, 3, 4, 23.987, 'hello']

# OR 

n.remove(1)
print(n)

# OUTPUT-
# ['hii', 1, 2, 3, 4, 5, 23.987, 'hello']



#  in KEYWORD WITH LIST
fruits= ['mango','apple','grapes','kiwi']
if 'kiwi' in fruits:
    print(fruits)
    print("kiwi present in list")
else:print("not in list")

# OUTPUT-
# ['mango', 'apple', 'grapes', 'kiwi']
# kiwi present in list



#  .sort() METHOD

# IT IS USE TO SORT OUR LIST IN ALPHABETICAL ORDER (CHARACTERS) OR IN ASCENDING ORDER (NUMBERS)

NUM= [2,3,5,1]
NUM.sort()
print(NUM)
    
# OUTPUT-
# [1, 2, 3, 5]


CHAR= ['BANANA','MANGO','APPLE','KIWI']
CHAR.sort()
print(CHAR)

# OUTPUT-
# ['APPLE', 'BANANA', 'KIWI', 'MANGO']


#   .count() METHOD

# IT IS USE TO COUNT HOW MANY TIMES A NUMBER , WORD,CHARACTER IS PRESENT IN OUR LIST

num=[2,3,4,5,1,2,3,6,7]
print(num.count(3))

# OUTPUT-
# 2


#  SORTED FUNCTION

#  WHEN WE DON'T WANT TO SORT OUR LIST BUT  PRINT OUR LIST AS A SORTED LIST THEN WE SORTED FUNCTION

num=[2,3,4,5,1,2,3,6,7]
print(sorted(num))

# OUTPUT-
# [1, 2, 2, 3, 3, 4, 5, 6, 7]

# BUT OUR LIST IS STILL UNSORTED IF WE PRINT IT THEN WE GE THAT-
print(num)
# [2,3,4,5,1,2,3,6,7]


#   .copy() METHOD

# IT IS USE TO COPY A LIST IN ANOTHER VARIABLE

num=[2,3,4,5,1,2,3,6,7]
SUM= num.copy()
print(SUM)

# OUTPUT-
# [2, 3, 4, 5, 1, 2, 3, 6, 7]



#   .clear()  METHOD

# IT IS USED TO CLEAR OUR LIST

num=[2,3,4,5,1,2,3,6,7]
num.clear()
print(num)

# OUTPUT-
# []