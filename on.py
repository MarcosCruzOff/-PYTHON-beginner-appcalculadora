import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")

        # criar a entrada de texto
        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # criar os botões
        self.buttons = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "0", ".", "C", "/",
            "=",
        ]
        self.create_buttons()

        # vincular eventos de teclado
        self.master.bind("<Key>", self.handle_key_press)

    def create_buttons(self):
        # criar e posicionar os botões na interface
        for i, button_text in enumerate(self.buttons):
            row = i // 4 + 1
            column = i % 4
            button = tk.Button(self.master, text=button_text, padx=20, pady=10, command=lambda x=button_text: self.handle_button_click(x), bg="#121212", fg="white")
            button.grid(row=row, column=column, padx=5, pady=5)

    def handle_button_click(self, button_text):
        # lidar com cliques de botão
        if button_text == "C":
            self.entry.delete(0, tk.END)
        elif button_text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        else:
            self.entry.insert(tk.END, button_text)

    def handle_key_press(self, event):
        # lidar com eventos de teclado
        if event.char in "0123456789.+-*/":
            self.handle_button_click(event.char)
        elif event.keysym == "Return":
            self.handle_button_click("=")
        elif event.keysym == "BackSpace":
            self.entry.delete(len(self.entry.get())-1, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
