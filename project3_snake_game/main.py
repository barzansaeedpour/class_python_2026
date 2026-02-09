import tkinter as tk      # برای ساخت رابط گرافیکی
import random             # برای تولید عدد تصادفی (محل غذا)

# ---------------- تنظیمات اولیه ----------------

WIDTH = 600               # عرض صفحه بازی
HEIGHT = 600              # ارتفاع صفحه بازی
SIZE = 20                 # اندازه هر خانه مار
SPEED = 100               # سرعت حرکت مار (هرچه کمتر باشد سریع‌تر است)

# ---------------- ساخت پنجره اصلی ----------------

root = tk.Tk()            # ساخت پنجره اصلی
root.title("Snake Game")  # عنوان پنجره

# ساخت بوم (صفحه رسم بازی)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()             # نمایش بوم روی صفحه

# ---------------- وضعیت اولیه مار ----------------

# لیستی از مختصات قسمت‌های مار
snake = [(100, 100), (80, 100), (60, 100)]

direction = "Right"       # جهت اولیه حرکت مار

food = (0, 0)             # متغیر غذا (بعداً مقدار می‌گیرد)

# ---------------- تابع ساخت غذای جدید ----------------

def new_food():
    # تولید مختصات تصادفی که روی شبکه 20 تایی باشد
    return (random.randint(0, (WIDTH-SIZE)//SIZE) * SIZE,
            random.randint(0, (HEIGHT-SIZE)//SIZE) * SIZE)

food = new_food()         # اولین غذا ساخته می‌شود

# ---------------- تابع رسم بازی ----------------

def draw():
    canvas.delete("all")  # پاک کردن کل صفحه برای رسم جدید

    # رسم قسمت‌های مار
    for x, y in snake:
        canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill="green")

    # رسم غذا
    canvas.create_oval(food[0], food[1],
                       food[0]+SIZE, food[1]+SIZE,
                       fill="red")

# ---------------- تابع حرکت مار ----------------

def move():
    global food

    head_x, head_y = snake[0]   # گرفتن مختصات سر مار

    # تغییر مختصات بر اساس جهت حرکت
    if direction == "Up":
        head_y -= SIZE
    elif direction == "Down":
        head_y += SIZE
    elif direction == "Left":
        head_x -= SIZE
    elif direction == "Right":
        head_x += SIZE

    new_head = (head_x, head_y)  # ساخت سر جدید

    # بررسی برخورد با دیوار یا بدن خودش
    if (head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake):
        game_over()  # اگر برخورد کرد → پایان بازی
        return

    snake.insert(0, new_head)  # اضافه کردن سر جدید به لیست

    # اگر غذا خورده شود
    if new_head == food:
        food = new_food()      # غذای جدید ساخته می‌شود
    else:
        snake.pop()            # اگر غذا نخورد → دم حذف می‌شود

    draw()                     # دوباره رسم صفحه
    root.after(SPEED, move)    # اجرای دوباره move بعد از چند میلی‌ثانیه

# ---------------- تغییر جهت حرکت ----------------

def change_direction(new_dir):
    global direction

    # جلوگیری از برگشت مستقیم مار
    opposite = {"Up":"Down", "Down":"Up",
                "Left":"Right", "Right":"Left"}

    if opposite[new_dir] != direction:
        direction = new_dir

# ---------------- پنجره پایان بازی ----------------

def game_over():
    popup = tk.Toplevel()           # ساخت پنجره جدید
    popup.title("Game Over")
    popup.geometry("250x150")
    popup.resizable(False, False)

    label = tk.Label(popup, text="Game Over!", font=("Arial", 18))
    label.pack(pady=20)

    restart_button = tk.Button(popup, text="Restart",
                               command=lambda: restart(popup))
    restart_button.pack()

# ---------------- ریست بازی ----------------

def restart(popup):
    global snake, direction, food

    popup.destroy()  # بستن پنجره پایان بازی

    # بازگرداندن وضعیت اولیه
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "Right"
    food = new_food()

    draw()
    move()

# ---------------- اتصال کلیدها ----------------

root.bind("<Up>", lambda e: change_direction("Up"))
root.bind("<Down>", lambda e: change_direction("Down"))
root.bind("<Left>", lambda e: change_direction("Left"))
root.bind("<Right>", lambda e: change_direction("Right"))

# ---------------- شروع بازی ----------------

draw()   # رسم اولیه
move()   # شروع حرکت

root.mainloop()   # اجرای حلقه اصلی برنامه


# تمرین 1:
#  یک امتیاز اضافه کنید که هر بار مار غذا
#  می‌خورد، ۱ امتیاز اضافه شود و در بالای صفحه نمایش داده شود

# تمرین 2:
# کاری کنید که بعد از هر ۵ بار غذا خوردن، سرعت مار بیشتر شود

# تمرین 3:
# رنگ سر مار را با بقیه بدن متفاوت کنید
# (راهنمایی: هنگام رسم، اگر اولین عضو لیست بود رنگ دیگری بدهید)