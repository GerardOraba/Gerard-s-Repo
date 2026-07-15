import tkinter as tk
 
 
class StudentGui:
    def submit(self):
        print("Salamat sir")
        print("Name:", self.entry_name.get())
        self.display_var.set(self.entry_name.get())
 
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")
 
        self.name_var = tk.StringVar()
        self.display_var = tk.StringVar()
 
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=1, column=1)
 
        self.entry_name = tk.Entry(root, textvariable=self.name_var)
        self.entry_name.grid(row=2, column=2)
 
        self.button_submit = tk.Button(root, text="Submit", command=self.submit)
        self.button_submit.grid(row=3, column=3)
 
        self.label_display = tk.Label(root, textvariable=self.display_var)
        self.label_display.grid(row=4, column=4)
 
    def save(self):
        print(self.entry_name.get())
 
 
root = tk.Tk()
app = StudentGui(root)
root.mainloop()