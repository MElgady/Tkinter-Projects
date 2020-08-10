# Tutorial from RealPython on Tkinter
# Link: https://realpython.com/python-gui-tkinter/#building-a-text-editor-example-app

# Known as wildcard import which pylint
# doesn't like this and will show 100
# problems with it
# from tkinter import *

from tkinter import Tk, Text, Frame, Label, Button, RAISED, END
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """
    Open a file for editing
    """
    # Displays file open dialog box,
    # gives options of filetypes and
    # stores selected filepath in filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    # Checks if user has clicked cancel button
    # for dialog box
    if not filepath:
        return
    # Clears whatever is in the textbox
    else:
        text_edit.delete("1.0", END)

    # Opens and reads selected file and places
    # inside the text box
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
    # Changes title of window to add name of current file
    window.title(f"Simple Tkinter Text Editor - {filepath} ")


def save_file():
    """
    Save a currently opened file
    """
    # Opens save as dialog box to ask user to save current file
    # and stores that location in filepath
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # If user clicks cancel or closes dialog box, function returns nothing
    if not filepath:
        return
    # Opens output file
    with open(filepath, "w") as output_file:
        # Gets text from textbox and assigns to
        # variable text
        text = text_edit.get("1.0", END)
        # Writes text to output file
        output_file.write(text)
    # Updates window title to include name of current file
    window.title(f"Simple Tkinter Text Editor - {filepath}")


window = Tk()
window.title("Simple Tkinter Text Editor")

# Following keeps button columns to stay
# fixed whilst the text box can move freely

# Sets height of 1st row to 800 pixels
window.rowconfigure(0, minsize=800, weight=1)
# Sets height of 2nd row to 800 pixels
window.columnconfigure(1, minsize=800, weight=1)

# Creates area to edit text using Text widget
text_edit = Text(window)

frame_buttons = Frame(window)

frame_buttons = Frame(window, relief=RAISED, bd=2)
# Creates 2 buttons to open and save files
button_open = Button(frame_buttons, text="Open", command=open_file)
button_save = Button(frame_buttons, text="Save As", command=save_file)

# Places open and save buttons using grid format
# sticky="ew" allows buttons to expand in width
button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5)

# Allows frame to expand vertically i.e. buttons
# fill entire column
frame_buttons.grid(row=0, column=0, sticky="ns")
# Allows text box to move in every direction
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
