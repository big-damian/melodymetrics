MelodyMetrics
-------------
![Python](https://badgen.net/badge/python/3.10.11/cyan?icon=pypi)
![Version](https://img.shields.io/github/v/release/big-damian/melodymetrics)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)
<br>
<br>
MelodyMetrics is a user-friendly, interactive tool designed to analyse dataset data in a very simple and visual way 
simplify and enhance the process of analyzing and 
preprocessing music-related datasets. The app provides a range of Exploratory Data Analysis (EDA) and data preprocessing
functions, as well as chart to extract data conclusions. It allows users
to easily visualize, clean, and prepare datasets for further analysis.

## Features
- First Steps:
  - Download Kaggle Dataframe: Quickly download datasets from Kaggle for analysis.
  - Load Dataframe: Load existing datasets into the application to begin exploration.

- Data Preprocessing:
  - Check Nulls in Columns: Check for missing data across dataset columns.
  - Check Number of Unique Values: Identify the number of unique values in each column.
  - Separate Genres: Separate a composite genre column into distinct genre columns.
  - Add Years Ago Column: Add a new column representing the number of years since a specific date.

- Exploratory Data Analysis (EDA) Actions:
  - Describe Dataframe Columns: View detailed statistics and descriptions of each column in the dataset.
  - Show Dataframe Shape and Info: Display the shape and other essential information about the dataframe.
  - Show Dataframe Statistics: Get descriptive statistics for numerical columns in the dataframe.
  - Show Dataframe Duration: Calculate and display the duration for date-based columns in the dataset.
  - Find Outliers: Detect and highlight outliers in the dataset.
  - Open Plot Visualization Window: Launch an interactive window for visualizing and exploring data through plots.

- The app is built with a sleek, intuitive GUI, featuring:
  - LabelFrames that clearly group functions into meaningful categories, such as "First Steps," "Data Preprocessing," and "EDA Actions."
  - Buttons arranged logically within each section for easy access to various functions.
  - Resizable Layout that adapts to different screen sizes, ensuring that the interface remains usable even when the window is maximized.
  - A TreeView that displays the actual dataframe as table.
  - A console view to get detailed information of what is happening in the background

## Installation
First, download the latest wheel (`.whl`) file and install it with:

  ```bash
  pip install melodymetrics-X.X.X-py3-none-any.whl
  ```

- Option 1: Write this in a Python script:

  ```python
  from melodymetrics import main as melodymetrics
  melodymetrics.main()
  ```

- Option 2: Locate the installed package and open a terminal.

  Locate yourself in the `melodymetrics` directory and type in the terminal:

  ```bash
  python melodymetrics/main.py
  ```
Additionally you can use this provided Python notebook in Google Colab. Just upload the wheel .whl file and run the code of the notebook file to see the main data analysis features:
<br>
![Python data analysis notebook](melodymetrics/resources/MelodyMetrics_DataAnalysis_example_usage_notebook.ipynb)

## How to use the app
Once the application is launched, you will see a main window with the following sections:
  - First Steps: Start by downloading or loading a dataset.
  - Data Preprocessing: Clean and preprocess the dataset by checking for null values, unique values, and adding new features.
  - EDA Actions: Perform exploratory analysis on the dataset, including statistical summaries, detecting outliers, and more.
  - Plot visualisation: Open the plot window and click the buttons to see the charts over the processed data

## UML Diagram
![UML Diagram](melodymetrics/resources/uml/uml.jpg)

## Requirements
  - Python 3.10.11 or greater
  - tkinter for the graphical user interface (GUI)
  - pandas for dataframe operations
  - kagglehub to download the dataframe automatically
  - matplotlib for data visualization
  - numpy for calculations

Each button performs a specific task within these sections, allowing you to interactively explore and prepare your dataset for further analysis.

## Credits
- Tkinter: A Python library for creating graphical user interfaces, used for building the interactive front-end of this application.
- Pandas: A powerful data manipulation and analysis library, used for handling datasets.
- Matplotlib: A plotting library for creating visualizations of data, used for generating interactive plots and charts.
- Kaggle: Source of datasets used for testing and demonstrating the app's functionality.
- Font: Arial font used for the GUI text.
- CEI School 

### Owner
- Damian Peña damian.example@email.com
