import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Initialize TTS engine
engine = pyttsx3.init()

# Create GUI window (main window) first
window = tk.Tk()
window.title("RoboSpeaker by Shruti")
window.geometry("420x350")
window.config(bg="#f9f9f9")

# Get available voices
voices = engine.getProperty('voices')

# Default settings after window creation
selected_voice = tk.StringVar(value='Female')
selected_speed = tk.StringVar(value='Normal')

# Function to speak text
def speak_text():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    # Set voice
    if selected_voice.get() == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    # Set speed
    if selected_speed.get() == 'Slow':
        engine.setProperty('rate', 120)
    elif selected_speed.get() == 'Fast':
        engine.setProperty('rate', 250)
    else:
        engine.setProperty('rate', 180)

    engine.say(text)
    engine.runAndWait()

# Function to save audio
def save_audio():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    engine.save_to_file(text, "robospeaker_output.mp3")
    engine.runAndWait()
    messagebox.showinfo("Saved", "Audio saved as robospeaker_output.mp3")

# Function to quit app
def quit_app():
    window.destroy()

# Heading
label = tk.Label(window, text="🎤 RoboSpeaker 2.0", font=("Helvetica", 16, "bold"), bg="#f9f9f9", fg="#333")
label.pack(pady=10)

# Text Entry
entry = tk.Entry(window, font=("Helvetica", 14), width=35)
entry.pack(pady=10)

# Voice Selector
voice_frame = tk.LabelFrame(window, text="Choose Voice", bg="#f9f9f9", font=("Helvetica", 12))
voice_frame.pack(pady=5)
tk.Radiobutton(voice_frame, text="Female", variable=selected_voice, value='Female', bg="#f9f9f9").pack(side='left', padx=10)
tk.Radiobutton(voice_frame, text="Male", variable=selected_voice, value='Male', bg="#f9f9f9").pack(side='left', padx=10)

# Speed Selector
speed_frame = tk.LabelFrame(window, text="Speed", bg="#f9f9f9", font=("Helvetica", 12))
speed_frame.pack(pady=5)
tk.Radiobutton(speed_frame, text="Slow", variable=selected_speed, value='Slow', bg="#f9f9f9").pack(side='left', padx=10)
tk.Radiobutton(speed_frame, text="Normal", variable=selected_speed, value='Normal', bg="#f9f9f9").pack(side='left', padx=10)
tk.Radiobutton(speed_frame, text="Fast", variable=selected_speed, value='Fast', bg="#f9f9f9").pack(side='left', padx=10)

# Buttons
btn_frame = tk.Frame(window, bg="#f9f9f9")
btn_frame.pack(pady=10)

speak_btn = tk.Button(btn_frame, text="🔊 Speak", command=speak_text, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=15)
speak_btn.grid(row=0, column=0, padx=5)

save_btn = tk.Button(btn_frame, text="💾 Save Audio", command=save_audio, font=("Helvetica", 12), bg="#2196F3", fg="white", padx=10)
save_btn.grid(row=0, column=1, padx=5)

quit_btn = tk.Button(btn_frame, text="❌ Quit", command=quit_app, font=("Helvetica", 12), bg="#f44336", fg="white", padx=15)
quit_btn.grid(row=0, column=2, padx=5)

# Start GUI
window.mainloop()
