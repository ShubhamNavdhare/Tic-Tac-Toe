import tkinter as tk
import random

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x420")
root.config(bg="#1e1e2f")

board = [""] * 9
buttons = []


def check_winner_state(state, player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in win_combos:
        if all(state[i] == player for i in combo):
            return True
    return False


def check_winner(player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw():
    return "" not in board


def ai_move():
    # 1. Try to WIN
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            if check_winner_state(board, "O"):
                buttons[i].config(text="O", state="disabled", fg="red")
                return
            board[i] = ""

    # 2. Try to BLOCK player
    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            if check_winner_state(board, "X"):
                board[i] = "O"
                buttons[i].config(text="O", state="disabled", fg="red")
                return
            board[i] = ""

    # 3. Random move
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = "O"
        buttons[move].config(text="O", state="disabled", fg="red")


def click(index):
    if board[index] == "":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled", fg="green")

        if check_winner("X"):
            status.config(text="You Win 🎉", fg="green")
            disable_all()
            return
        elif is_draw():
            status.config(text="It's a Draw 🤝", fg="orange")
            return

        ai_move()

        if check_winner("O"):
            status.config(text="Computer Wins 😢", fg="red")
            disable_all()
        elif is_draw():
            status.config(text="It's a Draw 🤝", fg="orange")


def disable_all():
    for btn in buttons:
        btn.config(state="disabled")


def restart():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")
    status.config(text="Your Turn (X)", fg="white")


title = tk.Label(root, text="Tic Tac Toe", font=(
    "Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

for i in range(9):
    btn = tk.Button(
        frame, text="", font=("Arial", 18),
        width=5, height=2,
        command=lambda i=i: click(i)
    )
    btn.grid(row=i//3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

status = tk.Label(root, text="Your Turn (X)", font=(
    "Arial", 12), bg="#1e1e2f", fg="white")
status.pack(pady=10)

restart_btn = tk.Button(root, text="Restart Game", command=restart)
restart_btn.pack(pady=10)

root.mainloop()
