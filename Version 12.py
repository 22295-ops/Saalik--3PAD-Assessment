# Author: Saalik Batliwala.
# Date: 22/06/26
# Purpose: Flow Computing Math Game.

from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# Stores the score, lives and time.
class Game:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.time_left = 60

    def reset(self):
        self.score = 0
        self.lives = 3
        self.time_left = 60


game = Game()

timer_job = None
current_user = None
current_difficulty = ""

# Font used throughout the code. 
font="Helvetica"

# All the questions for the 3 different difficulties. 
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
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

# Keep the background behind the other widgets.
    background_label.lower()
# Creating the login button in the main menu.
    login_button = Button(main_screen, text="LOGIN", command=login_screen, font=(font, 15, "bold"), width=20, height=2, bg="#17102B", fg="White")
    login_button.pack(pady=(250, 5), padx=5)
# Creating the signup button in the main menu.
    signup_button = Button( main_screen, text="SIGN UP", command=signup_screen, font=(font, 15, "bold"), width=20, height=2, bg="#17102B", fg="White")
    signup_button.pack(pady=10, padx=10)
# Creating the Leaderboard button in the main menu.
    leaderboard_button = Button(main_screen, text="LEADERBOARD", command=leaderboard_screen, font=(font, 15, "bold"), width=20, height=2, bg="#17102B", fg="White")                         
    leaderboard_button.pack(pady=10, padx=10)
# Creating the Exit button in the main menu.
    close_button = Button(main_screen, text="EXIT", command=close_program, font=(font, 20, "bold"), bg="#17102B", fg="White")
    close_button.pack(side="bottom", anchor="e", padx=10, pady=10)

# Creating the signup screen after clicking on the button.
def signup_screen():
    global signup_username, signup_password, signup_confirm
    clear_screen()

# Load the signup screen background image.
    image_path = os.path.join( os.path.dirname(os.path.dirname(__file__)), "Images", "signup_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)
    background_label.lower()

# Username label
    username_label = Label( main_screen, text="USERNAME", font=(font, 10, "bold"), bg="#09051C", fg="White")
    username_label.place(x=400, y=235, anchor="center")

# Username entry box
    signup_username = Entry( main_screen, font=(font, 12), width=25, bg="#17102B", fg="White", insertbackground="White")
    signup_username.place(x=400, y=265, anchor="center")

# Password label
    password_label = Label( main_screen, text="PASSWORD", font=(font, 10, "bold"), bg="#09051C", fg="White")
    password_label.place(x=400, y=300, anchor="center")

# Password entry box
    signup_password = Entry( main_screen, font=(font, 12), width=25, show="*", bg="#17102B", fg="White", insertbackground="White")
    signup_password.place(x=400, y=330, anchor="center")

# Confirm password label
    confirm_label = Label( main_screen, text="CONFIRM PASSWORD", font=(font, 10, "bold"), bg="#09051C", fg="White")
    confirm_label.place(x=400, y=365, anchor="center")

# Confirm password entry box
    signup_confirm = Entry( main_screen, font=(font, 12), width=25, show="*", bg="#17102B", fg="White", insertbackground="White")
    signup_confirm.place(x=400, y=395, anchor="center")

# Signup button
    signup_button = Button( main_screen, text="SIGN UP", command=signup, font=(font, 11, "bold"), width=15, height=2, bg="#17102B", fg="White")
    signup_button.place(x=400, y=445, anchor="center")

# Back button
    back_button = Button( main_screen, text="BACK", command=main_menu, font=(font, 9, "bold"), width=10, height=1, bg="#17102B", fg="White")
    back_button.place(x=400, y=485, anchor="center")

# Creating the signup button to take to the signup screen.
def signup():
    username = signup_username.get()
    password = signup_password.get()
    confirm_password = signup_confirm.get()

    if username == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "Please fill all fields")
    elif len(password) < 6:
        messagebox.showerror("Error","Password must be at least 6 characters.")
        return
# Checks the username is only letters and numbers.
    if not username.isalnum():
        messagebox.showerror( "Invalid Username", "Username can only contain letters and numbers.")
        return
    
    if password != confirm_password:
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
    background_label.place(x=0, y=0)

# Keep the background behind the login widgets.
    background_label.lower()
    global login_username, login_password
    
# Username label.
    username_label = Label(main_screen, text="USERNAME", font=(font, 10, "bold"), bg="#09051C", fg="White")
    username_label.place(x=400, y=260, anchor="center")

# Username entry box.
    login_username = Entry(main_screen, font=(font, 12), width=25, bg="#17102B", fg="White")
    login_username.place(x=400, y=290, anchor="center")
# Password label.
    password_label = Label( main_screen, text="PASSWORD", font=(font, 10, "bold"), bg="#09051C", fg="White")
    password_label.place(x=400, y=335, anchor="center")

# Password entry box.
    login_password = Entry( main_screen, font=(font, 12), width=25, show="*", bg="#17102B", fg="White")
    login_password.place(x=400, y=365, anchor="center")
    
# Login button.
    login_but = Button(main_screen, text="LOGIN", command=login, font=(font, 11, "bold"), width=15, height=2, bg="#17102B", fg="White")
    login_but.place(x=400, y=415, anchor="center")

# Back button.
    back_button = Button(main_screen, text="BACK", command=main_menu, font=(font, 9, "bold"), width=10, height=1, bg="#17102B", fg="White")
    back_button.place(x=400, y=465, anchor="center")
    
# Check the entered username and password are in the users textfile.
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

# Clears the screen from all the widgets. 
def clear_screen(cancel_timer=True):
    global timer_job, timer_label
# Cancel the existing timer before destroying the timer label.
    if cancel_timer and timer_job is not None:
        try:
            main_screen.after_cancel(timer_job)
        except:
            pass
        timer_job = None
        
    for widget in main_screen.winfo_children():
        widget.destroy()
    if cancel_timer:
        timer_label = None
        
def save_score():
    """Save the current player's score to the scores text file."""

    if current_user is None:
        return

    filepath = os.path.join(os.path.dirname(__file__), "scores.txt")

    time_taken = 60 - game.time_left

    with open(filepath, "a") as file:
        file.write(f"{current_user},{game.score},{time_taken},{current_difficulty}\n")


# Creating the main eaderboard screen.
def leaderboard_screen():
    clear_screen()
# Load the leaderboard background image.
    image_path = os.path.join( os.path.dirname(os.path.dirname(__file__)), "Images", "leaderboard_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.lower()

    title = Label( main_screen, text="LEADERBOARD", font=(font, 22, "bold"), bg="#09051C", fg="White" )
    title.pack(pady=20)
    
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
    leaderboard_data = leaderboard_data[:15]

    leaderboard_frame = Frame(main_screen, bg="#09051C")
    leaderboard_frame.pack(pady=10)

    header_player = Label( leaderboard_frame, text="PLAYER", font=(font, 12, "bold"), width=15, bg="#09051C", fg="#9D4EDD")
    header_score = Label( leaderboard_frame, text="SCORE", font=(font, 12, "bold"), width=10, bg="#09051C", fg="#9D4EDD")
    header_time = Label( leaderboard_frame, text="TIME TAKEN", font=(font, 12, "bold"), width=15, bg="#09051C", fg="#9D4EDD")
    header_mode = Label( leaderboard_frame, text="DIFFICULTY", font=(font, 12, "bold"), width=10, bg="#09051C", fg="#9D4EDD")
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

            Label( leaderboard_frame, text=player, font=(font, 10), width=15, bg="#09051C", fg="White").grid(row=i, column=0, padx=5)
            Label( leaderboard_frame, text=str(player_score), font=(font, 10, "bold"), width=10, bg="#09051C", fg="White").grid(row=i, column=1, padx=5)
            Label( leaderboard_frame, text=f"{minutes}m {seconds}s", font=(font, 10), width=15, bg="#09051C", fg="White").grid(row=i, column=2, padx=5)
            Label( leaderboard_frame, text=mode, font=(font, 10), width=10, bg="#09051C", fg="White").grid(row=i, column=3, padx=5)
    back_button = Button( main_screen, text="BACK TO MAIN MENU", command=main_menu, font=(font, 10, "bold"), bg="#17102B",fg="White")
    back_button.pack(pady=20)

# Creating the personal leaderboard screen.
def personal_leaderboard():
    clear_screen()
    image_path = os.path.join( os.path.dirname(os.path.dirname(__file__)), "Images", "personal_leaderboard_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label( main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place( x=0, y=0)
    background_label.lower()

    title = Label(main_screen, text="PERSONAL LEADERBOARD", font=(font, 20, "bold"), bg="#09051C", fg="white")
    title.place( x=400, y=65, anchor="center")

    filepath = os.path.join( os.path.dirname(__file__), "scores.txt")
    leaderboard_data = []
    try:
        with open(filepath, "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                try:
                    player, player_score, time_taken, mode = line.split(",")

                    if player == current_user:
                        leaderboard_data.append(( player, int(player_score), int(time_taken), mode))
                except ValueError:
                    continue

    except FileNotFoundError:
        pass
    leaderboard_data.sort( key=lambda x: (-x[1], x[2]))
    leaderboard_data = leaderboard_data[:10]

    leaderboard_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#9D4EDD")
    leaderboard_frame.place( x=400, y=315, width=600, height=390, anchor="center")

    Label( leaderboard_frame, text="SCORE", font=(font, 11, "bold"), width=15, bg="#09051C", fg="#C85CFF").grid(row=0, column=0, padx=25, pady=(15, 8))
    Label( leaderboard_frame, text="TIME TAKEN", font=(font, 11, "bold"), width=15, bg="#09051C", fg="#C85CFF").grid( row=0, column=1, padx=25, pady=(15, 8))
    Label( leaderboard_frame, text="DIFFICULTY", font=(font, 11, "bold"), width=15, bg="#09051C", fg="#C85CFF").grid( row=0, column=2, padx=25, pady=(15, 8))

    if len(leaderboard_data) == 0:
        Label( leaderboard_frame, text="No scores recorded yet.", font=(font, 12), bg="#09051C", fg="white").grid(row=1, column=0, columnspan=3, pady=30)

    else:
        for i, (player, player_score, time_taken, mode) in enumerate( leaderboard_data, start=1):
            seconds = time_taken % 60

            Label( leaderboard_frame, text=str(player_score), font=(font, 11, "bold"), width=15, bg="#09051C", fg="white").grid( row=i, column=0, pady=4)
            Label( leaderboard_frame, text=f"{seconds}s", font=(font, 11), width=15, bg="#09051C", fg="white").grid(row=i, column=1, pady=4)

            Label( leaderboard_frame, text=mode, font=(font, 11), width=15, bg="#09051C", fg="white").grid( row=i, column=2, pady=4)

    back_button = Button( main_screen, text="BACK", command=choose_difficulty_screen, font=(font, 10, "bold"), bg="#09051C", fg="white")
    back_button.place( x=400, y=555, width=130, height=40, anchor="center")

# Creating the difficulty screen after loging on the game.
def choose_difficulty_screen():
    clear_screen()

# Load the Choose Difficulty background image.
    image_path = os.path.join( os.path.dirname(os.path.dirname(__file__)), "Images", "difficulty_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label( main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place( x=0, y=0, relwidth=1, relheight=1)

# Put the background behind all other widgets.
    background_label.lower()

# All the buttons on the screen. 
    title = Label( main_screen, text="CHOOSE DIFFICULTY", font=(font, 22, "bold"), bg="#09051C", fg="White")
    title.pack(pady=(45, 25))

    easy_button = Button( main_screen, text="EASY", font=(font, 13, "bold"), width=15, height=2, command=start_game_easy, bg="#071F12", fg="White")
    easy_button.place( x=400, y=220, anchor="center" )

    medium_button = Button( main_screen, text="MEDIUM", font=(font, 13, "bold"), width=15, height=2, command=start_game_medium, bg="#211B05", fg="White")
    medium_button.place( x=400, y=290, anchor="center")

    hard_button = Button( main_screen, text="HARD", font=(font, 13, "bold"), width=15, height=2, command=start_game_hard,  bg="#26080C", fg="White")
    hard_button.place( x=400, y=360, anchor="center")

    personal_leaderboard_button = Button( main_screen, text="PERSONAL LEADERBOARD", font=(font, 11, "bold"), width=30, height=2, command=personal_leaderboard, bg="#17102B", fg="White")
    personal_leaderboard_button.place( x=400, y=430, anchor="center")
    
    back_button = Button( main_screen, text="BACK TO MAIN MENU", command=main_menu, font=(font, 9, "bold"), bg="#10152A", fg="White")
    back_button.place( x=400, y=500, anchor="center")

# Countdown timer.
def stop_timer():
    global timer_job, timer_label

    if timer_job is not None:
        try:
            main_screen.after_cancel(timer_job)
        except:
            pass

        timer_job = None

    timer_label = None

def update_timer():
    global timer_job, timer_label

# Stop if there is no active timer.
    if timer_label is None:
        timer_job = None
        return

# Display the current time.
    timer_label.config(text=f"Time Left: {game.time_left}s")

# Stop the game when the timer reaches zero.
    if game.time_left <= 0:
        timer_job = None
        game_over("Time's Up!")
        return
    game.time_left -= 1
    timer_job = main_screen.after(1000, update_timer)

# Game over screen.
def game_over(reason):
    clear_screen(False)
    stop_timer()

    image_path = os.path.join( os.path.dirname(os.path.dirname( __file__ )), "Images", "gameover_background.png" )
    background_image = Image.open(image_path)
    background_image = background_image.resize(( 800, 600 ))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label( main_screen, image=background_photo )
    background_label.image = background_photo
    background_label.place( x=0, y=0 )
    background_label.lower()

    reason_label = Label( main_screen, text=reason, font=(font, 16, "bold" ), bg="#09051C", fg="White" )
    reason_label.place( x=400, y=310, anchor="center")

    score_label = Label( main_screen, text=f"Final Score: {game.score}", font=(font, 18, "bold" ), bg="#09051C", fg="#C42CFF" )
    score_label.place( x=400, y=350, anchor="center" )

    if current_difficulty == "Easy":
        play_again_command = start_game_easy

    elif current_difficulty == "Medium":
        play_again_command = start_game_medium

    else:
        play_again_command = start_game_hard


    play_again_button = Button( main_screen, text="PLAY AGAIN", command=play_again_command, font=(font, 11, "bold"), bg="#09051C", fg="White" )
    play_again_button.place( x=400, y=400, width=180, height=45, anchor="center" )

    difficulty_button = Button( main_screen, text="CHOOSE DIFFICULTY", command=choose_difficulty_screen, font=(font, 11, "bold"), bg="#09051C", fg="White" )
    difficulty_button.place( x=400, y=455, width=220, height=45, anchor="center" )

    main_menu_button = Button( main_screen, text="MAIN MENU", command=main_menu, font=(font, 10, "bold"), bg="#09051C", fg="white" )
    main_menu_button.place( x=400, y=510, width=150, height=40, anchor="center" )

    exit_button = Button( main_screen, text="EXIT GAME", command=main_screen.destroy, font=(font, 9, "bold"), bg="#09051C", fg="white" )
    exit_button.place(x=400, y=555, width=130, height=35, anchor="center" )

# Shows the questions for easy difficulty.
def show_question_easy(i):
    clear_screen(False)
    global timer_label, lives_label
    
    image_path = os.path.join( os.path.dirname( os.path.dirname (__file__)), "Images", "quiz_background.png" )
    background_image = Image.open(image_path)
    background_image = background_image.resize( (800, 600) )
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label( main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place( x=0, y=0 )
    background_label.lower()

    time_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#00BFFF" )
    time_frame.place( x=200, y=70, width=250, height=70, anchor="center")
    Label( time_frame, text="TIME LEFT", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=( 7, 0) )
    timer_label = Label( time_frame, text=f"{game.time_left}s", font=(font, 20, "bold"), bg="#09051C",fg="#00BFFF" )
    timer_label.pack()

    lives_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#7B2CFF" )
    lives_frame.place( x=400, y=70, width=150, height=70, anchor="center")
    Label( lives_frame, text="LIVES", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    lives_label = Label( lives_frame, text="♥ " * game.lives, font=(font, 20, "bold"), bg="#09051C", fg="#FF3131" )
    lives_label.pack()

    score_frame = Frame( main_screen, bg="#09051C", highlightthickness=2,highlightbackground="#C42CFF" )
    score_frame.place( x=550, y=70, width=150, height=70, anchor="center")
    Label( score_frame, text="SCORE", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0) )
    Label( score_frame, text=str(game.score), font=(font, 20, "bold"), bg="#09051C", fg="White").pack()
                                                                                              
    if i >= len(quiz_questions["Easy"]):
        stop_timer()
        save_score()
        Label( main_screen, text="QUIZ FINISHED!", font=(font, 24, "bold"), bg="#09051C", fg="White").place( x=400, y=250, anchor="center")
        Label( main_screen, text=f"Score: {game.score}/{len(quiz_questions['Easy'])}", font=(font, 18, "bold"),
        bg="#09051C",fg="#C42CFF").place( x=400, y=300, anchor="center")

        Button( main_screen, text="PLAY AGAIN", command=start_game_easy, font=(font, 11, "bold"), bg="#09051C",fg="White").place( x=400, y=370, width=180, height=45, anchor="center")
        Button( main_screen, text="CHOOSE DIFFICULTY", command=choose_difficulty_screen, font=(font, 11, "bold"), bg="#09051C", fg="White").place( x=400, y=425, width=180, height=45, anchor="center")
        return

    question = quiz_questions["Easy"][i]

    question_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#C42CFF")
    question_frame.place( x=400, y=255, width=560, height=95, anchor="center")
    Label( question_frame, text=question["question"], font=(font, 20, "bold"), bg="#09051C", fg="White", wraplength=520, justify="center").pack(expand=True)

# Checks if the answer given was correct, if not then takes a live.
    def check_answer(selected):

        if selected == question["answer"]:
            game.score += 1
        else:
            game.lives -= 1
            if game.lives <= 0:
                game_over("You ran out of lives!")
                return
        show_question_easy(i + 1)


    answer_positions = [(270, 395),(530, 395),(270, 485),(530, 485)]
    for option, (x, y) in zip( question["options"], answer_positions):
        answer_button = Button( main_screen, text=str(option), font=(font, 16, "bold"), bg="#09051C", fg="White", command=lambda x=option: check_answer(x))
        answer_button.place( x=x, y=y, width=230, height=60, anchor="center")

    exit_button = Button( main_screen, text="EXIT GAME", command=main_menu, font=(font, 10, "bold"), bg="#09051C", fg="White")
    exit_button.place( x=400, y=555, width=150, height=40, anchor="center")

# Shows the questions for medium difficulty.
def show_question_medium(i):
    clear_screen(False)
    global timer_label, lives_label
    
    image_path = os.path.join( os.path.dirname(os.path.dirname(__file__)), "Images", "quiz_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label( main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place( x=0, y=0 )
    background_label.lower()

    time_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#00BFFF" )
    time_frame.place( x=200, y=70, width=250, height=70, anchor="center")
    Label( time_frame, text="TIME LEFT", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    timer_label = Label( time_frame, text=f"{game.time_left}s", font=(font, 20, "bold"), bg="#09051C",fg="#00BFFF" )
    timer_label.pack()

    lives_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#7B2CFF")
    lives_frame.place( x=400, y=70, width=150, height=70, anchor="center")
    Label( lives_frame, text="LIVES", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    lives_label = Label( lives_frame, text="♥ " * game.lives, font=(font, 20, "bold"), bg="#09051C", fg="#FF3131")
    lives_label.pack()

    score_frame = Frame( main_screen, bg="#09051C", highlightthickness=2,highlightbackground="#C42CFF")
    score_frame.place( x=550, y=70, width=150, height=70, anchor="center")
    Label( score_frame, text="SCORE", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    Label( score_frame, text=str(game.score), font=(font, 20, "bold"), bg="#09051C", fg="White").pack()
                                                                                              
    if i >= len(quiz_questions["Medium"]):
        stop_timer()
        save_score()
        Label( main_screen, text="QUIZ FINISHED!", font=(font, 24, "bold"), bg="#09051C", fg="White").place( x=400, y=250, anchor="center")
        Label( main_screen, text=f"Score: {game.score}/{len(quiz_questions['Medium'])}", font=(font, 18, "bold"),
        bg="#09051C",fg="#C42CFF").place( x=400, y=300, anchor="center")

        Button( main_screen, text="PLAY AGAIN", command=start_game_medium, font=(font, 11, "bold"), bg="#09051C",fg="White").place( x=400, y=370, width=180, height=45, anchor="center")
        Button( main_screen, text="CHOOSE DIFFICULTY", command=choose_difficulty_screen, font=(font, 11, "bold"), bg="#09051C", fg="White").place( x=400, y=425, width=180, height=45, anchor="center")
        return

    question = quiz_questions["Medium"][i]

    question_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#C42CFF")
    question_frame.place( x=400, y=255, width=560, height=95, anchor="center")
    Label( question_frame, text=question["question"], font=(font, 20, "bold"), bg="#09051C", fg="White", wraplength=520, justify="center").pack(expand=True)

# Checks if the answer given was correct, if not then takes a live. 
    def check_answer(selected):

        if selected == question["answer"]:
            game.score += 1
        else:
            game.lives -= 1
            if game.lives <= 0:
                game_over("You ran out of lives!")
                return
        show_question_medium(i + 1)


    answer_positions = [(270, 395),(530, 395),(270, 485),(530, 485)]
    for option, (x, y) in zip( question["options"], answer_positions):
        answer_button = Button( main_screen, text=str(option), font=(font, 16, "bold"), bg="#09051C", fg="White", command=lambda x=option: check_answer(x))
        answer_button.place( x=x, y=y, width=230, height=60, anchor="center")

    exit_button = Button( main_screen, text="EXIT GAME", command=main_menu, font=(font, 10, "bold"), bg="#09051C", fg="White")
    exit_button.place( x=400, y=555, width=150, height=40, anchor="center")


# Shows the questions for hard difficulty.
def show_question_hard(i):
    clear_screen(False)
    global timer_label, lives_label
    
    image_path = os.path.join( os.path.dirname(os.path.dirname(__file__)), "Images", "quiz_background.png")
    background_image = Image.open(image_path)
    background_image = background_image.resize((800, 600))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label( main_screen, image=background_photo)
    background_label.image = background_photo
    background_label.place( x=0, y=0 )
    background_label.lower()

    time_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#00BFFF" )
    time_frame.place( x=200, y=70, width=250, height=70, anchor="center")
    Label( time_frame, text="TIME LEFT", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    timer_label = Label( time_frame, text=f"{game.time_left}s", font=(font, 20, "bold"), bg="#09051C",fg="#00BFFF" )
    timer_label.pack()

    lives_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#7B2CFF")
    lives_frame.place( x=400, y=70, width=150, height=70, anchor="center")
    Label( lives_frame, text="LIVES", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    lives_label = Label( lives_frame, text="♥ " * game.lives, font=(font, 20, "bold"), bg="#09051C", fg="#FF3131")
    lives_label.pack()

    score_frame = Frame( main_screen, bg="#09051C", highlightthickness=2,highlightbackground="#C42CFF")
    score_frame.place( x=550, y=70, width=150, height=70, anchor="center")
    Label( score_frame, text="SCORE", font=(font, 10, "bold"), bg="#09051C", fg="White").pack(pady=(7, 0))
    Label( score_frame, text=str(game.score), font=(font, 20, "bold"), bg="#09051C", fg="White").pack()
                                                                                              
    if i >= len(quiz_questions["Hard"]):
        stop_timer()
        save_score()
        Label( main_screen, text="QUIZ FINISHED!", font=(font, 24, "bold"), bg="#09051C", fg="White").place( x=400, y=250, anchor="center")
        Label( main_screen, text=f"Score: {game.score}/{len(quiz_questions['Hard'])}", font=(font, 18, "bold"),
        bg="#09051C",fg="#C42CFF").place( x=400, y=300, anchor="center")

        Button( main_screen, text="PLAY AGAIN", command=start_game_hard, font=(font, 11, "bold"), bg="#09051C",fg="White").place( x=400, y=370, width=180, height=45, anchor="center")
        Button( main_screen, text="CHOOSE DIFFICULTY", command=choose_difficulty_screen, font=(font, 11, "bold"), bg="#09051C", fg="White").place( x=400, y=425, width=180, height=45, anchor="center")
        return

    question = quiz_questions["Hard"][i]

    question_frame = Frame( main_screen, bg="#09051C", highlightthickness=2, highlightbackground="#C42CFF")
    question_frame.place( x=400, y=255, width=560, height=95, anchor="center")
    Label( question_frame, text=question["question"], font=(font, 20, "bold"), bg="#09051C", fg="White", wraplength=520, justify="center").pack(expand=True)

# Checks if the answer given was correct, if not then takes a live. 
    def check_answer(selected):

        if selected == question["answer"]:
            game.score += 1
        else:
            game.lives -= 1
            if game.lives <= 0:
                game_over("You ran out of lives!")
                return
        show_question_hard(i + 1)


    answer_positions = [(270, 395),(530, 395),(270, 485),(530, 485)]
    for option, (x, y) in zip( question["options"], answer_positions):
        answer_button = Button( main_screen, text=str(option), font=(font, 16, "bold"), bg="#09051C", fg="White", command=lambda x=option: check_answer(x))
        answer_button.place( x=x, y=y, width=230, height=60, anchor="center")

    exit_button = Button( main_screen, text="EXIT GAME", command=main_menu, font=(font, 10, "bold"), bg="#09051C", fg="White")
    exit_button.place( x=400, y=555, width=150, height=40, anchor="center")

    
# Starts the Easy difficulty.
def start_game_easy():
    global current_difficulty
    current_difficulty = "Easy"
    game.reset()
    show_question_easy(0)
    update_timer()

# Starts the Medium difficulty.
def start_game_medium():
    global current_difficulty
    current_difficulty = "Medium"
    game.reset()
    show_question_medium(0)
    update_timer()

# Starts the Hard difficulty.
def start_game_hard():
    global current_difficulty
    current_difficulty = "Hard"
    game.reset()
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


