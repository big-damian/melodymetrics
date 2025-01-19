# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

- ## [1.0.3] - 2025-01-19 - Final version patched for a better dataset download and DataAnalysis standalone usage
  - Added UML to README.md 
  - Added UML and Dataset Excel file to git
  - Patched kaggle_download.py to download to resources if exists

- ## [1.0.2] - 2025-01-19 - Small download dataset fix patch
  - Fixed dataset_download and find_dataset_csv to download and read from anywhere
    - Added regex to identify file in directories

- ## [1.0.1] - 2025-01-19 - First final version patched find dataset method
  - Fixed find_dataset_csv method to search in melodymetrics directory
  - Redacted basic version of README.md
  - Removed example code from data_analysis.py

- ## [1.0.0] - 2025-01-19 - First final version
  - Removed unnecessary TODO's
  - Added button and functionality to go back to see the actual dataframe
  - Fixed error when trying to load a dataset file when no file is in directories and added DatasetFileNotFoundException custom exception
  - Fixed download kaggle dataset functionality
  - Added all docstrings and comments
  - Removed unused methods 'drop_duplicates' and 'clean_dataset'
  - Fixed clean_outliers_and_duplicates method
  - Fixed split genre bug, calling method more than once works now
  - Cleaned code
  - Refactored 'find outliers' button and method to 'clean outliers and duplicates' implementing said functionality
  - New style for red color to plot window button
  - Merged branch of LabelFrames redesign to 'master' (Added grouping to buttons and new layout)
  - Updated the 'check outliers' method to check for outliers in 'year' and in 'popularity' columns
  - Updated the 'check outliers' method to remove said outliers
  - Updated plot window button layout and adjusted for same window size
  - Implemented last plot explicit_songs_evolution (method and window button)
  - Integrated top three genres over time into plot window
  - Finished the code for the 'genre evolution over time' plot
  - Fixed barpie plot not separating genres correctly
  - Added index feature to dataframe display
  - Added method of plot_window to receive the dataanalysis object from the main window
  - Improved the check_if_dataframe_loaded method of main_window class
  - Added buttons to plot window

- ## [0.5.0] - 2025-01-11 - App looks pretty good. New window with bar of pie plot!
  - Added numpy to requirements.txt
  - Made a super cool Bar of pie chart for the most popular genre
  - Added Show dataframe info method and button
  - Big commit:
    - Added show_dataframe_info method
    - Added check for genre outliers
    - Added method to show most frequent genre plot
    - Modified plot_window.py load_chart method 
  - Improved main module Docstring
  - Added sample readme.md
  - Improved main module
  - Added setter and deleter methods for df in dataanalysis
  - Added new plot visualization window
    - Improved df getter method
    - Added check outliers
    - Fixed main window close button
    - Updated requirements.txt (matplotlib~=3.8.0)
  - Formatted .py files with PyCharm's help
  - Renamed script files to complain with PEP8 (added underscores)
  - Renamed custom_exceptions.py to exceptions.py 
  - Updated all CHANGELOG up to here and gitignore to ignore dist files (.eggs folder)

- ## [0.4.1] - 2025-01-06 - App working good, adheres to school reqs and first .whl file
  - Added License text
  - Fixed small errors in requirements
  - Renamed .bumpversion.cfg to original name setup.cfg
  - Made plenty of small changes and fixes for the project to adhere to school project requirements
    - Fixed requirements.txt
    - Optimized imports
    - Changed python version to 3.10
    - Updated gitignore
    - Need to update CHANGELOG.md

- ## [0.4.0] - 2025-01-05 - App now works pretty good
  To run the app download the code and run the main.py file (no .whl file yet)
  - Added three new buttons:
    - describe_columns
    - show_dataframe_statistics
    - find_dataset_duration
    - Made lots of fixes to window
  - Added:
    - custom_exceptions.py file
    - Implemented DatasetNotLoadedException
    - Made many fixes on main window and data analysis
  - New functionality and button:
    - Separate genres
    - Important changes to main window
    - Added one custom exception

- ## [0.3.0] - 2025-01-03 - App starts looking good and has good functionality
  Main window has now five working buttons and working displays.
  - New buttons and analysis functionalities added:
    - Check number of null values method and button
    - Check if any null values method and button
    - Check number of unique values method and button
    - Add a 'time ago' column method and button
    - Extra: Added gitignore file
    - Also made some fixes
  - New window layout method, changed from pack to grid

- ## [0.2.0] - 2024-12-31 - Main window opening, downloading dataframe and loading it to the window.
  - Added getter for _df property of DataAnalysis class
  - Fixed download errors and couple more fixes
  - Added buttons and dataset loading functionality on main window
  - Added console display to window and fixed errors
    - If dataframe not correctly loaded the table will still display
  - Fixed error, window couldn't be created if dataframe null
  - Added Data Analysis class, added methods to find and load the csv to a pandas dataframe
  - Improved main window to show a table with dataframe contents

- ## [0.1.0] - 2024-12-25
  - Finished method to download dataset from kaggle and bumped code version
  - Added new class to download dataset from Kaggle and updated requirements_dev
  - Added main module file, and first package that creates main mockup window

- ## [0.0.0] - 2024-12-24 - Initial version
  Created project template and added basic project files.