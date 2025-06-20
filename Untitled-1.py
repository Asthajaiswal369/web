from tkinter import *
from tkinter import ttk, filedialog, messagebox, font
import os

USERNAME = "admin"
PASSWORD = "admin123"

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1400x750+0+0")
        self.saved_employees = []
        self.leave_requests = []
        self.login_screen()

    def login_screen(self):
        self.clear_widgets()
        login_frame = Frame(self.root, bg="white")
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(login_frame, text="Employee Management System", font=("Times New Roman", 28 , "bold"), fg="#075C5C", bg="white").grid(row=0, column=0, columnspan=2, pady=20)

        Label(login_frame, text="Username", font=("Arial", 22), bg="white").grid(row=1, column=0, sticky="w", padx=10)
        self.username_entry = Entry(login_frame, font=("Arial", 22), width=40)
        self.username_entry.grid(row=1, column=1, pady=5)

        Label(login_frame, text="Password", font=("Arial", 22), bg="white").grid(row=2, column=0, sticky="w", padx=10)
        self.password_entry = Entry(login_frame, show="*", font=("Arial", 22), width=40)
        self.password_entry.grid(row=2, column=1, pady=5)

        Button(login_frame, text="Sign In", command=self.validate_login, font=("Arial", 18), bg="#006666", fg="white", width=20).grid(row=3, columnspan=2, pady=20)

    def validate_login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username == USERNAME and entered_password == PASSWORD:
            self.dashboard_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def dashboard_screen(self):
        self.clear_widgets()
        sidebar = Frame(self.root, bg="#0b6363", width=200)
        sidebar.pack(side=LEFT, fill=Y)

        Button(sidebar, text="Dashboard", bg="#004d4d", fg="white", font=("Arial", 20), relief=FLAT, command=self.employee_form).pack(fill=X, pady=5)
        Button(sidebar, text="Employee", bg="#004d4d", fg="white", font=("Arial", 20), relief=FLAT, command=self.show_employees).pack(fill=X, pady=5)
        Button(sidebar, text="Leave Type", bg="#004d4d", fg="white", font=("Arial", 20), relief=FLAT, command=self.show_leave_types).pack(fill=X, pady=5)
        Button(sidebar, text="Leave Request", bg="#004d4d", fg="white", font=("Arial", 20), relief=FLAT, command=self.show_leave_requests).pack(fill=X, pady=5)
        Button(sidebar, text="Report", bg="#004d4d", fg="white", font=("Arial", 20), relief=FLAT, command=self.show_helpdesk).pack(fill=X, pady=5)
        Button(sidebar, text="Logout", bg="red", fg="white", font=("Arial", 20), relief=FLAT, command=self.login_screen).pack(fill=X, pady=5)

        self.main_frame = Frame(self.root, bg="white")
        self.main_frame.pack(fill=BOTH, expand=True)
        Label(self.main_frame, text="YOU ARE WELCOME TO EMPLOYEE MANAGEMENT SYSTEM...", font=("Arial", 24, "bold"), bg="white", fg="#033a3a").pack(pady=100)

    def employee_form(self):
        self.clear_main()

        frame1 = LabelFrame(self.main_frame, text="Personal Information", padx=10, pady=10)
        frame1.pack(fill=X, padx=10, pady=5)

        fields1 = [
            "Employee Code", "First Name", "Last Name", "Designation", "DOB", "Age",
            "Experience", "Gender", "Proof ID", "Email", "Contact No", "Address"
        ]

        bold_fields1 = {
            "Employee Code", "First Name", "Last Name", "Designation", "DOB", "Age",
            "Experience", "Gender", "Proof ID", "Email", "Contact No", "Address"
        }
        bold_font = font.Font(weight="bold")

        self.entries = {}
        for i, label in enumerate(fields1):
            is_bold = label in bold_fields1
            lbl = Label(frame1, text=label, font=bold_font if is_bold else None)
            lbl.grid(row=i//2, column=(i % 2)*2, padx=10, pady=5, sticky="w")
            ent = Entry(frame1, width=50)
            ent.grid(row=i//2, column=(i % 2)*2+1, padx=10, pady=5)
            self.entries[label] = ent

        frame2 = LabelFrame(self.main_frame, text="Job Details", padx=10, pady=10)
        frame2.pack(fill=X, padx=10, pady=5)

        fields2 = [
            "Monthly Salary", "Date Hired", "Department", "City", "State", "Password", "Confirm Password"
        ]

        bold_fields2 = {
            "Monthly Salary", "Date Hired", "Department", "City", "State", "Password", "Confirm Password"
        }

        for i, label in enumerate(fields2):
            is_bold = label in bold_fields2
            lbl = Label(frame2, text=label, font=bold_font if is_bold else None)
            lbl.grid(row=i//2, column=(i % 2)*2, padx=10, pady=5, sticky="w")
            ent = Entry(frame2, width=50, show="*" if "Password" in label else None)
            ent.grid(row=i//2, column=(i % 2)*2+1, padx=10, pady=5)
            self.entries[label] = ent

        self.photo_path = StringVar()
        Button(frame2, text="Choose Photo", command=self.upload_photo).grid(row=4, column=0, pady=5, padx=10)
        Label(frame2, textvariable=self.photo_path).grid(row=4, column=1)

        btn_frame = Frame(self.main_frame)
        btn_frame.pack(pady=10)

        Button(btn_frame, text="Submit", command=self.submit_form, bg="green", fg="white", width=15).grid(row=0, column=0, padx=10)
        Button(btn_frame, text="Save", bg="blue", fg="white", width=15).grid(row=0, column=1, padx=10)
        Button(btn_frame, text="Print", bg="purple", fg="white", width=15).grid(row=0, column=2, padx=10)
        Button(btn_frame, text="Exit", command=self.root.quit, bg="red", fg="white", width=15).grid(row=0, column=3, padx=10)

    def show_employees(self):
        self.clear_main()
        Label(self.main_frame, text="Employee Records", font=("Arial", 26, "bold"), bg="white", fg="#004d4d").pack(pady=10)

        if not self.saved_employees:
            Label(self.main_frame, text="No records found.", font=("Arial", 20, "bold"), bg="white").pack(anchor="w", padx=20)
            return

        columns = ("Code", "Name", "Email", "Age", "Department", "Contact", "Address", "State", "Date Hired", "Password")
        tree_frame = Frame(self.main_frame)
        tree_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 18, "bold"))
        style.configure("Treeview", font=("Arial", 16, "bold"), rowheight=40)

        tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")

        for emp in self.saved_employees:
            tree.insert("", "end", values=(
                emp.get("Employee Code", ""),
                f"{emp.get('First Name', '')} {emp.get('Last Name', '')}",
                emp.get("Email", ""),
                emp.get("Age", ""),
                emp.get("Department", ""),
                emp.get("Contact No", ""),
                emp.get("Address", ""),
                emp.get("State", ""),
                emp.get("Date Hired", ""),
                emp.get("Password", "")
            ))

        tree.pack(fill=BOTH, expand=True)

    def show_leave_types(self):
        self.clear_main()
        Label(self.main_frame, text="Available Leave Types", font=("Arial", 28), bg="white", fg="#004d4d").pack(pady=10)

        leave_types = [
            "Bereavement Leave", "Sick Leave", "Sabbatical Leave", "Marriage Leave",
            "Holidays", "Parental Leave", "Jury Duty Leave", "Voting Leave",
            "Religious Observance Leave", "Casual Leave", "Annual Leave", "Unpaid Leave"
        ]

        self.leave_vars = []
        for leave in leave_types:
            var = BooleanVar()
            chk = Checkbutton(self.main_frame, text=leave, variable=var, font=("Arial", 16), bg="white", anchor="w")
            chk.pack(anchor="w", padx=30)
            self.leave_vars.append((leave, var))

    def show_leave_requests(self):
        self.clear_main()
        Label(self.main_frame, text="Leave Requests Received", font=("Arial", 26, "bold"), bg="white", fg="#004d4d").pack(pady=10)

        if not self.leave_requests:
            Label(self.main_frame, text="No leave requests found.", font=("Arial", 20, "bold"), bg="white").pack(anchor="w", padx=20)
        else:
            for req in self.leave_requests:
                Label(self.main_frame, text=req, font=("Arial", 18), bg="white").pack(anchor="w", padx=20)

    def show_helpdesk(self):
        self.clear_main()
        Label(self.main_frame, text="Help Desk / Support", font=("Arial", 28, "bold"), bg="white", fg="#004d4d").pack(pady=10)

        info = [
            "✉ Email: support@company.com",
            "📞 Phone: +91-9876543210",
            "⏰ Available: Mon-Fri (10AM - 6PM)"
        ]

        for line in info:
            Label(self.main_frame, text=line, font=("Arial", 18), bg="white").pack(anchor="w", padx=20)

    def upload_photo(self):
        path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
        if path:
            self.photo_path.set(os.path.basename(path))

    def submit_form(self):
        password = self.entries["Password"].get()
        confirm = self.entries["Confirm Password"].get()
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        data = {key: entry.get() for key, entry in self.entries.items()}
        data["Photo"] = self.photo_path.get()
        self.saved_employees.append(data)
        self.leave_requests.append(f"{data['Employee Code']} - {data['First Name']} {data['Last Name']} - Casual Leave - 2 Days")
        messagebox.showinfo("Submitted", f"Employee {data['First Name']} added successfully!")

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

root = Tk()
app = EmployeeManagementSystem(root)
root.mainloop()