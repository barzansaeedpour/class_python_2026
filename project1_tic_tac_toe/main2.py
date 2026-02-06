import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x400")
root.configure(bg="#2C3E50") # Dark blue background

# Global variables
current_player = "X"
board = ["" for _ in range(9)] # List to store 9 empty spots
game_active = True

def check_winner():
    """Checks all winning combinations."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    
    if "" not in board:
        return "Draw"
    
    return None

def on_click(index):
    """Handles button click."""
    global current_player, game_active

    # If cell is empty and game is running
    if board[index] == "" and game_active:
        # Update board and button text
        board[index] = current_player
        buttons[index].config(text=current_player, fg="#ECF0F1")
        
        # Check for winner
        winner = check_winner()
        
        if winner:
            if winner == "Draw":
                label_status.config(text="It's a Draw!", fg="#F1C40F")
            else:
                label_status.config(text=f"Player {winner} Wins!", fg="#2ECC71")
                game_active = False
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"
            label_status.config(text=f"Player {current_player}'s Turn", fg="#ECF0F1")

def reset_game():
    """Resets the game board."""
    global board, current_player, game_active
    board = ["" for _ in range(9)]
    current_player = "X"
    game_active = True
    
    for btn in buttons:
        btn.config(text="")
    
    label_status.config(text=f"Player {current_player}'s Turn", fg="#ECF0F1")

# --- GUI Setup ---

# Status Label
label_status = tk.Label(root, text=f"Player {current_player}'s Turn", 
                        font=("Helvetica", 14, "bold"), bg="#2C3E50", fg="#ECF0F1")
label_status.pack(pady=20)

# Frame for the 3x3 Grid
frame_grid = tk.Frame(root, bg="#2C3E50")
frame_grid.pack()

buttons = []

# Create 3x3 buttons
for i in range(9):
    btn = tk.Button(frame_grid, text="", font=("Helvetica", 20, "bold"), width=5, height=2,
                    bg="#34495E", activebackground="#95A5A6",
                    command=lambda idx=i: on_click(idx))
    # Grid layout: row is i//3, column is i%3
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Reset Button
btn_reset = tk.Button(root, text="Restart Game", command=reset_game, 
                      font=("Arial", 10), bg="#E74C3C", fg="white", activebackground="#C0392B")
btn_reset.pack(pady=20)

root.mainloop()