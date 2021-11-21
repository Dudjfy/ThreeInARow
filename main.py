from functools import partial
from tkinter import *

# Tkinter initialization
root = Tk()
root.geometry("600x400")
# Title
root.title("3 In A Row")


# Functions and Classes

# Score class to easier mange the scoring system
class Score:
    x = 0
    o = 0

    def __str__(self):
        return f"X: {self.x}     O: {self.o}"


# Game class with all objects to keep track of
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

    # Changes the score for the winner
    def change_score(self, winner):
        if winner == "X":
            self.score_data.x += 1
        elif winner == "O":
            self.score_data.o += 1

        self.score_label.config(text=self.score_data)

    # Resets score
    def reset_score(self):
        self.score_data.x = 0
        self.score_data.o = 0
        self.score_label.config(text=self.score_data)


# Resets the score, can also award points for the winner if specified
def reset(game, winner):
    game.change_score(winner)

    game.turn = 0
    game.pressed_buttons = []
    for button in game.buttons:
        button["text"] = ""


# Checks if all elements in a list are equal, used to determine if there is a winning row
def all_equal(lst):
    return lst[0] in ["X", "O"] and len(set(lst)) == 1, lst[0]


# Checks for win combinations
def check_for_win(game):
    for combo in game.win_combos:
        full_row, winner = all_equal([game.buttons[i]["text"] for i in combo])
        if full_row:
            return full_row, winner
    return False, ""


# Changes the button text
def change_txt(game, i):
    if i not in game.pressed_buttons:
        game.buttons[i]["text"] = "X" if game.turn % 2 == 0 else "O"
        game.pressed_buttons.append(i)
        game.turn += 1

        full_row, winner = check_for_win(game)
        if full_row:
            reset(game, winner)


# For testing the numbering of buttons
def try_i(game, i):
    game.buttons[i]["text"] = i


# Creates the playing field with buttons to put the Xs and Os
def create_buttons(game):
    for y in range(3):
        for x in range(3):
            b = Button(root,
                       font=("", game.font_size),
                       width=game.b_size_x,
                       height=game.b_size_y,
                       command=partial(change_txt, game, x + y * 3))
                       # command=partial(try_i, game, x + y * 3))  # For testing if the buttons are in correct positions
            b.grid(column=x + 1, row=y + 1)
            game.buttons.append(b)


# Labels, an example of using .grid()
sc = Label(text="X: 0     O: 0", padx=35, pady=20, font=("", 14))
sc.grid(column=0, row=0)

# Game object, game buttons
g = Game(Score(), sc)
create_buttons(g)

# Other buttons
reset_board_button = Button(root,
                            text="Reset Board",
                            font=("", g.font_size),
                            width=12,
                            height=1,
                            command=partial(reset, g, ""))
reset_board_button.grid(column=4, row=0, padx=30, pady=20)

reset_score_button = Button(root,
                            text="Reset Score",
                            font=("", g.font_size),
                            width=12,
                            height=1,
                            command=g.reset_score)
reset_score_button.grid(column=4, row=1, padx=30, pady=20)

# Exit button
exit_button = Button(root,
                     text="Exit",
                     font=("", g.font_size),
                     width=12,
                     height=1,
                     command=root.destroy)
exit_button.grid(column=4, row=5, padx=30, pady=20)

# Show screen
root.mainloop()

