"""
Module for handling the download and extraction of Kaggle datasets.
Provides functionality to download specific datasets, move and rename them.

Imports:
- os: Provides functions for interacting with the operating system, like file handling.
- shutil: Provides functions for high-level file operations, like moving and renaming files.
- kagglehub: Used for interacting with Kaggle to download datasets.
"""

import os
import shutil

import kagglehub


class KaggleDownload:
    """
    A class for managing Kaggle dataset downloads and file operations.

    Methods
    -------
    __init__:
        Initializes the KaggleDownload class.

    dataset_download:
        Downloads a specific Kaggle dataset and processes the file.
    """

    def __init__(self):
        """
        Initialize the KaggleDownload class.

        Parameters
        ----------
        None
        """
        pass

    @staticmethod
    def dataset_download(dataset_id="paradisejoy/top-hits-spotify-from-20002019",
                         file_path="songs_normalize.csv",
                         new_dataset_filename="spotify_top_hits_2020.csv"):
        """
        Download and extract a Kaggle dataset.

        Parameters
        ----------
        dataset_id : str, optional
            The Kaggle dataset identifier (e.g., "paradisejoy/top-hits-spotify-from-20002019").
        file_path : str, optional
            The Kaggle path to the single file (e.g., "songs_normalize.csv").
        new_dataset_filename : str, optional
            New filename for the dataset (e.g., "spotify_top_hits_2020.csv").

        Returns
        -------
        None
            Prints the status of the dataset download process.
        """

        # Ensure the path exists and move to the 'resources' folder
        resources_path = os.path.join(os.getcwd(), 'melodymetrics', 'resources')

        if os.path.exists(resources_path):
            # Move to resources folder if not yet
            if "melodymetrics\\resources" not in os.getcwd():
                os.chdir(resources_path)

        try:
            # Download the dataset
            print(f"Dataset ID: {dataset_id}")
            dataset_download_path = kagglehub.dataset_download('paradisejoy/top-hits-spotify-from-20002019',
                                                               path='songs_normalize.csv', force_download=True)
            print(f"Dataset successfully downloaded to: {dataset_download_path}")

        except Exception as e:
            print(f"Error downloading dataset: {e}")

        else:
            # Delete any existing dataset files
            if os.path.exists(file_path):
                os.remove(file_path)  # Remove old file (songs_normalize.csv)
                print(f"Removed already existing dataset {file_path}")
            if os.path.exists(new_dataset_filename):
                os.remove(new_dataset_filename)  # Remove old renamed file (spotify_top_hits_2020.csv)
                print(f"Removed already existing dataset {new_dataset_filename}")

            # Move the dataset file from cache folder to resources
            shutil.move(dataset_download_path, os.getcwd())

            # Rename the dataset file
            os.rename(file_path, new_dataset_filename)
            print(f"Final dataset file: {os.getcwd()}\\{new_dataset_filename}")
