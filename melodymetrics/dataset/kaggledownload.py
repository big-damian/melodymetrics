import kagglehub
import shutil
import os

class kaggledownload:
    def __init__(self):
        """
        Initialize the KaggleDownload class.

        Parameters:
        - download_path (str): Datasets that will be downloaded.
        """

    def dataset_download(self, dataset_id="paradisejoy/top-hits-spotify-from-20002019", file_path="songs_normalize.csv"):
        """
        Download and extract a Kaggle dataset.

        Parameters:
        - dataset_id (str): The Kaggle dataset identifier (e.g., "paradisejoy/top-hits-spotify-from-20002019").
        - path (str): The Kaggle path to single file (e.g., "songs_normalize.csv").
        """
        print(f"Downloading dataset: {dataset_id}")
        try:
            # Download the dataset
            dataset_download_path = kagglehub.dataset_download('paradisejoy/top-hits-spotify-from-20002019', path='songs_normalize.csv', )
            #print("Download complete!")

            # Move the dataset file
            shutil.move(dataset_download_path, os.getcwd())
            print(f"Dataset downloaded to: {os.getcwd()}")

        except Exception as e:
            print(f"Error downloading dataset: {e}")

    def rename_dataset(self, new_name="spotify_top_hits_2020"):
        """
        Download and extract a Kaggle dataset.

        Parameters:
        - new_name (str): New name for the dataset file (e.g., "spotify_top_hits_2020").
        """
        # TODO: Finish this method