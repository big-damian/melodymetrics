import os
import pandas as pd

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

# Example usage:
da = DataAnalysis()