from functools import partial
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("3 In A Row")

# Functions and Classes
class Game:
    win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def __init__(self, score, label, b_size_x=6, b_size_y=3, font_size=14):
        self.b_size_x = b_size_x
        self.b_size_y = b_size_y
        self.font_size = font_size

        self.turn = 0
        self.score_data = score
        self.score_label = label

        self.buttons = []
        self.pressed_buttons = []

    def change_score(self, winner):
        if winner == "X":
            self.score_data.x += 1
        elif winner == "O":
            self.score_data.o += 1

        self.score_label.config(text=self.score_data)


def reset(game, winner):
    game.change_score(winner)

    game.turn = 0
    game.pressed_buttons = []
    for button in game.buttons:
        button["text"] = ""


def all_equal(lst):
    return lst[0] in ["X", "O"] and len(set(lst)) == 1, lst[0]


def test_for_win(game):
    for combo in game.win_combos:
        full_row, winner = all_equal([game.buttons[i]["text"] for i in combo])
        if full_row:
            return full_row, winner
    return False, ""


def change_txt(game, i):
    if i not in game.pressed_buttons:
        game.buttons[i]["text"] = "X" if game.turn % 2 == 0 else "O"
        game.pressed_buttons.append(i)
        game.turn += 1

        full_row, winner = test_for_win(game)
        if full_row:
            reset(game, winner)


def try_i(game, i):
    game.buttons[i]["text"] = i


def create_buttons(game):
    for y in range(3):
        for x in range(3):
            b = Button(root,
                       font=("", game.font_size),
                       width=game.b_size_x,
                       height=game.b_size_y,
                       command=partial(change_txt, game, x + y * 3))
            b.grid(column=x + 1, row=y + 2)
            game.buttons.append(b)


# Label
class Score:
    x = 0
    o = 0

    def __str__(self):
        return f"X:{self.x}     O:{self.o}"


s = Label(text="X:0     O:0", padx=50, pady=20, font=("", 14))
s.grid(column=0, row=1)

g = Game(Score(), s)
create_buttons(g)

# Show screen
root.mainloop()

