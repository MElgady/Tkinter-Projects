# Tutorial from RealPython on Tkinter
# Link: https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app

# Imports everything from tkinter library
# Known as wildcard import which pylint
# doesn't like this and will show 100
# problems with it
# from tkinter import *

from tkinter import Tk, Frame, Label, Entry, Button

# TODO: Find a way to avoid repeating Tkinter widgets for each
# entry field


def fahrenheit_to_celsius():
    """
    Convert the value for Fahrenheit into Celsius
    and insert result into label_result.
    """
    fahrenheit = entry_temp.get()
    # If entry field is empty, convert temp
    if fahrenheit != "":
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        # Rounds celsius to 2 decimal places and converts
        # to text
        label_result["text"] = f"{round(celsius,2)} \N{DEGREE CELSIUS}"
    # Do nothing if entry field is empty
    else:
        pass


def celsius_to_fahrenheit():
    """
    Convert Celsius to Fahrenheit and insert
    into label_result2 widget.
    """
    celsius = entry_temp2.get()
    # If entry field is empty, convert temp
    if celsius != "":
        fahrenheit = (float(celsius) * (9/5) + 32)
        # Rounds fahrenheit to 2 decimal places and
        # converts to text
        label_result2["text"] = f"{round(fahrenheit,2)} \N{DEGREE FAHRENHEIT}"
    # Do nothing if entry field is empty
    else:
        pass


def fahrenheit_to_kelvin():
    """
    Convert Fahrenheit to Kelvin and insert
    into label_result3 widget.
    """

    fahrenheit = entry_temp3.get()

    if fahrenheit != "":
        celsius = (5 / 9) * (float(fahrenheit) - 32) + 273.15

        label_result3["text"] = f"{round(celsius, 2)} \N{DEGREE SIGN}K"
    else:
        pass


# Set up the window
window = Tk()
window.title("Temperature Converter")
# Can't resize window
window.resizable(width=True, height=False)

# Creates place to enter temp,
# label for entry and sets
# them to appear in window
form_entry = Frame(master=window)
entry_temp = Entry(master=form_entry, width=10)
label_temp = Label(master=form_entry, text="\N{DEGREE FAHRENHEIT}")

# Sets location of entry field and its
# label using grid method
entry_temp.grid(row=0, column=0, sticky="e")
# sticky="e" sets entry to be at right edge of cell
# sticky="w" sets label to be at left edge of cell
label_temp.grid(row=0, column=1, sticky="w")

# Creates button that shows up in main window of app,
# adds a black arrow -> and the function when
# button is pressed
btn_convert = Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius)

# Creates degrees celsius symbol next to converted number
label_result = Label(master=window, text="\N{DEGREE CELSIUS}")

# Sets location of button, entry field
# and label for degrees celsius
form_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
label_result.grid(row=0, column=3, padx=10)

# USED FOR CELSIUS TO FAHRENHEIT CONVERSION
# Creates place for celsius field and
# celsius label
form_entry2 = Frame(master=window)
entry_temp2 = Entry(master=form_entry2, width=10)
label_temp2 = Label(master=form_entry2, text="\N{DEGREE CELSIUS}")

# Sets location of 2nd entry field and celsius label
entry_temp2.grid(row=1, column=0, sticky="e")
label_temp2.grid(row=1, column=1, sticky="w")

# Button for the celsius to fahrenheit conversion
btn_convert2 = Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit)

# Sets location for the secondary entry field, button field
# and the converted temp value
label_result2 = Label(master=window, text="\N{DEGREE FAHRENHEIT}")
form_entry2.grid(row=1, column=0, padx=10)
btn_convert2.grid(row=1, column=1, pady=10)
label_result2.grid(row=1, column=3, padx=10)

# Creates place for celsius field and
# celsius label
form_entry3 = Frame(master=window)
entry_temp3 = Entry(master=form_entry3, width=10)
label_temp3 = Label(master=form_entry3, text="\N{DEGREE FAHRENHEIT}")

# Sets location of 2nd entry field and celsius label
entry_temp3.grid(row=2, column=0, sticky="e")
label_temp3.grid(row=2, column=1, sticky="w")

# Button for the celsius to fahrenheit conversion
btn_convert3 = Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_kelvin)

# Sets location for the secondary entry field, button field
# and the converted temp value
label_result3 = Label(master=window, text=u"\N{DEGREE SIGN}K")
form_entry3.grid(row=2, column=0, padx=10)
btn_convert3.grid(row=2, column=1, pady=10)
label_result3.grid(row=2, column=3, padx=10)

window.mainloop()
