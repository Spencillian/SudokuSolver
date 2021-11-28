import tkinter as tk
import evaluator


class Board:
    __instance = None

    @staticmethod
    def get_instance() -> __instance:
        if Board.__instance is None:
            Board()
        return Board.__instance

    def __init__(self):
        if Board.__instance is not None:
            # TODO: Find a more elegant way to handle this exception
            # Maybe just `pass` works
            raise Exception("Board: Attempt made to create more instances of singleton")
        else:
            Board.__instance = self
            self.board = [[None] * 9] * 9
            self.display()

    def display(self):
        root = tk.Tk()
        inputs = []

        for i in range(len(self.board)):
            temp = []
            for j in range(len(self.board)):
                e = tk.Entry(root, width=2, borderwidth=10)
                e.insert(0, self.board[i][j] if self.board[i][j] is not None else "")
                temp.append(e)
                e.grid(row=i, column=j)
            inputs.append(temp)

        btn = tk.Button(root, text="Check", command=lambda: self.get_input(inputs))
        btn.grid(row=10, column=0)

        tk.mainloop()

    def get_input(self, inputs):
        result = []
        for row in inputs:
            temp = []
            for entry in row:
                if entry.get():
                    temp.append(int(entry.get()))
                else:
                    temp.append(None)
            result.append(temp)
        self.board = result
        for row in self.board:
            print(row)
        print(self.check())

    def check(self):
        return evaluator.check(self.board)
