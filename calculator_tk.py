# A simple calculator to do basic operators.
# GUI made with TkInter

# import tkinter module
import tkinter as tk
import tkinter.font as font

# creating main tkinter window/toplevel
master = tk.Tk()
master.title("Calculator")

# Define font
cal_font = font.Font(size=18)

# entry widget to get user input
user_input = tk.Entry(master)
user_input.grid(row=5, column=0, pady=5, padx=10, ipadx=80, ipady=6, columnspan=4)
user_input["font"] = cal_font


# Function to connect buttons and set user input
def set_text_input(text):
    user_input.insert(tk.END, text)


# Function to clear user input
def clear_text_input():
    user_input.delete(0, tk.END)


# Function to get answer using eval
def get_answer():
    answer = eval(user_input.get())
    user_input.delete(0, tk.END)
    user_input.insert(0, answer)


# List of tuples (button_symbol, x, y)
symbols = [("(", 0, 0), (")", 0, 1), ("%", 0, 2), ("AC", 0, 3),
           ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
           ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
           ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
           ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)]

# Function to create buttons and calculator
# Grid method to arrange buttons in respective rows and columns


def create_calculator(symbol, x, y):
    if symbol != "AC" and symbol != "=":
        button = tk.Button(master, bg="snow2", height=1, width=6,
                           text=symbol, command=lambda: set_text_input(symbol))
        button["font"] = cal_font
        button.grid(row=x, column=y, pady=10)
    elif symbol == "AC":
        button = tk.Button(master, bg="SteelBlue1", height=1, width=6,
                           text=symbol, command=lambda: clear_text_input())
        button["font"] = cal_font
        button.grid(row=x, column=y)
    else:
        button = tk.Button(master, bg="SteelBlue1", height=1, width=6,
                           text=symbol, command=lambda: get_answer())
        button["font"] = cal_font
        button.grid(row=x, column=y)


for sign, x_grid, y_grid in symbols:
    create_calculator(sign, x_grid, y_grid)

# quit button to quit program
quit_button = tk.Button(master, text="QUIT", bg="red", fg="white", command=master.destroy)
quit_button["font"] = cal_font
quit_button.grid(row=6, column=0, ipadx=20, pady=10, columnspan=4)

# infinite loop. Can be terminated by keyboard or mouse interrupt
if __name__ == "__main__":
    tk.mainloop()
