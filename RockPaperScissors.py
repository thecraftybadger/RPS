from tkinter import * #Tkinter is a standard Python Graphical User Interface library and is a super easy way to build a GUI application

import random #The random module is used to generate a random number from whatever you set. In this instance it's a number between 1-3. These numbers are then assigned to the computers pick of 1=rock, 2=paper or 3=scissors

root = Tk() #Tk() is used to initialize an actual GUI window 
root.geometry('400x400') #Geometry sets the windows height and width 
root.resizable(0,0) #Resizable 0,0 makes it so we can resize the window 
root.title("Fry's Rock, Paper, Scissors Extravanganza!") #Obvs, the title that is displayed on the GUI window 
root.config(bg='seashell3') #Used to set the colour of the background 

Label(root, text = 'Rock, Paper, Scissors (Nerd Edition)' , font='arial 20 bold', bg = 'seashell2').pack() 
#The label() 'widget' implements a display box where you can place text or images. We then put the text, font and background into that widget. Pack is used to organise the widget into a block 

user_take = StringVar() # a string variable that takes and stores the choice that the user inputs. This then gets assigned to variable user_pick in the play function 
Label(root, text = 'Lets play, nerd. rock, paper or scissors?' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)#Explained above. 
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130) #Entry () widget is used when we want to create a user input text field 

comp_pick = random.randint(1,3) #Uses the random module to choose one of the below. Randomly takes any number from 1,3. This 1,3 is then assigned using ifelifelse statements below. 
if comp_pick == 1:
    comp_pick = 'rock'# IF the computer chooses 1, then 1 will be rock et al. 
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'


Result = StringVar() #The result will be a string variable 

def play():
    user_pick = user_take.get() #user take is a string variable that stores the choice hat the user enters 
    if user_pick == comp_pick: #We then give if-else statements to decide if the user or the computer win. 
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
    user_take.set("") #This function will set all variables to an empty string. So resetting the previous guesses once you press the reset button. 

def Exit(): #Will stop and quit the programme 
    root.destroy()

#The below are the defined buttons 

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190) #The button widget is used when we want to display a button 

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310) #Command will call the specific function when the button is clicked. 

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310) 


root.mainloop() #Executes when we run out main programme

#In this, I successfully used Tkinter library for rendering graphics. Used the random module to generate random choices. Created button widgets.
#How to call the function using button. 

