# Author: Saalik Batliwala.
# Date: 22/06/26
# Purpose: Flow Computing Math Game.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

score = 0

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

    global login_username, login_password

    title = Label(main_screen, text="Login", font = (font, 20))
    title.pack()

    username_label = Label(main_screen, text="Enter username", font = (font, 10))
    username_label.pack()
    login_username = Entry(main_screen)
    login_username.pack()

    password_label = Label(main_screen, text="Enter password", font = (font, 10))
    password_label.pack()
    login_password = Entry(main_screen, show="*")
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


def personal_leaderboard():
    clear_screen()

    Label(
        main_screen,
        text="Personal Leaderboard",
        font=(font,20)
    ).pack(pady=20)

    Label(
        main_screen,
        text="No scores recorded yet",
        font=(font,12)
    ).pack()

    Button(
        main_screen,
        text="Back",
        command=choose_difficulty_screen
    ).pack(pady=20)

def choose_difficulty_screen():
    clear_screen()
    title = Label(main_screen, text="Choose Difficulty", font=(font, 20))
    title.pack(pady=20)

    easy_button = Button(main_screen, text="Easy", font=(font, 14), width=15, command=start_game_easy)
    easy_button.pack(pady=10)

    typed_easy_button = Button(
    main_screen,
    text="Easy - Typed Answers",
    font=(font, 14),
    width=20,
    command=start_game_easy_typed
    )
    typed_easy_button.pack(pady=10)

    radio_button = Button(
        main_screen,
        text="Radio Button Trial",
        font=(font, 14),
        width=18,
        command=radio_answer
    )
    radio_button.pack(pady=10)

    dropdown_button = Button(
        main_screen,
        text="Dropdown Trial",
        font=(font, 14),
        width=18,
        command=dropdown_answer
    )
    dropdown_button.pack(pady=10)
    medium_button = Button(main_screen, text="Medium", font=(font, 14), width=15, command=start_game_medium)
    medium_button.pack(pady=10)

    hard_button = Button(main_screen, text="Hard", font=(font, 14), width=15, command=start_game_hard)
    hard_button.pack(pady=10)

    personal_leaderboard_button = Button(main_screen, text="Personal Leaderboard", font=(font, 14), width=18, command=personal_leaderboard)
    personal_leaderboard_button.pack(pady=10)

    back_button = Button(main_screen, text="Back to Main Menu", command=main_menu)
    back_button.pack(pady=20)

# Countdown timer
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

    Label(
        main_screen,
        text="YOU LOSE!",
        font=(font,25,"bold"),
        fg="red"
    ).pack(pady=20)

    Label(
        main_screen,
        text=reason,
        font=(font,15)
    ).pack()

    Button(
        main_screen,
        text="Main Menu",
        command=main_menu
    ).pack(pady=10)

    Button(
        main_screen,
        text="Exit Game",
        command=close_program
    ).pack(pady=10)


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
    update_timer()

# Check if quiz is finished
    if i >= len(quiz_questions["Easy"]):
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

# Show the next question
        show_question_easy(i + 1)
    for option in question["options"]:
            Button(main_screen, text=str(option), width=15, command=lambda x=option: check_answer(x)).pack(pady=5)

    Button(
        main_screen,
        text="Exit Game",
        command=main_menu
        ).pack(pady=15)

def show_question_easy_typed(i):
    clear_screen()

    global timer_label, lives_label, score

    timer_label = Label(main_screen, font=(font, 12))
    timer_label.pack()

    lives_label = Label(main_screen, font=(font, 12))
    lives_label.pack()

    lives_label.config(text=f"Lives: {lives}")

    # Check if all questions have been completed
    if i >= len(quiz_questions["Easy"]):
        Label(
            main_screen,
            text=f"Quiz Finished!\nScore: {score}/{len(quiz_questions['Easy'])}",
            font=(font, 18)
        ).pack(pady=20)

        Button(
            main_screen,
            text="Main Menu",
            command=main_menu
        ).pack(pady=10)

        return

    question = quiz_questions["Easy"][i]

    # Display the question
    Label(
        main_screen,
        text=question["question"],
        font=(font, 16),
        wraplength=700,
        justify="center"
    ).pack(pady=20)

    # Input box for the user to type their answer
    answer_entry = Entry(
        main_screen,
        font=(font, 16),
        width=20
    )
    answer_entry.pack(pady=10)

    def check_typed_answer():
        global score, lives

        user_input = answer_entry.get().strip()

        # Check that the user has actually entered something
        if user_input == "":
            messagebox.showerror(
                "Invalid Answer",
                "Please enter an answer."
            )
            return

        # Check whether the input is a valid number
        try:
            user_answer = int(user_input)
        except ValueError:
            messagebox.showerror(
                "Invalid Answer",
                "Please enter a valid number."
            )
            return

        # Check whether the answer is correct
        if user_answer == question["answer"]:
            score += 1
            messagebox.showinfo(
                "Correct!",
                "That answer is correct."
            )
        else:
            lives -= 1
            messagebox.showerror(
                "Incorrect",
                f"Incorrect. The correct answer was {question['answer']}."
            )

            if lives <= 0:
                game_over("You ran out of lives!")
                return

        # Move to the next question
        show_question_easy_typed(i + 1)

    Button(
        main_screen,
        text="Submit Answer",
        font=(font, 12),
        width=15,
        command=check_typed_answer
    ).pack(pady=10)

    Button(
        main_screen,
        text="Exit Game",
        command=main_menu
    ).pack(pady=15)

# Radio button answer input trial
def radio_answer():
    clear_screen()

    lives_label = Label(
        main_screen,
        text="Lives: 3",
        font=(font, 12)
    )
    lives_label.pack(pady=5)

    question_label = Label(
        main_screen,
        text="What is 12x12?",
        font=(font, 16)
    )
    question_label.pack(pady=10)

    # Stores which radio button the user has selected
    selected_answer = StringVar()
    selected_answer.set("")

    option1 = Radiobutton(
        main_screen,
        text="121",
        variable=selected_answer,
        value="121",
        font=(font, 12)
    )
    option1.pack(pady=2)

    option2 = Radiobutton(
        main_screen,
        text="132",
        variable=selected_answer,
        value="132",
        font=(font, 12)
    )
    option2.pack(pady=2)

    option3 = Radiobutton(
        main_screen,
        text="134",
        variable=selected_answer,
        value="134",
        font=(font, 12)
    )
    option3.pack(pady=2)

    option4 = Radiobutton(
        main_screen,
        text="144",
        variable=selected_answer,
        value="144",
        font=(font, 12)
    )
    option4.pack(pady=2)

    def submit_radio_answer():
        answer = selected_answer.get()

        # Check that the user has selected an option
        if answer == "":
            messagebox.showwarning(
                "No Answer",
                "Please select an answer."
            )

        # Check if the selected answer is correct
        elif answer == "144":
            messagebox.showinfo(
                "Correct",
                "Correct!"
            )

        # Handle an incorrect answer
        else:
            messagebox.showerror(
                "Incorrect",
                "Incorrect. The correct value was 144."
            )

    submit_button = Button(
        main_screen,
        text="Submit Answer",
        command=submit_radio_answer,
        font=(font, 11)
    )
    submit_button.pack(pady=15)

    exit_button = Button(
        main_screen,
        text="Exit Game",
        command=main_menu,
        font=(font, 9)
    )
    exit_button.pack(pady=5)

# Dropdown box answer input trial
def dropdown_answer():
    clear_screen()

    lives_label = Label(
        main_screen,
        text="Lives: 3",
        font=(font, 12)
    )
    lives_label.pack(pady=5)

    question_label = Label(
        main_screen,
        text="What is 12x12?",
        font=(font, 16)
    )
    question_label.pack(pady=10)

    # Stores the answer selected from the dropdown
    selected_answer = StringVar()
    selected_answer.set("Select an answer")

    answer_dropdown = OptionMenu(
        main_screen,
        selected_answer,
        "121",
        "132",
        "134",
        "144"
    )
    answer_dropdown.config(
        font=(font, 12),
        width=15
    )
    answer_dropdown.pack(pady=10)

    def submit_dropdown_answer():
        answer = selected_answer.get()

        # Check that an answer has been selected
        if answer == "Select an answer":
            messagebox.showwarning(
                "No Answer",
                "Please select an answer."
            )

        # Check if the selected answer is correct
        elif answer == "144":
            messagebox.showinfo(
                "Correct",
                "Correct!"
            )

        # Handle an incorrect answer
        else:
            messagebox.showerror(
                "Incorrect",
                "Incorrect. The correct answer was 144."
            )

    submit_button = Button(
        main_screen,
        text="Submit Answer",
        command=submit_dropdown_answer,
        font=(font, 11)
    )
    submit_button.pack(pady=15)

    exit_button = Button(
        main_screen,
        text="Exit Game",
        command=main_menu,
        font=(font, 9)
    )
    exit_button.pack(pady=5)



def show_question_medium(i):
    clear_screen()
    global timer_label, lives_label

    timer_label = Label(main_screen, font=(font,12))
    timer_label.pack()

    lives_label = Label(main_screen, font=(font,12))
    lives_label.pack()
    lives_label.config(text=f"Lives: {lives}")
    update_timer()

# Check if quiz is finished.
    if i >= len(quiz_questions["Medium"]):
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

# Show the next question
        show_question_medium(i + 1)
    for option in question["options"]:
        Button(
            main_screen,
            text=str(option),
            width=15,
            command=lambda x=option: check_answer(x)
        ).pack(pady=5)


def show_question_hard(i):
    clear_screen()
    global timer_label, lives_label
    timer_label = Label(main_screen, font=(font,12))
    timer_label.pack()
    lives_label = Label(main_screen, font=(font,12))
    lives_label.pack()
    lives_label.config(text=f"Lives: {lives}")
    update_timer()

# Check if quiz is finished
    if i >= len(quiz_questions["Hard"]):
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

# Show the next question
        show_question_hard(i + 1)
    for option in question["options"]:
        Button(
            main_screen,
            text=str(option),
            width=15,
            command=lambda x=option: check_answer(x)
        ).pack(pady=5)



def start_game_easy():
    global score
    score = 0
    global lives, time_left
    lives = 3
    time_left = 60
    timer_label = None
    lives_label = None
    show_question_easy(0)

def start_game_easy_typed():
    global score
    score = 0

    global lives, time_left
    lives = 3
    time_left = 60

    show_question_easy_typed(0)

def start_game_medium():
    global score
    score = 0
    global lives, time_left
    lives = 3
    time_left = 60
    timer_label = None
    lives_label = None
    show_question_medium(0)


def start_game_hard():
    global score
    score = 0
    global lives, time_left
    lives = 3
    time_left = 60
    timer_label = None
    lives_label = None
    show_question_hard(0)

        
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


