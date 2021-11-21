from functools import partial
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("3 In A Row")

# Label
score = Label(text="Score: ", padx=60, pady=20, font=("", 14))
score.grid(column=0, row=1)

turn = 0


# Functions

class Game:
    win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def __init__(self, b_size_x=6, b_size_y=3, font_size=14):
        self.b_size_x = b_size_x
        self.b_size_y = b_size_y
        self.font_size = font_size

        self.turn = 0

        self.buttons = []
        self.pressed_buttons = []


def reset(game):
    game.turn = 0
    game.pressed_buttons = []
    for button in game.buttons:
        button["text"] = ""


def all_equal(lst):
    return lst[0] in ["X", "O"] and len(set(lst)) == 1


def test_for_win(game):
    for combo in game.win_combos:
        if all_equal([game.buttons[i]["text"] for i in combo]):
            return True
    return False


def change_txt(game, i):
    if i not in game.pressed_buttons:
        game.buttons[i]["text"] = "X" if game.turn % 2 == 0 else "O"
        game.pressed_buttons.append(i)
        game.turn += 1

        win = test_for_win(game)
        print(win)
        if win:
            reset(game)


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


game = Game()
create_buttons(game)

# Show screen
root.mainloop()

