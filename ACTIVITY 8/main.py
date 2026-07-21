import tkinter as tk
from gui import StudentGui
from database import create_table
 
 
def main():
    
    create_table()
 
    
    root = tk.Tk()
    app = StudentGui(root)
    root.mainloop()
 
 
if __name__ == "__main__":
    main()
 