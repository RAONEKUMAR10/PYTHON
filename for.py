# for i in range (0,6):
#     print(i)
#     continue
# else:print("helo")
# print("hii")

# # OUTPUT-
# # 0
# # hii





# for i in range(0,5):    
#     print(i)    
#     break;    
# else:print("for loop is exhausted");    
# print("The loop is broken due to break statement...came out of the loop") 

# # OUTPUT-
# # 0
# # The loop is broken due to break statement...came out of the loop





# list =['ritik','harshit','paras','vishal']
# for i in range(len(list)):
#     print("hello",list[i])

# # OUTPUT-
# # hello ritik
# # hello harshit
# # hello paras
# # hello vishal




# num= int(input("enter your number "))
# for i in range(2,num,2):
#     print(i)

# # OUTPUT-
# # enter your number 10
# # 2
# # 4
# # 6
# # 8





# n = int(input("Enter the number of rows: "))  
# m = (2 * n) - 2  
# for i in range(0, n):  
#     for j in range(0, m):  
#         print(end=" ")  
#     m = m - 1  # decrementing m after each loop  
#     for j in range(0, i + 1):  
#         # printing full Triangle pyramid using stars  
#         print(j, end=' ')  
#     print(" ")  

# # OUTPUT-
# # Enter the number of rows: 6
# #           0
# #          0 1
# #         0 1 2
# #        0 1 2 3
# #       0 1 2 3 4
# #      0 1 2 3 4 5





# # PROGRAM FOR-
# k=2*5-2
# for i in range (0,5):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-2
#     for l in range(0,i+1):
#         print("*",end=" ")
#     print(" ")

# # OUTPUT-
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *





# # PROGRAM FOR-
# for i in range(0,5):
#     for j in range(5,i,-1):
#         print(j,end='')
#     print("")

# # OUTPUT-
# # 54321
# # 5432
# # 543 
# # 54  
# # 5 




# # PROGRAM FOR- 
# for i in range(0,2):
#     for j in range(0,2):
#         for k in range(0,2):
#             print(i,j,k)
#         print("")    
#     print("")       

# # OUTPUT-
# # 0 0 0
# # 0 0 1
# # 0 1 0
# # 0 1 1
# # 1 0 0
# # 1 0 1
# # 1 1 0
# # 1 1 1




# # PROGRAM FOR 
# for row in range(5,0,-1):
#     for column in range(1,row+1):
#         print("*",end=' ')
#     print("")

# # OUTPUT-
# # * * * * * 
# # * * * * 
# # * * *
# # * *
# # *



# # PROGRAM FOR
# for row in range (1,6):
#     for column in range(row):
#         print(row,end='')
#     print("")

# # OUTPUT-
# # 1
# # 22
# # 333
# # 4444
# # 55555




# # PROGRAM FOR
# for row in range(1,6):
#     for column in range (1,row+1):
#         print("*",end=' ')
#     print("") 
    
# # OUTPUT-
# # * 
# # * * 
# # * * *
# # * * * *
# # * * * * *




# # PROGRAM FOR
# for row in range(1,6):
#     for column in range(1,6):
#         print(row,end=' ')
#     print("\n")

# # OUTPUT-
# # 1 1 1 1 1 

# # 2 2 2 2 2

# # 3 3 3 3 3

# # 4 4 4 4 4

# # 5 5 5 5 5    



# # PROGRAM FOR 12345 5 TIMES
# for row in range(1,6):
#     for column in range(1,6):
#         print(column,end=" ")
#     print("")

# # OUTPUT-
# # 1 2 3 4 5 
# # 1 2 3 4 5 
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5



# # PROGRAM FOR REVERSE PRINT 
# for row in range(5,0,-1):
#     for column in range(1,row+1):
#         print(column ,end="")
#     print("")

# # OUTPUT-
# # 12345
# # 1234
# # 123
# # 12
# # 1



# # PROGRAM FOR INCREASING ORDER
# for row in range(1,6):
#     for column in range(1,row+1):
#         print(column,end="")
#     print("")

# # OUTPUT-
# # 1
# # 12
# # 123
# # 1234
# # 12345
        
    


# # PROGMAR FOR INCREASIG ORDER WITH *
# for row in range(1, 6):
#     for column in range(1, row +1):
#         print(column, end='*')
#     print(" ")

# # OUTPUT-
# # 1* 
# # 1*2* 
# # 1*2*3*
# # 1*2*3*4*
# # 1*2*3*4*5* 






# current_Number = 1  
# stop = 2  
# rows = int(input("enter number os rows"))
# for i in range(rows):  
#     for j in range(1, stop):  
#         print(current_Number, end=' ')  
#         current_Number += 1  
#     print("")  
#     stop += 1  

# # OUTPUT=
# # enter number os rows6
# # 1 
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # 11 12 13 14 15
# # 16 17 18 19 20 21






# n = int(input("enter your number := "))
# m= n-2
# for i in range(n,0,-1):
#    for j in range(m,0,-1):
#       print(end=" ")
#    m=m+1
#    for j in range(i,0,-1):
#       print("*",end=" ")
#    print("")
# m=n*2-2
# for i in range(0,n):
#    for j in range(1,m):
#       print(end= " ")
#    m=m-1
#    for j in range(0,i+1):
#       print("*",end=" ")
#    print("")

# # OUTPUT-
# # enter your number := 5
# #    * * * * *
# #     * * * *
# #      * * *
# #       * *
# #        *
# #        *
# #       * *
# #      * * *
# #     * * * *
# #    * * * * *





# n = int(input("enter your row number :- "))
# m= n*2-2
# for i in range(1,n):
#    for j in range(1,m):
#       print(end= " ")
#    m=m-1
#    for j in range(1,i+1):
#       print(n,end=" ")
#    print("")
# m=n-2
# for i in range(n,0,-1):
#    for j in range(m,0,-1):
#       print(end=" ")
#    m= m+1
#    for j in range(i,0,-1):
#       print(n,end=" ")
#    print("")

# # OUTPUT-
# # enter your row number :- 5
# #        *
# #       * *
# #      * * *
# #     * * * *
# #    * * * * *
# #     * * * *
# #      * * *
# #       * *
# #        *





# import time
# import datetime
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().date())
# startTime = time.time()
# name = input('enter your name :- ')
# var =""
# for i in range(0,len(name)):
#    if name[i] not in var:
#       print(f'{name[i]} : {name.count(name[i])}')
#       var += name[i]
# endTime = time.time()
# totalTime = endTime - startTime
# print(totalTime)

# # OUTPUT-
# # 20:19:26.146377   ----TIME
# # 2021-05-12    -----DATE
# # enter your name :- RITIK
# # R : 1
# # I : 2
# # T : 1
# # K : 1
# # 2.7473647594451904  -----TIME EXECUTE TO RUN A POGRAM



# import time
# import datetime
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().date())
# startTime = time.time()

# sum = 0
# for i in range(0,11):
#    sum += (i)
# print(sum)
# endTime = time.time()
# totalTime = endTime - startTime
# print(totalTime)



# import time
import datetime
import time
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())
startTime = time.time()
n = input('enter your number :- ')
sum=0
for  i in range(0,len(n)):
   sum = sum+int(n[i])
print(sum)

endTime = time.time()
totalTime = endTime - startTime
print(totalTime)