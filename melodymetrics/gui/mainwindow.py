import sys
import tkinter as tk
from tkinter import ttk

import pandas as pd

from melodymetrics.dataanalysis.dataanalysis import DataAnalysis
from melodymetrics.dataset.kaggledownload import KaggleDownload


class MainWindow:

    def __init__(self, title="MelodyMetrics by Damián Peña", width=800, height=600):
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

        # Other attributes
        self.df = pd.DataFrame({"No dataframe loaded.": ["No dataframe loaded."]})

        # Add widgets
        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = ttk.Label(self.root, text="Welcome to MelodyMetrics!", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons
        self.button_download_dataframe = ttk.Button(
            self.root, text="Download Kaggle dataframe", style="TButton", command=self.button_download_dataframe_action
        )
        self.button_load_dataframe = ttk.Button(
            self.root, text="Load dataframe", style="TButton", command=self.button_load_dataframe_action
        )
        self.button_check_any_null = ttk.Button(self.root, text="Check nulls in columns", style="TButton", command=self.button_check_any_null_action)
        self.button_check_num_unique_values = ttk.Button(self.root, text="Check number of unique values", style="TButton", command=self.button_check_num_unique_values)
        self.button_add_time_ago_column = ttk.Button(self.root, text="Add time ago column", style="TButton", command=self.button_add_time_ago_column)

        self.button_download_dataframe.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.button_load_dataframe.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.button_check_any_null.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
        self.button_check_num_unique_values.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
        self.button_add_time_ago_column.grid(row=2, column=3, padx=10, pady=5, sticky="ew")

        # Dataset frame
        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Treeview for the dataframe
        self.tree = ttk.Treeview(self.frame, columns=list(self.df.columns), show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbars for Treeview
        scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        scroll_x = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        # Configure frame resizing behavior
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Populate treeview with placeholder data
        self.update_dataframe_view()

        # Console output
        self.console_output = tk.Text(self.root, wrap="word", height=10)
        self.console_output.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Redirect stdout to the console output
        sys.stdout = RedirectOutput(self.console_output)

        # Configure root resizing behavior
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def load_dataframe_from_analysis(self):
        da = DataAnalysis()
        self.df = da.df

    def button_download_dataframe_action(self):
        self.label.config(text="Downloading dataframe from kaggle.com...")
        print("Downloading dataframe from kaggle.com...")

        kd = KaggleDownload()
        kd.dataset_download()

    def button_load_dataframe_action(self):
        self.label.config(text="Loading dataset...")
        print("Loading dataset...")

        da = DataAnalysis(load_dataset=True)
        self.df = da.df.sort_values(by="popularity", ascending=False)

        self.update_dataframe_view()
        print("Finished loading dataset into dataframe.")

    def button_check_any_null_action(self):
        da = DataAnalysis()
        new_df = da.check_any_null_values()

        self.update_dataframe_view(new_df)

        self.label.config(text=f"Total null values in dataframe is {da.check_num_null_values()}")
        print("Checked for nulls in dataframe")
        print(f"Total null values in dataframe is {da.check_num_null_values()}")

    def button_check_num_unique_values(self):
        da = DataAnalysis()

        # Update dataframe view with unique values dataframe
        self.update_dataframe_view(da.check_num_unique_values())

        self.label.config(text="Printed number of unique values in dataframe")
        print("Printed number of unique values in dataframe")

    def button_add_time_ago_column(self):
        da = DataAnalysis()
        da.add_time_ago_column()

        self.load_dataframe_from_analysis()
        self.update_dataframe_view()

        self.label.config(text=f"Added new column 'time ago'")
        print(f"Added new column 'time ago'")

    def run(self):
        # Start the main event loop
        self.root.mainloop()

    def update_dataframe_view(self, df=None):

        if df is None:
            df = self.df
        else:
            df = df

        # Create Treeview
        tree = ttk.Treeview(self.frame, columns=list(df.columns), show="headings")
        tree.grid(row=0, column=0, sticky="nsew")

        # Add Scrollbars
        scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=tree.yview)
        scroll_x = ttk.Scrollbar(self.frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        # Grid Layout for Scrollbars
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        # Configure the frame grid weights
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Add Column Headings
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        # Add Rows
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))


class RedirectOutput:
    """
    Redirects stdout and stderr to a Tkinter Text widget.
    """
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, f"{text}\n")
        self.text_widget.see(tk.END)  # Automatically scroll to the end

        # Output to the original console
        sys.__stdout__.write(text)

    def flush(self):
        pass  # Needed for compatibility with Python's standard stream handling