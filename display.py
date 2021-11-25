import tkinter as tk


def draw(board: list) -> None:
    root = tk.Tk()
    inputs = []

    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            e = tk.Entry(root, width=2)
            temp.append(e)
            e.grid(row=i, column=j)
        inputs.append(temp)

    tk.mainloop()

# TODO: add function for getting inputs
# TODO: add button for access to function
