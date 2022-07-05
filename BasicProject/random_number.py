import random
com=random.randint(0,100)
# print(com)
user=None
attempt=0
print("Enter the number Between 0-100 :")
while (user!=com):
    user=int(input())
    attempt+=1   
    if(com>user):
        print("Greater number please")
    elif(user>com):
        print("Smaller number please")


print(f"You win !! and guess in {attempt} attempt")
with open("hiscore.txt","r") as f:
    highscore=int(f.read())
if(highscore>attempt):
    with open("hiscore.txt","w") as f:
        f.write(str(attempt))
        print("You break highscore record nice!!!")
        print(f"Now Highscore is {attempt}")

