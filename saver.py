import tkinter as tk
import threading
import pyautogui
import time
import pygetwindow as gw
from tkinter import messagebox  # Import the messagebox module

# List of keywords commonly found in the titles of editor software
editor_keywords = ["Notepad", "Sublime Text", "Visual Studio Code", "Atom", "TextEdit", "VSCode", "Vim", "Emacs", "Word", "Excel", "PowerPoint", "Publisher", "Access", "Adobe Photoshop", "Adobe Illustrator", "Adobe Indesign"]

def is_editor_window(window_title):
    for keyword in editor_keywords:
        if keyword in window_title:
            return True
    return False

def save_editor_windows():
    while True:
        windows = gw.getAllTitles()
        for window_title in windows:
            if is_editor_window(window_title):
                # Switch to the editor window
                gw.getWindowsWithTitle(window_title)[0].activate()

                # Simulate pressing CTRL+S
                pyautogui.hotkey('ctrl', 's')

        # Sleep for 5 minutes (300 seconds)
        time.sleep(300)

def start_script():
    global exit_flag
    exit_flag = threading.Event()
    script_thread = threading.Thread(target=save_editor_windows)
    script_thread.start()
    # Your start script code here
    messagebox.showinfo("Confirmation", "DeoSaver has started successfully!")

def stop_script():
    global exit_flag
    exit_flag.set()
    # Your stop script code here
    messagebox.showinfo("Confirmation", "DeoSaver stopped successfully!")

# Create the main window
root = tk.Tk()
root.title("DeoSaver")

# Set the size of the main window using width and height attributes
#root.width = 900  # Width in pixels
#root.height = 600  # Height in pixels
root.geometry("240x120")

# Create Start button
space = tk.Label(root, text="", pady=1)# Add some space between the buttons
space.pack()
start_button = tk.Button(root, text="Start", command=start_script, bg="green", fg="white", padx=20)
start_button.pack()

# Create Stop button
space = tk.Label(root, text="", pady=1)# Add some space between the buttons
space.pack()
stop_button = tk.Button(root, text="Stop", command=stop_script, bg="red", fg="white", padx=20)
stop_button.pack()

# Run the GUI main loop
root.mainloop()
