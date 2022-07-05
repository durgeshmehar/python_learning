import speech_recognition

recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say something: ")
    audio=recognizer.listen(source)
print("You said:")
print(recognizer.recognize_google(audio))

words=recognizer.recognize_google(audio)
if "hello" in words:
     print("Hello to you too!")
elif "how are you" in words:
    print("I am a well,thanks")
elif "goodbye" in words:
    print("Huh ?")

# words=input("Saying something: ").lower()