# import os and win32 com as wincom
import os
import win32com.client as wincom

# adding voice to the speak command
speak = wincom.Dispatch("SAPI.SpVoice")

# running it infinite times
while True:
    text = input("Type What You Want To Speak :")
    if(text=='q'):
        # if user enters q program stops by saying Hey Bro Bye Bye
        speak.Speak("Hey Bro Bye Bye")
        exit()
    speak.Speak(text)
    
