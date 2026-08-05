# Author: Saalik Batliwala.
# Date: 22/06/26
# Purpose: Flow Computing Math Game.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

font="Helvetica"

quiz_questions = {
    "Easy" : [{
        "question": "What is 12x12",
        "options": [121, 132, 134, 144],
        "answer": 144
    },
    {
        "question": "What is 10x10",
        "options": [1.00, 10, 100, 1000],
        "answer": 100
    }],
    "Medium" : [{
            "question": "What is 9x12",
            "options": [108, 99, 110, 109],
            "answer": 108
        },
        {
            "question": "What is 7x8",
            "options": [55, 56, 46, 45],
            "answer": 56
        }], 
}

# Creating the main menu and signup and login buttons on the main menu.
def main_menu():
    clear_screen()
    title = Label(main_screen, text="Welcome to Flow Computing!", font=("Courier New", 30, "bold"))
    title.pack(pady=5, padx=5)

    login_button = Button(main_screen, text="Login", command=login_screen, font=(font, 10), width=20, height=3, bg="#FDF4DC")
    login_button.pack(pady=5, padx=5)

    signup_button = Button(main_screen, text="Signup", command=signup_screen, font=(font, 10), width=20, height=3, bg="#FDF4DC")
    signup_button.pack(pady=5, padx=5)

    leaderboard_button = Button(main_screen, text="Leaderboard",command=leaderboard_screen, font=(font, 10), width=20, height=3, bg="#FDF4DC")                         
    leaderboard_button.pack(pady=5, padx=5)

    close_button = Button(main_screen, text="Exit", command=close_program, bg="#FDF4DC")
    close_button.pack(pady=100, padx=5, anchor="e")

# Creating the signup screen after clicking on the button.
def signup_screen():
    clear_screen()

    global username_entry, password_entry, con_password_entry

    title = Label(main_screen, text="Sign Up", font = (font, 20))
    title.pack()

    username_label = Label(main_screen, text="Enter desired username", font = (font, 10))
    username_label.pack()
    username_entry = Entry(main_screen)
    username_entry.pack()

    password_label = Label(main_screen, text="Create a new password", font = (font, 10))
    password_label.pack()
    password_entry = Entry(main_screen)
    password_entry.pack()

    con_password_label = Label(main_screen, text="Confirm password", font = (font, 10))
    con_password_label.pack()
    con_password_entry = Entry(main_screen)
    con_password_entry.pack()

    sign_up_but = Button(main_screen, text="Sign Up", command=signup, font=(font, 10))
    sign_up_but.pack()

    back_but = Button(main_screen, text="Back", command=main_menu, font = (font, 10))
    back_but.pack()

# Creating the signup button to take to the signup screen.
def signup():
    username=username_entry.get()
    password = password_entry.get()
    con_password = con_password_entry.get()

    if username == "" or password == "" or con_password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    if password != con_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    filepath = os.path.join(os.path.dirname(__file__), "users.txt")

    try:
        with open(filepath, "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(",")
                if stored_user == username:
                    messagebox.showerror("Error", "Username already exists")
                    return
    except FileNotFoundError:
        pass

    with open(filepath, "a") as file:
        file.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Account created!")
    
    main_menu()

# Creating the login screen after clicking on the button.
def login_screen():
    clear_screen()

    global login_username, login_password

    title = Label(main_screen, text="Login", font = (font, 20))
    title.pack()

    username_label = Label(main_screen, text="Enter username", font = (font, 10))
    username_label.pack()
    login_username = Entry(main_screen)
    login_username.pack()

    password_label = Label(main_screen, text="Enter password", font = (font, 10))
    password_label.pack()
    login_password = Entry(main_screen)
    login_password.pack()

    login_but = Button(main_screen, text="Login", command=login, font=(font, 10))
    login_but.pack()

    back_but = Button(main_screen, text="Back", command=main_menu, font = (font, 10))
    back_but.pack()
    
# Creating the login button to take to the login screen.
def login():
    username = login_username.get()
    password = login_password.get()

    filepath = os.path.join(os.path.dirname(__file__), "users.txt")

    try:
        with open(filepath, "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(",")

                if username == stored_user and password == stored_pass:
                    global current_user
                    current_user = username
                    messagebox.showinfo("Success", "Login successful!")
                    choose_difficulty_screen()
                    return

        messagebox.showerror("Error", "Invalid username or password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users registered")

def clear_screen():
    for widget in main_screen.winfo_children():
        widget.destroy()

# Creating the main leaderboard screen.
def leaderboard_screen():
    clear_screen()

    title = Label(main_screen, text="Leaderboard", font=(font, 20))
    title.pack(pady=10)

    leaderboard_data = [
        ("Player1", 100, "2m 30s", "Easy"),
        ("Player2", 80, "3m 15s", "Medium"),
        ("Player3", 60, "4m 0s", "Hard"),
    ]

    leaderboard_frame = Frame(main_screen)
    leaderboard_frame.pack(pady=10)

    header_player = Label(leaderboard_frame, text="Player", font=(font, 12, "bold"), width=15)
    header_score = Label(leaderboard_frame, text="Score", font=(font, 12, "bold"), width=10)
    header_time = Label(leaderboard_frame, text="Time Taken", font=(font, 12, "bold"), width=15)
    header_mode = Label(leaderboard_frame, text="Difficulty", font=(font, 12, "bold"), width=10)

    header_player.grid(row=0, column=0, padx=5)
    header_score.grid(row=0, column=1, padx=5)
    header_time.grid(row=0, column=2, padx=5)
    header_mode.grid(row=0, column=3, padx=5)

    for i, (player, score, time_taken, mode) in enumerate(leaderboard_data, start=1):
        Label(leaderboard_frame, text=player, font=(font, 10), width=15).grid(row=i, column=0, padx=5)
        Label(leaderboard_frame, text=str(score), font=(font, 10), width=10).grid(row=i, column=1, padx=5)
        Label(leaderboard_frame, text=time_taken, font=(font, 10), width=15).grid(row=i, column=2, padx=5)
        Label(leaderboard_frame, text=mode, font=(font, 10), width=10).grid(row=i, column=3, padx=5)

    back_button = Button(main_screen, text="Back to Main Menu", command=main_menu, font=(font, 10))
    back_button.pack(pady=20)


def choose_difficulty_screen():
    clear_screen()
    title = Label(main_screen, text="Choose Difficulty", font=(font, 20))
    title.pack(pady=20)

    easy_button = Button(main_screen, text="Easy", font=(font, 14), width=15, command=start_game_easy)    #command=login_screen, font=(font, 10), width=20, height=3, bg="#FDF4DC")
    easy_button.pack(pady=10)

    medium_button = Button(main_screen, text="Medium", font=(font, 14), width=15, command=start_game_medium)
    medium_button.pack(pady=10)

    hard_button = Button(main_screen, text="Hard", font=(font, 14), width=15, command=start_game_hard)
    hard_button.pack(pady=10)

    personal_leaderboard_button = Button(main_screen, text="Personal Leaderboard", font=(font, 14), width=18, command=personal_leaderboard)
    personal_leaderboard_button.pack(pady=10)

    back_button = Button(main_screen, text="Back to Main Menu", command=main_menu)
    back_button.pack(pady=20)


def start_game_easy():
    clear_screen()
    i = 0
    question = quiz_questions["Easy"][i]

    Label(main_screen, text=question["question"], font=(font, 16)).pack(pady=20)

    for option in question["options"]:
        Button(main_screen, text=str(option), width=15).pack(pady=5)


def start_game_medium():
    clear_screen()
    i = 0
    question = quiz_questions["Medium"][i]

    Label(main_screen, text=question["question"], font=(font, 16)).pack(pady=20)

    for option in question["options"]:
        Button(main_screen, text=str(option), width=15).pack(pady=5)

def start_game_hard():
    clear_screen()
    i = 0
    question = quiz_questions["Hard"][i]

    Label(main_screen, text=question["question"], font=(font, 16)).pack(pady=20)

    for option in question["options"]:
        Button(main_screen, text=str(option), width=15).pack(pady=5)

        
# Creating the exit button to quit the program.
def close_program():
    if messagebox.askyesno("Exit", "Are you sure you want to quit?"):
        main_screen.destroy()

main_screen = Tk()
main_screen.geometry("800x600")
main_screen.title("Welcome to Flow Computing Math Game")
main_screen.config(bg="#A799B7")
main_menu()
main_screen.mainloop()


