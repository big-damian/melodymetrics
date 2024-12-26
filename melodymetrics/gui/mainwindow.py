import tkinter as tk
from tkinter import ttk

import pandas as pd


class MainWindow:

    def __init__(self, title="MelodyMetrics by Damián Peña", width=400, height=300):
        # Initialize the main window
        self.df = None
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        #self.root.configure(bg="#F5F5F5")  # Set a background color

        # Define a style for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a modern theme
        self.style.configure('TButton', font=('Arial', 12), padding=10, background='#4CAF50', foreground='white')
        self.style.map('TButton', background=[('active', '#45A049')])

        # Add widgets
        self.create_widgets()

    def create_widgets(self):
        # Add a label
        self.label = ttk.Label(self.root, text="Welcome to the Simple Window", font=("Arial", 14))
        self.label.pack(pady=20)

        # Add buttons
        self.button1 = ttk.Button(self.root, text="Button 1", style="TButton", command=self.button1_action)
        self.button1.pack(pady=10)

        self.button2 = ttk.Button(self.root, text="Button 2", style="TButton", command=self.button2_action)
        self.button2.pack(pady=10)

        # Create Frame for Treeview and Scrollbars
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")

        # Create Treeview
        if isinstance(self.df, pd.DataFrame):
            tree = ttk.Treeview(frame, columns=list(self.df.columns), show="headings")
            tree.grid(row=0, column=0, sticky="nsew")

            # Add Scrollbars
            scroll_y = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

            # Grid Layout for Scrollbars
            scroll_y.grid(row=0, column=1, sticky="ns")
            scroll_x.grid(row=1, column=0, sticky="ew")

            # Configure the frame grid weights
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            # Add Column Headings
            for col in df.columns:
                tree.heading(col, text=col)
                tree.column(col, width=100, anchor="center")

            # Add Rows
            for _, row in df.iterrows():
                tree.insert("", "end", values=list(row))
        else:
            print("Couldn't create the table view because df is None")

    def load_dataframe(self, df):
        self.df = df

    def button1_action(self):
        self.label.config(text="Button 1 Clicked!")

    def button2_action(self):
        self.label.config(text="Button 2 Clicked!")

    def run(self):
        # Start the main event loop
        self.root.mainloop()