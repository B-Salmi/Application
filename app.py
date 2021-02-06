from tkinter import *

# premier fenetre 
window = Tk()


# perso

window.title("Application")
window.geometry("1080x720")
window.minsize(480,360)
window.iconbitmap("icon.ico")
window.config(background="white")



#text

label_title = Label(window,text="Bienvenue sur l'Application", font=("Typo Round Regular Demo", 40))
label_title.pack()


# affichage
window.mainloop()
