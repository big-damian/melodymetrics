import datetime as dt
import os

import pandas as pd

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
        return self._df

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
                print(self.df.head())

            return self.df.head()
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
        any_null_values_df = self._df.isnull().any().to_frame(name="Any null values in dataframe columns?").reset_index()
        any_null_values_df.rename(columns={"index": "Column name"}, inplace=True)

        print(any_null_values_df)
        return any_null_values_df

    def check_num_unique_values(self):
        self.check_if_dataframe_loaded()
        unique_counts = []

        for column in self.df.columns:
            # Calculate the number of unique values in the column
            unique_count = len(self.df[column].unique())
            # Create a tuple with the column name and the number of unique values
            column_info = (column, unique_count)
            # Add the tuple to the list
            unique_counts.append(column_info)

        # Convert the list of tuples into a DataFrame
        unique_values_df = pd.DataFrame(unique_counts, columns=['Column name', 'Unique values'])

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

        self.df[["genre", "subgenres"]] = self.df["genre"].apply(split_genre).apply(pd.Series)
        print(self._df)

    def find_dataset_duration(self):
        self.check_if_dataframe_loaded()

        # Extract the start and end dates
        start_date = self._df['year'].min()
        end_date = self._df['year'].max()

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