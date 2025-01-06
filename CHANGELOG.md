# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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