# Author: Saalik Batliwala.
# Date: 22/06/26
# Purpose: Flow Computing Math Game.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk


score = 0
timer_job = None
current_user = None
current_difficulty = ""

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
    },
    {
        "question": "What is 9x12",
        "options": [108, 99, 110, 109],
        "answer": 108
    },
    {
        "question": "What is 7x8",
        "options": [56, 54, 45, 65],
        "answer": 56
    },
    {
        "question": "What is 11x12",
        "options": [132, 121, 111, 142],
        "answer": 132
    },
    {
        "question": "What is 9x7",
        "options": [63, 36, 97, 72],
        "answer": 63
    },
    {
        "question": "What is 48x2",
        "options": [96, 69, 88, 98],
        "answer": 96
    },
    {
        "question": "What is 13x10",
        "options": [120, 100, 130, 110],
        "answer": 130
    },
    {
        "question": "What is 35x3",
        "options": [105, 100, 70, 10.5],
        "answer": 105
    },
    {
        "question": "What is 62x2",
        "options": [122, 124, 123, 120],
        "answer": 124
    }],
"Medium": [{
        "question": "What is the area of a rectangle with length 12cm and width 8cm?",
        "options": [96, 40, 20, 120],
        "answer": 96
    },
    {
        "question": "A triangle has a base of 10cm and height of 6cm. What is its area?",
        "options": [30, 60, 16, 36],
        "answer": 30
    },
    {
        "question": "What is the perimeter of a square with sides of 15cm?",
        "options": [60, 30, 225, 45],
        "answer": 60
    },
    {
        "question": "What is the volume of a cube with side length 5cm?",
        "options": [125, 25, 100, 75],
        "answer": 125
    },
    {
        "question": "Solve for x: 3x + 7 = 22",
        "options": [5, 7, 15, 3],
        "answer": 5
    },
    {
        "question": "A circle has a radius of 7cm. What is its area? (π = 3.14)",
        "options": [153.86, 43.96, 21.98, 307.72],
        "answer": 153.86
    },
    {
        "question": "A right triangle has sides 6cm and 8cm. What is the hypotenuse?",
        "options": [10, 12, 14, 8],
        "answer": 10
    },
    {
        "question": "What is 15% of 240?",
        "options": [36, 24, 45, 60],
        "answer": 36
    },
    {
        "question": "Simplify: 4x + 3x - 2x",
        "options": ["5x", "7x", "9x", "3x"],
        "answer": "5x"
    },
    {
        "question": "A cylinder has radius 3cm and height 10cm. What is its volume? (π = 3.14)",
        "options": [282.6, 94.2, 90, 300],
        "answer": 282.6
    }],

"Hard": [{
        "question": "What is the derivative of f(x)=x²?",
        "options": ["2x", "x", "x²", "2"],
        "answer": "2x"
    },
    {
        "question": "What is the derivative of f(x)=3x³?",
        "options": ["9x²", "3x²", "x³", "9x"],
        "answer": "9x²"
    },
    {
        "question": "What is the derivative of f(x)=5x²+4x?",
        "options": ["10x+4", "5x+4", "10x²", "9x"],
        "answer": "10x+4"
    },
    {
        "question": "Solve: x² = 49",
        "options": ["7", "-7", "±7", "14"],
        "answer": "±7"
    },
    {
        "question": "What is the gradient of y = 4x + 3?",
        "options": [4, 3, 7, 1],
        "answer": 4
    },
    {
        "question": "Differentiate: f(x)=x³+2x",
        "options": ["3x²+2", "x²+2", "3x+2", "x³"],
        "answer": "3x²+2"
    },
    {
        "question": "Find x if 2x² = 50",
        "options": [5, 10, 25, 2],
        "answer": 5
    },
    {
        "question": "What is the integral of 2x?",
        "options": ["x²+C", "2x²+C", "x+C", "2+C"],
        "answer": "x²+C"
    },
    {
        "question": "What is the turning point of y=x²?",
        "options": ["(0,0)", "(1,1)", "(0,1)", "(-1,0)"],
        "answer": "(0,0)"
    },
    {
        "question": "If f(x)=2x+5, what is f(6)?",
        "options": [17, 12, 11, 20],
        "answer": 17
    }]
}
# Creating the main menu.
def main_menu():
    clear_screen()
# Load the background image for the main menu.
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images", "main_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))

# Convert the image so Tkinter can display it.
    background_photo = ImageTk.PhotoImage(background_image)

# Create and position the background.
    background_label = Label(main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep the background behind the other widgets.
    background_label.lower()
# Creating the login button in the main menu.
    login_button = Button(main_screen, text="LOGIN", command=login_screen, font=("Arial", 15, "bold"), width=20, height=2,
    bg="#17102B", fg="#FFFFFF", activebackground="#7B2CBF", activeforeground="#FFFFFF", relief="flat", bd=0,
    highlightthickness=2, highlightbackground="#9D4EDD", highlightcolor="#9D4EDD", cursor="hand2")
    login_button.pack(pady=(250, 5), padx=5)
# Creating the signup button in the main menu.
    signup_button = Button( main_screen, text="SIGN UP", command=signup_screen, font=("Arial", 15, "bold"), width=20, height=2,
    bg="#17102B", fg="#FFFFFF", activebackground="#7B2CBF", activeforeground="#FFFFFF", relief="flat", bd=0,
    highlightthickness=2, highlightbackground="#9D4EDD", highlightcolor="#9D4EDD", cursor="hand2")
    signup_button.pack(pady=10, padx=10)
# Creating the Leaderboard button in the main menu.
    leaderboard_button = Button(main_screen, text="LEADERBOARD", command=leaderboard_screen, font=("Arial", 15, "bold"), width=20, height=2,
    bg="#17102B", fg="#FFFFFF", activebackground="#7B2CBF", activeforeground="#FFFFFF", relief="flat", bd=0,
    highlightthickness=2, highlightbackground="#9D4EDD", highlightcolor="#9D4EDD", cursor="hand2")                         
    leaderboard_button.pack(pady=10, padx=10)
# Creating the Exit button in the main menu.
    close_button = Button(main_screen, text="EXIT", command=close_program, font=("Arial", 20, "bold"),
    bg="#17102B", fg="#FFFFFF", activebackground="#7B2CBF", activeforeground="#FFFFFF", relief="flat", bd=0,
    highlightthickness=1, highlightbackground="#9D4EDD", highlightcolor="#9D4EDD", cursor="hand2")
    close_button.pack(side="bottom", anchor="e", padx=10, pady=10)

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
    password_entry = Entry(main_screen, show="*")
    password_entry.pack()

    con_password_label = Label(main_screen, text="Confirm password", font = (font, 10))
    con_password_label.pack()
    con_password_entry = Entry(main_screen, show="*")
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
    elif len(password) < 6:
        messagebox.showerror("Error","Password must be at least 6 characters.")
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
# Load the login screen background image.
    image_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "Images", "login_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
# Create and position the background.
    background_label = Label(main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep the background behind the login widgets.
    background_label.lower()
    global login_username, login_password
# Username label.
    username_label = Label(main_screen, text="USERNAME", font=("Arial", 10, "bold"), bg="#09051C", fg="#FFFFFF")
    username_label.place(x=400, y=260, anchor="center")

# Username entry box.
    login_username = Entry(main_screen, font=("Arial", 12), width=25,
        bg="#17102B", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat", bd=0,
        highlightthickness=2, highlightbackground="#9D4EDD", highlightcolor="#7B2CBF")
    login_username.place(x=400, y=290, anchor="center")
# Password label.
    password_label = Label( main_screen, text="PASSWORD", font=("Arial", 10, "bold"), bg="#09051C", fg="#FFFFFF")
    password_label.place(x=400, y=335, anchor="center")

# Password entry box.
    login_password = Entry( main_screen, font=("Arial", 12), width=25, show="*",
        bg="#17102B", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat", bd=0,
        highlightthickness=2, highlightbackground="#9D4EDD", highlightcolor="#7B2CBF")
    login_password.place(x=400, y=365, anchor="center")


# Login button.
    login_but = Button(main_screen, text="LOGIN", command=login, font=("Arial", 11, "bold"), width=15, height=2,
        bg="#17102B", fg="#FFFFFF", activebackground="#7B2CBF", activeforeground="#FFFFFF", relief="flat", bd=0,
        highlightthickness=2, highlightbackground="#9D4EDD", highlightcolor="#9D4EDD",cursor="hand2")
    login_but.place(x=400, y=415, anchor="center")


# Back button.
    back_button = Button(main_screen, text="BACK", command=main_menu, font=("Arial", 9, "bold"), width=10, height=1,
        bg="#17102B", fg="#FFFFFF", activebackground="#7B2CBF", activeforeground="#FFFFFF", relief="flat", bd=0,
        highlightthickness=1, highlightbackground="#6A3FA0", highlightcolor="#9D4EDD", cursor="hand2")
    back_button.place(x=400, y=465, anchor="center")
    
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
    global timer_job
    # Cancel the existing timer before destroying the timer label.
    if timer_job is not None:
        try:
            main_screen.after_cancel(timer_job)
        except:
            pass
        timer_job = None
        
    for widget in main_screen.winfo_children():
        widget.destroy()

        
def save_score():
    """Save the current player's score to the scores text file."""

    if current_user is None:
        return

    filepath = os.path.join(os.path.dirname(__file__), "scores.txt")

    time_taken = 60 - time_left

    with open(filepath, "a") as file:
        file.write(f"{current_user},{score},{time_taken},{current_difficulty}\n")


# Creating the main eaderboard screen.
def leaderboard_screen():
    clear_screen()

    title = Label(main_screen, text="Leaderboard", font=(font, 20))
    title.pack(pady=10)

    filepath = os.path.join(os.path.dirname(__file__), "scores.txt")

    leaderboard_data = []

    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                try:
                    player, player_score, time_taken, mode = line.split(",")
                    leaderboard_data.append((player, int(player_score), int(time_taken), mode))
                except ValueError:
                    continue

    except FileNotFoundError:
        pass

# Sort highest score first.
    leaderboard_data.sort(key=lambda x: (-x[1], x[2]))

    leaderboard_frame = Frame(main_screen)
    leaderboard_frame.pack(pady=10)

    header_player = Label( leaderboard_frame, text="Player", font=(font, 12, "bold"), width=15)
    header_score = Label( leaderboard_frame, text="Score", font=(font, 12, "bold"), width=10)
    header_time = Label( leaderboard_frame, text="Time Taken", font=(font, 12, "bold"), width=15)
    header_mode = Label( leaderboard_frame, text="Difficulty", font=(font, 12, "bold"), width=10)
    header_player.grid(row=0, column=0, padx=5)
    header_score.grid(row=0, column=1, padx=5)
    header_time.grid(row=0, column=2, padx=5)
    header_mode.grid(row=0, column=3, padx=5)

    if len(leaderboard_data) == 0:

        Label( leaderboard_frame, text="No scores recorded yet.", font=(font, 12)).grid(row=1, column=0, columnspan=4, pady=10)
    else:
        for i, (player, player_score, time_taken, mode) in enumerate( leaderboard_data, start=1):
            minutes = time_taken // 60
            seconds = time_taken % 60

            Label( leaderboard_frame, text=player, font=(font, 10), width=15).grid(row=i, column=0, padx=5)
            Label( leaderboard_frame, text=str(player_score), font=(font, 10), width=10).grid(row=i, column=1, padx=5)
            Label( leaderboard_frame, text=f"{minutes}m {seconds}s", font=(font, 10), width=15).grid(row=i, column=2, padx=5)
            Label( leaderboard_frame, text=mode, font=(font, 10), width=10).grid(row=i, column=3, padx=5)
    back_button = Button( main_screen, text="Back to Main Menu", command=main_menu, font=(font, 10))
    back_button.pack(pady=20)

# Creating the personal leaderboard screen.
def personal_leaderboard():
    clear_screen()

    Label( main_screen, text="Personal Leaderboard", font=(font, 20)).pack(pady=20)
    filepath = os.path.join(os.path.dirname(__file__), "scores.txt")
    personal_data = []

    if current_user is not None:

        try:
            with open(filepath, "r") as file:

                for line in file:

                    line = line.strip()

                    if line == "":
                        continue

                    try:
                        player, player_score, time_taken, mode = line.split(",")

                        if player == current_user:
                            personal_data.append((player,int(player_score), int(time_taken), mode))
                    except ValueError:
                        continue

        except FileNotFoundError:
            pass

    # Sort highest score first.
    personal_data.sort(key=lambda x: (-x[1], x[2]))

    leaderboard_frame = Frame(main_screen)
    leaderboard_frame.pack(pady=10)

    Label( leaderboard_frame, text="Score", font=(font, 12, "bold"), width=10).grid(row=0, column=0, padx=5)
    Label( leaderboard_frame, text="Time Taken", font=(font, 12, "bold"), width=15).grid(row=0, column=1, padx=5)
    Label( leaderboard_frame, text="Difficulty", font=(font, 12, "bold"), width=10).grid(row=0, column=2, padx=5)
    if len(personal_data) == 0:
        Label( leaderboard_frame, text="No scores recorded yet.", font=(font, 12)).grid(row=1, column=0, columnspan=3, pady=10)
    else:

        for i, (player, player_score, time_taken, mode) in enumerate(
            personal_data,
            start=1
        ):

            minutes = time_taken // 60
            seconds = time_taken % 60

            Label( leaderboard_frame, text=str(player_score), font=(font, 10), width=10).grid(row=i, column=0, padx=5)
            Label( leaderboard_frame, text=f"{minutes}m {seconds}s", font=(font, 10), width=15).grid(row=i, column=1, padx=5)
            Label( leaderboard_frame, text=mode, font=(font, 10), width=10).grid(row=i, column=2, padx=5)
    Button( main_screen, text="Back", command=choose_difficulty_screen).pack(pady=20)

# Creating the difficulty screen after loging on the game.
def choose_difficulty_screen():
    clear_screen()
    title = Label(main_screen, text="Choose Difficulty", font=(font, 20))
    title.pack(pady=20)

    easy_button = Button(main_screen, text="Easy", font=(font, 14), width=15, command=start_game_easy)
    easy_button.pack(pady=10)

    medium_button = Button(main_screen, text="Medium", font=(font, 14), width=15, command=start_game_medium)
    medium_button.pack(pady=10)

    hard_button = Button(main_screen, text="Hard", font=(font, 14), width=15, command=start_game_hard)
    hard_button.pack(pady=10)

    personal_leaderboard_button = Button(main_screen, text="Personal Leaderboard", font=(font, 14), width=18, command=personal_leaderboard)
    personal_leaderboard_button.pack(pady=10)

    back_button = Button(main_screen, text="Back to Main Menu", command=main_menu)
    back_button.pack(pady=20)

# Countdown timer.
def update_timer():
    global time_left

    timer_label.config(text=f"Time Left: {time_left}s")

    if time_left <= 0:
        game_over("Time's Up!")
        return

    time_left -= 1

    if len(main_screen.winfo_children()) > 0:
        main_screen.after(1000, update_timer)

# Game over screen
def game_over(reason):
    clear_screen()

    Label(main_screen, text="YOU LOSE!", font=(font,25,"bold"), fg="red").pack(pady=20)
    Label(main_screen, text=reason, font=(font,15)).pack()

    Button(main_screen, text="Main Menu", command=main_menu).pack(pady=10)
    Button(main_screen, text="Exit Game", command=close_program).pack(pady=10)
    Button(main_screen, text="Play Again", command=choose_difficulty_screen).pack(pady=10)

# Shows the questions for Hard difficulty.
def show_question_easy(i):
    clear_screen()
    global timer_label, lives_label, score
    timer_label = Label(main_screen, font=(font,12))
    timer_label.pack()
    lives_label = Label(main_screen, font=(font,12))
    lives_label.pack()
    score_label = Label(main_screen, text=f"Score: {score}", font=(font,12))
    score_label.pack()

    lives_label.config(text=f"Lives: {lives}")

# Check if quiz is finished.
    if i >= len(quiz_questions["Easy"]):
        save_score()
        Label(main_screen, text=f"Quiz Finished!\nScore: {score}/{len(quiz_questions['Easy'])}", font=(font, 18)).pack(pady=20)
        Button(main_screen, text="Main Menu", command=main_menu).pack(pady=10)
        return

    question = quiz_questions["Easy"][i]

    Label(main_screen, text=question["question"], font=(font,16), wraplength=700, justify="center").pack(pady=20)

    def check_answer(selected):
        global score

        if selected == question["answer"]:
            score += 1
            print("Correct")
        else:
            global lives
            lives -= 1

            if lives <= 0:
                game_over("You ran out of lives!")
                return

# Show the next question.
        show_question_easy(i + 1)
    for option in question["options"]:
            Button(main_screen, text=str(option), width=15, command=lambda x=option: check_answer(x)).pack(pady=5)

    Button(
        main_screen,
        text="Exit Game",
        command=main_menu
        ).pack(pady=15)

# Shows the questions for Medium difficulty.
def show_question_medium(i):
    clear_screen()
    global timer_label, lives_label

    timer_label = Label(main_screen, font=(font,12))
    timer_label.pack()

    lives_label = Label(main_screen, font=(font,12))
    lives_label.pack()
    lives_label.config(text=f"Lives: {lives}")

# Check if quiz is finished.
    if i >= len(quiz_questions["Medium"]):
        save_score()
        Label(main_screen, text=f"Quiz Finished!\nScore: {score}/{len(quiz_questions['Medium'])}", font=(font, 18)).pack(pady=20)
        Button(main_screen, text="Main Menu", command=main_menu).pack(pady=10)
        return

    question = quiz_questions["Medium"][i]

    Label(main_screen, text=question["question"], font=(font,16), wraplength=700, justify="center").pack(pady=20)

    def check_answer(selected):
        global score, lives
        if selected == question["answer"]:
            score += 1
            print("Correct")  
        else:
            lives -= 1
            print("Wrong")

            if lives <= 0:
                game_over("You ran out of lives!")
                return

# Show the next question.
        show_question_medium(i + 1)
    for option in question["options"]:
        Button(
            main_screen,
            text=str(option),
            width=15,
            command=lambda x=option: check_answer(x)
        ).pack(pady=5)

# Shows the questions for Hard difficulty.
def show_question_hard(i):
    clear_screen()
    global timer_label, lives_label
    timer_label = Label(main_screen, font=(font,12))
    timer_label.pack()
    lives_label = Label(main_screen, font=(font,12))
    lives_label.pack()
    lives_label.config(text=f"Lives: {lives}")

# Check if quiz is finished.
    if i >= len(quiz_questions["Hard"]):
        save_score()
        Label(main_screen, text=f"Quiz Finished!\nScore: {score}/{len(quiz_questions['Hard'])}", font=(font, 18)).pack(pady=20)
        Button(main_screen, text="Main Menu", command=main_menu).pack(pady=10)
        return

    question = quiz_questions["Hard"][i]

    Label(main_screen, text=question["question"], font=(font,16), wraplength=700, justify="center").pack(pady=20)

    def check_answer(selected):
        global score, lives
        if selected == question["answer"]:
            score += 1
            print("Correct")
        else:
            lives -= 1
            print("Wrong")

            if lives <= 0:
                game_over("You ran out of lives!")
            return

# Show the next question.
        show_question_hard(i + 1)
    for option in question["options"]:
        Button( main_screen, text=str(option), width=15, command=lambda x=option: check_answer(x)).pack(pady=5)


# Starts the Easy difficulty.
def start_game_easy():
    global score, current_difficulty, lives, time_left
    current_difficulty = "Easy"
    score = 0
    lives = 3
    time_left = 60
    show_question_easy(0)
    update_timer()

# Starts the Medium difficulty.
def start_game_medium():
    global score, current_difficulty, lives, time_left
    current_difficulty = "Medium"
    score = 0
    lives = 3
    time_left = 60
    show_question_medium(0)
    update_timer()

# Starts the Hard difficulty.
def start_game_hard():
    global score, current_difficulty, lives, time_left
    current_difficulty = "Hard"
    score = 0
    lives = 3
    time_left = 60
    show_question_hard(0)
    update_timer()

        
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


