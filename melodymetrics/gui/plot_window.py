"""
PlotWindow Module

This module defines the PlotWindow class, which creates and manages a dedicated window for visualizing
various plots related to the dataset in the MelodyMetrics application. It provides functionality to display
multiple types of plots (bar charts, pie charts, line charts) based on the data loaded in the `DataAnalysis`
instance passed from the main window.

Classes
--------
PlotWindow : A class that handles the creation of the plot window, displaying different types of charts,
            and updating the view based on user interaction.
"""

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame


class PlotWindow:
    """
    PlotWindow class for visualizing various charts related to the dataset in the MelodyMetrics application.

    This class manages the creation of a separate top-level window where the user can interact with different
    types of plots generated from the dataset. It provides buttons for generating and displaying multiple
    plot types (bar charts, pie charts, line charts), allowing users to explore the dataset visually.

    Methods
    -------
    __init__(master)
        Initializes the PlotWindow class with the main window reference.
    create_widgets()
        Creates and organizes widgets for the plot window, including buttons for each type of plot.
    obtain_da_from_main_window(dataanalysis)
        Receives the DataAnalysis instance from the main window to get the plotting data/figures.
    button_plot_most_frequent_genres_bar_action()
        Generates and displays a bar chart of the most frequent genres in the dataset.
    button_plot_most_frequent_genres_barpie_action()
        Generates and displays a pie chart (or bar-of-pie chart) of the most frequent genres.
    button_plot_top_genres_evolution_action()
        Generates and displays a line chart showing the evolution of the top three genres over time.
    button_plot_explicit_songs_evolution_action()
        Generates and displays a line chart showing the evolution of explicit songs in the top charts.
    """

    def __init__(self, master):
        """
        Initializes the PlotWindow class.

        Parameters
        ----------
        master : Tk
            The main window of the application to which the plot window will be attached.

        Attributes
        ----------
        master : Tk
            The main Tkinter window (root window).
        chart_window : Toplevel
            The top-level window that will contain the plot and the widgets.
        frame : Frame
            The frame within the top-level window that will hold the plot.
        da : DataAnalysis
            Instance of the DataAnalysis class for generating plots based on the dataset.
        """
        self.master = master
        self.chart_window = None  # Will hold the Toplevel window
        self.frame = None  # Frame for chart

        self.da = None

    def create_widgets(self):
        """
        Creates and organizes widgets for the plot window.

        This method creates a new top-level window and organizes buttons in a grid layout.
        The buttons allow the user to interact with different plot types (bar charts, pie charts, line charts).
        """
        # Create the top-level window
        self.chart_window = tk.Toplevel(self.master)
        self.chart_window.title("MelodyMetrics plot visualization")
        self.chart_window.geometry("1000x650")

        # Configure the style for TButton
        style = ttk.Style(self.chart_window)
        style.configure("TButton", font=("Arial", 12), padding=5)

        # Create the main grid layout
        self.chart_window.grid_rowconfigure(0, weight=1)  # Frame row
        self.chart_window.grid_columnconfigure(0, weight=1)  # Frame column

        # Create a frame for the chart
        self.frame = ttk.Frame(self.chart_window, padding=5, relief=tk.SUNKEN)
        self.frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Allow the frame to expand
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Add buttons
        self.button_plot_most_frequent_genres_bar = ttk.Button(self.chart_window,
                                                               text="1. Open plot: Most frequent genres (Bar chart)",
                                                               style="TButton",
                                                               command=self.button_plot_most_frequent_genres_bar_action)
        self.button_plot_most_frequent_genres_barpie = ttk.Button(self.chart_window,
                                                                  text="2. Open plot: Most frequent genres (Bar of pie chart)",
                                                                  style="TButton",
                                                                  command=self.button_plot_most_frequent_genres_barpie_action)
        self.button_plot_top_genres_evolution = ttk.Button(self.chart_window,
                                                           text="3. Open plot: Evolution of top three genres over time (Line chart)",
                                                           style="TButton",
                                                           command=self.button_plot_top_genres_evolution_action)
        self.button_plot_explicit_songs_evolution = ttk.Button(self.chart_window,
                                                               text="4. Open plot: Evolution of explicit songs in the top charts (Line chart)",
                                                               style="TButton",
                                                               command=self.button_plot_explicit_songs_evolution_action)
        self.button_plot_most_frequent_genres_bar.grid(row=1, column=0, columnspan=2, padx=15, pady=10, sticky="ew")
        self.button_plot_most_frequent_genres_barpie.grid(row=1, column=2, columnspan=2, padx=15, pady=10, sticky="ew")
        self.button_plot_top_genres_evolution.grid(row=2, column=0, columnspan=2, padx=15, pady=10, sticky="ew")
        self.button_plot_explicit_songs_evolution.grid(row=2, column=2, columnspan=2, padx=15, pady=10, sticky="ew")

    def obtain_da_from_main_window(self, dataanalysis):
        """
        Receives and stores an instance of the DataAnalysis class from the main window.

        This method links the `DataAnalysis` object passed from the main window to the plot window,
        enabling the plot window to generate charts using data from that object.

        Parameters
        ----------
        dataanalysis : DataAnalysis
            The DataAnalysis instance that holds the dataset and methods for creating plots.
        """

        if isinstance(dataanalysis.df, DataFrame):
            self.da = dataanalysis
        else:
            raise TypeError(
                "The provided object must be a DataAnalysis object to the plot window for the data analysis.")

    def button_plot_most_frequent_genres_bar_action(self):
        """
        Action triggered by the 'Open plot: Most frequent genres (Bar chart)' button.

        This method generates and displays a bar chart of the most frequent genres from the dataset.
        """
        # Get the fig of the plot
        fig = self.da.plot_most_frequent_genres(plt_show=False)

        # Remove any existing canvas
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Load the chart to the canvas
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def button_plot_most_frequent_genres_barpie_action(self):
        """
        Action triggered by the 'Open plot: Most frequent genres (Bar of pie chart)' button.

        This method generates and displays a pie chart (or bar of pie chart) of the most frequent genres.
        """
        # Get the fig of the plot
        fig = self.da.plot_most_frequent_genres_pie(plt_show=False)

        # Remove any existing canvas
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Load the chart to the canvas
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def button_plot_top_genres_evolution_action(self):
        """
        Action triggered by the 'Open plot: Evolution of top three genres over time' button.

        This method generates and displays a line chart showing the evolution of the top three genres over time.
        """
        # Get the fig of the plot
        fig = self.da.plot_top_genres_evolution(plt_show=False)

        # Remove any existing canvas
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Load the chart to the canvas
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def button_plot_explicit_songs_evolution_action(self):
        """
        Action triggered by the 'Open plot: Evolution of explicit songs in the top charts' button.

        This method generates and displays a line chart showing the evolution of explicit songs in the top charts.
        """
        # Get the fig of the plot
        fig = self.da.plot_explicit_songs_evolution(plt_show=False)

        # Remove any existing canvas
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Load the chart to the canvas
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
