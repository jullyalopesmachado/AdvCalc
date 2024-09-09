from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("500x600")  # Set window size

# Create a Text widget for displaying input and results
e = Text(root, width=60, height=4, borderwidth=5)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)  # Position the Text widget

# Function to handle button clicks and update the Text widget
def button_click(number):
    current = e.get("1.0", END).strip()  # Get current text and remove trailing newline
    e.delete("1.0", END)  # Clear the text box
    e.insert("1.0", str(current) + str(number))  # Insert the new number

# Function to clear the Text widget
def button_clear():
    e.delete("1.0", END)  # Clear the text box

# Function to compute and display the result
def button_equal():
    second_number = e.get("1.0", END).strip()  # Get second number and remove trailing newline
    e.delete("1.0", END)  # Clear the text box

    # Perform the appropriate arithmetic operation 
    if math == "addition":
        e.insert("1.0", f_num + int(second_number))
    elif math == "subtraction":
        e.insert("1.0", f_num - int(second_number))
    elif math == "multiplication":
        e.insert("1.0", f_num * int(second_number))
    elif math == "division":
        e.insert("1.0", f_num / int(second_number))

# Function to handle addition operation
def button_add():
    first_number = e.get("1.0", END).strip()  # Get first number and remove trailing newline
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)  # Store the first number
    e.delete("1.0", END)  # Clear the text box

# Function to handle subtraction operation
def button_subtract():
    first_number = e.get("1.0", END).strip()  # Get first number and remove trailing newline
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)  # Store the first number
    e.delete("1.0", END)  # Clear the text box

# Function to handle multiplication operation
def button_multiply():
    first_number = e.get("1.0", END).strip()  # Get first number and remove trailing newline
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)  # Store the first number
    e.delete("1.0", END)  # Clear the text box

# Function to handle division operation
def button_divide():
    first_number = e.get("1.0", END).strip()  # Get first number and remove trailing newline
    global f_num
    global math
    math = "division"
    f_num = int(first_number)  # Store the first number
    e.delete("1.0", END)  # Clear the text box 
    
# Function to handle parentheses
def leftparent():
    current = e.get("1.0", END).strip()  # Get current text
    e.delete("1.0", END)  # Clear the text box
    e.insert("1.0", str(current) + "(")  # Insert left parenthesis

def rightparent():
    current = e.get("1.0", END).strip()  # Get current text
    e.delete("1.0", END)  # Clear the text box
    e.insert("1.0", str(current) + ")")  # Insert right parenthesis

# Function to handle percentage
def percent():
    current = e.get("1.0", END).strip()  # Get current text
    try:
        result = eval(current) / 100  # Calculate percentage
        e.delete("1.0", END)  # Clear the text box
        e.insert("1.0", str(result))  # Insert the result
    except:
        e.delete("1.0", END)  # Clear the text box if error
        e.insert("1.0", "Error")

# Function to calculate square root
def get_root():
    current = e.get("1.0", END).strip()  # Get current text
    try:
        result = math.sqrt(eval(current))  # Calculate square root
        e.delete("1.0", END)  # Clear the text box
        e.insert("1.0", str(result))  # Insert the result
    except:
        e.delete("1.0", END)  # Clear the text box if error
        e.insert("1.0", "Error")

# Function to calculate factorial
def get_expo():
    current = e.get("1.0", END).strip()  # Get current text
    try:
        result = math.factorial(eval(current))  # Calculate factorial
        e.delete("1.0", END)  # Clear the text box
        e.insert("1.0", str(result))  # Insert the result
    except:
        e.delete("1.0", END)  # Clear the text box if error
        e.insert("1.0", "Error")

# Function to compute and display the result with parentheses support
def button_equal():
    expression = e.get("1.0", END).strip()  # Get expression
    e.delete("1.0", END)  # Clear the text box
    try:
        result = eval(expression)  # Evaluate the expression
        e.insert("1.0", str(result))  # Insert the result
    except:
        e.insert("1.0", "Error")  # Insert "Error" if eval fails

# Function to handle addition (no need for number conversion)
def button_add():
    current = e.get("1.0", END).strip()
    e.delete("1.0", END)
    e.insert("1.0", current + "+")  # Just append the operator

# Similar functions for subtraction, multiplication, and division
def button_subtract():
    current = e.get("1.0", END).strip()
    e.delete("1.0", END)
    e.insert("1.0", current + "-")

def button_multiply():
    current = e.get("1.0", END).strip()
    e.delete("1.0", END)
    e.insert("1.0", current + "*")

def button_divide():
    current = e.get("1.0", END).strip()
    e.delete("1.0", END)
    e.insert("1.0", current + "/")
# Insert "Error" if eval fails


# Define buttons with appropriate text and commands
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

# Define non-number buttons with commands
button_add = Button(root, text="+", padx=20, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=20, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=20, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=20, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=20, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=20, pady=20, command=button_divide)

button_lefparent = Button(root, text="(" , padx=20, pady=20, command=leftparent )
button_rightparent = Button(root, text=")" , padx=20, pady=20, command=rightparent )

button_percent = Button (root,text = "%", padx=20, pady=20, command=percent)
button_root = Button (root, text="√", padx=20, pady=20, command=get_root)
button_expo = Button (root, text="!", padx=20, pady=20, command=get_expo)

# Configure grid columns and rows to ensure buttons are spaced correctly
for i in range(3):
    root.grid_columnconfigure(i, weight=1)  # Configure the first 3 columns to stretch evenly
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)  # Configure rows to stretch evenly

# Place buttons on the grid
button_1.grid(row=3, column=0, padx=1, pady=1, sticky="nsew")
button_2.grid(row=3, column=1, padx=1, pady=1, sticky="nsew")
button_3.grid(row=3, column=2, padx=1, pady=1, sticky="nsew")
button_4.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
button_5.grid(row=2, column=1, padx=1, pady=1, sticky="nsew")
button_6.grid(row=2, column=2, padx=1, pady=1, sticky="nsew")
button_7.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
button_8.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
button_9.grid(row=1, column=2, padx=1, pady=1, sticky="nsew")
button_0.grid(row=4, column=0, padx=1, pady=1, sticky="nsew")

button_clear.grid(row=1, column=3, padx=1, pady=1, sticky="nsew")
button_add.grid(row=4, column=3, padx=1, pady=1, sticky="nsew")
button_equal.grid(row=6, column=3, padx=1, pady=1, sticky="nsew")
button_subtract.grid(row=5, column=3, padx=1, pady=1, sticky="nsew")
button_multiply.grid(row=3, column=3, padx=1, pady=1, sticky="nsew")
button_divide.grid(row=2, column=3, padx=1, pady=1, sticky="nsew")

button_lefparent.grid(row=4, column=1,padx=1, pady=1, sticky="nsew")
button_rightparent.grid(row=4, column=2,padx=1, pady=1, sticky="nsew")

button_percent.grid(row= 5, column= 0,padx=1, pady=1, sticky="nsew")
button_root.grid(row= 5, column= 1,padx=1, pady=1, sticky="nsew")
button_expo.grid(row= 5, column= 2,padx=1, pady=1, sticky="nsew")

# Start the main loop to run the application
root.mainloop()
