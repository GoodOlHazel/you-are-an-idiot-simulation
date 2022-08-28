# This code won't work unless you create the program with pyinstaller.

# Disclaimer! 
# This program is not the real "You Are An Idiot" virus, but a safe simulation created by SirBluberry.
# I am not associated with "You Are An Idiot" in any way, shape, or form.

from logging import root
import tkinter
from PIL import Image
from pygame import mixer
import pygame
from tkinter import messagebox

messagebox.askokcancel('Disclaimer', 'This program is not the real "You Are An Idiot" virus, but a safe simulation created by SirBluberry.\n\nI am not associated with "You Are An Idiot" in any way, shape, or form.\n\nBy continuing, you agree to listen to an annoying choir insulting you to 3 happy faces and a text saying "You are an idiot!" while the colors of the image invert.')

def idiot():

    root = tkinter.Tk()

    root.attributes("-topmost", True)

    root.title("You are an idiot!")

    root.iconbitmap("idioticon.ico")

    root.geometry("640x480")

    root.resizable(False, False)

    mixer.init()

    pygame.init()

    pygame.mixer.music.load("idiot.ogg")

    pygame.mixer.music.play(5)
    
    frameCnt = 20
    frames = [tkinter.PhotoImage(file='idiot.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

    def update(ind):

        frame = frames[ind]

        ind += 1

        if ind == frameCnt:

            ind = 0

        label.configure(image=frame)

        root.after(50, update, ind)

        pygame.mixer.music.queue("idiot.ogg")

    label = tkinter.Label(root)
    label.pack()
    
    root.after(0, update, 0)

    root.mainloop()

idiot()