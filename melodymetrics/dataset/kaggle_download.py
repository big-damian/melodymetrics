import os
import shutil

import kagglehub


class KaggleDownload:

    def __init__(self):
        """
        Initialize the KaggleDownload class.

        Parameters:
        - download_path (str): Datasets that will be downloaded.
        """

    @staticmethod
    def dataset_download(dataset_id="paradisejoy/top-hits-spotify-from-20002019",
                         file_path="songs_normalize.csv",
                         new_dataset_filename="spotify_top_hits_2020.csv"):
        """
        Download and extract a Kaggle dataset.

        Parameters:
        - dataset_id (str): The Kaggle dataset identifier (e.g., "paradisejoy/top-hits-spotify-from-20002019").
        - path (str): The Kaggle path to single file (e.g., "songs_normalize.csv").
        - new_dataset_filename (str): New filename for the dataset (e.g., "spotify_top_hits_2020.csv")
        """

        print(f"Downloading dataset: {dataset_id}")

        try:
            # Download the dataset
            dataset_download_path = kagglehub.dataset_download('paradisejoy/top-hits-spotify-from-20002019',
                                                               path='songs_normalize.csv', )
            # print("Download complete!")

            # Delete any existing dataset files
            if os.path.exists(file_path):
                os.remove(file_path)
            if os.path.exists(new_dataset_filename):
                os.remove(new_dataset_filename)

            # Move the dataset file
            # TODO: Fix this location "dataset_download_path"
            # TODO: The .csv file must en up in resources folder
            shutil.move(dataset_download_path, os.getcwd())

            # Rename the dataset file TODO: Delete this text "and delete any remains"
            os.rename(file_path, new_dataset_filename)

        except Exception as e:
            print(f"Error downloading dataset: {e}")

        else:
            print(f"Dataset downloaded to: {os.getcwd()}\\{new_dataset_filename}")
