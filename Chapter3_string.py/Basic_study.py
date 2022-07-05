'''
s1="Durgesh "
s2="Good morning"
c=s1+s2
print(c)               #Durgesh Good morning
print(s1,s2)           #Durgesh  Good morning
print(c[11])           #d

print(c[0:11:1])     #Durgesh Goo
print(c[:11:1])      #Durgesh Goo
print(c[0:11:4])     #DeG
print(c[-1])         #g
print(c[5:1:1])      #____________
print(c[:12:2])      #DrehGo
'''

story="my name is durgesh.as i describe myself i am much hardworking,focus ,concentration person.these all quality i learn from my father."

short="whats you"

print(len(story))                  #130
print(len(short))                  #9
print(story.endswith("father."))   #True

print(story.count("f"))            #4
print(story.count("my"))           #3

print(story.capitalize())          #My name is durgesh.....

print(story.find("is"))            #8   (at index 8 the word start)
print(story.find("ism"))            #-1   (false,no word found)

print(story.replace("father","best father"))

story="my name is durgesh\n.as i describe\'s myself i am much hardworking,focus\\concentration person.\tthese all quality i learn from my father."
print(story)

