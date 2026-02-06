import tkinter as tk
from tkinter import font

def translate():
    input_word = entry_word.get().strip().lower()
    
    try:
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        found = False
        for line in lines:
            if ":" in line:
                word, meaning = line.strip().split(":", 1)
                if word.lower() == input_word:
                    label_result.config(text=f"{meaning}", fg="#2E8B57") # Sea Green
                    found = True
                    break
        
        if not found:
            label_result.config(text="Word not found!", fg="#CD5C5C") # Indian Red

    except FileNotFoundError:
        label_result.config(text="File 'dictionary.txt' missing!", fg="#CD5C5C")

# --- GUI Setup ---
root = tk.Tk()
root.title("My Dictionary")
root.geometry("350x250")
root.configure(bg="#F0F0F0") # Light gray background

# Define a custom font
custom_font = font.Font(family="Helvetica", size=12)
header_font = font.Font(family="Helvetica", size=14, weight="bold")

# Main Frame for better centering
frame = tk.Frame(root, bg="#F0F0F0")
frame.pack(expand=True)

# Title Label
tk.Label(frame, text="Simple Translator", font=header_font, bg="#F0F0F0", fg="#333").pack(pady=(0, 20))

# Input Label
tk.Label(frame, text="Enter a word:", font=custom_font, bg="#F0F0F0").pack()

# Entry Box with padding
entry_word = tk.Entry(frame, font=custom_font, width=20, justify="center")
entry_word.pack(pady=5, ipady=5) # ipady adds internal vertical padding

# Translate Button with styling
btn_translate = tk.Button(frame, text="Translate", command=translate, 
                          font=custom_font, bg="#4A90E2", fg="white", 
                          activebackground="#357ABD", relief="flat", padx=20)
btn_translate.pack(pady=15)

# Result Label
label_result = tk.Label(frame, text="", font=("Helvetica", 13, "italic"), 
                        bg="#F0F0F0", wraplength=300)
label_result.pack()

root.mainloop()