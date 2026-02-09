import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
SIZE = 20
SPEED = 1

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = [(100, 100), (80, 100), (60, 100)]
direction = "Right"

food = (0, 0)

# --- تمرین 1: متغیر امتیاز ---
score = 0

# --- تمرین 2: شمارش تعداد غذا برای افزایش سرعت ---
foods_eaten = 0

def new_food():
    return (random.randint(0, (WIDTH-SIZE)//SIZE) * SIZE,
            random.randint(0, (HEIGHT-SIZE)//SIZE) * SIZE)

food = new_food()

def draw():
    canvas.delete("all")

    # --- تمرین 1: نمایش امتیاز روی صفحه ---
    canvas.create_text(70, 20,
                       text="Score: " + str(score),
                       fill="white",
                       font=("Arial", 16))
    canvas.create_text(70, 50,
                       text="Speed: " + str(SPEED),
                       fill="white",
                       font=("Arial", 16))

    # --- تمرین 3: رنگ متفاوت برای سر مار ---
    for i, (x, y) in enumerate(snake):
        if i == 0:
            color = "yellow"   # سر مار
        else:
            color = "green"
        canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=color)

    canvas.create_oval(food[0], food[1],
                       food[0]+SIZE, food[1]+SIZE,
                       fill="red")

def move():
    global food, score, foods_eaten, SPEED

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= SIZE
    elif direction == "Down":
        head_y += SIZE
    elif direction == "Left":
        head_x -= SIZE
    elif direction == "Right":
        head_x += SIZE

    new_head = (head_x, head_y)

    if (head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake):
        game_over()
        return

    snake.insert(0, new_head)

    if new_head == food:
        food = new_food()

        # --- تمرین 1: افزایش امتیاز ---
        score += 1

        # --- تمرین 2: افزایش سرعت هر 5 غذا ---
        foods_eaten += 1
        if foods_eaten % 5 == 0 and SPEED < 30:
            SPEED += 1
    else:
        snake.pop()

    draw()
    root.after(101-10*SPEED, move)

def change_direction(new_dir):
    global direction
    opposite = {"Up":"Down", "Down":"Up",
                "Left":"Right", "Right":"Left"}
    if opposite[new_dir] != direction:
        direction = new_dir

def game_over():
    popup = tk.Toplevel()
    popup.title("Game Over")
    popup.geometry("250x180")
    popup.resizable(False, False)

    label = tk.Label(popup, text="Game Over!", font=("Arial", 18))
    label.pack(pady=10)

    # --- تمرین 1: نمایش امتیاز نهایی ---
    score_label = tk.Label(popup,
                           text="Final Score: " + str(score))
    score_label.pack()

    restart_button = tk.Button(popup, text="Restart",
                               command=lambda: restart(popup))
    restart_button.pack(pady=10)

def restart(popup):
    global snake, direction, food, score, foods_eaten, SPEED

    popup.destroy()

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "Right"
    food = new_food()

    # --- ریست کردن مقادیر تمرین‌ها ---
    score = 0
    foods_eaten = 0
    SPEED = 1

    draw()
    move()

root.bind("<Up>", lambda e: change_direction("Up"))
root.bind("<Down>", lambda e: change_direction("Down"))
root.bind("<Left>", lambda e: change_direction("Left"))
root.bind("<Right>", lambda e: change_direction("Right"))

draw()
move()

root.mainloop()
