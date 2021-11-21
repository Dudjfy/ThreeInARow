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
def all_equal(lst):
    return lst[0] in ["X", "O"] and len(set(lst)) == 1


def test_for_win(buttons, win_combos):
    for combo in win_combos:
        if all_equal([buttons[i]["text"] for i in combo]):
            return True
    return False


win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def change_txt(buttons, pressed_buttons, i):
    if i not in pressed_buttons:
        global turn
        buttons[i]["text"] = "X" if turn % 2 == 0 else "O"
        pressed_buttons.append(i)
        turn += 1
        print(test_for_win(buttons, win_combos))


def try_i(buttons, i):
    buttons[i]["text"] = i



buttons = []
pressed_buttons = []
for y in range(3):
    for x in range(3):
        b = Button(root,
              width=b_size_x,
              height=b_size_y,
              command=partial(change_txt, buttons, pressed_buttons, x + y * 3))
        buttons.append(b)
        b.grid(column=x + 1, row=y + 2)

# Show screen
root.mainloop()

