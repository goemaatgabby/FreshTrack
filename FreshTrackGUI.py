import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from GroceryItem import GroceryItem


class FreshTrackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FreshTrack - Grocery Expiration Tracker")
        self.root.geometry("800x550")
        self.root.configure(bg="#eaf4e5")

        # Temporary storage for Sprint 2 GUI testing.
        self.groceries = []
        self.next_id = 1

        # Title
        title = tk.Label(
            root,
            text="FreshTrack Grocery Tracker",
            font=("Arial", 20, "bold"),
            bg="#eaf4e5",
            fg="#31572c"
        )
        title.pack(pady=15)

        # Grocery entry form
        form = tk.Frame(root, bg="#eaf4e5")
        form.pack(pady=10)

        tk.Label(
            form, text="Grocery Name:",
            bg="#eaf4e5"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(form, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(
            form, text="Quantity:",
            bg="#eaf4e5"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.quantity_entry = tk.Entry(form, width=25)
        self.quantity_entry.grid(row=1, column=1, padx=5)

        tk.Label(
            form, text="Expiration Date (YYYY-MM-DD):",
            bg="#eaf4e5"
        ).grid(row=2, column=0, padx=5, pady=5)

        self.date_entry = tk.Entry(form, width=25)
        self.date_entry.grid(row=2, column=1, padx=5)

        # Add grocery button
        tk.Button(
            root,
            text="Add Grocery",
            command=self.add_grocery,
            bg="#4f7048",
            fg="white",
            width=20
        ).pack(pady=10)

        # Grocery inventory table
        self.table = ttk.Treeview(
            root,
            columns=("ID", "Name", "Quantity", "Expiration"),
            show="headings",
            height=9
        )

        for column in ("ID", "Name", "Quantity", "Expiration"):
            self.table.heading(column, text=column)
            self.table.column(column, width=145, anchor="center")

        self.table.pack(pady=10, padx=15, fill="both", expand=True)

        # Search section
        search_frame = tk.Frame(root, bg="#eaf4e5")
        search_frame.pack(pady=10)

        tk.Label(
            search_frame,
            text="Search Grocery:",
            bg="#eaf4e5"
        ).pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame, width=25)
        self.search_entry.pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="Search",
            command=self.search_grocery
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="Show All",
            command=self.display_groceries
        ).pack(side="left", padx=5)

    def add_grocery(self):
        name = self.name_entry.get().strip()
        quantity_text = self.quantity_entry.get().strip()
        expiration = self.date_entry.get().strip()

        # Validate grocery name
        if not name:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a grocery name."
            )
            return

        # Validate quantity
        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Quantity must be a positive whole number."
            )
            return

        # Validate expiration date
        try:
            datetime.strptime(expiration, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Enter a valid date in YYYY-MM-DD format."
            )
            return

        # Create grocery item
        item = GroceryItem(
            self.next_id,
            name,
            quantity,
            expiration
        )

        self.groceries.append(item)
        self.next_id += 1

        self.display_groceries()

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            f"{name} was added successfully!"
        )

    def display_groceries(self):
        # Clear existing table rows
        for row in self.table.get_children():
            self.table.delete(row)

        # Display all groceries
        for item in self.groceries:
            self.table.insert(
                "",
                tk.END,
                values=(
                    item.item_id,
                    item.name,
                    item.quantity,
                    item.expiration_date
                )
            )

    def search_grocery(self):
        search_name = self.search_entry.get().strip().lower()

        if not search_name:
            messagebox.showerror(
                "Search Error",
                "Please enter a grocery name to search."
            )
            return

        # Clear table
        for row in self.table.get_children():
            self.table.delete(row)

        found = False

        for item in self.groceries:
            if search_name in item.name.lower():
                self.table.insert(
                    "",
                    tk.END,
                    values=(
                        item.item_id,
                        item.name,
                        item.quantity,
                        item.expiration_date
                    )
                )
                found = True

        if not found:
            messagebox.showinfo(
                "Search Results",
                "No matching groceries found."
            )
