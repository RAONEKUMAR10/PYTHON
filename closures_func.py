# CLOSURES FUNCTION IS ALSO KNOWN AS FUNCTION RETURN FUNCTION OR FIRDT CLASS FUNCTION 

def to_power(x):   #X=3
   def calc_power(n): #N=2
      return n**x #2**2
   return calc_power #8

cube=to_power(3)
print(cube(2))

# OUTPUT-
# 8

# Also work for calculate square----------------

def to_power(x):   #X=2
   def calc_power(n): #N=2
      return n**x #2**2
   return calc_power #4

square =to_power(2)
print(square(2))

# OUTPUT-
# 4

# THIS FUNCTION IS USED TO CALCULATE ANY POWER OF ANY NUMBER///////////////////////////////////////////