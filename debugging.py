#            DEBUGGING//////////////////////////////////////////////////

# DEBUGGING IS THE PROCESS OF FINDING AND RESOLVING DEFECTS OR PROBLEMS WITHIN A COMPUTER PROGRAM THAT PREVENT CORECT OPERATION OF
# COMPUTER SOFTWARE OR A SYSTEM

# STEPS OF DEBUGGING -------------
# 1) SET TRACE :- IN WHICH WE USE PYHTON INBUILDS MODULE(import pdb) TO FIND BUG IN OUR PROGRAM
# 2) EXECUTE CODE LINE BY LINE :- IN THIS PROCESS WE EXECUTE OUR PROGRAMM LINE ONE BY ONE AND FIND IN WHICH LINE BUGG OCCURS

# NOTE 

# WE CAN IMPORT OUR pdb MODULE IN ANY LINE OF OUR PROGRAM
   

 
# EXG-
# name=input("enter your name")
# age=input("enter your age")
# age2=age + 5 
# print(f"your name is {name} and your age is {age2}")

# OUTPUT-
# enter your nameritik
# enter your age76
# Traceback (most recent call last):
#   File "debugging.py", line 9, in <module>
#     age2=age + 5
# TypeError: can only concatenate str (not "int") to str



# EXG-
# USING PYTHON MODULE

# import pdb    # pdb IS A MODULE OF PYTHON 
# pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION 
# name=input("enter your name:- ")
# age=input("enter your age:-  ")
# age2=age + 5 
# print(f"your name is {name} and your age is {age2}")


# IN DEBUGGING WE USE THREE COMMANDS OF pdb MODULE AND THAT IS :-
# l (LINE) = IF WE WANT TO KNOW THAT AT WHICH LINE OUR PROGRAMM IS STOP.THEN WE USE "l" COMMAND .AND IT INDICATE THE LINE BY AN ARROW (->)
# n (RUN) = IF WE WANT TO RUN OUR LINE OF CODE OR PROGRAMM THE WE USE "n" COMMAND
# q (QUIT) = IF WE WANT TO QUIT TO THE DEBUGGING THEN WE USE "q" COMMAND
# c (CONTINUE) = WHEN WE DON'T WANT TO DEBUG OUR PROGRAMM LINE BY LINE AND  CONTINUE OUR PROGRAMM AS IT IS THEN WE USE "c" COMMAND.THEN OUR CODE 
# RUN NORMALLY

# OUTPUT-
# > e:\python\debugging.py(34)<module>()
# -> name=input("enter your name:- ")   
# (Pdb) l          #HERE WE USE "l" TO GET THE LINE OF CODE LOCATION
#  29     # EXG-
#  30     # USING PYTHON MODULE
#  31     
#  32     import pdb    # pdb IS A MODULE OF PYTHON
#  33     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
#  34  -> name=input("enter your name:- ")        #HERE WE HAVE OUR RESULT
#  35     age=input("enter your age:-  ")
#  36     age2=age + 5
#  37     print(f"your name is {name} and your age is {age2}")
#  38     
#  39     
# (Pdb) n      # HERE WE USE "n" TO EXECUTE THE LINE OF CODE
# enter your name:- ritik kumar
# > e:\python\debugging.py(35)<module>()
# -> age=input("enter your age:-  ")    
# (Pdb) l
#  30     # USING PYTHON MODULE
#  31     
#  32     import pdb    # pdb IS A MODULE OF PYTHON
#  33     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
#  34     name=input("enter your name:- ")
#  35  -> age=input("enter your age:-  ")
#  36     age2=age + 5
#  37     print(f"your name is {name} and your age is {age2}")
#  38
#  39
#  40     # IN DEBUGGING WE USE THREE COMMANDS OF pdb MODULE AND THAT IS :-
# (Pdb) n
# enter your age:-  21
# > e:\python\debugging.py(36)<module>()
# -> age2=age + 5
# (Pdb) l
#  31     
#  32     import pdb    # pdb IS A MODULE OF PYTHON
#  33     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
#  34     name=input("enter your name:- ")
#  35     age=input("enter your age:-  ")
#  36  -> age2=age + 5
#  37     print(f"your name is {name} and your age is {age2}")
#  38
#  39
#  40     # IN DEBUGGING WE USE THREE COMMANDS OF pdb MODULE AND THAT IS :-
#  41     # l  = IF WE WANT TO KNOW THAT AT WHICH LINE OUR PROGRAMM IS STOP.THEN WE USE "l" .AND IT INDICATE THE LINE BY AN ARROW (->)        
# (Pdb) n
# TypeError: can only concatenate str (not "int") to str    #HERE WE FIND A BUG IN LINE 36 
# > e:\python\debugging.py(36)<module>()
# -> age2=age + 5
# (Pdb) q           #HERE WE USE "q" TO QUIT OUR DEBUGGING
# Traceback (most recent call last):
#   File "DEBUGGING.PY", line 36, in <module>
#     age2=age + 5
#   File "C:\Users\lenovo\AppData\Local\Programs\Python\Python38\lib\bdb.py", line 94, in trace_dispatch
#     return self.dispatch_exception(frame, arg)
#   File "C:\Users\lenovo\AppData\Local\Programs\Python\Python38\lib\bdb.py", line 174, in dispatch_exception
#     if self.quitting: raise BdbQuit
# bdb.BdbQuit


# NOTE -----
#  NOW WE GET WHERE IS BUG IN OUR PROGRAM SO WE HAVE TO FIX IT

# IF WE DO 


# name=input("enter your name:- ")
# age=input("enter your age:-  ")
# # age2=age + 5    #HERE EITHER WE HAVE TO CHANGE BOTH IN STRING OU BOTH IN INTEGER BECAUSE  STRING AND INTEGER CAN'T BE CONCATENATE
# age2= age + "5"
# print(f"your name is {name} and your age is {age2}")

# OUTPUT-
# enter your name:- RITIK KUMAR
# enter your age:-  21
# your name is RITIK KUMAR and your age is 215


# NOW IF WE CHECK OUR PRGRAMM AGAIN USING PYTHON 

import pdb    # pdb IS A MODULE OF PYTHON 
pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION 
name=input("enter your name:- ")
age=input("enter your age:-  ")
# age2=age + 5    #HERE EITHER WE HAVE TO CHANGE BOTH IN STRING OU BOTH IN INTEGER BECAUSE  STRING AND INTEGER CAN'T BE CONCATENATE
age2= age + "5"
print(f"your name is {name} and your age is {age2}")

# > e:\python\debugging.py(115)<module>()
# -> name=input("enter your name:- ")
# (Pdb) l
# 110     
# 111     # IF WE DO
# 112
# 113     import pdb    # pdb IS A MODULE OF PYTHON
# 114     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
# 115  -> name=input("enter your name:- ")
# 116     age=input("enter your age:-  ")
# 117     # age2=age + 5    #HERE EITHER WE HAVE TO CHANGE BOTH IN STRING OU BOTH IN INTEGER BECAUSE  STRING AND INTEGER CAN'T BE CONCATENATE 
# 118     age2= age + "5"
# 119     print(f"your name is {name} and your age is {age2}")
# 120
# (Pdb) n
# enter your name:- ritik kumar
# > e:\python\debugging.py(116)<module>()
# -> age=input("enter your age:-  ")
# (Pdb) l
# 111     # IF WE DO
# 112
# 113     import pdb    # pdb IS A MODULE OF PYTHON
# 114     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
# 115     name=input("enter your name:- ")
# 116  -> age=input("enter your age:-  ")
# 117     # age2=age + 5    #HERE EITHER WE HAVE TO CHANGE BOTH IN STRING OU BOTH IN INTEGER BECAUSE  STRING AND INTEGER CAN'T BE CONCATENATE 
# 118     age2= age + "5"
# 119     print(f"your name is {name} and your age is {age2}")
# 120
# 121
# (Pdb) n
# enter your age:-  21
# > e:\python\debugging.py(118)<module>()
# -> age2= age + "5"
# (Pdb) l
# 113     import pdb    # pdb IS A MODULE OF PYTHON
# 114     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
# 115     name=input("enter your name:- ")
# 116     age=input("enter your age:-  ")
# 117     # age2=age + 5    #HERE EITHER WE HAVE TO CHANGE BOTH IN STRING OU BOTH IN INTEGER BECAUSE  STRING AND INTEGER CAN'T BE CONCATENATE 
# 118  -> age2= age + "5"
# 119     print(f"your name is {name} and your age is {age2}")
# 120
# 121
# [EOF]
# (Pdb) n
# > e:\python\debugging.py(119)<module>()
# -> print(f"your name is {name} and your age is {age2}")
# (Pdb) l
# 114     pdb.set_trace()  #IN pdb MODULE set_trace() IS A PREDEFINE FUNCTION
# 115     name=input("enter your name:- ")
# 116     age=input("enter your age:-  ")
# 117     # age2=age + 5    #HERE EITHER WE HAVE TO CHANGE BOTH IN STRING OU BOTH IN INTEGER BECAUSE  STRING AND INTEGER CAN'T BE CONCATENATE 
# 118     age2= age + "5"
# 119  -> print(f"your name is {name} and your age is {age2}")
# 120
# 121
# [EOF]
# (Pdb) n
# your name is ritik kumar and your age is 215
# --Return--
# > e:\python\debugging.py(119)<module>()->None
# -> print(f"your name is {name} and your age is {age2}")
# (Pdb) q
# Traceback (most recent call last):
#   File "DEBUGGING.PY", line 119, in <module>
#     print(f"your name is {name} and your age is {age2}")
#   File "C:\Users\lenovo\AppData\Local\Programs\Python\Python38\lib\bdb.py", line 92, in trace_dispatch
#     return self.dispatch_return(frame, arg)
#   File "C:\Users\lenovo\AppData\Local\Programs\Python\Python38\lib\bdb.py", line 154, in dispatch_return
#     if self.quitting: raise BdbQuit
# bdb.BdbQuit


# NOTE :- WE DID'NT GET ANY BUG OR ANY ERROR IN OUR PROGRAMM


# OUTPUT-

# WHEN WE USE C COMMAND THEN THE OUTPUT IS------

# > e:\python\debugging.py(131)<module>()
# -> name=input("enter your name:- ")
# (Pdb) c
# enter your name:- ritik kumar
# enter your age:-  32
# your name is ritik kumar and your age is 325




