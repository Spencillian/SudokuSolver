import tkinter as tk


def get_input(inputs: list) -> list:
    result = []
    for row in inputs:
        temp = []
        for entry in row:
            if entry.get():
                temp.append(int(entry.get()))
            else:
                temp.append(None)
        result.append(temp)
    print(result)
    return result


def draw(board: list) -> None:
    root = tk.Tk()
    inputs = []

    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            e = tk.Entry(root, width=2, borderwidth=10)
            temp.append(e)
            e.grid(row=i, column=j)
        inputs.append(temp)

    btn = tk.Button(root, text="Input", command=lambda: get_input(inputs))
    btn.grid(row=10, column=0)

    tk.mainloop()
