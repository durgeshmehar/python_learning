text=input("Enter the discussion\n")
discuss=False

if("harry" in text):
    discuss=True
elif("HARRY" in text):
    discuss=True
elif("Harry" in text):
    discuss=True
elif("HarrY" in text):
    discuss=True
elif("HaRrY" in text):
    discuss=True
elif("HaRRY" in text):
    discuss=True
elif("HARrY" in text):
    discuss=True
elif("HARry" in text):
    discuss=True
elif("HArRY" in text):
    discuss=True
elif("hArRY" in text):
    discuss=True
else:
    print("Not about harry\n")
if(discuss==True):
    print("discussion about harry")
