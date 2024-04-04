import tkinter as tk
import random
from tkinter import messagebox
# initial scores of player
player1_score = 0
player2_score = 0
p1_current= 0
p2_current= 0
turn=5

#function:
def start():
    global p1_current 
    p1_current =0
    global p2_current
    p2_current =0
    global player1_score
    player1_score = 0 
    global player2_score
    player2_score = 0
    global turn 
    turn = 5
    f_score_1.config(text=str(player1_score))
    p1_cs.config(text=str(p1_current))

    f_score_2.config(text=str(player2_score))
    p2_cs.config(text=str(p2_current))
    
def play():
    global p1_current
    global p2_current
    global player1_score 
    global player2_score
    global turn
   
    if(turn != 0):
      p1_current = random.randint(1,6)
      player1_score+=p1_current
      f_score_1.config(text=str(player1_score))
      p1_cs.config(text=str(p1_current))

      p2_current = random.randint(1,6)
      player2_score+=p2_current
      f_score_2.config(text=str(player2_score))
      p2_cs.config(text=str(p2_current))

      turn -= 1

    else:
       if(player1_score < player2_score):
        messagebox.showinfo(title='Result', message="You Win!")
       elif(player1_score == player2_score):
         messagebox.showinfo(title='Result', message="Tie!") 
       else:
        messagebox.showinfo(title='Result', message="You Lose!")

window= tk.Tk()
window.title("Dice Game")
window.geometry("800x800")
window.resizable(False, False)
window.config(bg='#cdb4db')
frame_a = tk.Frame(window, bg='#ffc8dd')

#Widgets: 
heading_game = tk.Label(window, text='Welcome to Dice Game!', font=('arial', 40), bg='#cdb4db', fg='#03045e', height= 2)
rule_heading= tk.Label(frame_a, text='Rules', font=('arial', 25), bg='#ffc8dd', fg='#212529', )

#Displaying rules:
rule_heading.grid(row=1,column=1)
rules= { 'rule-1':'Each player will have five turns.',
         'rule-2': 'There will be two players: 1st: you and the 2nd: computer',
         'rule-3':'The numbers on the dice will be added to the final score after each turn.',
         'rule-4':'At the end score will be compared and the winner will be decided. ' }
number = 1
for i, rule in rules.items():
    number += 1

    i= tk.Label(frame_a, text=rule , font=('arial', 16), bg='#ffc8dd', fg='#212529', pady=2, padx=2, height= 2) 
    i.grid(row= number, column=1 )
#Display Box:
number = 0
resultLabel = tk.Label(window, text= 'Final Scores:', font=('arial', 16, 'bold'),bg='#cdb4db', fg='#212529', height=4 )
frame_b = tk.Frame(window, bg='#ffc8dd')

# Final scores:
p1_label = tk.Label(frame_b, text ='Player-1:', font=('arial', 16), bg='#5e548e', fg='#f6fff8', height=6, width= 8)
p1_label.grid(row=1, column=1)
f_score_1 = tk.Label(frame_b, text ='0', font=('arial', 16), bg='#5e548e', fg='#f6fff8', height=6, width= 16 )
f_score_1.grid(row=1, column=2)
p2_label = tk.Label(frame_b, text ='Player-2:', font=('arial', 16), bg='#5e548e', fg='#f6fff8', height=6, width= 8)
p2_label.grid(row=1, column=3)
f_score_2 = tk.Label(frame_b,font=('arial', 16),text= '0', bg='#5e548e', fg='#f6fff8', height= 6, width= 16 )
f_score_2.grid(row=1, column=4)

# current scores of player 1 anad player 2
current_score_label = tk.Label(window, text= 'Current Score:', font=('arial', 16, 'bold'),bg='#cdb4db', fg='#212529', height=4 )
frame_c = tk.Frame(window, bg='#cdb4db')
p1_label = tk.Label(frame_c, text ='Player-1:', font=('arial', 16), bg='#cdb4db', fg='#212529', height=6, width= 8)
p1_label.grid(row=1, column=1)
p1_cs = tk.Label(frame_c, text ='0', font=('arial', 16), bg='#cdb4db', fg='#212529', height=4, width= 16 )
p1_cs.grid(row=1, column=2)
p2_label = tk.Label(frame_c, text ='Player-2:', font=('arial', 16), bg='#cdb4db', fg='#212529', height=6, width= 8)
p2_label.grid(row=1, column=3)
p2_cs = tk.Label(frame_c,font=('arial', 16),text= '0', bg='#cdb4db',fg='#212529', height= 4, width= 16 )
p2_cs.grid(row=1, column=4)
button = tk.Button(window, text= 'Go-on', font=('arial', 16), height=2, width=4, command=lambda: play())
start_button = tk.Button(window, text= 'start New!', font=('arial', 16), height=2, width=8, command=lambda: start())

heading_game.pack()
frame_a.pack()
resultLabel.pack()
frame_b.pack()
current_score_label.pack()
frame_c.pack()
button.pack()
start_button.pack()
window.mainloop()