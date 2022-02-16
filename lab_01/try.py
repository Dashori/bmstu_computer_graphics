import tkinter as tk

root = tk.Tk()


def config(event):
    if event.widget == root:
        button.place(x=10, y=10, width=event.width/50, height=event.height/50)


root.bind("<Configure>", config)

button = tk.Button(root, text="Button")

root.mainloop()