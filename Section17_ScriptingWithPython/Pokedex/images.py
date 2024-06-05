import tkinter as tk
from PIL import ImageTk, Image
import sys

def display_images(image_paths, resize_size=(200, 200)):
    root = tk.Tk()
    root.title("Image Viewer")

    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize(resize_size)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=photo)
        label.image = photo  # Keep a reference to prevent garbage collection
        label.pack()

    root.mainloop()

image_paths = [
    "pikachu.jpg",
    "charmander.jpg",
    "bulbasaur.jpg",
    "squirtle.jpg",
]

display_images(image_paths)