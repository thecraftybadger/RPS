from tkinter import * #Tkinter is a standard Python Graphical User Interface library and is a super easy way to build a GUI application

import random #The random module is used to generate a random number from whatever you set. In this instance it's a number between 1-3. These numbers are then assigned to the computers pick of 1=rock, 2=paper or 3=scissors

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Fry's Rock, Paper, Scissors Extravanganza!")
root.config(bg='seashell3')

Label(root, text = 'Rock, Paper, Scissors (Nerd Edition)' , font='arial 20 bold', bg = 'seashell2').pack()

user_take = StringVar()
Label(root, text = 'Lets play, nerd. rock, paper or scissors?' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'


Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie,you both selected same. Unlucky bruv')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You lose,computer selected paper IDIOT')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('y=You win,computer selected scissors, ledgend')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You lose,computer selected scissors IDIOT')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win,computer selected rock YA ROCKSTAR')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You lose,computer selected rock NERD')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win, computer selected paper YA PAPERSTAR')
    else:
        Result.set('Invalid: choose any one -- rock, paper, scissors. Jheez it is so simple and you jacked it up')


def Reset():
    Result.set("") 
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()

