import tkinter as tk

def translate():
    # Get the word typed by the user and convert to lowercase
    input_word = entry_word.get().strip().lower()
    try:
        # Open the file and read lines
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        found = False
        for line in lines:
            # Split the line at the colon ':'
            if ":" in line:
                word, meaning = line.strip().split(":", 1)
                
                # Check if the typed word matches the word in the file
                if word.lower() == input_word:
                    label_result.config(text=f"Translation: {meaning}", fg="green")
                    found = True
                    break
        if not found:
            label_result.config(text="Translation not found!", fg="red")
    except FileNotFoundError:
        label_result.config(text="Error: 'dictionary.txt' not found.", fg="red")

root = tk.Tk()
root.title("Simple Translator")
root.geometry("300x200")
tk.Label(root, text="Enter word:").pack(pady=5)
entry_word = tk.Entry(root)
entry_word.pack(pady=5)
btn_translate = tk.Button(root, text="Translate", command=translate)
btn_translate.pack(pady=10)
label_result = tk.Label(root, text="")
label_result.pack(pady=20)

root.mainloop()