import tkinter as tk

# ساخت پنجره
root = tk.Tk()
root.title("ماشین حساب ساده")

# متغیر برای نگه داشتن عبارت
expression = ""

# متغیر برای نمایش در ورودی
text_var = tk.StringVar()

# کادر نمایش
entry = tk.Entry(root, textvariable=text_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)


def click(char):
    global expression

    if char == "C":
        expression = ""
    elif char == "=":
        try:
            expression = str(eval(expression))
        except:
            expression = "خطا"
    else:
        expression = expression + char

    text_var.set(expression)


tk.Button(root, text="7", width=8, height=2, command=lambda: click("7")).grid(row=1, column=0)
tk.Button(root, text="8", width=8, height=2, command=lambda: click("8")).grid(row=1, column=1)
tk.Button(root, text="9", width=8, height=2, command=lambda: click("9")).grid(row=1, column=2)
tk.Button(root, text="/", width=8, height=2, command=lambda: click("/")).grid(row=1, column=3)

tk.Button(root, text="4", width=8, height=2, command=lambda: click("4")).grid(row=2, column=0)
tk.Button(root, text="5", width=8, height=2, command=lambda: click("5")).grid(row=2, column=1)
tk.Button(root, text="6", width=8, height=2, command=lambda: click("6")).grid(row=2, column=2)
tk.Button(root, text="*", width=8, height=2, command=lambda: click("*")).grid(row=2, column=3)

tk.Button(root, text="1", width=8, height=2, command=lambda: click("1")).grid(row=3, column=0)
tk.Button(root, text="2", width=8, height=2, command=lambda: click("2")).grid(row=3, column=1)
tk.Button(root, text="3", width=8, height=2, command=lambda: click("3")).grid(row=3, column=2)
tk.Button(root, text="-", width=8, height=2, command=lambda: click("-")).grid(row=3, column=3)

tk.Button(root, text="0", width=8, height=2, command=lambda: click("0")).grid(row=4, column=0)
tk.Button(root, text=".", width=8, height=2, command=lambda: click(".")).grid(row=4, column=1)
tk.Button(root, text="C", width=8, height=2, command=lambda: click("C")).grid(row=4, column=2)
tk.Button(root, text="+", width=8, height=2, command=lambda: click("+")).grid(row=4, column=3)

tk.Button(root, text="=", width=22, height=2, command=lambda: click("=")).grid(row=5, column=0, columnspan=4)

root.mainloop()
