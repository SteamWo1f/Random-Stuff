import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

def speak():
    text = entry.get()
    # Set the selected voice and speed
    engine.setProperty('voice', voice_var.get())
    engine.setProperty('rate', speed_var.get())
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.geometry("500x200")
root.title("TTS Program")

# Create a Label widget
label = tk.Label(root, text="Enter text to speak:")
label.pack()

# Create an Entry widget
entry = tk.Entry(root)
entry.pack()

# Create a variable to store the selected voice
voice_var = tk.StringVar(value=voices[0].id)
# Create a OptionMenu widget to select the voice
voice_dropdown = tk.OptionMenu(root, voice_var, *[voice.name for voice in voices])
voice_dropdown.pack()

# Create a variable to store the selected speed
speed_var = tk.DoubleVar(value=200)
# Create a Scale widget to select the speed
speed_scale = tk.Scale(root, from_=50, to=500, variable=speed_var, orient="horizontal")
speed_scale.pack()

# Create a button to speak the text
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack()

root.mainloop()
