import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, title="MelodyMetrics by Damián Peña", width=400, height=300):
        # Initialize the main window
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

    def button1_action(self):
        self.label.config(text="Button 1 Clicked!")

    def button2_action(self):
        self.label.config(text="Button 2 Clicked!")

    def run(self):
        # Start the main event loop
        self.root.mainloop()

