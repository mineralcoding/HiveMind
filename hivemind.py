import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Hive Mind")

# Load images
hive_image = Image.open("HiveMind.png")
hive_photo = ImageTk.PhotoImage(hive_image)

creeper_image = Image.open("DankCreeper.png")
creeper_photo = ImageTk.PhotoImage(creeper_image)

# Display HiveMind in the main window
label = tk.Label(root, image=hive_photo)
label.pack()

# Screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# --- Glide logic for any window ---
def glide_window(win, width, height, x, y, target_x, target_y):
    # Move closer to target
    if x < target_x: x += 5
    if x > target_x: x -= 5
    if y < target_y: y += 5
    if y > target_y: y -= 5
    win.geometry(f"{width}x{height}+{x}+{y}")
    # If reached target, pick a new one
    if abs(x - target_x) < 10 and abs(y - target_y) < 10:
        target_x = random.randint(0, screen_width - width)
        target_y = random.randint(0, screen_height - height)
    win.after(30, glide_window, win, width, height, x, y, target_x, target_y)

# Start HiveMind glide
start_x = random.randint(0, screen_width - hive_image.width)
start_y = random.randint(0, screen_height - hive_image.height)
root.geometry(f"{hive_image.width}x{hive_image.height}+{start_x}+{start_y}")
glide_window(root, hive_image.width, hive_image.height, start_x, start_y,
             random.randint(0, screen_width - hive_image.width),
             random.randint(0, screen_height - hive_image.height))

# --- Function to spawn new Creeper windows ---
def spawn_creeper():
    win = tk.Toplevel(root)
    win.title("Dank Creeper")
    lbl = tk.Label(win, image=creeper_photo)
    lbl.pack()
    w, h = creeper_image.width, creeper_image.height
    x = random.randint(0, screen_width - w)
    y = random.randint(0, screen_height - h)
    win.geometry(f"{w}x{h}+{x}+{y}")
    glide_window(win, w, h, x, y,
                 random.randint(0, screen_width - w),
                 random.randint(0, screen_height - h))
    root.after(5000, spawn_creeper)  # schedule next spawn

# Start spawning creepers
root.after(5000, spawn_creeper)

root.mainloop()