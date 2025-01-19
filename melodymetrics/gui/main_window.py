"""
Module to create and manage the main window for the MelodyMetrics application.
This module provides a detailed GUI to interact with the application for dataset handling, data analysis, preprocessing tasks and plotting.

Imports:
- sys: Provides access to some variables used by the interpreter to display console info in the GUI.
- tkinter: A Python library for creating graphical user interfaces (GUIs).
- pandas: A library for data manipulation and analysis, used to handle datasets.
- melodymetrics: Custom library for the data analysis and plotting.
"""

import sys
import tkinter as tk
from tkinter import ttk

import pandas as pd

from melodymetrics.dataanalysis.data_analysis import DataAnalysis
from melodymetrics.dataset.kaggle_download import KaggleDownload
from melodymetrics.exceptions import DatasetNotLoadedException, DatasetFileNotFoundException
from melodymetrics.gui.plot_window import PlotWindow


class MainWindow:

    def __init__(self, title="MelodyMetrics by Damián Peña", width=850, height=780):
        """
        MainWindow class for handling the GUI and interaction with various tasks in the MelodyMetrics application.

        Attributes
        ----------
        root : Tk
            The main window of the application.
        style : Style
            The style configuration for the ttk widgets.
        da : DataAnalysis
            An instance of the DataAnalysis class for performing data analysis.
        df : DataFrame
            The DataFrame containing the dataset loaded for analysis.

        Methods
        -------
        __init__ :
            Initializes the main window and sets up the GUI.
        create_widgets :
            Sets up the various widgets (buttons, labels, etc.) for user interaction with the app.
        load_dataframe_from_analysis :
            Loads the dataframe from the DataAnalysis class.
        check_if_dataframe_loaded :
            Checks if a dataframe has been loaded into the application.
        """
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        # self.root.configure(bg="#F5F5F5")  # Set a background color

        # Define a style for ttk widgets
        # TODO: Change this theme or leave it as is ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Main style (green)
        self.style.configure('TButton', font=('Arial', 11), padding=3, background='#4CAF50', foreground='white')
        self.style.map('TButton', background=[('active', '#45A049')])

        # Secondary style (red)
        self.style.configure('Red.TButton', font=('Arial', 11), padding=3, background='#F44336', foreground='white')
        self.style.map('Red.TButton', background=[('active', '#E53935')])

        # Other attributes
        self.da = None
        self.df = pd.DataFrame({"No dataframe loaded.": [
            "No dataframe loaded."]})  # TODO: Maybe its possible to stop using this variable and use always the df from the da class

        # Add widgets
        self.create_widgets()

    def create_widgets(self):
        """
        Create and place the widgets (labels, buttons, frames) in the main window.

        The widgets are organized into different LabelFrames:
        - First Steps: For downloading and loading datasets.
        - Data Preprocessing: For data preprocessing tasks.
        - EDA Actions: For exploratory data analysis tasks.
        """
        # Label
        self.label = ttk.Label(self.root, text="Welcome to MelodyMetrics!", font=("Arial", 14), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # First Steps LabelFrame
        self.first_steps_frame = ttk.LabelFrame(self.root, text="First steps:", padding=(10, 10))
        self.first_steps_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Buttons in First Steps
        self.button_download_dataframe = ttk.Button(self.first_steps_frame, text="Download Kaggle dataframe",
                                                    style="TButton", command=self.button_download_dataframe_action)
        self.button_load_dataframe = ttk.Button(self.first_steps_frame, text="Load dataframe .csv",
                                                style="TButton", command=self.button_load_dataframe_action)
        self.button_see_actual_dataframe = ttk.Button(self.first_steps_frame, text="See actual dataframe",
                                                style="TButton", command=self.button_see_actual_dataframe_action)
        self.button_download_dataframe.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.button_load_dataframe.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.button_see_actual_dataframe.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Data Preprocessing LabelFrame
        self.data_preprocessing_frame = ttk.LabelFrame(self.root, text="Data preprocessing:", padding=(10, 10))
        self.data_preprocessing_frame.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Buttons in Data Preprocessing
        self.button_check_any_null = ttk.Button(self.data_preprocessing_frame, text="Check nulls in columns",
                                                style="TButton", command=self.button_check_any_null_action)
        self.button_clean_outliers_duplicates = ttk.Button(self.data_preprocessing_frame,
                                                           text="Clean outliers/duplicates",
                                                           style="TButton",
                                                           command=self.button_clean_outliers_duplicates_action)
        self.button_separate_main_genre = ttk.Button(self.data_preprocessing_frame, text="Separate genres",
                                                     style="TButton", command=self.button_separate_main_genre_action)
        self.button_add_years_ago_column = ttk.Button(self.data_preprocessing_frame, text="Add years ago column",
                                                      style="TButton", command=self.button_add_years_ago_column_action)
        self.button_check_any_null.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.button_clean_outliers_duplicates.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.button_separate_main_genre.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.button_add_years_ago_column.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        # EDA Actions LabelFrame
        self.eda_actions_frame = ttk.LabelFrame(self.root, text="EDA Actions (Exploratory Data Analysis)",
                                                padding=(10, 10))
        self.eda_actions_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

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
        self.button_check_num_unique_values = ttk.Button(self.eda_actions_frame,
                                                         text="Check number of unique values",
                                                         style="TButton",
                                                         command=self.button_check_num_unique_values_action)
        self.button_open_plot_window = ttk.Button(self.eda_actions_frame, text="Open plot visualization window",
                                                  style='Red.TButton', command=self.button_open_plot_window_action)
        self.button_describe_columns.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.button_show_df_info.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.button_show_dataframe_statistics.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.button_find_dataset_duration.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        self.button_check_num_unique_values.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.button_open_plot_window.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        # Adding weights to rows and columns
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=20)
        self.root.grid_rowconfigure(4, weight=12)
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

        # Populate treeview with placeholder text
        self.update_dataframe_view()

        # Console output
        self.console_output = tk.Text(self.root, wrap="word", height=10)
        self.console_output.bind("<Key>", "break")  # Disable writing in the text field
        self.console_output.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Redirect stdout to the console output
        sys.stdout = RedirectOutput(self.console_output)

        # Configure root resizing behavior
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Ensure the process terminates when the window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit())

    def load_dataframe_from_analysis(self):
        """
        Loads the dataframe from the DataAnalysis instance into the current class instance, as it will be used in the next actions.

        This method assigns the dataframe from the DataAnalysis instance (self.da.df) to the local
        dataframe attribute (self.df).
        """
        self.df = self.da.df

    def check_if_dataframe_loaded(self):
        """
        Checks if a DataAnalysis instance is properly initialized so that the actions can be completed correctly.

        Raises:
            DatasetNotLoadedException: If the DataAnalysis instance is not initialized or loaded.
        """
        if not isinstance(self.da, DataAnalysis):
            raise DatasetNotLoadedException

    def button_download_dataframe_action(self):
        """
        Action triggered by the 'Download Kaggle dataframe' button.

        This method triggers the download of a dataset from Kaggle using the KaggleDownload class.
        The status of the download is displayed on the label and printed to the console.
        """
        self.label.config(text="Downloading dataframe from kaggle.com...")
        print("Downloading dataframe from kaggle.com...")

        kd = KaggleDownload()
        kd.dataset_download()

    def button_load_dataframe_action(self):
        """
        Action triggered by the 'Load dataframe' button.

        This method loads the dataset by initializing a DataAnalysis instance, sorting the dataframe by
        popularity in descending order, and updating the GUI view of the dataframe.
        """
        self.label.config(text="Loading dataset...")
        print("Loading dataset...")

        try:
            # Create  DataAnalysis and try to find dataset file
            self.da = DataAnalysis(load_dataset=False)
            self.da.find_dataset_csv()

        except DatasetFileNotFoundException as e:
            print(f"Error: {e}")
            return f"Error: {e}"

        else:
            self.da.load_csv_dataset()
            self.load_dataframe_from_analysis()
            self.df = self.df.sort_values(by="popularity", ascending=False)

            self.update_dataframe_view(index=True)
            print("Finished loading dataset into dataframe (sorted by most popular).")

    def button_see_actual_dataframe_action(self):
        """
        Action triggered by the 'See actual dataframe' button.

        This method displays the actual dataframe. It loads the dataframe
        to the GUI.
        """
        self.check_if_dataframe_loaded()

        self.update_dataframe_view(self.df)

        self.label.config(text="Actual dataframe:")
        print("Showing actual dataframe:")

    def button_describe_columns_action(self):
        """
        Action triggered by the 'Describe dataframe columns' button.

        This method displays a detailed explanation of the dataframe columns. It checks if the dataframe
        is loaded, and then shows the column descriptions in the GUI.
        """
        self.check_if_dataframe_loaded()
        aux_df = self.da.explain_dataframe_columns()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe columns explanation")
        print("Showing dataframe columns explanation")

    def button_show_df_info_action(self):
        """
        Action triggered by the 'Show dataframe info' button.

        This method displays the shape and main information of the loaded dataframe.
        It checks if the dataframe is loaded and then shows the information in the GUI.
        """
        self.check_if_dataframe_loaded()
        aux_df = self.da.show_dataframe_info()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe shape and main information")
        print("Showing dataframe shape and main information")

    def button_show_dataframe_statistics_action(self):
        """
        Action triggered by the 'Show dataframe statistics' button.

        This method shows the summarized statistics of the loaded dataframe. It checks if the dataframe
        is loaded and then presents the statistics in the GUI.
        """
        self.check_if_dataframe_loaded()
        aux_df = self.da.summarize_dataframe_statistics()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe summarized dataframe statistics")
        print("Showing dataframe summarized dataframe statistics")

    def button_find_dataset_duration_action(self):
        """
        Action triggered by the 'Show dataframe duration' button.

        This method calculates the duration of the dataset and displays it. It checks if the dataframe
        is loaded and then shows the dataset's duration in the GUI.
        """
        self.check_if_dataframe_loaded()
        aux_df = self.da.find_dataset_duration()

        self.update_dataframe_view(aux_df)

        self.label.config(text="Showing dataframe duration")
        print("Showing dataframe duration")

    def button_check_any_null_action(self):
        """
        Action triggered by the 'Check any null values' button.

        This method checks for null values in the dataframe and displays the total number of null values in the dataframe.
        It updates the view with the dataframe containing the null values information.
        """
        self.check_if_dataframe_loaded()
        aux_df = self.da.check_any_null_values()

        self.update_dataframe_view(aux_df)

        self.label.config(text=f"Total null values in dataframe is {self.da.check_num_null_values()}")
        print("Checked for nulls in dataframe")
        print(f"Total null values in dataframe is {self.da.check_num_null_values()}")

    def button_clean_outliers_duplicates_action(self):
        """
        Action triggered by the 'Clean outliers and duplicates' button.

        This method cleans the dataframe by removing outliers and duplicates. All information of the process is displayed.
        Also shows in the UI the outliers and duplicates (if any).
        """
        self.check_if_dataframe_loaded()
        aux_df = self.da.clean_outliers_and_duplicates()

        self.update_dataframe_view(aux_df, index=True)

        self.label.config(text="Cleaning outliers and duplicates")
        print("Cleaned outliers and duplicates...")

    def button_check_num_unique_values_action(self):
        """
        Action triggered by the 'Check number of unique values' button.

        This method prints the number of unique values in the dataframe and updates the view with the dataframe.
        """
        self.check_if_dataframe_loaded()
        # Update dataframe view with unique values dataframe
        self.update_dataframe_view(self.da.check_num_unique_values())

        self.label.config(text="Printed number of unique values in dataframe")
        print("Printed number of unique values in dataframe")

    def button_separate_main_genre_action(self):
        """
        Action triggered by the 'Separate genres' button.

        This method separates the genres in the dataframe into main genres and subgenres. The dataframe is updated and shown.
        """
        self.check_if_dataframe_loaded()
        self.da.separate_genres()

        self.load_dataframe_from_analysis()
        self.update_dataframe_view(index=True)

        self.label.config(text="Separated genres into main genre and subgenre")
        print("Separated genres into main genre and subgenre")

    def button_add_years_ago_column_action(self):
        """
        Action triggered by the 'Add years ago column' button.

        This method adds a new column, 'years ago', to the dataframe. The updated dataframe is shown in the GUI.
        """
        self.check_if_dataframe_loaded()
        self.da.add_years_ago_column()

        self.load_dataframe_from_analysis()
        self.update_dataframe_view(index=True)

        self.label.config(text="Added new column 'years ago'")
        print("Added new column 'years ago'")

    def button_open_plot_window_action(self):
        """
        Action triggered by the 'Open plot window' button.

        This method opens a plot visualization window if the dataframe is loaded. If the dataframe is not loaded, an error message is displayed.
        """
        # Open the plot window if dataframe is loaded
        try:
            self.check_if_dataframe_loaded()
        except DatasetNotLoadedException as e:
            print(f"Couldn't open plot window because dataframe hasn't been loaded yet \nException: {e}")
        else:
            try:
                plot_window = PlotWindow(self.root)
                plot_window.obtain_da_from_main_window(self.da)
            except TypeError as e:
                print(f"Couldn't open plot window because DataAnalysis object hasn't been loaded correctly \nException: {e}")
            else:
                plot_window.create_widgets()

    def update_dataframe_view(self, df=None, index=False):
        """
        Updates the Treeview widget to display the dataframe with an optionally added index column.

        Parameters
        ----------
        df : DataFrame, optional
            The dataframe to display in the Treeview widget. If not provided, the current dataframe (self.df) will be used.
        index : bool, optional
            Whether to add an "Index" column to the displayed dataframe. Default is False.

        This method updates the GUI with the dataframe, adding either an index column or not.
        It also sets up scrollbars and column headings in the Treeview widget.
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
        """
        Starts the main event loop for the Tkinter application.

        This method runs the Tkinter application, waiting for user interactions.
        """
        self.root.mainloop()


class RedirectOutput:
    """
    Redirects stdout and stderr to the Tkinter Text widget.

    This class captures output from print statements and errors, displaying them in a Tkinter Text widget,
    while also allowing the output to be printed to the original console.
    """

    def __init__(self, text_widget):
        """
        Initializes the RedirectOutput instance.

        Parameters
        ----------
        text_widget : Text
            The Tkinter Text widget where the output will be displayed.
        """
        self.text_widget = text_widget

    def write(self, text):
        """
        Redirects text to the Tkinter Text widget and to the original stdout.

        Parameters
        ----------
        text : str
            The text to redirect to the widget and console.
        """
        self.text_widget.insert(tk.END, f"{text}\n")
        self.text_widget.see(tk.END)  # Automatically scroll to the end

        # Output to the original console
        sys.__stdout__.write(text)

    def flush(self):
        """
        This method does nothing, it is needed for compatibility with Python's standard stream handling.
        """
        pass  # Needed for compatibility with Python's standard stream handling
