# or use random library
# *****Second Method***

import random
computer_num=random.randint(1,3)
print(computer_num)
if(computer_num==1):
    comp='s'
if(computer_num==2):
    comp='w'
if(computer_num==3):
    comp='g'

# ****** first method *******

# def game(user,com):  
#     if(user==com):
#         return 0
#     elif(user=='s' and com=='w'):
#         return 1
#     elif(user=='s' and com=='g'):
#         return -1
#     elif(user=='w' and com=='g'):
#         return 1
#     elif(user=='w' and com=='s'):
#         return -1
#     elif(user=='g' and com=='w'):
#         return -1
#     elif(user=='g' and com=='s'):
#         return 1
# print("**** SNAKE WATER GUN ****")
# user=input('Enter s for "snake",w for water ,g for gun:')
# c={'s','w','g'}
# com=c.pop()
# n=game(user,com)
# if(n==0):
#     print("Match tie friend !!!")
# elif(n==1):
#     print("You win Bro!!!")
# else:
#     print("You loss Brother !!!")
# print(f"You Choose {user} and computer choose {com}")


