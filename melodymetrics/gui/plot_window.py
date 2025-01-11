import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from melodymetrics.dataanalysis.data_analysis import DataAnalysis


class PlotWindow:
    def __init__(self, master):
        self.master = master
        self.chart_window = None  # Will hold the Toplevel window
        self.frame = None  # Frame for chart

    def create_widgets(self):
        """Create and organize widgets for the plot window."""
        # Create the top-level window
        self.chart_window = tk.Toplevel(self.master)
        self.chart_window.title("MelodyMetrics plot visualization")
        self.chart_window.geometry("600x450")

        # Configure the style for TButton
        style = ttk.Style(self.chart_window)
        style.configure("TButton", font=("Arial", 12), padding=5)

        # Create the main grid layout
        self.chart_window.grid_rowconfigure(0, weight=1)  # Frame row
        self.chart_window.grid_columnconfigure(0, weight=1)  # Frame column

        # Create a frame for the chart
        self.frame = ttk.Frame(self.chart_window, padding=5, relief=tk.SUNKEN)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Allow the frame to expand
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Add a styled button to load the chart
        button = ttk.Button(self.chart_window, text="Load Chart", style="TButton", command=self.load_chart)
        button.grid(row=1, column=0, pady=10)

    def create_chart(self):
        """Create a sample chart to display."""
        # TODO: Change this
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', linestyle='-', color='b', label='Sample Data')
        ax.set_title('Sample Chart')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.legend()
        return fig

    def load_chart(self):
        """Load the provided chart into the frame."""
        # Remove any existing canvas
        # TODO: Change this
        da = DataAnalysis()
        fig = da.plot_most_frequent_genres()
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Load the chart
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
