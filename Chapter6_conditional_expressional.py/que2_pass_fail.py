sub1=int(input("Enter mark os sub 1: "))
sub2=int(input("Enter mark os sub 2: "))
sub3=int(input("Enter mark os sub 3: "))
total=(sub1+sub2+sub3)/3
if(sub1>=33 and sub2>=33 and sub3>=33 and total>=40):
    print("You passed with pecentage of ",total)
else:
    if(total<40):
        print("You failed due to total percentage is less,your pecentage:",total)
    else:
        print("You failed due to one of subject get less mark,your pecentage:",total)

