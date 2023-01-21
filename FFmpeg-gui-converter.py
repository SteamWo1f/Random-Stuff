import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog

def convert_video_to_audio():
    video_file = filedialog.askopenfilename(title = "Select video file", filetypes = (("MP4 files", "*.mp4"), ("AVI files", "*.avi"), ("All files", "*.*")))
    audio_file = filedialog.asksaveasfilename(title = "Save audio file as", defaultextension=".mp3", filetypes = (("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*")))
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    print("File converted successfully!")

root = Tk()
root.title("Video to Audio Converter")
root.geometry("200x100")

convert_button = Button(root, text = "Convert", command = convert_video_to_audio)
convert_button.pack()

root.mainloop()
