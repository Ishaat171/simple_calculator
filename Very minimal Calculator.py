import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.entry = tk.Entry(self, width=35, font=("Arial", 16))
        self.entry.pack()
        self.button = tk.Button(self, text="Calculate", command=self.calculate)
        self.button.pack()
    
    def calculate(self):
        # Get the expression from the entry box
        expression = self.entry.get()
        # Evaluate the expression and display the result
        result = eval(expression)
        self.entry.delete(0, "end")
        self.entry.insert(0, result)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()