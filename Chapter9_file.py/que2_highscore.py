def game():
    return 772

score=game()
with open('highscore.txt','r') as f:
    savescore=f.read()

if savescore=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))

elif score > int(savescore):
    with open('highscore.txt','w') as f:
        f.write(str(score))
else:
    print("Previous score is highest")
print("Success!!")

