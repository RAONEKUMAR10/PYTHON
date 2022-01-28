import pyttsx3
# Create a string
string = "Lorem Ipsum is simply dummy text " \
    + "of the prting and typesetting industry."
  
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
  
# Command it to speak the given string
engine.say(string)
  
# Wait until above command is not finished.
engine.runAndWait()


# # Create a string
# string = "Lorem Ipsum is simply dummy text " \
#     + "of the prting and typesetting industry."
  
# # Initialize the Pyttsx3 engine
# engine = pyttsx3.init()
  
# # We can use file extension as mp3 and wav, both will work
# engine.save_to_file(string, 'speech.mp3')
  
# # Wait until above command is not finished.
# engine.runAndWait()