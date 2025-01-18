import sys
import tkinter as tk
from tkinter import ttk

import pandas as pd

from melodymetrics.dataanalysis.data_analysis import DataAnalysis
from melodymetrics.dataset.kaggle_download import KaggleDownload
from melodymetrics.exceptions import DatasetNotLoadedException
from melodymetrics.gui.plot_window import PlotWindow


class MainWindow:

    def __init__(self, title="MelodyMetrics by Damián Peña", width=900, height=700):
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        # self.root.configure(bg="#F5F5F5")  # Set a background color

        # Define a style for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a modern theme
        self.style.configure('TButton', font=('Arial', 11), padding=5, background='#4CAF50', foreground='white')
        self.style.map('TButton', background=[('active', '#45A049')])

        # Other attributes
        self.da = None
        self.df = pd.DataFrame({"No dataframe loaded.": [
            "No dataframe loaded."]})  # TODO: Maybe its possible to stop using this variable and use always the df from the da class

        # Add widgets
        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = ttk.Label(self.root, text="Welcome to MelodyMetrics!", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        # First Steps LabelFrame
        self.first_steps_frame = ttk.LabelFrame(self.root, text="First steps:", padding=(10, 10))
        self.first_steps_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        # Buttons in First Steps
        self.button_download_dataframe = ttk.Button(self.first_steps_frame, text="Download Kaggle dataframe",
                                                    style="TButton", command=self.button_download_dataframe_action)
        self.button_load_dataframe = ttk.Button(self.first_steps_frame, text="Load dataframe",
                                                style="TButton", command=self.button_load_dataframe_action)
        self.button_download_dataframe.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.button_load_dataframe.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        # Data Preprocessing LabelFrame
        self.data_preprocessing_frame = ttk.LabelFrame(self.root, text="Data preprocessing:", padding=(10, 10))
        self.data_preprocessing_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        # Buttons in Data Preprocessing
        self.button_check_any_null = ttk.Button(self.data_preprocessing_frame, text="Check nulls in columns",
                                                style="TButton", command=self.button_check_any_null_action)
        self.button_check_num_unique_values = ttk.Button(self.data_preprocessing_frame,
                                                         text="Check number of unique values",
                                                         style="TButton",
                                                         command=self.button_check_num_unique_values_action)
        self.button_separate_main_genre = ttk.Button(self.data_preprocessing_frame, text="Separate genres",
                                                     style="TButton", command=self.button_separate_main_genre_action)
        self.button_add_years_ago_column = ttk.Button(self.data_preprocessing_frame, text="Add years ago column",
                                                      style="TButton", command=self.button_add_years_ago_column_action)
        self.button_check_any_null.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.button_check_num_unique_values.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.button_separate_main_genre.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.button_add_years_ago_column.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        # EDA Actions LabelFrame
        self.eda_actions_frame = ttk.LabelFrame(self.root, text="EDA Actions (Exploratory Data Analysis)",
                                                padding=(10, 10))
        self.eda_actions_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        # Buttons in EDA Actions
        self.button_describe_columns = ttk.Button(self.eda_actions_frame, text="Describe dataframe columns",
                                                  style="TButton", command=self.button_describe_columns_action)
        self.button_show_df_info = ttk.Button(self.eda_actions_frame, text="Show df shape and info",
                                              style="TButton", command=self.button_show_df_info_action)
        self.button_show_dataframe_statistics = ttk.Button(self.eda_actions_frame, text="Show dataframe statistics",
                                                           style="TButton",
                                                           command=self.button_show_dataframe_statistics_action)
        self.button_find_dataset_duration = ttk.Button(self.eda_actions_frame, text="Show dataframe duration",
                                                       style="TButton",
                                                       command=self.button_find_dataset_duration_action)
        self.button_find_outliers = ttk.Button(self.eda_actions_frame, text="Find any outliers",
                                               style="TButton", command=self.button_find_outliers_action)
        self.button_open_plot_window = ttk.Button(self.eda_actions_frame, text="Open plot visualization window",
                                                  style="TButton", command=self.button_open_plot_window_action)
        self.button_describe_columns.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.button_show_df_info.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.button_show_dataframe_statistics.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.button_find_dataset_duration.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        self.button_find_outliers.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.button_open_plot_window.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        # Adding weights to rows and columns
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.first_steps_frame.grid_rowconfigure(0, weight=1)
        self.first_steps_frame.grid_columnconfigure(0, weight=1)
        self.first_steps_frame.grid_columnconfigure(1, weight=1)

        self.data_preprocessing_frame.grid_rowconfigure(0, weight=1)
        self.data_preprocessing_frame.grid_rowconfigure(1, weight=1)
        self.data_preprocessing_frame.grid_columnconfigure(0, weight=1)
        self.data_preprocessing_frame.grid_columnconfigure(1, weight=1)

        self.eda_actions_frame.grid_rowconfigure(0, weight=1)
        self.eda_actions_frame.grid_rowconfigure(1, weight=1)
        self.eda_actions_frame.grid_rowconfigure(2, weight=1)
        self.eda_actions_frame.grid_columnconfigure(0, weight=1)
        self.eda_actions_frame.grid_columnconfigure(1, weight=1)

        # TODO: Add index to the dataframe viewer
        # Dataset frame
        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

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
        self.console_output.bind("<Key>", "break")  # Disable writing in the text field
        self.console_output.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Redirect stdout to the console output
        sys.stdout = RedirectOutput(self.console_output)

        # Configure root resizing behavior
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Ensure the process terminates when the window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit())

    def load_dataframe_from_analysis(self):
        self.df = self.da.df

    def check_if_dataframe_loaded(self):
        if not isinstance(self.da, DataAnalysis):
            raise DatasetNotLoadedException

    def button_download_dataframe_action(self):
        self.label.config(text="Downloading dataframe from kaggle.com...")
        print("Downloading dataframe from kaggle.com...")

        kd = KaggleDownload()
        kd.dataset_download()

    def button_load_dataframe_action(self):
        self.label.config(text="Loading dataset...")
        print("Loading dataset...")

        self.da = DataAnalysis(load_dataset=True)
        self.load_dataframe_from_analysis()
        self.df = self.df.sort_values(by="popularity", ascending=False)

        self.update_dataframe_view(index=True)
        print("Finished loading dataset into dataframe (sorted by most popular).")

    def button_describe_columns_action(self):
        self.check_if_dataframe_loaded()
        aux_df = self.da.explain_dataframe_columns()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe columns explanation")
        print("Showing dataframe columns explanation")

    def button_show_df_info_action(self):
        self.check_if_dataframe_loaded()
        aux_df = self.da.show_dataframe_info()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe shape and main information")
        print("Showing dataframe shape and main information")

    def button_show_dataframe_statistics_action(self):
        self.check_if_dataframe_loaded()
        aux_df = self.da.summarize_dataframe_statistics()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe summarized dataframe statistics")
        print("Showing dataframe summarized dataframe statistics")

    def button_find_dataset_duration_action(self):
        self.check_if_dataframe_loaded()
        aux_df = self.da.find_dataset_duration()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe duration")
        print("Showing dataframe duration")

    def button_check_any_null_action(self):
        self.check_if_dataframe_loaded()
        aux_df = self.da.check_any_null_values()

        self.update_dataframe_view(aux_df)

        self.label.config(text=f"Total null values in dataframe is {self.da.check_num_null_values()}")
        print("Checked for nulls in dataframe")
        print(f"Total null values in dataframe is {self.da.check_num_null_values()}")

    def button_find_outliers_action(self):
        self.check_if_dataframe_loaded()
        aux_df = self.da.check_outliers_in_columns()

        self.update_dataframe_view(aux_df, index=True)

        self.label.config(text="Checking and deleting any outliers")
        print("Checked outliers...")

    def button_check_num_unique_values_action(self):
        self.check_if_dataframe_loaded()
        # Update dataframe view with unique values dataframe
        self.update_dataframe_view(self.da.check_num_unique_values())

        self.label.config(text="Printed number of unique values in dataframe")
        print("Printed number of unique values in dataframe")

    def button_separate_main_genre_action(self):
        self.check_if_dataframe_loaded()
        self.da.separate_genres()

        self.load_dataframe_from_analysis()
        self.update_dataframe_view(index=True)

        self.label.config(text="Separated genres into main genre and subgenre")
        print("Separated genres into main genre and subgenre")

        self.button_separate_main_genre.config(state="disabled")

    def button_add_years_ago_column_action(self):
        self.check_if_dataframe_loaded()
        self.da.add_years_ago_column()

        self.load_dataframe_from_analysis()
        self.update_dataframe_view(index=True)

        self.label.config(text="Added new column 'years ago'")
        print("Added new column 'years ago'")

    def button_open_plot_window_action(self):
        # Open the plot window if dataframe is loaded
        try:
            self.check_if_dataframe_loaded()
        except DatasetNotLoadedException as e:
            print(f"Couldn't open plot window because dataframe hasn't been loaded yet \nException: {e}")
        else:
            plot_window = PlotWindow(self.root)
            plot_window.create_widgets()
            plot_window.obtain_da_from_main_window(self.da)

    def update_dataframe_view(self, df=None, index=False):
        """
        Updates the Treeview widget to display the dataframe with an added index column.
        """
        if df is None:
            df = self.df

        if index:
            # Add an "Index" column as the first column
            columns = ["index"] + list(df.columns)
        else:
            columns = list(df.columns)

        # Create Treeview
        tree = ttk.Treeview(self.frame, columns=columns, show="headings")
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
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        if index:
            # Add Rows with Index
            for idx, (i, row) in enumerate(df.iterrows(), start=1):
                tree.insert("", "end", values=[idx] + list(row))

        else:
            # Add Rows
            for _, row in df.iterrows():
                tree.insert("", "end", values=list(row))

        # Save the Treeview
        self.tree = tree

    def run(self):
        # Start the main event loop
        self.root.mainloop()


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
