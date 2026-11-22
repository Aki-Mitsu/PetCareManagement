import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from system.db_handler import DBHandler
from system.user_manager import UserManager
from system.pet_manager import PetManager

class PetCareApp:
    def __init__(self, root):
        """Initialize the main application window and backend."""
        self.root = root
        self.root.title("PetCare Management System")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f0f0")  # light background

        self.db = DBHandler()
        self.um = UserManager(self.db)

        self.user = None
        self.pm = None

        self.login_screen()

    def login_screen(self):
        """Show login/register screen."""
        self.clear_window()
        tk.Label(self.root, text="PetCare Management System", font=("Helvetica", 20, "bold"),
                 bg="#f0f0f0", fg="#333").pack(pady=30)
        tk.Button(self.root, text="Register", width=20, height=2, bg="#4CAF50", fg="white",
                  font=("Helvetica", 12), command=self.register).pack(pady=10)
        tk.Button(self.root, text="Login", width=20, height=2, bg="#2196F3", fg="white",
                  font=("Helvetica", 12), command=self.login).pack(pady=10)

    def register(self):
        """Register a new user and log them in."""
        username = simpledialog.askstring("Register", "Enter username:")
        password = simpledialog.askstring("Register", "Enter password:", show='*')
        if username and password:
            self.um.register(username, password)
            messagebox.showinfo("Success", "Registration successful!")
            self.user = self.um.login(username, password)
            self.pm = PetManager(self.db, self.user.user_id)
            self.main_menu()

    def login(self):
        """Log in an existing user."""
        username = simpledialog.askstring("Login", "Enter username:")
        password = simpledialog.askstring("Login", "Enter password:", show='*')
        self.user = self.um.login(username, password)
        if self.user:
            self.pm = PetManager(self.db, self.user.user_id)
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def main_menu(self):
        """Display main menu with pet management options."""
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {self.user.username}!", font=("Helvetica", 18, "bold"),
                 bg="#f0f0f0", fg="#333").pack(pady=30)

        tk.Button(self.root, text="Add Pet", width=20, height=2, bg="#4CAF50", fg="white",
                  font=("Helvetica", 12), command=self.add_pet).pack(pady=5)
        tk.Button(self.root, text="View Pets", width=20, height=2, bg="#FF9800", fg="white",
                  font=("Helvetica", 12), command=self.view_pets).pack(pady=5)
        tk.Button(self.root, text="Remove Pet", width=20, height=2, bg="#f44336", fg="white",
                  font=("Helvetica", 12), command=self.remove_pet).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, height=2, bg="#9E9E9E", fg="white",
                  font=("Helvetica", 12), command=self.logout).pack(pady=20)

    def add_pet(self):
        """Add a new pet for the current user."""
        name = simpledialog.askstring("Add Pet", "Pet Name:")
        age = simpledialog.askinteger("Add Pet", "Age:")
        pet_type = simpledialog.askstring("Add Pet", "Pet Type (Dog/Cat/Rabbit/Hamster):")
        if name and age and pet_type:
            self.pm.add_pet(name, age, pet_type)
            messagebox.showinfo("Success", f"{name} added successfully!")

    def view_pets(self):
        """Display all pets in a table view using Treeview."""
        self.clear_window()
        tk.Label(self.root, text=f"{self.user.username}'s Pets", font=("Helvetica", 16, "bold"),
                 bg="#f0f0f0", fg="#333").pack(pady=10)

        # Create Treeview widget
        columns = ("Name", "Age", "Type")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#f9f9f9",
                        foreground="#333",
                        rowheight=25,
                        fieldbackground="#f9f9f9",
                        font=("Helvetica", 11))
        style.configure("Treeview.Heading",
                        font=("Helvetica", 12, "bold"),
                        background="#4CAF50",
                        foreground="white")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(pady=10)

        # Insert pets into the tree
        pets = self.pm.get_pets()
        for pet in pets:
            self.tree.insert("", "end", values=(pet.name, pet.age, pet.pet_type))

        tk.Button(self.root, text="Back", width=15, height=2, bg="#9E9E9E", fg="white",
                  font=("Helvetica", 12), command=self.main_menu).pack(pady=10)

    def remove_pet(self):
        """Remove a pet selected from a dialog or Treeview."""
        pets = self.pm.get_pets()
        if not pets:
            messagebox.showinfo("Info", "No pets to remove.")
            return

        pet_names = [pet.name for pet in pets]
        name = simpledialog.askstring("Remove Pet", f"Enter pet name to remove:\nAvailable: {', '.join(pet_names)}")
        if name:
            self.pm.remove_pet(name)
            messagebox.showinfo("Removed", f"{name} removed successfully!")

    def logout(self):
        """Log out current user and return to login screen."""
        self.user = None
        self.pm = None
        self.login_screen()

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PetCareApp(root)
    root.mainloop()
