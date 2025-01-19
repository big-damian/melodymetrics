"""
Music Dataset Analysis Module
=============================

This module provides a set of methods to analyze and visualize the dataset.
It includes all functionalities: cleaning, transforming, and extracting plots.

Classes and Methods
-------------------
The module primarily operates on a DataFrame loaded into the `_df` attribute of the class.
To load the dataframe, there is a method called 'find_dataset_csv' and another called 'load_csv_dataset'
that automate the process.
Before using most methods, ensure that the DataFrame is properly loaded or exceptions will raise.

Key Methods:
    - `check_num_unique_values`: Check the number of unique values for each column.
    - `drop_duplicates`: Remove duplicate rows from the dataset.
    - `add_years_ago_column`: Add a column representing the number of years ago each entry occurred.
    - `convert_duration_to_minutes`: Convert song duration from milliseconds to minutes.
    - `separate_genres`: Split the genre column into main genres and subgenres.
    - `find_dataset_duration`: Calculate the time span of the dataset based on years.
    - `clean_dataset`: Perform dataset cleaning operations (method implementation pending).
    - `plot_most_frequent_genres`: Generate a bar chart of the most frequent genres.
    - `plot_most_frequent_genres_pie`: Create a pie chart and bar plot to show genre distribution.
    - `plot_top_genres_evolution`: Plot the evolution of the top 3 genres over time.
    - `plot_explicit_songs_evolution`: Plot the evolution of explicit songs over time.

Usage
-----
1. Load a DataFrame into the `_df` attribute of the class using the setter method or 'load_csv_dataset'.
2. Call the desired methods to analyze or transform the dataset.
3. Use the plotting methods to generate visual insights.

Dependencies
------------
This module relies on the following Python libraries:
    - pandas (`pd`): Data manipulation and analysis.
    - numpy (`np`): Numerical operations.
    - matplotlib.pyplot (`plt`): Visualization.
    - matplotlib.cm (`cm`): Color mapping for plots.
    - datetime (`dt`): Date and time operations.
    - matplotlib.patches.ConnectionPatch: For connecting pie and bar chart components.

Example
-------
Below is an example of how to use this module:

```python
# Assume 'df' is a pandas DataFrame containing the music dataset.

# Initialize the class with the dataset.
analysis = MusicDatasetAnalyzer()
analysis._df = df  # Load the DataFrame.

# Check unique values in the dataset.
unique_values_df = analysis.check_num_unique_values()

# Add a 'years_ago' column.
analysis.add_years_ago_column()

# Plot the evolution of the top 3 genres.
analysis.plot_top_genres_evolution(plt_show=True)
"""

import datetime as dt
import os

import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch

from melodymetrics.exceptions import DatasetNotLoadedException, DatasetFileNotFoundException


class DataAnalysis:
    """
    The class for analyzing and visualizing the Spotify top hits dataset.

    This class provides methods for cleaning, transforming, and visualizing music data in a pandas DataFrame. Key functionalities include:
    - Data cleaning: Removing duplicates, adding time-based columns.
    - Data transformation: Converting durations, separating genres.
    - Analysis: Checking unique values, calculating dataset time span.
    - Visualizations: Plotting genre distribution, top genres evolution, and explicit songs trends.

    The dataset should be loaded into the '_df' attribute before use (through 'load_csv_dataset' or setter method).

    Dependencies:
    - pandas, numpy, matplotlib, datetime

    Example usage:
    - Load dataset with 'load_csv_dataset' or with setter method.
    - Perform analysis and plotting (e.g., 'check_num_unique_values', 'plot_top_genres_evolution').
    """

    def __init__(self, load_dataset=True, print_preview=False):
        """
        Initialize the DataAnalysis class.

        Parameters
        ----------
        load_dataset : bool, optional
            If True, loads the dataset CSV file on initialization (default is True).
        print_preview : bool, optional
            If True, prints the first 5 rows of the dataset upon loading (default is False).
        """
        self.csv_path = None
        self._df = None

        if load_dataset:
            if print_preview:
                print(self.load_csv_dataset())
            else:
                self.load_csv_dataset()

    @property
    def df(self):
        """
        Get the dataframe.

        Returns
        -------
        pd.DataFrame
            The loaded dataset.
        """
        try:
            self.check_if_dataframe_loaded()
        except DatasetNotLoadedException as e:
            print(f"Error: {e}")
            return pd.DataFrame({"No dataframe loaded yet.": [
                "No dataframe loaded yet."]})
        else:
            return self._df

    @df.setter
    def df(self, new_df):
        """
        Set a new dataframe.

        Parameters
        ----------
        new_df : pd.DataFrame
            The new dataframe to set.
        """
        if isinstance(new_df, pd.DataFrame):
            print(f"DataFrame has been replaced from {self._df.head(2)} to {new_df.head(2)}")
            self._df = new_df
        else:
            try:
                raise TypeError("Can't set a value that is not a DataFrame.")
            except TypeError as e:
                print(f"Error: {e}")

    @df.deleter
    def df(self):
        """
        Delete the dataframe.
        """
        print("DataFrame attribute has been removed.")
        self._df = None

    def __str__(self):
        """
        Return the string representation of the dataframe.

        Returns
        -------
        str
            The first 5 rows of the dataframe as a string.
        """
        self.check_if_dataframe_loaded()
        return self._df.head().to_string()

    def find_dataset_csv(self):
        """
        Find the dataset CSV file in the project directory.

        Returns
        -------
        str or None
            The path to the first CSV file found, or None if no CSV file is found.
        """
        project_directory = os.path.dirname(os.getcwd())

        # Cycle through the different directories and files
        for root, _, files in os.walk(project_directory):
            # Skip .venv .git and .idea directories
            if "melodymetrics\\." in root:
                continue
            for file in files:
                if file.endswith(".csv"):
                    self.csv_path = os.path.join(root, file)
                    print(f"Found dataset csv at {self.csv_path}")
                    return self.csv_path
        print("No csv file found in melodymetrics folder")
        raise DatasetFileNotFoundException

    def load_csv_dataset(self, print_preview=False):
        """
        Load the dataset CSV file into the dataframe.

        Parameters
        ----------
        print_preview : bool, optional
            If True, prints the first 5 rows of the dataset (default is False).

        Returns
        -------
        pd.DataFrame or str
            The first 5 rows of the dataframe or an error message.
        """
        try:
            # Construct the file path
            file_path = self.find_dataset_csv()

            # Read the CSV file
            self._df = pd.read_csv(file_path)

            # Return the first few rows for verification
            if print_preview:
                print(self._df.head())

            return self._df.head()

        except DatasetFileNotFoundException as e:
            print(f"Error: {e}")
            return f"Error: {e}"

    def check_if_dataframe_loaded(self):
        """
        Check if the dataframe is loaded.

        Raises
        ------
        DatasetNotLoadedException
            If the dataframe is not loaded.
        """
        if self._df is None:
            print("Error: No dataset loaded yet. Please load the dataset first")
            raise DatasetNotLoadedException

    @staticmethod
    def explain_dataframe_columns():
        """
        Generate and display a hardcoded dataframe describing the dataset columns.

        Returns
        -------
        pd.DataFrame
            A dataframe containing column names and their descriptions.
        """
        explanatory_dataframe = pd.DataFrame({
            "Attribute": [
                "artist",
                "song",
                "duration_ms",
                "explicit",
                "year",
                "popularity",
                "danceability",
                "energy",
                "key",
                "loudness",
                "mode",
                "speechiness",
                "acousticness",
                "instrumentalness",
                "liveness",
                "valence",
                "tempo",
                "genre"
            ],
            "Description": [
                "Name of the Artist.",
                "Name of the Track.",
                "Duration of the track in milliseconds.",
                "Indicates if content is offensive or unsuitable for children.",
                "Release Year of the track.",
                "Popularity of the track (higher value = more popular).",
                "Describes how suitable a track is for dancing (0.0 to 1.0).",
                "A measure of intensity and activity (0.0 to 1.0).",
                "The key the track is in, mapped using Pitch Class notation.",
                "The overall loudness of a track in decibels (dB).",
                "Modality of a track: major (1) or minor (0).",
                "Detects the presence of spoken words in a track.",
                "Confidence measure of whether a track is acoustic (0.0 to 1.0).",
                "Predicts if a track contains no vocals (closer to 1.0 = instrumental).",
                "Detects the presence of an audience in the recording.",
                "Describes the musical positiveness of a track (0.0 to 1.0).",
                "The estimated tempo of a track in beats per minute (BPM).",
                "Genres of the track."]})
        print(f"Dataframe columns explanation:\n{explanatory_dataframe.to_string()}")
        return explanatory_dataframe

    def show_dataframe_info(self):
        """
        Display dataframe shape and column data types.

        Returns
        -------
        pd.DataFrame
            A dataframe showing rows, columns, and data types.
        """
        self.check_if_dataframe_loaded()

        # Create a DataFrame with the shape information
        shape_info = {"Rows": str(self._df.shape[0]), "Columns": str(self._df.shape[1]), "|": "|"}
        shape_df = pd.DataFrame([shape_info])

        # Get the dtypes and convert to DataFrame
        dtypes_df = pd.DataFrame(self._df.dtypes).reset_index()
        dtypes_df.columns = ["Column Name", "Dtype"]  # Renaming the columns for clarity

        # Add the "|" column for a separator
        dtypes_df["|"] = "|"

        # Concatenate the shape_df with the dtypes_df
        result_info_df = pd.concat([shape_df, dtypes_df], ignore_index=True)

        # Replace any NaN values with an empty string
        result_info_df = result_info_df.fillna("")

        print(result_info_df)
        return result_info_df

    def summarize_dataframe_statistics(self):
        """
        Generate summary statistics for the dataframe.

        Returns
        -------
        pd.DataFrame
            A transposed dataframe of summary statistics.
        """
        self.check_if_dataframe_loaded()

        # Prints summary statistics for all columns (numerical and categorical), transposes the DataFrame, and resets the index to display the statistics as columns.
        print(self._df.describe(include="all").T.reset_index())
        return self._df.describe(include="all").T.reset_index()

    def check_num_null_values(self):
        """
        Count the number of null values in the dataframe.

        Returns
        -------
        int
            Total number of null values in the dataframe.
        """
        self.check_if_dataframe_loaded()
        num_null_values = self._df.isnull().values.sum()
        print(f"Total null values in dataframe: {num_null_values}")
        return num_null_values

    def check_any_null_values(self):
        """
        Check for null values in each dataframe column.

        Returns
        -------
        pd.DataFrame
            A dataframe showing whether each column has null values.
        """
        self.check_if_dataframe_loaded()
        any_null_values_df = self._df.isnull().any().to_frame(
            name="Any null values in dataframe columns?").reset_index()
        any_null_values_df.rename(columns={"index": "Column name"}, inplace=True)

        print(any_null_values_df)
        return any_null_values_df

    def clean_outliers_and_duplicates(self):
        """
        Searches and cleans outliers and duplicate rows in the dataframe.

        Returns
        -------
        pd.DataFrame
            A dataframe containing outliers and duplicates, if any, or a dataframe
            with a message indicating no outliers found.
        """
        # Ensure the DataFrame is loaded
        self.check_if_dataframe_loaded()

        # List of columns to check for outliers
        columns_to_check = ["danceability", "energy", "speechiness", "acousticness", "instrumentalness", "liveness",
                            "valence"]

        # Dictionary to store outliers for each column
        outliers = {}

        # List to accumulate outlier rows for all columns
        all_outliers = []

        # Check for values outside the range [0, 1] in the specified columns
        for column in columns_to_check:
            outlier_rows = self._df[(self._df[column] < 0) | (self._df[column] > 1)]
            outliers[column] = outlier_rows

            # Add outlier rows to the list of all outliers
            if not outlier_rows.empty:
                all_outliers.append(outlier_rows)

        # Check any outliers in year
        outlier_rows = self._df[(self._df["year"] > int(dt.date.today().year)) | (self._df["year"] < 1900)]
        outliers["year"] = outlier_rows
        if not outlier_rows.empty:
            all_outliers.append(outlier_rows)

        # Check any outliers in popularity
        outlier_rows = self._df[(self._df["popularity"] > 100) | (self._df["popularity"] < 0)]
        outliers["popularity"] = outlier_rows
        if not outlier_rows.empty:
            all_outliers.append(outlier_rows)

        # Check any outliers in genre
        outlier_rows = self._df[self._df["genre"] == "set()"]
        outliers["genre"] = outlier_rows
        if not outlier_rows.empty:
            all_outliers.append(outlier_rows)

        # Print the results for each column
        for column, outlier_rows in outliers.items():
            if not outlier_rows.empty:
                print(f"Outliers detected in column '{column}':")
                print(outlier_rows)
            else:
                print(f"No outliers detected in column '{column}'.")

        # Check for duplicates
        duplicate_rows = self._df[self._df.duplicated()]

        # Print duplicate rows if any
        if not duplicate_rows.empty:
            print("\nDuplicates detected:")
            print(duplicate_rows)

        # Combine all outlier and duplicate rows into a single DataFrame (if any)
        all_outliers_and_duplicates = all_outliers.copy()  # Copy the outliers list

        # Append duplicates if any
        if not duplicate_rows.empty:
            all_outliers_and_duplicates.append(duplicate_rows)

        # Check if there are any outliers or duplicates to return
        if all_outliers_and_duplicates:
            # Concatenate all outliers and duplicates into one DataFrame
            all_outliers_df = pd.concat(all_outliers_and_duplicates,
                                        ignore_index=False)  # Ignore index False to keep the original indices
            print("\nOutliers and duplicates across all columns:")
            print(all_outliers_df)

            # Drop the outlier and duplicate rows from the original DataFrame using their indices
            self._df = self._df.drop(all_outliers_df.index).reset_index(drop=True)
            print("\nThese outliers and duplicates have been removed from the DataFrame.")
            return all_outliers_df  # Return the DataFrame containing all outliers and duplicates
        else:
            print("\nNo outliers or duplicates detected in any of the columns.")
            return pd.DataFrame({"No outliers or duplicates detected in any of the columns.": [
                "No outliers or duplicates detected in any of the columns."]})  # Return an empty DataFrame if no outliers or duplicates were found

    def check_num_unique_values(self):
        """
        Checks and displays the number of unique values in each column of the dataframe.

        Returns
        -------
        pd.DataFrame
            A dataframe containing column names and their respective count of unique values.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()
        unique_counts = []

        for column in self._df.columns:
            # Calculate the number of unique values in the column
            unique_count = len(self._df[column].unique())
            # Create a tuple with the column name and the number of unique values
            column_info = (column, unique_count)
            # Add the tuple to the list
            unique_counts.append(column_info)

        # Convert the list of tuples into a DataFrame
        unique_values_df = pd.DataFrame(unique_counts, columns=["Column name", "Unique values"])

        print(unique_values_df)
        return unique_values_df

    def add_years_ago_column(self):
        """
        Adds a column to the object dataframe indicating the difference in years from the current year of the 'year' column.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()

        def get_years_ago(row):
            # Get the current year
            current_year = dt.datetime.now().year

            # Calculate the difference using the row's year value
            time_ago = current_year - row["year"]
            return time_ago

        # Apply the function to calculate years ago for each row
        self._df["years_ago"] = self._df.apply(get_years_ago, axis=1)
        print(self._df)

    def convert_duration_to_minutes(self):
        """
        Converts the 'duration_ms' column from milliseconds to minutes and renames it to 'duration_minutes'.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()

        # Convert milliseconds to seconds and apply lambda to return the float with one decimal
        self._df["duration_ms"] = (self._df["duration_ms"] / 60000).apply(lambda x: float(f"{x:.1f}"))
        # Rename the column
        self._df.rename(columns={"duration_ms": "duration_minutes"}, inplace=True)

        print(self._df)

    def separate_genres(self):
        """
        Splits the 'genre' column into 'genre' and 'subgenres' columns.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()

        def split_genre(row):
            parts = row.split(sep=", ", maxsplit=1)  # Split by ", "
            # Handle cases where there might not be a subgenre
            if len(parts) >= 2:
                return parts[0], parts[1]  # Main genre and subgenre
            else:
                return parts[0], None  # Only main genre

        # Check if the 'subgenres' column already exists
        if 'subgenres' not in self._df.columns:
            self._df[["genre", "subgenres"]] = self._df["genre"].apply(split_genre).apply(pd.Series)
        else:
            print("Genres already split between genre and subgenre column. Nothing to do.")

        print(self._df)

    def find_dataset_duration(self):
        """
        Calculates and displays the duration of the dataset in terms of years.

        Returns
        -------
        pd.DataFrame
            A dataframe containing the start year, end year, and duration.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()

        # Extract the start and end dates
        start_date = self._df["year"].min()
        end_date = self._df["year"].max()

        # Calculate the duration
        duration = end_date - start_date

        # Print the results
        print(f"Start Year: {start_date} \nEnd Year: {end_date} \nDuration: {duration} years")
        return pd.DataFrame({
            "Dataframe duration": [
                f"Start Year: {start_date}",
                f"End Year: {end_date}",
                "-o-",
                f"Duration: {duration} years"
            ]})

    def plot_most_frequent_genres(self, plt_show):
        """
        Plots a bar chart of the most popular genres.

        Parameters
        ----------
        plt_show : bool
            Whether to display the plot for text use.

        Returns
        -------
        matplotlib.figure.Figure
            The figure object containing the plot for the graphic interface.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()

        # Separate genres again, in case they haven't been separated before
        genres = self._df["genre"].str.split(", ").explode()  # Split and "explode" genres
        genre_counts = genres.value_counts()

        # Create a plot
        fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axes
        genre_counts.plot(kind="bar", color="skyblue", edgecolor="black", ax=ax)  # Plot on the axes
        ax.set_title("Most frequent genres", fontsize=16)
        ax.set_xlabel("Genre", fontsize=14)
        ax.set_ylabel("Count", fontsize=14)
        ax.tick_params(axis="x", rotation=45)
        plt.tight_layout()  # Adjust layout

        if plt_show:
            plt.show()

        return fig  # Return the figure object

    def plot_most_frequent_genres_pie(self, plt_show):
        """
        Plots a pie chart of the most popular/frequent genres with a breakdown of less popular genres.

        Parameters
        ----------
        plt_show : bool
            Whether to display the plot for text use.

        Returns
        -------
        matplotlib.figure.Figure
            The figure object containing the plot for the graphic interface.

        Raises
        ------
        ValueError
            If the dataframe is not loaded.
        """
        self.check_if_dataframe_loaded()

        # Separate genres and count their occurrences keeping only the main genre
        genres = self._df["genre"].str.split(",").str[0]  # Split by comma and get the first element
        genres = genres.str.strip()  # Remove any leading or trailing whitespace
        genre_counts = genres.value_counts()  # Count occurrences of main genres

        # Separate the top 4 genres and group the rest into "Others"
        top_genres = genre_counts.head(4)
        others = genre_counts.iloc[4:]
        genre_counts_other = pd.concat([top_genres, pd.Series({'Others': others.sum()})])

        # Create figure and axes for both plots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))  # Increase figure size for better spacing
        fig.subplots_adjust(wspace=-0.5)  # Reduce space between the pie and bar chart and add right margin

        # Pie chart parameters
        pie_data = genre_counts_other
        labels = pie_data.index
        ratios = pie_data.values
        explode = [0.1 if i == len(ratios) - 1 else 0 for i in range(len(ratios))]  # Explode the "Others" slice
        angle = 10  # Rotate the pie chart

        # Plot the pie chart with exploded "Others" slice
        wedges, *_ = ax1.pie(ratios, autopct='%1.1f%%', startangle=angle, labels=labels, explode=explode)

        # Move the pie chart up and make it bigger
        ax1.set_position([0.1, 0.45, 0.35, 0.6])  # Adjust position and size of the pie chart

        # Bar chart parameters (exploded "Others" breakdown)
        if 'Others' in genre_counts_other.index:
            # Break down the "Others" genre
            exploded_genre_data = genres[~genres.isin(top_genres.index)].value_counts()

            # Define colors for the bars

            colors = cm.get_cmap('Paired')(np.linspace(0, 1, len(exploded_genre_data)))

            # Bar chart for the breakdown of the exploded "Others" genre
            bar_height = 0  # Start from zero
            total_height = sum(exploded_genre_data.values)  # Calculate the total height of the bars

            for j, (height, label) in enumerate(
                    reversed([*zip(exploded_genre_data.values, exploded_genre_data.index)])):
                bc = ax2.bar(0, height, width=0.2, bottom=bar_height, color=colors[j], label=label)
                ax2.bar_label(bc, labels=[f"{height / total_height:.1%}"], label_type='center')
                bar_height += height  # Increment bar height

            ax2.set_title(f'Breakdown of "Others" Genre')
            handles, labels = ax2.get_legend_handles_labels()  # Get handles and labels
            ax2.legend(reversed(handles), reversed(labels))  # Reverse the order of the legend
            ax2.axis('off')
            ax2.set_xlim(-2.5 * 0.2, 2.5 * 0.2)  # Ensure bars fit properly in the x-axis

            # Use ConnectionPatch to draw lines between the pie and bar chart
            theta1, theta2 = wedges[-1].theta1, wedges[-1].theta2  # "Others" slice
            center, r = wedges[-1].center, wedges[-1].r

            # Draw top connecting line
            x = r * np.cos(np.pi / 180 * theta2) + center[0]
            y = r * np.sin(np.pi / 180 * theta2) + center[1]
            con = ConnectionPatch(xyA=(-0.2 / 2, total_height), coordsA=ax2.transData,
                                  xyB=(x, y), coordsB=ax1.transData)
            con.set_color((0, 0, 0))
            con.set_linewidth(4)
            ax2.add_artist(con)

            # Draw bottom connecting line
            x = r * np.cos(np.pi / 180 * theta1) + center[0]
            y = r * np.sin(np.pi / 180 * theta1) + center[1]
            con = ConnectionPatch(xyA=(-0.2 / 2, 0), coordsA=ax2.transData,
                                  xyB=(x, y), coordsB=ax1.transData)
            con.set_color((0, 0, 0))
            ax2.add_artist(con)
            con.set_linewidth(4)

        plt.tight_layout()  # Adjust layout to prevent overlap
        fig.suptitle('Most Frequent Main Genres Bar of Pie chart', fontsize=16)  # Add main title

        if plt_show:
            plt.show()

        return fig  # Return the figure object

    def plot_top_genres_evolution(self, plt_show):
        """
        Plot the evolution of the top 3 most frequent genres over time.

        Parameters
        ----------
        plt_show : bool
            Whether to display the plot for text use.

        Returns
        -------
        matplotlib.figure.Figure
            The figure object containing the plot for the graphic interface.
        """
        self.check_if_dataframe_loaded()

        # Prepare data for plotting
        self._df['year'] = self._df['year'].astype(int)
        genres = self._df["genre"].str.split(",").str[0].str.strip()
        top_genres = genres.value_counts().head(3).index
        filtered_data = self._df[self._df["genre"].str.split(",").str[0].str.strip().isin(top_genres)]
        genre_year_counts = filtered_data.groupby(["year", "genre"]).size().unstack(fill_value=0)

        # Sort genres to maintain consistent color order
        genre_year_counts = genre_year_counts[top_genres]

        # Remove years where all genres have low counts
        genre_year_counts = genre_year_counts.loc[(genre_year_counts > 4).any(axis=1)]

        # Plot line chart
        fig, ax = plt.subplots(figsize=(10, 6))
        genre_year_counts.plot(ax=ax, linewidth=2)

        # Set x-axis ticks for each year with a range rotated 45 degrees
        ax.set_xticks(range(genre_year_counts.index.min(), genre_year_counts.index.max() + 1))
        ax.tick_params(axis='x', rotation=45)

        # Set titles and labels
        ax.set_title('Top 3 Genres Evolution Over Time (Line Chart)', fontsize=16)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Number of Songs', fontsize=12)
        ax.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

        # Adjust layout
        plt.tight_layout()

        if plt_show:
            plt.show()

        # Debug
        # print(genre_year_counts.tail(10))
        # print("---")
        # print(self._df[self._df["year"] >= 2020])

        return fig

    def plot_explicit_songs_evolution(self, plt_show):
        """
        Plot the evolution of the number of explicit songs over time.

        Parameters
        ----------
        plt_show : bool
            Whether to display the plot for text use.

        Returns
        -------
        matplotlib.figure.Figure
            The figure object containing the plot for the graphic interface.
        """
        # Ensure dataframe is loaded
        self.check_if_dataframe_loaded()

        # Prepare data for plotting
        self._df['year'] = self._df['year'].astype(int)

        # Count explicit songs by year
        explicit_year_counts = (
            self._df[self._df['explicit'] == True]
            .groupby('year')
            .size()
        )

        # Remove years with no explicit songs
        explicit_year_counts = explicit_year_counts[explicit_year_counts > 4]

        # Plot line chart
        fig, ax = plt.subplots(figsize=(10, 6))
        explicit_year_counts.plot(ax=ax, kind='line', linewidth=2, marker='o')

        # Set x-axis ticks for each year with a range rotated 45 degrees
        ax.set_xticks(range(explicit_year_counts.index.min(), explicit_year_counts.index.max() + 1))
        ax.tick_params(axis='x', rotation=45)

        # Set titles and labels
        ax.set_title('Evolution of Explicit Songs Over Time', fontsize=16)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Number of Explicit Songs', fontsize=12)

        # Adjust layout
        plt.tight_layout()

        if plt_show:
            plt.show()

        return fig


# Example usage:
# da = DataAnalysis(load_dataset=False)
# da.find_dataset_csv()
# da.load_csv_dataset()
# # da.check_num_null_values()
# # da.check_any_null_values()
# # da.check_num_unique_values()
# # da.separate_genres()
# # da.add_time_ago_column()
# # da.find_dataset_duration()
# # da.drop_duplicates()
# print(da)
# da.find_dataset_duration()
# da.convert_duration_to_minutes()
# print(da)
# # da.plot_most_frequent_genres()
#
# da = DataAnalysis(load_dataset=False)
# da.find_dataset_csv()
# da.load_csv_dataset()
# da.separate_genres()
# print(da.df["genre"].unique())
# print(da.df.info())
