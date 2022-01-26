import datetime

# Print date and time
print(datetime.datetime.now())

# only time
print(datetime.datetime.now().time())







N= int(input("ENTER YOUR NUMBER :- "))
S=input("ENTER YOUR STRING :- ")
if 0<=N<=999 and ('a'<S<'z' or 'A'<S<'Z'):
    print("YOUR ARE A HUMAN")
else:
    print("TUM IS GOLA KE NHI HO")  


number= int(input("enter your number"))
if number:
    print(len(number))
else:
    print('go to hell')