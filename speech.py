import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
import threading

# define the recognition function
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=20)
            text = r.recognize_google(audio, language='fr-FR')
            messagebox.showinfo("Input", f"Vous avez dit : {text}")
        except sr.WaitTimeoutError:
            messagebox.showwarning("Timeout", "Aucune parole détectée en 20 secondes. Veuillez réessayer.")
        except Exception as e:
            messagebox.showinfo("Error", f"Désolée, je n'ai pas reconnu ce que vous avez dit. Veuillez réessayer.\n\nException: {str(e)}")

# define the function to launch the recognition in a new thread
def listen():
    recognition_thread = threading.Thread(target=recognize_speech)
    recognition_thread.start()

root = tk.Tk()
listen_button = tk.Button(root, text="Start Listening", command=listen)
listen_button.pack()
root.mainloop()
