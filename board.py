import tkinter as tk
import evaluator
import solver


class Board:
    __instance = None

    @staticmethod
    def get_instance() -> __instance:
        if Board.__instance is None:
            Board()
        return Board.__instance

    def __init__(self) -> None:
        if Board.__instance is not None:
            # TODO: Find a more elegant way to handle this exception
            # Maybe just `pass` works
            raise Exception("Board: Attempt made to create more instances of singleton")
        else:
            Board.__instance = self
            self.board = [[None] * 9] * 9
            self.display()
            self.board_dual = []

    def display(self) -> None:
        root = tk.Tk()
        inputs = []

        for i in range(len(self.board)):
            temp = []
            for j in range(len(self.board)):
                e = tk.Entry(root, width=2, borderwidth=15)
                e.insert(0, self.board[i][j] if self.board[i][j] is not None else "")
                temp.append(e)
                e.grid(row=i, column=j)
            inputs.append(temp)

        check_btn = tk.Button(root, text="Check", command=lambda: self.check(inputs))
        check_btn.grid(row=10, column=0)

        solve_btn = tk.Button(root, text="Solve", command=lambda: self.solve(inputs))
        solve_btn.grid(row=10, column=1)

        tk.mainloop()

    def get_input(self, inputs: list) -> None:
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

    def check(self, inputs: list) -> None:
        self.get_input(inputs)
        return print(evaluator.check(self.board))  # TODO: Is there a better way to output this data

    def solve(self, inputs: list) -> None:
        self.board_dual = [[[i for i in range(1, 10)]] * 9] * 9
        self.get_input(inputs)

        row_dual = solver.row_solid(self.board)
        print(row_dual)

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                # TODO: There is something wrong with the way this filters every row instead of just the focused
                self.board_dual[i][j] = list(filter(lambda x: x not in row_dual[i], self.board_dual[i][j]))

        for row in self.board_dual:
            print(row)

        pass
