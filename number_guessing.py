import tkinter as tk
import random

# random number generate
number = random.randint(1, 100)
attempts = 0

# function jab button click hoga
def check_guess():
    global attempts
    guess = int(entry.get())
    attempts += 1

    if guess > number:
        result_label.config(text="📉 Thoda chhota socho")
    elif guess < number:
        result_label.config(text="📈 Thoda bada socho")
    else:
        result_label.config(text=f"🎉 Jeet gaye! Attempts: {attempts}")

# main window
root = tk.Tk()
root.title("Number Guessing Game 🎮")
root.geometry("300x200")

# heading
title_label = tk.Label(root, text="Guess Number (1-100)", font=("Arial", 14))
title_label.pack(pady=10)

# input box
entry = tk.Entry(root)
entry.pack(pady=5)

# button
check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(pady=5)

# result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# run app
root.mainloop()