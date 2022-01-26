# READ  FILES (TEXT,PDF,CSV,ETC) ///////////////////////////



# READ TEXT FILES //////////////////////////////
# WE CAN WRITE AND READ ANY FILE AT ANY LOCATION IN OUR SYSTEM

# .open() FUNCTON//////////////////

# TO READ ANY FILE FIRST WE HANE TO OPEN IT SO WE  USE OPEN FUNCTION 

# SYNTAX---
# VARIABLE_NAME=open('path of file','operation ('r','w') ')
# 'r' = read operation
# 'w' = write operation  

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt')

# NOTE :- IF WE DON'T GIVE ANY OPERATION ('r','w') THEN THE DEFAULT OPERATION IS READ ('r')


# .read() METHOD/////////////////////////
# THEN WE HAVE TO READ IT SO WE USE .read() METHOD

# SYNTAX--- 
# VARIABLE_NAME.read()
# WE CAN ALSO PRINT IT 

# print(f.read())

# .close() METHOD///////////////////////
# FOR A GOOD PROGRAMMER WE HAVE TO CLOSE OUR FILE AFTER WORK ON IT

# TO CLOSE ANY FILE WE USE .close() METHOD
# SYNTAX---

# VARIABLE_NAME.close()
# f.close()

# EXG-
# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt')
# print(f.read())
# f.close()

# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON. 

# IF WE WRITE AGAIN TO PRINT FUNCTION THEN

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt')
# print(f.read())
# print(f.read())
# f.close()



# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON. 

# NOTE:- 
# WE STILL GET ONLY ONE OUTPUT
# BECAUSE WHEN FIRST WE EXECUTE PRINT FUNCTION THEN OUR CURSOR START MOVING AND IN THE LAST 
# IT PRINT ALL THE DATA OF OUR FILE.SO WHEM SECOND PRINT FUNCTION EXECUTE THAT TIME OUR CURSOR IS ALREADY IN LAST
# THATS WHY IT DON'T PRINT ANYTHING SECOND TIME.

# .tell() METHOD////////////////

# IT IS USE TO PRINT CURSOR LOCATION 

# SYNTAX---
# VARIABLE_NAME.tell()

# f.tell()

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt')
# print(f"CURSOR POSITION - {f.tell()}")
# print(f.read())
# print(f.read())
# print(f"CURSOR POSITION - {f.tell()}")
# f.close()

# OUTPUT-
# CURSOR POSITION - 0    #STARING POSITION OF CURSOR
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.
 
                                    
# CURSOR POSITION - 179   #ENDING POSITION OF CURSOR

#  .seek() METHOD//////////////

# IT IS USE TO CHANGE THE POSITION OF CURSOR
 
# AS ABOVE WE KNOW THAT THE LOCATION OF OUR CURSOR IS 179 SO WE WANT TO CHGNAGE IT  

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt')  
# print(f"CURSOR LOCATION IS {f.tell()}")
# print(f.read())
# print(f"CURSOR LOCATION IS {f.tell()}")
# print('BEFORE .seek() METHOD')
# f.seek(65)
# print('AFTER .seek() METHOD')
# print(f"CURSOR POSITION IS {f.tell()}")
# print(f.read())
# f.close()

# OUTPUT-

# CURSOR LOCATION IS 0                      #OUR FIRST CURSOR LOCATION  
# MY NAME IS RITIK KUMAR.                   # f.read() METHOD EXECUTE
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.

# CURSOR LOCATION IS 179                    #OUR LAST CURSOR LOCATION  BEFORE .seek METHOD()
# BEFORE .seek() METHOD
# AFTER .seek() METHOD
# CURSOR POSITION IS 0                      #CURSOR LOCATION AFTER .seek() METHOD
# MY NAME IS RITIK KUMAR.                   #AGAIN f.read() METHOD EXECUTE
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.


# IF WE DO ---

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt')  
# print(f"CURSOR LOCATION IS {f.tell()}")
# print(f.read())
# print(f"CURSOR LOCATION IS {f.tell()}")
# print('BEFORE .seek() METHOD')
# f.seek(65)
# print('AFTER .seek() METHOD')
# print(f"CURSOR POSITION IS {f.tell()}")
# print(f.read())
# f.close()

# OUTPUT-
# CURSOR LOCATION IS 0
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.

# CURSOR LOCATION IS 179
# BEFORE .seek() METHOD
# AFTER .seek() METHOD
# CURSOR POSITION IS 65
#  TEXT FILE.                                 #IT START AGAIN .read() METHOD AT POSITION
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.


#  .readline() METHOD////////////////////

# IT IS EXECUTE ONE LINE AT A TIME

# SYNTAX--

# VARIABLE_NAME.readline()

# print(f.readline())

# EXG-

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r')
# print(f.readline())

# OUTPUT-         #WE GET ONLY ONE LINE
# MY NAME IS RITIK KUMAR.

# print(f.readline())

# OUTPUT-      #HERE WE GET TWO LINES
# MY NAME IS RITIK KUMAR.

# THIS FILE NAME IS READ&WRITE.


#  .readlines() METHOD///////////////////////////

# THIS METHOD CONVERT LINES OF OUR FILE INTO A LIST.
# IN .readlines() METHOD WE CAN USE SLICING

# SYNTAX--

# VARIABLE_NAME.readlines()

# print(f.readsline())

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r')
# print(f.readlines())

# OUTPUT-
# ['MY NAME IS RITIK KUMAR.\n', 'THIS FILE NAME IS READ&WRITE.\n', 'THIS IS A TEXT FILE.\n', 'THIS FILE IS SAVE ON A DESKTOP OF 
# MY LAPTOP.\n', "I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.\n"]

# WE CAN USE LOP IN THIS METHOD

# f=open(r"C:\Users\lenovo\Desktop\READ&WRITE.txt",'r')
# print(f.read())
# l=f.readlines()
# for i in l:
#    print(i)

# f.close()

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r')
# print(f.readlines()[:3])

# OUTPUT-
# ['MY NAME IS RITIK KUMAR.\n', 'THIS FILE NAME IS READ&WRITE.\n', 'THIS IS A TEXT FILE.\n']

# WE CAN DO--
# print(f.readlines()[1:5:1])
# OUTPUT-
# ['THIS FILE NAME IS READ&WRITE.\n', 'THIS IS A TEXT FILE.\n', 'THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.\n', "I'M GONNA USE THIS FILE TO 
# READ AND WRITE VIA PYTHON.\n"]


# DATA DISCRIPTOR/////////////////////////////////

# THEY ARE USED TO PRINT FILE'S NAME.THESE ARE NOT METHODS 
# THERE ARE TWO DATA DISCRIPORS

# 1.) NAME   ------------------------
# SYNTAX--
# print(VARIABLE_NAME.name)

# print(f.name)
# OUTPUT-       #HERE WE GET THE NAME OF OUR FILE
# C:\Users\lenovo\Desktop\READ&WRITE.txt

# 2.) CLOSED   ------------------------
# IT IS USE TO CHECK THAT OUR FILE IS CLOSED OR NOT. IT GAVE US VALUE IN BOOLEAN WAI
# SYNTAX--
# print(VARIABLE_NAME.closed)

# print(f.closed)
# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r')
# print(f.read())
# print(f.closed)
# f.close()

# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.

# False


# BUT IF WE DO--

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r')
# print(f.read())
# f.close()  
# print(f.closed)

# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.

# True


# WE CAN ITERATE OUR DATA WITHOUT USING read() FUNCTION

# f=open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r')
# for i in f:
#    print(i,end="")

# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.



# WITH BLOCK////////////////////////////////

# IT IS ALSO KNOWN AS CONTEXT MANAGER
# IN THIS METHOD WE DON'T ANY NEED TO CLOSE OUR PROGRAM AS WE DO IN SIMPLE READ FILES.
# IF OUR FILE IS DAMAGED OR AYNTHING ELSE THEN CONTEXT MANAGER HANDEL IT SELF
# SYNTAX-
# with open('file_name or file_path') as VARIABLE_NAME:

with open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r') as P:
   data=P.read()      # data IS ALSO A VARIABLE.WHICH IS USING TO PRINT 
   print(data)

# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON. 

# WE CAN CHECK THAT OUR FILE IS CLOSED OR NOT 

with open(r'C:\Users\lenovo\Desktop\READ&WRITE.txt','r') as P:
   # f=P.open()      # WE CAN WRITE THIS OR NOT IT IS DEPEND ON US
   print(P.read())

print(P.closed)

# OUTPUT-
# MY NAME IS RITIK KUMAR.
# THIS FILE NAME IS READ&WRITE.
# THIS IS A TEXT FILE.
# THIS FILE IS SAVE ON A DESKTOP OF MY LAPTOP.
# I'M GONNA USE THIS FILE TO READ AND WRITE VIA PYTHON.

# True





    
