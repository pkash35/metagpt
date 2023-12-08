import tkinter as tk
from calculator import Calculator

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.binary1_entry = tk.Entry(self)
        self.binary1_entry.pack(side="top")

        self.binary2_entry = tk.Entry(self)
        self.binary2_entry.pack(side="top")

        self.add_button = tk.Button(self, text="Add", command=self.add)
        self.add_button.pack(side="top")

        self.subtract_button = tk.Button(self, text="Subtract", command=self.subtract)
        self.subtract_button.pack(side="top")

        self.multiply_button = tk.Button(self, text="Multiply", command=self.multiply)
        self.multiply_button.pack(side="top")

        self.divide_button = tk.Button(self, text="Divide", command=self.divide)
        self.divide_button.pack(side="top")

        self.result_label = tk.Label(self)
        self.result_label.pack(side="top")

        self.clear_button = tk.Button(self, text="Clear", command=self.clear)
        self.clear_button.pack(side="top")

    def calculate(self, operation):
        binary1 = self.binary1_entry.get()
        binary2 = self.binary2_entry.get()
        calculator = Calculator(binary1, binary2)
        result = getattr(calculator, operation)()
        self.result_label["text"] = result

    def add(self):
        self.calculate('add')

    def subtract(self):
        self.calculate('subtract')

    def multiply(self):
        self.calculate('multiply')

    def divide(self):
        self.calculate('divide')

    def clear(self):
        self.binary1_entry.delete(0, 'end')
        self.binary2_entry.delete(0, 'end')
        self.result_label["text"] = ""

root = tk.Tk()
app = Application(master=root)
app.mainloop()
