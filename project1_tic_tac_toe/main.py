import tkinter as tk
from tkinter import messagebox

# ساخت پنجره اصلی
root = tk.Tk()
root.title("Tic Tac Toe")

# بازیکن فعلی
current_player = "X"

# وضعیت خانه‌ها (9 خانه خالی)
board = [""] * 9

# لیست دکمه‌ها
buttons = []


def check_winner():
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # سطرها
        (0,3,6), (1,4,7), (2,5,8),  # ستون‌ها
        (0,4,8), (2,4,6)            # قطرها
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index]["text"] = current_player

        winner = check_winner()

        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            # تغییر نوبت
            current_player = "O" if current_player == "X" else "X"


def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn["text"] = ""


# ساخت دکمه‌های صفحه بازی
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# دکمه ریست
reset_button = tk.Button(root, text="Restart", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()
