class DatasetNotLoadedException(Exception):
    """
    Exception raised when a dataset is not loaded.

    Attributes:
        message (str): A descriptive message indicating the cause of the error.
    """
    def __init__(self, message="default"):
        if message == "default":
            message = "No dataset loaded yet. Please load the dataset first"
        super().__init__(message)

    def __str__(self):
        print(f"{self.args[0]}")
        return f"{self.args[0]}"