from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from Algorithm import Algorithm

root = Tk(className = " Are You the One?") # sets up beginning window, its background, and music
root.geometry("510x750")
root.resizable(0,0)

background_start = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\Resources\\AYTO_Background.jpg").resize((510,750)))
background = Label(image=background_start)
background.place(x=0, y=0, relwidth=1, relheight=1)

def begin():
    startContinue.destroy()
    messagebox.showinfo("Instructions", "Welcome to Are You the One! There are 16 people and each person has their own quirks. The goal of this game is to match each contestant with their perfect match as quick as possible. There is a truth booth that shows if two people are a perfect pair and how many of the seven other pairs are correct. Pick a difficulty and proceed.")
    easy.place(x=20, y=675)
    medium.place(x=175, y=675)
    hard.place(x=350, y=675)
def info(place):
    top = Toplevel()
    top.geometry('600x300')
    top.title("Know the Contestants")
    v = Scrollbar(top)
    v.pack(side = RIGHT, fill = Y)
    t = Text(top, width = 15, height = 50, wrap = NONE,
                 yscrollcommand = v.set)
    index = 0
    for place in range(16):
        for info in game.players[place].getData():
            t.insert(END, info + "\n")
    t.pack(side=TOP, fill=X)
def TB():
    pairs = [(n1.get(),n2.get()), (n3.get(),n4.get()), (n5.get(),n6.get()), (n7.get(),n8.get()), 
             (n9.get(),n10.get()), (n11.get(),n12.get()), (n13.get(),n14.get())]
    good = game.perfectMatches(pairs)
    if good == 7 and game.perfectPair(game.getName(n15.get()),game.getName(n16.get())):
        messagebox.showinfo("Congratulations", "You matched everyone in " + str(game.weeks) + " weeks!")
        root.destroy()
    try:
        for p in game.players:
            p.learn()
        if game.perfectPair(game.getName(n15.get()),game.getName(n16.get())):
            t1 = Label(text="The truth booth says these are the perfect match!")
            t1.place(x=100,y=600)
        else:
            t1 = Label(text="The truth both says these aren't the perfect match")
            t1.place(x=100,y=600)
        t2 = Label(text="There are " + str(good) + " other good matches")
        t2.place(x=100,y=700)
        game.weeks += 1
    except IndexError:
        if game.perfectPair(game.getName(n15.get()),game.getName(n16.get())):
            t1 = Label(text="The truth booth says these are the perfect match!")
            t1.place(x=100,y=600)
        else:
            t1 = Label(text="The truth both says these aren't the perfect match")
            t1.place(x=100,y=600)
        t2 = Label(text="There are " + str(good) + " other good matches")
        t2.place(x=100,y=700)
        game.weeks += 1
def start(dif):
    global game
    global n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16

    game = Algorithm(dif)
    easy.destroy()
    medium.destroy()
    hard.destroy()
    names = game.save

    n1 = StringVar()
    n1.set(names[0])
    a1 = OptionMenu(root, n1, *names)
    a1.place(x=30,y=30)
    n2 = StringVar()
    n2.set(names[1])
    a2 = OptionMenu(root, n2, *names)
    a2.place(x=150,y=30)

    n3 = StringVar()
    n3.set(names[2])
    b1 = OptionMenu(root, n3, *names)
    b1.place(x=30,y=90)
    n4 = StringVar()
    n4.set(names[3])
    b2 = OptionMenu(root, n4, *names)
    b2.place(x=150,y=90)

    n5 = StringVar()
    n5.set(names[4])
    c1 = OptionMenu(root, n5, *names)
    c1.place(x=30,y=150)
    n6 = StringVar()
    n6.set(names[5])
    c2 = OptionMenu(root, n6, *names)
    c2.place(x=150,y=150)

    n7= StringVar()
    n7.set(names[6])
    d1 = OptionMenu(root, n7, *names)
    d1.place(x=30,y=210)
    n8 = StringVar()
    n8.set(names[7])
    d2 = OptionMenu(root, n8, *names)
    d2.place(x=150,y=210)

    n9 = StringVar()
    n9.set(names[8])
    e1 = OptionMenu(root, n9, *names)
    e1.place(x=30,y=270)
    n10 = StringVar()
    n10.set(names[9])
    e2 = OptionMenu(root, n10, *names)
    e2.place(x=150,y=270)

    n11 = StringVar()
    n11.set(names[10])
    f1 = OptionMenu(root, n11, *names)
    f1.place(x=30,y=330)
    n12 = StringVar()
    n12.set(names[11])
    f2 = OptionMenu(root, n12, *names)
    f2.place(x=150,y=330)

    n13 = StringVar()
    n13.set(names[12])
    g1 = OptionMenu(root, n13, *names)
    g1.place(x=30,y=390)
    n14 = StringVar()
    n14.set(names[13])
    g2 = OptionMenu(root, n14, *names)
    g2.place(x=150,y=390)

    n15 = StringVar()
    n15.set(names[14])
    h1 = OptionMenu(root, n15, *names)
    h1.place(x=30,y=500)
    n16 = StringVar()
    n16.set(names[15])
    h2 = OptionMenu(root, n16, *names)
    h2.place(x=150,y=500)

    information.place(x=300,y=100)
    truth.place(x=300,y=500)

startContinue = Button(text = "Continue",command = begin, padx=50, pady=25) # starting the game
startContinue.place(x=175, y=675)

easy = Button(text = "Easy",command=lambda: start(3), padx=50, pady=25)
easy.place(x=-100,y=-100)
medium = Button(text = "Medium",command=lambda: start(2), padx=50, pady=25)
medium.place(x=-100,y=-100)
hard = Button(text = "Hard",command=lambda: start(1), padx=50, pady=25)
hard.place(x=-100,y=-100)

information = Button(text = "Info",command=lambda: info(0), padx=50, pady=25)
information.place(x=-100,y=-100)

truth = Button(text = "Truth Booth",command = TB, padx=50, pady=25)
truth.place(x=-100,y=-100)

root.mainloop()