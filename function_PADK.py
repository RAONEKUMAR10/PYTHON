# FUNCTION WITH ALL TYPE OF PARAMETERS 

# THERE ARE FOUR TYPE OF PARAMETERS ////////////
# 1- NORMAL PARAMETERS
# 2- *args PARAMETERS
# 3- DEFAULT PARAMETERS
# 4- **kwargs PARAMETERS

# IF WE WANT USE THSE ALL FOUR PARAMETERS IN A SINGLE FUNCTION THEN WE HAVE TO FOLLOW THIS ORDER

# P - PARAMETER
# A - *args PARAMETERS
# D - DEFAULT PARAMETERS
# K - **kwargs PARAMETERS

# SYNTAX--------

# function (parameter,*args,default parameter,**kwargs):

def func(name,*args,last_name='unknown',**kwargs):
   print(name)
   print(args)
   print(last_name)
   print(kwargs)

func('ritik',1,2,3,4,'kumar',a=319.8)

# OUTPUT-
# ritik                         #PARAMETER
# (1, 2, 3, 4, 'kumar')         #*args
# unknown                       #DEFAULT PARAMETER
# {'a': 319.8}                  #**kwargs

# WE HAVE O ALWAYS FOLLOW "PADK" SEQUENCE EITHER WE GET AN ERROR 
# IF WE USE ANY TWO OR THREE TYPE OF PARAMETERS THEN THE ORDER IS FOLLOW AS "PADK"

# ORDER ARE---

# PA   # PARAMETER,*args
# PD   # PARAMETER,DEFAULT PARAMETER
# PK   # PARAMETER,**kwrags
# AD   # *args,DEFAULT PARAMETER
# AK   # *args,**kwrags
# DK   # DEFAULT PARAMETER,**kwargs