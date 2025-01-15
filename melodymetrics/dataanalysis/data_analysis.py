import datetime as dt
import os

import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch

from melodymetrics.exceptions import DatasetNotLoadedException


class DataAnalysis:

    def __init__(self, load_dataset=True, print_preview=False):
        """
        Initialize the DataAnalysis class with the file name.
        :load_dataset (bool): If True, the app will load the dataset csv file.
        :print_preview (bool): If True and load_dataset True, the first five rows of the dataset will be printed.
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
        """Getter method for the dataframe (df)."""
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
        print("DataFrame attribute has been removed.")
        self._df = None

    def __str__(self):
        self.check_if_dataframe_loaded()
        return self._df.head().to_string()

    def find_dataset_csv(self):
        """
        Finds the dataset CSV file in the project directory or its subdirectories.
        :return: The path to the first CSV file, or None if no CSV file is found.
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
        print("No csv file found in project folder")
        return None

    def load_csv_dataset(self, print_preview=False):
        """
        Loads the dataset CSV file to the df variable.
        :return: The first 5 rows of the dataset or an error message if no CSV file is found.
        """
        try:
            # Construct the file path
            file_path = self.find_dataset_csv()

            # Read the CSV file
            self._df = pd.read_csv(file_path)

            # Return the first few rows for verification
            if print_preview:
                print(self._df.head())

            # TODO: Here I can enable the 'separate_genere' button again in case you load the dataframe again

            return self._df.head()
        except Exception as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"

    def check_if_dataframe_loaded(self):
        if self._df is None:
            print("Error: No dataset loaded yet. Please load the dataset first")
            raise DatasetNotLoadedException

    @staticmethod
    def explain_dataframe_columns():
        """
           Generate and display a hardcoded DataFrame describing/explaining the columns of the DataFrame that will be analyzed.

           Returns:
               pandas.DataFrame: A DataFrame containing the attribute names and their explanations.
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
                "Genre of the track."]})
        print(f"Dataframe columns explanation:\n{explanatory_dataframe.to_string()}")
        return explanatory_dataframe

    def show_dataframe_info(self):
        self.check_if_dataframe_loaded()

        # TODO: Cambiar los comentarios y nombres de variable
        # Create a DataFrame with the shape information (Rows and Columns as integers)
        shape_info = {"Rows": str(self._df.shape[0]), "Columns": str(self._df.shape[1]), "|": "|"}
        shape_df = pd.DataFrame([shape_info])

        # Get the dtypes and convert to DataFrame
        dtypes_df = pd.DataFrame(self._df.dtypes).reset_index()
        dtypes_df.columns = ["Column Name", "Dtype"]  # Renaming the columns for clarity

        # Add the "|" column to dtypes_df and fill it with "|"
        dtypes_df["|"] = "|"

        # Concatenate the shape_df with the dtypes_df
        final_info_df = pd.concat([shape_df, dtypes_df], ignore_index=True)

        # Replace any NaN values with an empty string
        final_info_df = final_info_df.fillna("")

        print(final_info_df)
        return final_info_df

    def summarize_dataframe_statistics(self):
        self.check_if_dataframe_loaded()

        # Prints summary statistics for all columns (numerical and categorical), transposes the DataFrame, and resets the index to display the statistics as columns.
        print(self._df.describe(include="all").T.reset_index())
        return self._df.describe(include="all").T.reset_index()

    def check_num_null_values(self):
        self.check_if_dataframe_loaded()
        num_null_values = self._df.isnull().values.sum()
        print(f"Total null values in dataframe: {num_null_values}")
        return num_null_values

    def check_any_null_values(self, return_df=False):
        self.check_if_dataframe_loaded()
        any_null_values_df = self._df.isnull().any().to_frame(
            name="Any null values in dataframe columns?").reset_index()
        any_null_values_df.rename(columns={"index": "Column name"}, inplace=True)

        print(any_null_values_df)
        return any_null_values_df

    def check_outliers_in_columns(self):
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

        # Check any outliers in genre
        outlier_rows = self._df[self._df["genre"] == "set()"]
        outliers["genre"] = outlier_rows
        all_outliers.append(outlier_rows)

        # Print the results for each column
        for column, outlier_rows in outliers.items():
            if not outlier_rows.empty:
                print(f"Outliers detected in column '{column}':")
                print(outlier_rows)
            else:
                print(f"No outliers detected in column '{column}'.")

        # Combine all outlier rows into a single DataFrame (if any)
        if all_outliers:
            all_outliers_df = pd.concat(all_outliers, ignore_index=True)
            print("\nOutliers across all columns:")
            print(all_outliers_df)
            return all_outliers_df  # Return the DataFrame containing all outliers
        else:
            print("\nNo outliers detected in any of the columns.")
            return pd.DataFrame({"No outliers detected in any of the columns.": [
                "No outliers detected in any of the columns."]})  # Return an empty DataFrame if no outliers were found


    def check_num_unique_values(self):
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

    def drop_duplicates(self):
        self.check_if_dataframe_loaded()
        pass

    def add_years_ago_column(self):
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
        self.check_if_dataframe_loaded()

        # Convert milliseconds to seconds and apply lambda to return the float with one decimal
        self._df["duration_ms"] = (self._df["duration_ms"] / 60000).apply(lambda x: float(f"{x:.1f}"))
        # Rename the column
        self._df.rename(columns={"duration_ms": "duration_minutes"}, inplace=True)

        print(self._df)

    def separate_genres(self):
        # TODO: Found bug, if trying to use this method more than once, all subgenres become None
        self.check_if_dataframe_loaded()

        def split_genre(row):
            parts = row.split(sep=", ", maxsplit=1)  # Split by ", "
            # Handle cases where there might not be a subgenre
            if len(parts) >= 2:
                return parts[0], parts[1]  # Main genre and subgenre
            else:
                return parts[0], None  # Only main genre

        self._df[["genre", "subgenres"]] = self._df["genre"].apply(split_genre).apply(pd.Series)
        print(self._df)

    def find_dataset_duration(self):
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

    def clean_dataset(self):
        pass

    def plot_most_frequent_genres(self, plt_show):
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

    def plot_top_genres_evolution(self, plt_show=True):
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

    def plot(self):
        # TODO: Think of the last idea
        pass




# Example usage:
da = DataAnalysis(load_dataset=False)
da.find_dataset_csv()
da.load_csv_dataset()
# da.check_num_null_values()
# da.check_any_null_values()
# da.check_num_unique_values()
# da.separate_genres()
# da.add_time_ago_column()
# da.find_dataset_duration()
# da.drop_duplicates()
print(da)
da.find_dataset_duration()
da.convert_duration_to_minutes()
print(da)
# da.plot_most_frequent_genres()

da = DataAnalysis(load_dataset=False)
da.find_dataset_csv()
da.load_csv_dataset()
da.separate_genres()
print(da.df["genre"].unique())
print(da.df.info())