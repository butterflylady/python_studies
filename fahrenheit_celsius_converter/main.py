# Converts degrees Fahrenheit to degrees Celsius

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


def fahrenheit_to_celsius_convert(f):
    """
    Converts degrees Fahrenheit to degrees Celsius
    """
    return (f - 32) * 5 / 9


window = tk.Tk()
window.title('Fahrenheit to Celsius Converter')
window.geometry('400x90+700+350')
window.resizable(False, False)

# frame
frame = ttk.Frame(window)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# field options
options = {'padx': 7, 'pady': 7}

# temperature label
temperature_label = ttk.Label(frame, text='degrees Fahrenheit:')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)


# convert button
def convert_button_click():
    """
    Handle convert button click event
    """
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius_convert(f)
        result = f'{f:.1f} degrees Fahrenheit = {c:.1f} degrees Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_click)

# start the app
window.mainloop()
