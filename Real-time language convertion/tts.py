import pyttsx3

# Our Speak function: using pyttsx3 engine

engine = pyttsx3.init('sapi5')   # sapi5: Microsoft speech API
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('rate',110)  #120 words per minute
engine.setProperty('volume',0.9) 
engine.setProperty('voice', voices[0].id)  # setting our voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Speech system is working fine!")
