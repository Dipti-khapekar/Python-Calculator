
import tkinter as tk

root = tk.Tk()
root.title("Python Calculator")
root.geometry("450x650")
root.resizable(False, False)
root.configure(bg="#171717")
root.configure(bg="#171717")

expression = ""
first_number = None
current_operator = None
new_number = True

display_text = tk.StringVar(value="0")


def update_display(value):
    display_text.set(value)


def number_click(number):
    global expression, new_number

    if new_number:
        expression = number
        new_number = False
    else:
        if number == "." and "." in expression:
            return
        expression += number

    update_display(expression)


def clear():
    global expression, first_number, current_operator, new_number

    expression = ""
    first_number = None
    current_operator = None
    new_number = True

    update_display("0")


def delete():
    global expression, new_number

    if new_number:
        return

    expression = expression[:-1]

    if not expression:
        expression = "0"
        new_number = True

    update_display(expression)


def operation_click(operator):
    global first_number, current_operator, new_number

    try:
        if not new_number:
            first_number = float(expression)
        elif first_number is None:
            return
    except ValueError:
        return

    current_operator = operator
    new_number = True


def calculate():
    global expression, first_number, current_operator, new_number

    if first_number is None or current_operator is None or new_number:
        return

    try:
        second_number = float(expression)

        if current_operator == "+":
            result = first_number + second_number
        elif current_operator == "-":
            result = first_number - second_number
        elif current_operator == "×":
            result = first_number * second_number
        elif current_operator == "÷":
            if second_number == 0:
                update_display("Cannot divide by 0")
                expression = ""
                first_number = None
                current_operator = None
                new_number = True
                return
            result = first_number / second_number

        if result == int(result):
            result = int(result)

        expression = str(result)
        update_display(expression)

        first_number = None
        current_operator = None
        new_number = True

    except (ValueError, OverflowError):
        update_display("Error")
        clear()


display = tk.Label(
    root,
    textvariable=display_text,
    font=("Arial", 36, "bold"),
    bg="#242424",
    fg="white",
    anchor="e",
    padx=20,
    pady=35
)
display.pack(fill="both", padx=15, pady=20)


buttons = [
    ["C", "⌫", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", "."]
]

button_frame = tk.Frame(root, bg="#171717")
button_frame.pack(expand=True, fill="both", padx=12, pady=5)


for row_index, row in enumerate(buttons):

    for col_index, button_text in enumerate(row):

        if button_text == "C":
            command = clear
            bg_color = "#555555"

        elif button_text == "⌫":
            command = delete
            bg_color = "#555555"

        elif button_text in ["+", "-", "×", "÷"]:
            command = lambda op=button_text: operation_click(op)
            bg_color = "#F39C12"

        elif button_text == "=":
            command = calculate
            bg_color = "#F39C12"

        else:
            command = lambda num=button_text: number_click(num)
            bg_color = "#303030"

        button = tk.Button(
            button_frame,
            text=button_text,
            font=("Arial", 22 , "bold"),
            bg=bg_color,
            fg="white",
            activebackground="#777777",
            activeforeground="white",
            relief="flat",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=5,
            pady=5
        )


for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Start application
root.mainloop()
