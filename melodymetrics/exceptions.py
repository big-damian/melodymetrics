"""
Module for handling custom exceptions in the application.

This module defines custom exceptions used in the application.
"""


class DatasetNotLoadedException(Exception):
    """
    Exception raised when a dataset is not loaded.

    Attributes
    ----------
    message : str
        A descriptive message indicating the cause of the error.
    """

    def __init__(self, message="default"):
        """
        Initializes the DatasetNotLoadedException with a message.

        Parameters
        ----------
        message : str, optional
            The error message to display. Defaults to "No dataset loaded yet.
            Please load the dataset first" if "default" is passed.
        """
        if message == "default":
            message = "No dataset loaded yet. Please load the dataset first"
        super().__init__(message)

    def __str__(self):
        """
        Returns the string representation of the exception.

        Returns
        -------
        str
            The error message.
        """
        print(f"{self.args[0]}")  # Print the error message
        return f"{self.args[0]}"
