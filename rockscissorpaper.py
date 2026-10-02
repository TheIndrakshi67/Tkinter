import random
from tkinter import *
from tkinter import messagebox

def play_game(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    user_choice_label.config(text=f"Your Move:\n{user_choice}", fg="blue")
    computer_choice_label.config(text=f"Computer's Move:\n{computer_choice}", fg="red")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
        result_color = "gray"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
        result_color = "green"
    else:
        result = "Computer Wins! 🤖"
        result_color = "red"
        
    result_label.config(text=result, fg=result_color)

def reset_game():
    user_choice_label.config(text="Your Move:\n-", fg="black")
    computer_choice_label.config(text="Computer's Move:\n-", fg="black")
    result_label.config(text="Make Your Move!", fg="purple")

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("450x550")
root.config(bg="#f0f4f8")

title = Label(
    root, 
    text="Rock Paper Scissors", 
    font=("Arial", 22, "bold"), 
    bg="#3b5998", 
    fg="white", 
    pady=10
)
title.pack(fill=X)

instruction = Label(
    root, 
    text="Choose one of the options below to play against the computer:", 
    font=("Arial", 11), 
    bg="#f0f4f8", 
    wraplength=400
)
instruction.pack(pady=15)

button_frame = Frame(root, bg="#f0f4f8")
button_frame.pack(pady=10)

rock_btn = Button(
    button_frame, 
    text="🪨 Rock", 
    font=("Arial", 12, "bold"), 
    bg="#ff9999", 
    width=10, 
    command=lambda: play_game("Rock")
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = Button(
    button_frame, 
    text="📄 Paper", 
    font=("Arial", 12, "bold"), 
    bg="#99ccff", 
    width=10, 
    command=lambda: play_game("Paper")
)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = Button(
    button_frame, 
    text="✂️ Scissors", 
    font=("Arial", 12, "bold"), 
    bg="#99ff99", 
    width=10, 
    command=lambda: play_game("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=5)

display_frame = Frame(root, bg="white", bd=2, relief=GROOVE, padx=20, pady=20)
display_frame.pack(pady=20, fill=X, padx=40)

user_choice_label = Label(
    display_frame, 
    text="Your Move:\n-", 
    font=("Arial", 14, "bold"), 
    bg="white", 
    justify=CENTER
)
user_choice_label.grid(row=0, column=0, sticky=EW)

vs_label = Label(
    display_frame, 
    text="VS", 
    font=("Arial", 16, "bold"), 
    bg="white"
)
vs_label.grid(row=0, column=1, padx=10)

computer_choice_label = Label(
    display_frame, 
    text="Computer's Move:\n-", 
    font=("Arial", 14, "bold"), 
    bg="white", 
    justify=CENTER
)
computer_choice_label.grid(row=0, column=2, sticky=EW)

display_frame.grid_columnconfigure(0, weight=1)
display_frame.grid_columnconfigure(2, weight=1)

result_label = Label(
    root, 
    text="Make Your Move!", 
    font=("Arial", 18, "bold"), 
    bg="#f0f4f8", 
    fg="purple"
)
result_label.pack(pady=15)

reset_btn = Button(
    root, 
    text="🔄 Reset Game", 
    font=("Arial", 12), 
    bg="#e0e0e0", 
    fg="black", 
    command=reset_game
)
reset_btn.pack(pady=10)

root.mainloop()
