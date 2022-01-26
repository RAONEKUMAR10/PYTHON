# class My:
#    print('this is my frist class')
#    def __init__(self,name,last_name,age):
#       #instance variables
#        self.name=name
#        self.last_name=last_name
#        self.age=age


# p1=My('ritik','kumar',22)
# p2=My('avantika','tomar',21)
# print(p1.name,p2.name)

# print(p1.name)
# print(p2.age)


# class Bike:
#    def __init__(self,model,year,price):
#       self.model=model
#       self.year=year
#       self.price=price
#       # we can declare a instance variable who hold the values of "__init__" function
#       self.company=model+" "+year

# b1=Bike("yamaha",'2002',88000)
# b2=Bike('hero','2007',55000)
# print(b1.year)
# print(b2.model)
# print(b1.model,b2.year)
# print(b1.company)


# INSTANCE METHOD///////////////////////////////////////

# IT IS RELATED TO INSTANCE 
# INSTANCE ALSO KNOWN AS OBJECT

# class Person:
#    def __init__(self,first_name,last_name,age):
#       self.first_name=first_name
#       self.last_name=last_name
#       self.age=age
#       self.full_name=first_name+" "+last_name  #here we can't use this instance variable either we get an error
#    def full_name(self):
#       return f"{self.first_name} {self.last_name}"

#    def is_above(self):  #here we don't need any other attribute or instance to define because in our class age is already defined
#       if self.age>18:
#          return 'ADULT'
#       return 'KID'
      

# p1=Person('ritik','kumar',22)  
# # print(p1.full_name())
# print(p1.is_above())
# # or we can do it

# print(Person.full_name(p1))

# we get an same output as same as previous

# exg==================================

# THESE ARE THE PROCESS BEHIND OF CLASS  
# l=[1,2,3]
# l.append(6)
# print(l)

# output-
# [1, 2, 3, 6]

# or we can do
# list.append(l,8)
# print(l)

# output-
# [1, 2, 3, 6, 8]

# exg================================

# class Bike:
#       def __init__(self,model,year,price):
#          self.model=model
#          self.year=year
#          self.price=price
#       # we can declare a instance variable who hold the values of "__init__" function
#          self.company=model+" "+year
#       def discount(self,n):
#          return self.price-(self.price*n/100)
# b1=Bike("yamaha",'2002',88000)
# b2=Bike('hero','2007',55000)
# print(b1.year)
# print(b2.model)
# print(b1.model,b2.year)
# print(b1.company)
# print(b1.discount(30))


# CLASS VARIABLE////////////////////////////////////////////////////

# THIS IS DEFINE IN CLASS BEFORE DEFINE "__init__" FUNCTION OR ANY OTHER FUNCTION
# AFTER DEFINE IT WE DON'T HAVE TO DEFINE IT IN "__init__" FUNCTION PARAMETER
# WE JUST HAVE TO CALL IT WITH THIS SYNTAX------------------------------------------------------------------------

# CLASS_NAME.CLASS_VARIABLE_NAME

# class Circle:
#    pi=3.14 # CLASS_VARIABLE
#    def __init__(self,radius):
#       self.radius=radius
#    def circumference (self):
#       # circle_circumference == 2*pi*radius
#       return 2*Circle.pi*self.radius

# c1=Circle(23)
# print(c1.circumference())

# c2=Circle(12)
# print(c2.circumference())
      

# class Bike:
# # IF WE WANT TO GAVE SAME DISCOUNT AT ALL LAPTOPS THEN HERE WE CAN USE CLASS VARIABLE
#       discount=10
#       def __init__(self,model,year,price):
#          self.model=model
#          self.year=year
#          self.price=price
#       def discount_apply(self):
#          return self.price-(self.price*Bike.discount/100)

# b1=Bike("yahama",2001,320000)
# print(b1.discount_apply())

# b2=Bike('tvs',1998,89000)
# print(b2.discount_apply())

# # WE CAN FINISH THE DISCOUNT ON OUR BIKES THEN WE HAVE TO DO------
# Bike.discount=0  #HERE WE CAN APPLY DISCOUNT WHAT EVER WE WANT
# b1=Bike("yahama",2001,320000)
# print(b1.discount_apply())

# b2=Bike('tvs',1998,89000)
# print(b2.discount_apply())

# BUT IF WE WANT TO GAVE DIFFERENT DISCOUNT ON DIFFERENT LAPTOP  THEN WE HAVE TO USE "self" INSTED OF "CLASS_VARIABLE"-----------

# class Bike:
#       discount=10
#       def __init__(self,model,year,price):
#          self.model=model
#          self.year=year
#          self.price=price
#       def discount_apply(self):
#          return self.price-(self.price*self.discount/100) #HERE WE USE "self.discount" INSTED OF "BIKE.discount"-----------


# b1=Bike("yahama",2001,320000)
# b1.discount=30 #HERE WE CAN APPLY DISCOUNT WHAT EVER WE WANT
# print(b1.discount_apply())
# print(b1.__dict__)


# b2.discount_apply=87
# b2=Bike('tvs',1998,89000)
# print(b2.discount_apply())


# IF WE  WANT TOKNOW THAT WHAT PARAMETERS HAVE OUR OBJECT THEN WE CAN DO-----------------

# SYNTAX-------

# print(OBJECT_NAME.__dict__)

# print(b1.__dict__)

# OUTPUT-
# {'model': 'yahama', 'year': 2001, 'price': 320000}


# exg=========

# class Cricket:
#    count_instance=0
#    def __init__(self,region_name,team_name,captain,trophy,win_year):
#       Cricket.count_instance+=1
#       self.region_name=region_name
#       self.team_name=team_name
#       self.captain=captain
#       self.trophy=trophy
#       self.win_year=win_year
      
   

# I=Cricket('ASIA','INDIA','DHONI',['WORLD_CUP','T-20 WORLD_CUP','CHAMPIONS_TROPHY'],[2011,2007,2013])  #INSTANCE=1
# E=Cricket('EUROPE','ENGLAND','MORGAN',['WORLD_CUP','T-20 WORLD_CUP'],[2019,2011])  #INSTANCE=2
# print(I.trophy)
# print(I.win_year)
# print(E.captain)
# print(Cricket.count_instance)


# CLASS METHODS/////////////////////////////////////////////////////////////
# IT USE RARERLY 
# IT IS RELATED TO CLASS  

# SYNTAX-----------
# CLASS_NAME.METHOD_NAME()  

# IN CLASS METHOD FIRST ARGUMENT IS CLASS INSTED OF SELF AND IT IS DENOTED BY "cls".
 
# WE USE DECORATORS WHUCH IS PREDEFINED "@classmethod"
 
# class Cricket:
#    count_instance=0
#    def __init__(self,region_name,team_name,captain,trophy,win_year):
#       Cricket.count_instance+=1
#       self.region_name=region_name
#       self.team_name=team_name
#       self.captain=captain
#       self.trophy=trophy
#       self.win_year=win_year
#    @classmethod
#    def count_instances(cls):
#       return f"you have {cls.count_instance}  instance of Cricket class"
#    def champion(self):
#       return f"{self.team_name} champion of  {self.trophy} {self.win_year} "
# I=Cricket('asia','india','dhoni','all_icc_cups',2011)
# E=Cricket('europe','england','morgan','world_cup',2019)
# print(I.trophy)
# print(Cricket.count_instances())
# print(I.champion())


# OUTPUT-
# all_icc_cups
# you have2  instance of Cricket class
# india all_icc_cups 2011

# OR WE CAN CALL CLASS INSTANCES BY ITS OBJECT NAME 

# print(I.count_instances())
# OUTPUT-
# you have2  instance of Cricket class


# CLASS METHOD AS A CONSTRUCTOR ///////////////////////////////////////////

# BY USING THESE FUNCTION WE CAN CREATE OUR CONSTRUSTOR LIKE PRE DEFINED CONSTRUCTOR "__init__".

#IT IS DEFINED BY USING PRE DEFINED DECORATOR 

# @countmethod
#    def constructor_name(cls,parameter):
#       functionality of function
#       return cls(functionaloty of function)

# class Person:
#    def __init__(self,first_name,last_name,age):
#       self.first_name=first_name
#       self.last_name=last_name
#       self.age=age
#       self.full_name=first_name+" "+last_name  #here we can't use this instance variable either we get an error
   # @classmethod
   # def from_string(cls,string):
   #    first,last,age=string.split(',')
   #    return cls(first,last,age)
   # def full_name(self):
   #    return f"{self.first_name} {self.last_name}"

# p1=Person('ritik','kumar',22)
# p2=Person('avantika','tomar',21)
# p3=Person.from_string('ujjwal,singh,19') #calling our classmethod
# print(p3.full_name())
# print(p3.full_name())



# STATIC METHOD//////////////////////////////////////////////

# IT IS LOGICALLY CONNECTED TO OUR CLASS
# TO DEFINE STATIC METHOD WE USE PREDIFNE DECORATOR "@staticmethod"

# WE DON'T NEED TO DEFINE ANY FIRST ARGUMENT LIKE "cls" AND "self"

# class Person:
#    def __init__(self,first_name,last_name,age):
#       self.first_name=first_name
#       self.last_name=last_name
#       self.age=age
#       self.full_name=first_name+" "+last_name  #here we can't use this instance variable either we get an error
#    @classmethod
#    def from_string(cls,string):
#       first,last,age=string.split(',')
#       return cls(first,last,age)

#    @staticmethod
#    def hello():
#       print('hello,static method called')
#    def full_name(self):
#       return f"{self.first_name} {self.last_name}"

# p1=Person('ritik','kumar',22)
# p2=Person.from_string('ujjwal,singh,19')
# Person.hello()

# OUTPUT-
# hello,static method called




# FUNDAMENTAL CONCEPT OF OBJECT ORIENTED PROGRAMMING/////////////////////////////////////////

# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.model_name=model_name
#          self.price=price
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{brand} {model_name}"
   
# p1=Phone("xiaomi","redmi A",8500)
# print(p1.model_name)


# ENCAPSULATION :- WHENB DE DEFINE ALL OUR DATA AND IT'S METHOD AT SAME PLACE THEN IT IS KNOWN AS ENCAPSULATION
# EXG :- ALL ABOVE THE CLASS AND OBJECT WE DEFINE AT THE SAME PLACE ARE THE EXAMPLE OF ENCAPSULATION



# ABSTRACTION :- IT IS DEFINE AS TO HIDE THE COMPLIXITY FROM USER OR THE PROCESS OF OUR FUNCTION WICH IS IN PROCESS OF WHEN WE CALL HE FUNCTION
# EXG :- 
# l=[1,2,3,4]
# ln=len(l)
# print(ln)
 
# OUTPUT-
# 4

# WE HAVE A OUTPUT 4 BUT WE CAN'T SEE THE PROCESS BEHIND THE len() FUNCTION WE USE 
# THIS IS CALLED ABSTRACTION


# NOTE :- FOR ABSTRACTION WE NEED TO FIRST DEFINE ENCAPSULATION 

# NAMING CONVENTION//////////////////////////

# IN PYTHON EVERY THING IS PUBLIC NOTHING IS PRIVATE BUT IF WE WANT TO MAKE SOMETHING DIFFERENT FROM PUBLIC THAT LOOK LIKE IT IS NOT PUBLIC
# THEN WE USE NAMING CONVENTION 
# EXG:- _NAME 
# WE USE ONE UNDERSCORE BEFORE OUR VARIABLE TO SHOW THAT THIS IS A PRIVATE METHOD .
# BUT THE THING IS THAT IT CAN BE CHANGE IT BECAUSE AS I FIRST SAID THAT IN PYTHION EVERY THING IS PUBLIC NOTHING IS PRIVATE


# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.model_name=model_name
#          self._price=price  #NAMING CONVENTION
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{brand} {model_name}"

# P2=Phone('vivo','y51',15000)
# print(P2._price)
# OUTPUT-
# 15000

# WE CAN CHANGE THE VALUE OF PRICE WHENEVER WE WANT
# P2._price=13000
# print(P2._price)
# OUTPUT-
# 13000


# NAMING MANGLING//////////////////////////////////////////////////

# IN NAMEING CONVENTION WE USE DOUBLE UNDER SCORE BEFORE VARIABLE,OBJECT,INSTANCE.
# EXG:-  " __NAMEOF" 
# IT IS ALSO KNOWN AS DUNDER AND MAGIC METHOD IT IS USE WE CREATE OBJECT AND INSTENCES



# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.__model_name=model_name
#          self._price=price  #NAMING CONVENTION
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{brand} {model_name}"

# P2=Phone('vivo','y51',15000)
# print(P2.__model_name)

# OUTPUT-
# AttributeError: 'Phone' object has no attribute '__model_name' 

# WE GET AN ERROR . TO CHECK WE USE DATA DISCRIPTER "__dict__"
# print(P2.__dict__)
# OUTPUT-
# {'brand': 'vivo', '_Phone__model_name': 'y51', '_price': 15000}
# PYTHON SELF CHANGE IT IN THIS FORMAT FOR USE IN ONLY  THIS CLASS

# TO PRINT OUR NAMING MANGLIG WE HAVE TO USE THIS SYNTAX--------------

# SYNTAX----------
# print(ObjectName._ClassName__NamingMangling)

# SO NOW WE CAN DO-

# print(P2._Phone__model_name)

# OUTPUT-
# y51

# P2._Phone__model_name= 'y21'
# print(P2._Phone__model_name)

# OUTPUT-
# y21



# PROPERTY,SETTER() AND GETTER() DECORATOR////////////////////////////////////////////////



# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.__model_name=model_name
#          self._price=price  #NAMING CONVENTION
#          self.specification=f"specifications are {brand} {model_name} {price}"
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{self.brand} {self.__model_name}"
   

# P2=Phone('vivo','y51',15000)
# print(P2.brand)
# print(P2._Phone__model_name)
# print(P2._price)
# print(P2.specification)

# OUTPUT-
# vivo
# y51
# 15000
# specifications are vivo y51 15000
 
# but if we do-----

# P2._price=-1345
# print(P2._price)
# print(P2.specification)

# OUTOUT-
# -1345    #HERE WE CAN SEE THAT PRICE IS UPDATE 
# specifications are vivo y51 15000       # BUT HERE WE CAN SEE THAT PRICE IS STILL SAME AS BEFORE HERE IS NO CHANGE

# TO REMOVE THIS BUG WE DO------

# USE "max()"  
# 
# WE EASILY CAN DO WITH IF-ELSE LOOP BUT WITH THE HELP OF "max()" MAKE IT MORE EASIER

# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.__model_name=model_name
#          self._price=max(price,0)  #NAMING CONVENTION
#          self.specification=f"specifications are {brand} {model_name} {price}"
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{self.brand} {self.__model_name}"

# P2=Phone('vivo','y51',-1220)
# print(P2.brand)
# print(P2._Phone__model_name)
# print(P2._price)
# print(P2.specification)

# OUTPUT-
# vivo
# y51
# 15000
# specifications are vivo y51 15000

# NOW IF WE DO PRICE NEGATIVE OR LESS THEB ZERO ----

# P2._price=-1190
# print(P2._price)
# print(P2.specification)
# WE CAN SEE THAT VALUE IS CHANGE ONLY IF WE CHANGE IN WHEN WE DEFINE INSTANCE
#TO REMOVE THIS BUG WE CAN DO ONE THING THAT  WE CAN DEFINE FUNCTION INSTED OF INSTANCE METHOD 

# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.__model_name=model_name
#          self._price=max(price,0)  #NAMING CONVENTION
#          # self.specification=f"specifications are {brand} {model_name} {price}"
#    def specification(self):
#       return f"{self.brand} {self.__model_name} {self._price}"
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{self.brand} {self.__model_name}"

# P2=Phone('vivo','y51',-1220)
# print(P2.brand)
# print(P2._Phone__model_name)
# print(P2._price)
# print(P2.specification())

# OUTPUT-
# vivo
# y51
# 0
# vivo y51 0

# BUT IF WE DO-
# P2._price=-19000  #HERE WE CHANGE THE  PRICE WITHOUT CHANGING IN INSTANCE VARIABLE
# print(P2._price)
# print(P2.specification())

# OUTPUT-
# 19000
# vivo y51 -19000    HERE WE CAN SEE THAT WE CAN GAVE VALUE IN NEGATIVES



# P2._Phone__model_name='nokia'
# print(P2._Phone__model_name)
# print(P2.specification())

# OUTPUT-
# nokia
# vivo nokia 19000

# TO REMOVE THESE 

# PROPERTY DECORATOR AND SETTER DECORATOR /////////////////

# class Phone:
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.__model_name=model_name
#          self._price=max(price,0)  #NAMING CONVENTION
#          # self.specification=f"specifications are {brand} {model_name} {price}"
#    def specification(self):
#       return f"{self.brand} {self.__model_name} {self._price}"
#    def make_call(self,phone_number):
#       print(f"calling {phone_number}....")
#    def full_name(self):
#       return f"{self.brand} {self.__model_name}"

#    @property               #THIS IS A PREDEFINE DECORATOR IN PYTHON 
#    def price(self):
#       return self._price
   # AFTER DEFINE THIS WE HAVE TO DEFINE @setter 
   # SYNTAX 
   # @NAME.setter
#    @price.setter
#    def price(self,new_price):
#       self._price=max(new_price,0)

# P2=Phone('vivo','y51',-1220)     #NOW IF USE O
# print(P2.brand)
# print(P2._Phone__model_name)
# print(P2._price)
# print(P2.specification())

# OUTPUT;
# vivo
# y51
# 0
# vivo y51 0



# INHERITANCE////////////////////////////////////////////////////////

# IN THIS METHOD WE DEFINE A PARENT CLASS IN ANOTHER CHID/DERIVED CLASS
# THERE ARE TWO WAYS TO DEFINE INHERITANCE

# FIRST METHOD------------------------------

# NOTE :- THIS IS A UNCOMMON WAY AND USE VERY RARELY

# class Phone:    #PARENT CLASS
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.model_name=model_name
#          self.price=price 
         
#    def specification(self):
#       return f"{self.brand} {self.model_name} {self.price}"
#    def make_call(self,phone_number):
#       return f"calling {phone_number}...."
#    def full_name(self):
#       return f"{self.brand} {self.model_name}"

# class Smartphone(Phone):    #DERIVED/CHILD CLASS 
#    def __init__(self,brand,model_name,price,ram,camera):   #HERE WE DEFINE SELF AND FEATURES OF PARENT CLASS ADD SOME OTHER FEATURE WHICH IS NOT IN OUR PARENT CLASS
#       Phone.__init__(self,brand,model_name,price)     #HERE WE CALL OUR PARENT CLASS WITH ITS FEATURE THAT WE WANT TO HANDEL BY PARENT CLASS
#       self.ram=ram          #HERE WE DEFINE THAT FEATURE WHICH IS NEW IN CHILD CLASS
#       self.camera=camera    #
   # def full_specification(self,specification,ram,camera)
      # return 
      #WE DON'T HAVE TO REDEFINE ANY METHOD/FUNCTION WHICH IS ALREADY DEFINE IN PARENT CLASS BECAUSE THEY WILL BE HANDEL BY PARENT CLASS
 
# P1=Phone('VIVO','Y31',15000)
# P2=Smartphone('XIAOMI','REDMI 8',8500,'4GB','13MP')

# print(P1.specification())
# print(P2.specification())
# print(P2.full_name())
# print(P1.make_call(8193045571))
# print(P2.ram)
# print(P2.camera)
# print(P2.make_call(7983689212))

# OUTPUT-
# VIVO Y31 15000
# XIAOMI REDMI 8 8500
# XIAOMI REDMI 8
# calling 8193045571....
# 4GB
# 13MP
# calling 7983689212....



# SECOND METHOD ------------------------

# IN THIS METHOD WE USE "super()" METHOD TO CALL PARENT CLAS IN CHILD CLASS 
# IN TIS METHID EVERY THING IS SAME JUST WE USE "super()" METHOD INSTED OF 

# class Phone:    #PARENT CLASS/BASE CLASS
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.model_name=model_name
#          self.price=price 
         
#    def specification(self):
#       return f"{self.brand} {self.model_name} {self.price}"
#    def make_call(self,phone_number):
#       return f"calling {phone_number}...."
#    def full_name(self):
#       return f"{self.brand} {self.model_name}"

# class Smartphone(Phone):    #DERIVED/CHILD CLASS 
#    def __init__(self,brand,model_name,price,ram,camera):   #SAME AS PREVIOUS METHOD WE HAVE TO DEFINE "__init__" FUNCTION
#       super().__init__(brand,model_name,price) #NOT USE OF "self"  IT IS HANDEL BY "super()"
#       self.ram=ram                             #WHEN WE USE "super()" THEN "self"  IS NOT USE
#       self.camera=camera

# P1=Phone('VIVO','Y31',15000)
# P2=Smartphone('XIAOMI','REDMI 8',8500,'4GB','13MP')
 
#STILL WE GET SAME OUTPUT AS WE GET  PREVIOUS/ABOVE METHOD
# print(P1.specification())
# print(P2.specification())
# print(P2.full_name())
# print(P1.make_call(8193045571))
# print(P2.ram)
# print(P2.camera)
# print(P2.make_call(7983689212))
# OUTPUT-
# VIVO Y31 15000
# XIAOMI REDMI 8 8500
# XIAOMI REDMI 8
# calling 8193045571....
# 4GB
# 13MP
# calling 7983689212....




# MULTILEVEL INHERITANCE ///////////////////////////////////////////////////

# class Phone:    #PARENT CLASS/BASE CLASS
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.model_name=model_name
#          self.price=price 
         
#    def specification(self):
#       return f"{self.brand} {self.model_name} {self.price}"
#    def make_call(self,phone_number):
#       return f"calling {phone_number}...."
#    def full_name(self):
#       return f"{self.brand} {self.model_name}"

# class Smartphone(Phone):    #DERIVED/CHILD CLASS 
#    def __init__(self,brand,model_name,price,ram,camera):   #SAME AS PREVIOUS METHOD WE HAVE TO DEFINE "__init__" FUNCTION
#       super().__init__(brand,model_name,price) #NOT USE OF "self"  IT IS HANDEL BY "super()"
#       self.ram=ram                             #WHEN WE USE "super()" THEN "self"  IS NOT USE
#       self.camera=camera

# class Flagshipphone(Smartphone):
#    def __init__(self,brand,model_name,price,ram,camera,processor,battery): 
#       super().__init__(brand,model_name,price,ram,camera)
#       self.processor=processor
#       self.battery=battery
#    def full_specs(self):
#       return f" {self.processor} {self.ram} {self.camera} {self.battery}"
# P1=Phone('NOKIA','1100',1500)
# P2=Smartphone('XIAOMI','REDMI 8',8500,'4GB','13MP')
# P3=Flagshipphone("SAMSUNG","Z FLIP",123000,"128GB","86MP","SNAP DRAGON","10000MAH") 
# print(P3.full_specs())
# print(P3.full_name())

# OUTPUT-
# SNAP DRAGON 128GB 86MP 10000MAH
# SAMSUNG Z FLIP



# METHOD RESOLUTION ORDER (MRO)////////////////////////////////////////////////

# SYNTAX////////////////

# print(help(class_name))      # help() is a function

# EVERY CLASS HAVE MRO 

# print(help(Flagshipphone))
#  WE GET ANSWER IN A FORMAT WHICH IS USED BY PYTHON FOR SEARCH ANY THING

# OUTPUT-
# Help on class Flagshipphone in module __main__:

# class Flagshipphone(Smartphone)
#  |  Flagshipphone(brand, model_name, price, ram, camera, processor, battery)
#  |
#  |  Method resolution order:
#  |      Flagshipphone
#  |      Smartphone
#  |      Phone
#  |      builtins.object      #THIS IS A P REDEFINE CLASS AND EVERY CLASS IN INHERITANCE BY THIS CLASS DEFAULTLY
#  |
#  |  Methods defined here:
#  |
#  |
#  |  full_specs(self)
#  |
#  |  Methods inherited from Phone:
#  |
#  |  full_name(self)
#  |
#  |  make_call(self, phone_number)
#  |
#  |  specification(self)
#  |
#  |  Data descriptors inherited from Phone:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
# None


# print(help(P2))

# OUTPUT-
# Help on Smartphone in module __main__ object:

# class Smartphone(Phone)
#  |  Smartphone(brand, model_name, price, ram, camera)
#  |
#  |  Method resolution order:
#  |      Smartphone
#  |      Phone
#  |      builtins.object
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, brand, model_name, price, ram, camera)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Phone:
#  |
#  |  full_name(self)
#  |
#  |  make_call(self, phone_number)
#  |
#  |  specification(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Phone:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)

# None




# METHOD OVERRIDING//////////////////////////////////////////

# IF WE DEFINE A FUNCTION IN A CLASS  AND WE INHERT THAT CLASS IN OTHER CLASS AND CALL THAT FUNCTION THEN THE FUNCTION OUTPUT IS 
# DEPEND ON THE PARAMETER OF PHONE CLASS 
# BUT IF WE WANT SOME CHANGE IN THAT FUNCTION IF WE CALL IN CHILD CLASS THEN WE CAN CHANGE IT EASILY AND WE GET OUTPUT ON THE BASIS OF 
# CHILD CLASS PARAMETER 
# BUT NOW THE OUTPUT OF THAT FUNCTION IS CHANGE FOR BOTH CLASS PARENT CLASS GET OUTPUT ON THE BASIS OF ITE PARAMETER 
# AND CHILD CLASS GET OUTPUT ON THE BASIS OF ITS PARAMETER 
# THIS METHOD IS CALLED METHOD OVERRIDING

# class Phone:    #PARENT CLASS/BASE CLASS
#    def __init__(self,brand,model_name,price):
#          self.brand=brand
#          self.model_name=model_name
#          self.price=price 
         
#    def specification(self):
#       return f"{self.brand} {self.model_name} {self.price}"
#    def make_call(self,phone_number):
#       return f"calling {phone_number}...."
#    def full_name(self):
#       return f"{self.brand} {self.model_name}"

# class Smartphone(Phone):    #DERIVED/CHILD CLASS 
#    def __init__(self,brand,model_name,price,ram,camera):   #SAME AS PREVIOUS METHOD WE HAVE TO DEFINE "__init__" FUNCTION
#       super().__init__(brand,model_name,price) #NOT USE OF "self"  IT IS HANDEL BY "super()"
#       self.ram=ram                             #WHEN WE USE "super()" THEN "self"  IS NOT USE
#       self.camera=camera

# class Flagshipphone(Smartphone):
#    def __init__(self,brand,model_name,price,ram,camera,processor,battery): 
#       super().__init__(brand,model_name,price,ram,camera)
#       self.processor=processor
#       self.battery=battery
#    def full_specs(self):
#       return f" {self.processor} {self.ram} {self.camera} {self.battery}"
# # WE ALL READY  DEFINE "full_name()" FUNCTION IN PARENT CLASS BUT NOW WE WANT THAT SOME CHANGES IN THIS FUNCTION 
#    def full_name(self):
#       return f"{self.brand} {self.model_name} now in just {self.price}"
# # LET SEE THIS FUNCTION

# P1=Phone('NOKIA','1100',1500)
# P2=Smartphone('XIAOMI','REDMI 8',8500,'4GB','13MP')
# P3=Flagshipphone("SAMSUNG","Z FLIP",123000,"128GB","86MP","SNAP DRAGON","10000MAH") 
# print(P1.full_name())
# print(P3.full_name())

# OUTPUT-
# NOKIA 1100  # "full_name()" FUNCTION FOR PARENT (Phone) CLASS
# SAMSUNG Z FLIP now in just 123000   # "full_name()" FUNCTION FOR CHILD (Flagshipphone) CLASS


# "isinstance()" METHOD/FUNCTION //////////////////////////////
 
# THIS IS A BUILTIN FUNCTION
#WE USE THIS METHOD TO FIND THAT THIS OBJECT IS BELONG TO THIS CLASS OR NOT

# SYNTAX :- 
# print(isinstance(OBJECT_NAME,CLASS_NAME)) 

# print(isinstance(P1,Flagshipphone))
# OUTPUT-
# False

# print(isinstance(P3,Phone))
# OUTPUT-
# True

# print(isinstance(P2,Phone))
# print(isinstance(P2,Smartphone))
# print(isinstance(P2,Flagshipphone))

# OUTPUT-
# True
# True
# False

# print(isinstance(P1,Phone))
# print(isinstance(P1,Smartphone))
# print(isinstance(P1,Flagshipphone))

# OUTPUT-
# True
# False
# False

# print(isinstance(P3,Phone))
# print(isinstance(P3,Smartphone))
# print(isinstance(P3,Flagshipphone))

# OUTPUT-
# True
# True
# True



# "issubclass()" METHOD/FUNCTION /////////////////////////////////////////////

# THIS IS A BUILTIN FUNCTION
# SYNTAX:-

# print(issubclass(CLASS_NAME,CLASS_NAME))

# WE USE THIS FUNCTION TO CHECK A CLASS IS A SUBCLASS/CHILDCLASS OF THAT CLASS OR NOT

# print(issubclass(Phone,Smartphone))    
# print(issubclass(Phone,Flagshipphone))
# OUTPUT-
# False    #BECAUSE PHONE_CLASS IS A PARENT CLASS FOR SMARTPHONE_CLASS AND FLAGSHIPPHONE_CLASS
# False

# print(issubclass(Smartphone,Phone))      
# print(issubclass(Smartphone,Flagshipphone))
# OUTPUT-   
# True    #BECAUSE SMARTPHONE_CLASS IS THE SUBCLASS/CHILDCLASS OF PHONE_CLASS
# False   #BECAUSE sMARTPHONE_CLASS IS THE PARENT CLASS OF FLAGSHIPPHONE_CLASS

# print(issubclass(Flagshipphone,Phone))
# print(issubclass(Flagshipphone,Smartphone))
# OUTPUT-
# True    #BECAUSE FLAGSHIPPHONE_CLASS IS THE SUBCLASS/CHILDCLASS OF BOTH SMARTPHONE_CLASS AND PHONE_CLASS
# True



# MULTIPLE INHERITANCE ////////////////////////////////////////////////////////////////////////////////////

# class A:
#    def func_A(self):
#       return "i am class A"
#    def hello(self):
#       return "this is first class"

# class B:
#    def func_B(self):
#       return "i am class B"
#    def hello(self):
#       return "this is second class "

# class C(A,B):
#    pass  #THIS IS USE WHEN WE DONT WANT TO WRITE ANY THING IN CLASS BODY BUT JUST INHERITANCE CLASS

# instance_1=C()
# print(instance_1.func_B())
# # OUTPUT-
# # i am class B
# print(instance_1.func_A())
# # OUTPUT-
# # i am class A
# print(instance_1.hello())
# OUTPUT-
# this is first class    #WE GET CLASS_A HELLO() BECAUSE IN CLASS_C WHEN WE INHERT CLASS_A AND CLASS_B
                         #THEN PYHTON FOLLOW THAT ORDER  THAT'S WHY WE GET THIS 

# IF WE CHANGE THE ORDER OF CLASS_A AND CLASS_B AT THE TIME OF INHERTING THEN WE GET THE CHANGED OUTPUT

# class C(B,A):
#    pass
# instance_1=C()
# print(instance_1.hello())
# OUTPUT-
# this is second class  #HERE WE CAN SEE THAT THE OUTPUT IS CHANGE


# SPECIAL_MAGIC_METHODS/DUNDER_METHOD

# THESE METHODS ARE DETERMINE BY "__NAME__"
# EXG :- __init__ 

# class Phone:
#    def __init__(self,brand,model,price):
#       self.brand=brand
#       self.model=model
#       self.price=price
#    def phone_name(self):
#       return f"{self.brand} {self.model}"

# my_phone=Phone("blackberry","passport",289000)
# print(my_phone)

# OUTPUT-
# <__main__.Phone object at 0x0000025093FEF1C0>  #THIS IS A LOCATION WHERE OUR PROGRAMM IS STORE

