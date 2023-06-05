import time
import random
import tkinter as tk

PHRASES = [
    "The quick brown fox jumps over the lazy dog",
    "Hello, World!",
    "Programming is fun",
    "Keep calm and code on",
    "Python is awesome"
]

def calculate_typing_speed(start_time, end_time, text):
    # Calculates typing speed in words per minute
    time_elapsed = end_time - start_time
    num_words = len(text.split())
    speed = num_words / (time_elapsed / 60)
    return speed

def check_accuracy(text, user_text):
    # Compare the characters up to the length of the shorter text
    min_length = min(len(text), len(user_text))
    matches = sum(1 for i in range(min_length) if text[i] == user_text[i])
    accuracy = matches / len(text)
    return accuracy

def start_typing():
    # Disable the start button
    start_button.config(state=tk.DISABLED)
    type_again_button.config(state=tk.DISABLED)
    text_entry.delete("1.0", tk.END)

    # Update the countdown visually
    countdown_label.config(text="Get ready! Starting in 5 seconds...")
    countdown_label.update()
    time.sleep(1)
    countdown_label.config(text="Get ready! Starting in 4 seconds...")
    countdown_label.update()
    time.sleep(1)
    countdown_label.config(text="Get ready! Starting in 3 seconds...")
    countdown_label.update()
    time.sleep(1)
    countdown_label.config(text="Get ready! Starting in 2 seconds...")
    countdown_label.update()
    time.sleep(1)
    countdown_label.config(text="Get ready! Starting in 1 second...")
    countdown_label.update()
    time.sleep(1)
    countdown_label.config(text="Start typing!")

    # Enable the text entry field for typing
    text_entry.config(state=tk.NORMAL)
    text_entry.delete("1.0", tk.END)
    text_entry.focus_set()

    # Start the timer
    global start_time
    start_time = time.time()

def stop_typing():
    # Stop the typing process
    end_time = time.time()
    speed = calculate_typing_speed(start_time, end_time, text_prompt.get("1.0", tk.END))
    accuracy = check_accuracy(text_prompt.get("1.0", tk.END), text_entry.get("1.0", tk.END))
    result_label.config(text="Typing Speed: {:.2f} words per minute\nAccuracy: {:.2f}%".format(speed, accuracy * 100))

    # Disable the text entry field
    text_entry.config(state=tk.DISABLED)

    # Enable the "Type Again" button
    type_again_button.config(state=tk.NORMAL)

def type_again():
    # Clear the typing text box
    text_entry.delete("1.0", tk.END)

    # Clear the result label
    result_label.config(text="")

    # Enable the start button
    start_button.config(state=tk.NORMAL)

    # Disable the "Type Again" button
    type_again_button.config(state=tk.DISABLED)

    # Select a new random phrase and display it in the text prompt
    phrase = random.choice(PHRASES)
    text_prompt.delete("1.0", tk.END)
    text_prompt.insert(tk.END, phrase)

# Create the main window
window = tk.Tk()
window.title("Typing App")

# Create and position the text prompt
text_prompt = tk.Text(window, height=5, width=50)
text_prompt.pack()

# Select a random phrase and display it in the text prompt
phrase = random.choice(PHRASES)
text_prompt.insert(tk.END, phrase)

# Create and position the text entry field
text_entry = tk.Text(window, height=5, width=50)
text_entry.config(state=tk.DISABLED)
text_entry.pack()

# Create and position the start button
start_button = tk.Button(window, text="Start Typing", command=start_typing)
start_button.pack()

# Create and position the countdown label
countdown_label = tk.Label(window, text="")
countdown_label.pack()

# Create and position the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Create and position the "Type Again" button
type_again_button = tk.Button(window, text="Type Again", command=type_again)
type_again_button.config(state=tk.DISABLED)
type_again_button.pack()

# Stop typing when the Enter key is pressed
window.bind("<Return>", lambda event: stop_typing())

# Start the Tkinter event loop
window.mainloop()

