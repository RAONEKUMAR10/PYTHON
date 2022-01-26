# EARPHONE WITH MIC IS MUST 
# AFTER PRINT OR RUN THIS PROGRAN SPEAK IN YOUR MIC WHAT EVER YOU WANT 


import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
   print("SPEAK.......")
   audio = r.listen(source)
print(r.recognize_google(audio).title())



