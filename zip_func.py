#   ZIP() FUNCTION

# IT IS USE TO COMBINE TwO OR MORE THEN TWO LIST ,SET,TUPLE.
# IT RETURN A OBJECT WHICH WE CAN STORE IN LIST,SET,TUPLE,DICTIONARY.
# THE VALUE OF OBJECT IS IN TUPLE THAT MEANS IT MAKE A PAIR IN TUPLE

name=['ritik','ujjwal','arjun']
last_name=('kumar','singh','thakur')
print(zip(name,last_name))

# OUTPUT-
# <zip object at 0x0000022CA2A98900>

# BUT IF WE DO-

print(set(zip(name,last_name)))

# OUTPUT-
# {('ujjwal', 'singh'), ('ritik', 'kumar'), ('arjun', 'thakur')}

# IF WE HAVE A LIST CONTAINING 3 ELEMENTS AND A LIST CONTAINING 2 OR 4 ELEMENTE THEN THE ZIP FUNCTION ONLY PAIR OF THOSE ELEMENTE WHO 
# HAVE IN BOTH LIST

S=['A','B','C']
N=[1,2,3,4,5] 
print(tuple(zip(S,N)))

# OUTPUT-
# (('A', 1), ('B', 2), ('C', 3))

# OR IF WE DO-

S=['A','S','D','F','G']
N=(1,2,3,)
print(set(zip(N,S)))

# OUTPUT-
# {(3, 'D'), (1, 'A'), (2, 'S')}

# WE CAN GAVE ARGUMENT IN ANY ORDER FOR ABOVE EXAMPLE FIRST WE HAVE "S" AND THEN WE HAVE "N" BUT IN ZIP FUNCTION WE GAVE ARGUMENTS
# AS "N" AND "S" 

# IF WE HAVE A LIST OR SET OR TUPLE WHICH HAVE A TWO VALUE INSIDE THE TUPLE THEN WE CAN DIRECTLY CONVERT INTO A DICTIONARY

L=[('A',2),('B',4,)]
print(dict(L))

# OUTPUT-
# {'A': 2, 'B': 4}

# BUT IF WE USE USE ZIP() FUNCTION THEN WE GET AN ERROR BECAUSE ZIP() FUNCTION REQUIRE 2 OR MORE THEN 2 VARIABLE
#  TO COMBINE IT IN A LIST,SET,TUPLE. BUT WE CAN'T COMBINE IT IN A DICTIONARY

L=[('A',2),('B',4,)]
N=(5,6)
S={'A','B'}
F=[32.3,76.9]
print(list(zip(L,N,S,F)))

# OUTPUT-
# [(('A', 2), 5, 'A', 32.3), (('B', 4), 6, 'B', 76.9)]


# *ARGS IN ZIP() FUNCTION //////////////////////////////////////////////////////////

L=[(1,2),(3,4),(5,6)]
print(list(zip(*L)))

# OUTPUT-
# [(1, 3, 5), (2, 4, 6)]

L=[(1,2),(3,4),(5,6)]
L1,L2=zip(*L)
print(f"L1 == {L1}")
print(f"L2 == {L2}")


# OUTPUT-
# L1 == (1, 3, 5)
# L2 == (2, 4, 6)


#Q- FIND BIGGER ANS SMALLER NUMBER IN BETWEEN TWO LIST AND  CONVERT IT INTO A ZIP 

L1=[2,4,8,5]
L2=[3,6,1,7]
MX=[]
MN=[]
print(list(zip(L1,L2)))
for pair in zip(L1,L2):
   MX.append(max(pair))
   MN.append(min(pair))
print(MX)
print(MN)

# OUTPUT-
# [(2, 3), (4, 6), (8, 1), (5, 7)]
# [3, 6, 8, 7]
# [2, 4, 1, 5]


# Q- DEFINE A FUNCTION TAKE ANY NO. OF LISTS CONTAINING NUMBER AND RETURN AVERAGE OF LIST

def avg(*args):
   average=[]
   for pair in zip(*args):
      average.append(sum(pair)/len(pair))
   return average

print(avg([1,2,3,4],[8,9,7,9]))

# OUTPUT-    ((1+8)/2)  etc....
# [4.5, 5.5, 5.0, 6.5]


# USING LAMBDA FUNCTION //////////////////////////////////////

avg=lambda *args:[sum(pair)/len(pair)  for pair in zip(*args)]
print(avg([2,3,4],[6,4,3]))


# OUTPUT-
# [4.0, 3.5, 3.5]   
