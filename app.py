from tkinter import *


# premier fenetre 
window = Tk()


# perso

window.title("Application")
window.geometry("1080x720")
window.minsize(480,360)
window.iconbitmap("icon.ico")
window.config(background="#1C013B")


#frame

frame = Frame(window, bg ="#1C013B")

#text

label_title = Label(frame, text="Bienvenue sur l'Application", font=("Typo Round Regular Demo", 40), bg='#1C013B', fg='#A70048')
label_title.pack()


#text

label_subtitle = Label(frame, text="Premier tache", font=("Courrier", 25), bg='#1C013B', fg='white')
label_subtitle.pack()


yt_button = Button(frame, text="Trier", font=("Courrier", 25), bg='white', fg='yellow' )
yt_button.pack(pady=25,fill=X)


frame.pack(expand=YES)



# affichage
window.mainloop()
