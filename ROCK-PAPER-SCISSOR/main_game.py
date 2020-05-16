from tkinter import * # pip install tkinter
from tkinter import font as tkfont
from tkinter import messagebox
from random import choice
import pygame # pip install pygame

win = Tk()	# main window
win.title("ROCK-PAPER-SCISSOR [Created By KD SINGH]")	# title of the window
win.iconbitmap("logo.ico")	# logo 
win.geometry("900x500")	# window size
win.resizable(0,0)	# disable maximize button
win['bg'] = 'sky blue'	# background color of the window
main_heading = Label(win, text='ROCK PAPER SCISSOR', bg='sky blue', fg='blue')	
main_heading.config(anchor=CENTER, font=('Arial', 40))
main_heading.pack()


# user choose his/her hand
def user_choice(stri):
    '''
    if user choose stone
    '''
    global player
    player = stri

    global player_choice
    player_choice.destroy()
    if stri == 'SCISSOR':
        player_choice = Label(win, text=f'You choose {stri}', bg='Sky blue') # shows the player choice on screen
    else:
        player_choice = Label(win, text=f'You choose     {stri}', bg='Sky blue')
    player_choice.config(font=('Arial', 20))
    player_choice.place(x=20, y=325)
    stone_button = Button(win, text='STONE', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=100,
                          bd=3, command=lambda: [user_choice('STONE'), computer_choice(), wining_selection()])
    paper_button = Button(win, text='PAPER', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=97.5,
                          bd=3, command=lambda: [user_choice('PAPER'), computer_choice(), wining_selection()])
    scissor_button = Button(win, text='SCISSOR', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=84,
                            bd=3, command=lambda: [user_choice('SCISSOR'), computer_choice(), wining_selection()])
    stone_button1 = Button(win, text='STONE', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=100,
                           bd=3, state=DISABLED)
    paper_button1 = Button(win, text='PAPER', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15),
                           padx=97.5, bd=3, state=DISABLED)
    scissor_button1 = Button(win, text='SCISSOR', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15),
                             padx=84, bd=3, state=DISABLED)

    stone_button.place(x=20, y=155)
    paper_button.place(x=20, y=210)
    scissor_button.place(x=20, y=265)

    stone_button1.place(x=525, y=155)
    paper_button1.place(x=525, y=210)
    scissor_button1.place(x=525, y=265)


#  take random computer choice
def computer_choice():
    list1 = ["STONE", "PAPER", "SCISSOR"]
    global pc_choice
    global count
    count += 1 # counts the total rounds
    pc_choice = choice(list1)
    pc_choice1 = Label(win, text='Computer choice ', bg='Sky blue')
    pc_choice1.config(font=('Arial', 20))
    pc_choice1.place(x=525, y=325)
    if pc_choice == 'SCISSOR':
        pc_choice1 = Label(win, text=f'Computer choice {pc_choice}', bg='Sky blue')
    else:
        pc_choice1 = Label(win, text=f'Computer choice     {pc_choice}', bg='Sky blue')
    pc_choice1.config(font=('Arial', 20))
    pc_choice1.place(x=525, y=325)


# select the winner
def wining_selection():
    global count, pc_choice, player, pc_score, player_score, wini, rounds
    if count < (rounds+1):
        if (pc_choice == 'STONE' and player == 'SCISSOR') or (pc_choice == 'PAPER' and player == 'STONE') or (pc_choice == 'SCISSOR' and player == 'PAPER'):
            pc_score += 10
            your_score = Label(win, text=f'Your Score:  {player_score}\t\t\t\tComputer Score:    {pc_score}',
                               bg='sky blue')
            your_score.config(font=('Arial', 20))
            your_score.place(x=20, y=75)
        elif (pc_choice == 'SCISSOR' and player == 'STONE') or (pc_choice == 'STONE' and player == 'PAPER') or (pc_choice == 'PAPER' and player == 'SCISSOR'):
            player_score += 10
            your_score = Label(win, text=f'Your Score:  {player_score}\t\t\t\tComputer Score:    {pc_score}',
                               bg='sky blue')
            your_score.config(font=('Arial', 20))
            your_score.place(x=20, y=75)
        elif pc_choice == player:
            pass
    if count == rounds:
        if player_score > pc_score:
            wini = Label(win, text='PLAYER WINS', bg='sky blue', fg='blue')
            wini.config(anchor=CENTER, font=('Arial', 40))
            wini.place(x=290, y = 400)
            response = messagebox.askyesno("ROCK-PAPER-SCISSOR [Created By KD SINGH]", "Do you want to play again")
            if response == 1:
                rounds_frame()
            else:
                win.destroy()
        elif player_score < pc_score:
            wini = Label(win, text='COMPUTER WINS', bg='sky blue', fg='blue')
            wini.config(anchor=CENTER, font=('Arial', 40))
            wini.place(x=290, y = 400)
            response = messagebox.askyesno("ROCK-PAPER-SCISSOR [Created By KD SINGH]", "Do you want to play again")
            if response == 1:
                rounds_frame()
            else:
                win.destroy()

        else:
            wini = Label(win, text='GAME TIE', bg='sky blue', fg='blue')
            wini.config(anchor=CENTER, font=('Arial', 40))
            wini.place(x=290, y = 400)
            response = messagebox.askyesno("ROCK-PAPER-SCISSOR [Created By KD SINGH]", "Do you want to play again")
            if response == 1:
                rounds_frame()
            else:
                win.destroy()

# get input from user of total rounds
def take_rounds(num):
    """
    it returns the number of rounds
    """
    choice_frame.destroy()
    global player_score, pc_score, rounds
    rounds = num
    your_score = Label(win, text=f'Your Score:  {player_score}\t\t\t\tComputer Score:    {pc_score}', bg='sky blue')
    hand_choice = Label(win, text='Select your hand\t\t\t\t\t\tComputer Hand', bg='sky blue')
    your_score.config(font=('Arial',20))
    hand_choice.config(font=('Arial', 15))
    your_score.place(x=20,y=75)
    hand_choice.place(x=20,y=120)
    global player_choice
    player_choice = Label(win, text=f'You choose ', bg='Sky blue')
    player_choice.config(font=('Arial', 20))
    player_choice.place(x=20, y=325)
    stone_button = Button(win, text='STONE', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=100, bd=3, command=lambda: [user_choice('STONE'), computer_choice(), wining_selection()])
    paper_button = Button(win, text='PAPER', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=97.5, bd=3, command=lambda: [user_choice('PAPER'), computer_choice(), wining_selection()])
    scissor_button = Button(win, text='SCISSOR', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=84, bd=3, command=lambda: [user_choice('SCISSOR'), computer_choice(), wining_selection()])
    stone_button1 = Button(win, text='STONE', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=100,
                          bd=3, state=DISABLED)
    paper_button1 = Button(win, text='PAPER', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15),
                          padx=97.5, bd=3, state=DISABLED)
    scissor_button1 = Button(win, text='SCISSOR', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15),
                            padx=84, bd=3, state=DISABLED)

    stone_button.place(x=20, y=155)
    paper_button.place(x=20, y=210)
    scissor_button.place(x=20, y=265)

    stone_button1.place(x=525, y=155)
    paper_button1.place(x=525, y=210)
    scissor_button1.place(x=525, y=265)







def rounds_frame():
    '''
    Its is used for taking the input of numbers of rounds from user using radio buttons
    '''
    stone_button = Button(win, text='STONE', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=100,
                          bd=3, state=DISABLED)
    paper_button = Button(win, text='PAPER', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=97.5,
                          bd=3, state=DISABLED)
    scissor_button = Button(win, text='SCISSOR', bg='orange', font=tkfont.Font(family='Goudy Stout', size=15), padx=84,
                            bd=3, state=DISABLED)

    stone_button.place(x=20, y=155)
    paper_button.place(x=20, y=210)
    scissor_button.place(x=20, y=265)
    global choice_frame, count, player_score, pc_score,wini
    player_score = pc_score = count = 0
    choice_frame = LabelFrame(win)
    choice_frame['bg'] = 'sky blue'
    choice_frame.place(x=275, y=125)
    lable1 = Label(choice_frame, text='How many rounds do you want to play:', bg='sky blue')
    lable1.config(anchor=CENTER, font=('Arial', 15))
    lable1.grid(row=0)
    round = IntVar()
    round.set(3)

    # these the radio buttons, user choose number of rounds by selecting the button
    r1 = Radiobutton(choice_frame, text='Three Rounds', bg='sky blue', variable=round, value=3)
    r2 = Radiobutton(choice_frame, text='Five Rounds', bg='sky blue', variable=round, value=5)
    r3 = Radiobutton(choice_frame, text='Ten Rounds', bg='sky blue', variable=round, value=10)
    r4 = Radiobutton(choice_frame, text='Fifteen Rounds', bg='sky blue', variable=round, value=15)
    r5 = Radiobutton(choice_frame, text='Twenty Rounds', bg='sky blue', variable=round, value=20)

    r1.config(font=('Arial', 10))
    r2.config(font=('Arial', 10))
    r3.config(font=('Arial', 10))
    r4.config(font=('Arial', 10))
    r5.config(font=('Arial', 10))

    r1.grid(row=1, sticky=W)
    r2.grid(row=2, sticky=W)
    r3.grid(row=3, sticky=W)
    r4.grid(row=4, sticky=W)
    r5.grid(row=5, sticky=W)


    my_font = tkfont.Font(family='Arial', size=10, weight=tkfont.BOLD)
    submit_button = Button(choice_frame, text='Play Now', font=my_font, bg='sky blue', fg='Blue', padx=15, bd=5,
                           command=lambda: [take_rounds(round.get()), wini.destroy()]).grid(row=6)





if __name__ == '__main__':
    count = 0 # count number of rounds
    player_score = 0 # store player score
    pc_score = 0	# store computer score
    pc_choice = player = ''
    choice_frame = LabelFrame(win) # frame for choices buttons or radio buttons
    choice_frame['bg'] = 'sky blue'
    choice_frame.place(x=275, y=125)
    lable1 = Label(choice_frame, text='How many rounds do you want to play:', bg='sky blue')
    lable1.config(anchor=CENTER, font=('Arial', 15))
    lable1.grid(row=0)

    round = IntVar()
    round.set(3)
    r1 = Radiobutton(choice_frame, text='Three Rounds', bg='sky blue', variable=round, value=3)
    r2 = Radiobutton(choice_frame, text='Five Rounds', bg='sky blue', variable=round, value=5)
    r3 = Radiobutton(choice_frame, text='Ten Rounds', bg='sky blue', variable=round, value=10)
    r4 = Radiobutton(choice_frame, text='Fifteen Rounds', bg='sky blue', variable=round, value=15)
    r5 = Radiobutton(choice_frame, text='Twenty Rounds', bg='sky blue', variable=round, value=20)

    r1.config(font=('Arial', 10))
    r2.config(font=('Arial', 10))
    r3.config(font=('Arial', 10))
    r4.config(font=('Arial', 10))
    r5.config(font=('Arial', 10))

    r1.grid(row=1, sticky=W)
    r2.grid(row=2, sticky=W)
    r3.grid(row=3, sticky=W)
    r4.grid(row=4, sticky=W)
    r5.grid(row=5, sticky=W)

    my_font = tkfont.Font(family='Arial', size=10, weight=tkfont.BOLD)
    submit_button = Button(choice_frame, text='Play Now', font=my_font, bg='sky blue', fg='Blue', padx=15, bd=5,
                           command=lambda : take_rounds(round.get())).grid(row=6)
    # play the music in background
    pygame.mixer.init()
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play(999)


win.mainloop()