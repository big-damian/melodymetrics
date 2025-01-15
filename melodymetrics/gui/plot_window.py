import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PlotWindow:
    def __init__(self, master):
        self.master = master
        self.chart_window = None  # Will hold the Toplevel window
        self.frame = None  # Frame for chart

        self.da = None

    def create_widgets(self):
        """Create and organize widgets for the plot window."""
        # Create the top-level window
        self.chart_window = tk.Toplevel(self.master)
        self.chart_window.title("MelodyMetrics plot visualization")
        self.chart_window.geometry("1000x710")

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

        # Add buttons
        self.button_plot_most_frequent_genres_bar = ttk.Button(self.chart_window, text="1. Open plot: Most frequent genres (Bar chart)", style="TButton",
                                                  command=self.button_plot_most_frequent_genres_bar_action)
        self.button_plot_most_frequent_genres_barpie = ttk.Button(self.chart_window,
                                                           text="2. Open plot: Most frequent genres (Bar of pie chart)",
                                                           style="TButton",
                                                           command=self.button_plot_most_frequent_genres_barpie_action)
        self.button_plot_top_genres_evolution = ttk.Button(self.chart_window,
                                                           text="3. Open plot: Evolution of top three genres over time (Line chart)",
                                                           style="TButton",
                                                           command=self.button_plot_top_genres_evolution_action)
        self.button_plot_most_frequent_genres_bar.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.button_plot_most_frequent_genres_barpie.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        self.button_plot_top_genres_evolution.grid(row=3, column=0, columnspan=2, padx=5, pady=10)



    def obtain_da_from_main_window(self, dataanalysis):
        self.da = dataanalysis
        # if isinstance(dataanalysis)
        #     self.da = dataanalysis
        # except DatasetNotLoadedException as e:
        #     print(f"Error: {e}")
        #     self.chart_window.quit()

    # TODO: Delete this (tras usarlo como ejemplo o lo que sea)
    # def create_chart(self):
    #     """Create a sample chart to display."""
    #     x = [1, 2, 3, 4, 5]
    #     y = [2, 3, 5, 7, 11]
    #     fig, ax = plt.subplots()
    #     ax.plot(x, y, marker='o', linestyle='-', color='b', label='Sample Data')
    #     ax.set_title('Sample Chart')
    #     ax.set_xlabel('X-axis')
    #     ax.set_ylabel('Y-axis')
    #     ax.legend()
    #     return fig

    def button_plot_most_frequent_genres_bar_action(self):
        """Load the provided chart into the frame."""
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
        """Load the provided chart into the frame."""
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
        """Load the provided chart into the frame."""
        # Get the fig of the plot
        fig = self.da.plot_top_genres_evolution(plt_show=False)

        # Remove any existing canvas
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Load the chart to the canvas
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
