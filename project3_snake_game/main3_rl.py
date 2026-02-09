import tkinter as tk
import random
import time
import copy
from collections import defaultdict

# ================= CONFIG =================
WIDTH = 600
HEIGHT = 600
SIZE = 20
GRID_W = WIDTH // SIZE
GRID_H = HEIGHT // SIZE

BASE_SPEED = 80
DISPLAY_TIME = 10

TRAIN_STEPS = 1000000
SAVE_STEPS = [50, 100, 500, 1000, 5000, 100000, 1000000]
# ========================================


# ================= ENV =================
class SnakeEnv:
    def reset(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.new_food()
        self.score = 0
        self.done = False
        return self.get_state()

    def new_food(self):
        return (random.randint(0, GRID_W-1) * SIZE,
                random.randint(0, GRID_H-1) * SIZE)

    def get_state(self):
        hx, hy = self.snake[0]
        fx, fy = self.food

        dir_map = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0)
        }

        dx, dy = dir_map[self.direction]

        return (
            fx > hx, fx < hx,
            fy > hy, fy < hy,
            dx, dy
        )

    def step(self, action):
        # 0 up, 1 down, 2 left, 3 right
        actions = ["Up", "Down", "Left", "Right"]
        opposite = {"Up":"Down","Down":"Up","Left":"Right","Right":"Left"}

        new_dir = actions[action]
        if opposite[new_dir] != self.direction:
            self.direction = new_dir

        hx, hy = self.snake[0]

        if self.direction == "Up": hy -= SIZE
        elif self.direction == "Down": hy += SIZE
        elif self.direction == "Left": hx -= SIZE
        elif self.direction == "Right": hx += SIZE

        new_head = (hx, hy)

        if (
            hx < 0 or hx >= WIDTH or
            hy < 0 or hy >= HEIGHT or
            new_head in self.snake
        ):
            self.done = True
            return self.get_state(), -10, True

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.new_food()
            self.score += 1
            reward = 10
        else:
            self.snake.pop()
            reward = -0.1

        return self.get_state(), reward, False


# ================= AGENT =================
class QAgent:
    def __init__(self):
        self.q = defaultdict(lambda: [0,0,0,0])
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0

    def act(self, state):
        if random.random() < self.epsilon:
            return random.randint(0,3)
        return max(range(4), key=lambda a: self.q[state][a])

    def learn(self, s, a, r, s2):
        self.q[s][a] += self.lr * (
            r + self.gamma * max(self.q[s2]) - self.q[s][a]
        )


# ================= TRAIN =================
def train_models():
    env = SnakeEnv()
    agent = QAgent()
    models = {}

    steps = 0
    env.reset()
    models[0] = copy.deepcopy(agent.q)

    while steps < TRAIN_STEPS:
        state = env.get_state()
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)

        agent.epsilon = max(0.05, agent.epsilon * 0.999)
        steps += 1

        if steps in SAVE_STEPS:
            models[steps] = copy.deepcopy(agent.q)
            print(f"Saved model at step {steps}")

        if done:
            env.reset()

    return models


# ================= GUI =================
class SnakeGUI:
    def __init__(self, root, models):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.label = tk.Label(root, font=("Arial", 16))
        self.label.pack()

        self.models = models
        self.steps = list(models.keys())
        self.index = 0

        self.env = SnakeEnv()
        self.agent = QAgent()
        self.agent.epsilon = 0

        self.start_time = None
        self.env.reset()
        self.load_model()

    def load_model(self):
        step = self.steps[self.index]
        self.agent.q = self.models[step]
        self.env.reset()
        self.start_time = time.time()
        self.label.config(text=f"Step {step}")
        self.update()

    def update(self):
        step = self.steps[self.index]

        if step != self.steps[-1] and time.time() - self.start_time > DISPLAY_TIME:
            self.index += 1
            self.load_model()
            return

        state = self.env.get_state()
        action = self.agent.act(state)
        _, _, done = self.env.step(action)

        if done:
            self.env.reset()

        self.draw()
        self.root.after(BASE_SPEED, self.update)

    def draw(self):
        self.canvas.delete("all")

        self.canvas.create_text(
            70, 20,
            text=f"Score: {self.env.score}",
            fill="white",
            font=("Arial", 16)
        )

        for i, (x,y) in enumerate(self.env.snake):
            color = "yellow" if i == 0 else "green"
            self.canvas.create_rectangle(
                x, y, x+SIZE, y+SIZE, fill=color
            )

        fx, fy = self.env.food
        self.canvas.create_oval(
            fx, fy, fx+SIZE, fy+SIZE, fill="red"
        )


# ================= MAIN =================
def main():
    print("Training...")
    models = train_models()
    print("Training finished")

    root = tk.Tk()
    root.title("Snake RL – Learning Progress")
    SnakeGUI(root, models)
    root.mainloop()


if __name__ == "__main__":
    main()
