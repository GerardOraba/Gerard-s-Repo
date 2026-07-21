import tkinter as tk
from tkinter import ttk, messagebox
import os
import threading
from student import Student
from database import save_student, search_student, update_student, delete_student, fetch_all_students, get_next_student_id
from validation import validate_fields


class StudentGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information Management System")
        self.root.resizable(False, False)

        # Set window icon
        icon_path = os.path.join(os.path.dirname(__file__), "ISCPschool_logo.png")
        if os.path.exists(icon_path):
            icon = tk.PhotoImage(file=icon_path)
            self.root.iconphoto(True, icon)

        # ── StringVars ──────────────────────────────────────────
        self.var_id     = tk.StringVar()
        self.var_name   = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year   = tk.StringVar()
        self.var_gender = tk.StringVar(value="Male")
        self.var_email  = tk.StringVar()

        # ── Header Frame ─────────────────────────────────────────
        header_frame = tk.Frame(self.root)
        header_frame.grid(row=0, column=0, columnspan=5, sticky="ew", padx=10, pady=8)

        # System title
        tk.Label(header_frame, text="Student Information Management System",
                 font=("Arial", 13, "bold"))\
            .pack(side="left")

        # ── Form Fields ─────────────────────────────────────────
        fields = [
            ("Student ID:", self.var_id),
            ("Name:",       self.var_name),
            ("Course:",     self.var_course),
            ("Year Level:", self.var_year),
            ("Email:",      self.var_email),
        ]

        for i, (label_text, var) in enumerate(fields, start=1):
            tk.Label(self.root, text=label_text, anchor="w")\
                .grid(row=i, column=0, padx=10, pady=4, sticky="w")
            tk.Entry(self.root, textvariable=var, width=35)\
                .grid(row=i, column=1, columnspan=2, padx=5, pady=4, sticky="w")

        # ── Gender Radio Buttons ─────────────────────────────────
        tk.Label(self.root, text="Gender:", anchor="w")\
            .grid(row=6, column=0, padx=10, pady=4, sticky="w")
        tk.Radiobutton(self.root, text="Male",   variable=self.var_gender, value="Male")\
            .grid(row=6, column=1, sticky="w")
        tk.Radiobutton(self.root, text="Female", variable=self.var_gender, value="Female")\
            .grid(row=6, column=2, sticky="w")

        # ── Buttons Row 1: Save, Search, Update ─────────────────
        btn_frame1 = tk.Frame(self.root)
        btn_frame1.grid(row=7, column=0, columnspan=4, pady=6)
        tk.Button(btn_frame1, text="Save",   width=10, bg="#4CAF50", fg="white",
                  command=self.save).pack(side="left", padx=5)
        tk.Button(btn_frame1, text="Search", width=10, bg="#2196F3", fg="white",
                  command=self.search).pack(side="left", padx=5)
        tk.Button(btn_frame1, text="Update", width=10, bg="#FF9800", fg="white",
                  command=self.update).pack(side="left", padx=5)

        # ── Buttons Row 2: Delete, Display All, Clear, Exit ─────
        btn_frame2 = tk.Frame(self.root)
        btn_frame2.grid(row=8, column=0, columnspan=4, pady=4)
        tk.Button(btn_frame2, text="Delete",      width=10, bg="#f44336", fg="white",
                  command=self.delete).pack(side="left", padx=5)
        tk.Button(btn_frame2, text="Display All", width=10, bg="#9C27B0", fg="white",
                  command=self.display_all).pack(side="left", padx=5)
        tk.Button(btn_frame2, text="Clear",       width=10,
                  command=self.clear).pack(side="left", padx=5)
        tk.Button(btn_frame2, text="Exit",        width=10, bg="#607D8B", fg="white",
                  command=self.root.destroy).pack(side="left", padx=5)

        # ── Student Records Table ────────────────────────────────
        tk.Label(self.root, text="Student Records",
                 font=("Arial", 10, "bold")).grid(row=9, column=0,
                 columnspan=4, pady=(10, 2))

        columns = ("Student ID", "Name", "Course", "Year", "Gender", "Email")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=8)

        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Email":
                self.tree.column(col, width=280, anchor="center")
            else:
                self.tree.column(col, width=120, anchor="center")

        self.tree.grid(row=10, column=0, columnspan=4, padx=10, pady=5)

        # Scrollbar for table
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=10, column=4, sticky="ns")

        # Click on row to fill form
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        # Auto-fill next Student ID on startup
        self.var_id.set(get_next_student_id())

    # ── Helper: run a function in a background thread ────────────
    def run_in_thread(self, target):
        thread = threading.Thread(target=target, daemon=True)
        thread.start()

    # ── Helper: collect form values ──────────────────────────────
    def get_form_values(self):
        return (
            self.var_id.get().strip(),
            self.var_name.get().strip(),
            self.var_course.get().strip(),
            self.var_year.get().strip(),
            self.var_gender.get(),
            self.var_email.get().strip()
        )

    # ── Save ─────────────────────────────────────────────────────
    def save(self):
        sid, name, course, year, gender, email = self.get_form_values()
        valid, msg = validate_fields(sid, name, course, year, gender, email)
        if not valid:
            messagebox.showerror("Validation Error", msg)
            return

        student = Student(sid, name, course, year, gender, email)

        def task():
            result = save_student(student)
            def update_ui():
                if result:
                    messagebox.showinfo("Success", "Student record saved successfully!")
                    self.clear()
                else:
                    messagebox.showerror("Error", f"Student ID '{sid}' already exists.")
            self.root.after(0, update_ui)

        self.run_in_thread(task)

    # ── Search ───────────────────────────────────────────────────
    def search(self):
        sid = self.var_id.get().strip()
        if not sid:
            messagebox.showwarning("Input Required", "Please enter a Student ID to search.")
            return

        def task():
            student = search_student(sid)
            def update_ui():
                if student:
                    self.var_id.set(student.student_id)
                    self.var_name.set(student.name)
                    self.var_course.set(student.course)
                    self.var_year.set(student.year_level)
                    self.var_gender.set(student.gender)
                    self.var_email.set(student.get_email())

                    for row in self.tree.get_children():
                        self.tree.delete(row)
                    self.tree.insert("", "end", values=(
                        student.student_id, student.name, student.course,
                        student.year_level, student.gender, student.get_email()
                    ))
                else:
                    messagebox.showwarning("Not Found", "Student not found.")
            self.root.after(0, update_ui)

        self.run_in_thread(task)

    # ── Update ───────────────────────────────────────────────────
    def update(self):
        sid, name, course, year, gender, email = self.get_form_values()
        valid, msg = validate_fields(sid, name, course, year, gender, email)
        if not valid:
            messagebox.showerror("Validation Error", msg)
            return

        student = Student(sid, name, course, year, gender, email)

        def task():
            result = update_student(student)
            def update_ui():
                if result:
                    messagebox.showinfo("Success", "Student record updated successfully!")
                    self.clear()
                    self.display_all()
                else:
                    messagebox.showerror("Error", f"Student ID '{sid}' not found.")
            self.root.after(0, update_ui)

        self.run_in_thread(task)

    # ── Delete ───────────────────────────────────────────────────
    def delete(self):
        sid = self.var_id.get().strip()
        if not sid:
            messagebox.showwarning("Input Required", "Please enter a Student ID to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete",
                                      f"Are you sure you want to delete Student ID '{sid}'?")
        if not confirm:
            return

        def task():
            result = delete_student(sid)
            def update_ui():
                if result:
                    messagebox.showinfo("Deleted", "Student record deleted successfully!")
                    self.clear()
                    self.display_all()
                else:
                    messagebox.showerror("Error", f"Student ID '{sid}' not found.")
            self.root.after(0, update_ui)

        self.run_in_thread(task)

    # ── Display All ──────────────────────────────────────────────
    def display_all(self):
        def task():
            students = fetch_all_students()
            def update_ui():
                for row in self.tree.get_children():
                    self.tree.delete(row)
                for s in students:
                    self.tree.insert("", "end", values=(
                        s.student_id, s.name, s.course,
                        s.year_level, s.gender, s.get_email()
                    ))
            self.root.after(0, update_ui)

        self.run_in_thread(task)

    # ── Clear ────────────────────────────────────────────────────
    def clear(self):
        self.var_id.set(get_next_student_id())
        self.var_name.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_gender.set("Male")
        self.var_email.set("")

    # ── Click row to fill form ───────────────────────────────────
    def on_row_select(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            if values:
                self.var_id.set(values[0])
                self.var_name.set(values[1])
                self.var_course.set(values[2])
                self.var_year.set(values[3])
                self.var_gender.set(values[4])
                self.var_email.set(values[5])