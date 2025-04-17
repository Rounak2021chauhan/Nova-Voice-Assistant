import pyttsx3 as p
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext, Button, Frame
import datetime
from PIL import ImageTk, Image
from selenium_web import infow
from selenium_yt import music
from news import news
import randfacts
from jokes import joke
from weather import temp, des

# Initialize the speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text, listen_after=False):
    console.config(state='normal')
    console.insert(tk.END, "Nova: " + text + "\n")
    console.see(tk.END)
    console.config(state='disabled')
    
    engine.say(text)
    engine.runAndWait()

    if listen_after:
        root.after(500, handle_commands)
        console.insert(tk.END, "Listening...\n")

def speak2(text):
   engine.say(text)
   engine.runAndWait()

def wishes():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "Good morning"
    elif hour >= 12 and hour < 16:
        return "Good afternoon"
    else:
        return "Good evening"

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        console.insert(tk.END, "Listening...\n")
        r.energy_threshold=10000
        recognizer.adjust_for_ambient_noise(source,1.2)
        console.config(state='normal')
        console.see(tk.END)
        console.config(state='disabled')
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            console.config(state='normal')
            console.insert(tk.END, "You said: " + text + "\n")
            console.see(tk.END)
            console.config(state='disabled')
            return text.lower()
        except sr.WaitTimeoutError:
            console.config(state='normal')
            console.insert(tk.END, "Listening timed out. Please try again.\n")
            console.see(tk.END)
            console.config(state='disabled')
            return None
        except sr.UnknownValueError:
            console.config(state='normal')
            console.insert(tk.END, "Nova could not understand audio\n")
            console.see(tk.END)
            console.config(state='disabled')
            return None
        except sr.RequestError as e:
            console.config(state='normal')
            console.insert(tk.END, "Could not request results from Speech Recognition service; {0}\n".format(e))
            console.see(tk.END)
            console.config(state='disabled')
            return None

def clear_console():
    console.config(state='normal')
    console.delete(1.0, tk.END)
    console.config(state='disabled')


def handle_commands():
    console.insert(tk.END, "Listening...\n")
    while True:
        text2 = recognize_speech_from_mic(r, sr.Microphone())
        if text2 is not None:
            text2 = text2.lower()
            if "stop" in text2 or "exit" in text2 or text2 == "q":
                speak("Goodbye!")
                root.destroy()  
                break
            elif "information" in text2:
                speak("You need information related to which topic?", listen_after=True)
                console.insert(tk.END, "Listening...\n")
                infor = recognize_speech_from_mic(r, sr.Microphone())
                speak2("Searching {} in Wikipedia.".format(infor))
                assist = infow()
                assist.get_info(infor)
            elif "play video" in text2:
                speak("You want me to play which video?", listen_after=True)
                video_name = recognize_speech_from_mic(r, sr.Microphone())
                console.insert(tk.END, "Listening...\n")
                speak2("Playing {} on YouTube.".format(video_name))
                assist = music()
                assist.play(video_name)
            elif "news" in text2:
                speak("Sure, now I will read news for you.", listen_after=False)
                arr = news()
                for news_item in arr:
                    console.config(state='normal')
                    console.insert(tk.END, news_item + "\n")
                    console.see(tk.END)
                    console.config(state='disabled')
                    speak2(news_item)
            elif "fact" in text2:
                fact = randfacts.get_fact()
                console.config(state='normal')
                console.insert(tk.END, "Fact: " + fact + "\n")
                console.see(tk.END)
                console.config(state='disabled')
                speak2("Did you know that, " + fact, listen_after=False)
            elif "joke" in text2:
                speak("Sure, get ready to laugh.", listen_after=False)
                joke_text = joke()
                for line in joke_text:
                    console.config(state='normal')
                    console.insert(tk.END, line + "\n")
                    console.see(tk.END)
                    console.config(state='disabled')
                    speak2(line)
            speak("What else do you want me to do?", listen_after=True)
        else:
            speak("Sorry, I couldn't understand you. Can you please repeat?")
            break  

def main():
    speak("Hello, " + wishes() + ". I'm your voice assistant, Nova.", listen_after=False)
    today_date = datetime.datetime.now()
    speak("Today is " + today_date.strftime("%d of %B, and it's currently %I:%M %p."), listen_after=False)
    speak("Temperature in Gwalior is " + str(temp()) + " °C and with " + str(des()), listen_after=False)
    speak("What do you want me to do?", listen_after=True)

# Setup the GUI
root = tk.Tk()
root.title("Nova Voice Assistant")
root.geometry("900x500")

# Load the background image
background_image = Image.open(r'D:\Voice assistance\Voice assistance\Nova.jpg')  
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Upper frame for buttons
upper_frame = Frame(root, bg="#000000", bd=2)
upper_frame.place(relx=0.7, rely=0.01, relwidth=0.5, relheight=0.2, anchor='n')

# Button to start the assistant
start_btn = Button(upper_frame, text="Start Assistant", command=main, bg="#2E598F", fg="white")
start_btn.pack(side='left', padx=20)

# Button to manually initiate listening
listen_btn = Button(upper_frame, text="Listen", command=lambda: handle_commands(), bg="#001F47", fg="white")
listen_btn.pack(side='left', padx=10)

clear_btn = Button(upper_frame, text="Clear Console", command=clear_console, bg="#9B0606", fg="white")
clear_btn.pack(side='left', padx=10)

# Lower frame for console
console_frame = Frame(root, bg="#000000")
console_frame.place(relx=0.7, rely=0.7, relwidth=0.5, relheight=0.3, anchor='n')

console = scrolledtext.ScrolledText(console_frame, state='disabled', width=100, height=20, wrap=tk.WORD, bg="#000000", fg="#FFFFFF")
console.pack(pady=10, padx=10, fill='both', expand=True)

r = sr.Recognizer()

root.mainloop()
