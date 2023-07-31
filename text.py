import pyttsx3
from tkinter import *

def text_to_speech():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Création de l'interface utilisateur
window = Tk()
window.title("Convertisseur de texte en parole")
window.geometry('400x200')

label = Label(window, text="Entrez le texte :")
label.grid(column=0, row=0)

text_entry = Entry(window,width=50)
text_entry.grid(column=0, row=1)

button = Button(window, text="Convertir", command=text_to_speech)
button.grid(column=0, row=2)

window.mainloop()
