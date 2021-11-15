from functools import partial
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("3 In A Row")

b_size_x, b_size_y = 11, 5

# Label
score = Label(text="Score: ", padx=60, pady=20, font=("", 14))
score.grid(column=0, row=1)

turn = 0


# Functions
def change_txt(buttons, pressed_buttons, i):
    if i not in pressed_buttons:
        global turn
        buttons[i]["text"] = "X" if turn % 2 == 0 else "O"
        pressed_buttons.append(i)
        turn += 1


buttons = []
pressed_buttons = []
for x in range(3):
    for y in range(3):
        b = Button(root,
              width=b_size_x,
              height=b_size_y,
              command=partial(change_txt, buttons, pressed_buttons, x * 3 + y))
        buttons.append(b)
        b.grid(column=4 - x, row=4 - y)

# Show screen
root.mainloop()

