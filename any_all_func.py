#  ALL() FUNCTION & ANY() FUNCTION 

# ALL() FUNCTION /////////////////////////////////////////////////////////////

# ALL FUNCTION AND WE CAN USE LIST COMPREHENSIONS,DICT COMPREHENSIONS AND ETC.
#  ALL() FUNCTION IS USED TO CHECK THAT THE ALL THE CONDITIONS ARE SATISFIED .
# IF ALL CONDITIONS ARE SATISFIED THEN IT GAVE BACK "TRUE" OR IF ANY ONE CONDITION ARE NOT SATISFIED THEN IT GAVE US "FALSE".
# WE CAN DIRECTALY PRINT IT .
# 

numbers1=[2,4,6,8,12,14,4]
print(all([num%2==0 for num in numbers1]))

# OUTPUT-
# True   #OUR ALL ELEMENTS OF LIST IS SATISFIED IN CONDITION THATS WHY WE GET "True"

# BUT IF WE DO-

numbers1=[2,4,3,8,12,14,4]
print(all([num%2==0 for num in numbers1]))

# OUTPUT-
# False   #OUR ALL ELEMENTS OF LIST IS NOT SATISFIED IN CONDITION THATS WHY WE GET "False"


# ANY() FUNCTION //////////////////////////////////////

# IF ANY ONE CONDITION WILL BE TRUE THEN WE GET BACK "True" OR  IF OUR ALL CONDITIONS ARE FALSE THEN WE GET BACK "False"


numbers1=[1,3,5,2,9,11,13,15]
print(any([num%2==0 for num in numbers1]))

# OUTPUT- 
# True    # BECAUSE ONE CONDITION IS TRUE THATS WHY  WE GET BACK "True"

# BUT IF WE DO-

numbers1=[1,3,5,7,9,11,13,15]
print(any([num%2==0 for num in numbers1]))

# OUTPUT-.
# False   # BECAUSE ALL CONDITIONS IS FALSE THATS WHY WE GET BACK "False"




def add(*args):
   if all([(type(num)==int or float) for num in args]):
      total=0
      for i in args:
         total+=i
      return total
   else:
      return "wrong input"
print(add(2,1,5,3,4,8,7.3))

# OUTPUT-
# 30.3

# IF WE DO-

print(add(2,1,5,3,'RITIK',4,8,7.3))

# OUTPUT-
# wrong input


  
  
  
  
  
   