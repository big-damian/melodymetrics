"""
Main module to launch the MelodyMetrics application.

This module serves as the entry point for the application, initializing
and running the main graphical user interface (GUI).
"""

from melodymetrics.gui.main_window import MainWindow


def main():
    """
    Initializes and runs the main window of the MelodyMetrics application.

    This function creates an instance of the MainWindow class and calls
    its `run` method to start the application's GUI.
    """

    # Create and run the main window for the app
    app = MainWindow()
    app.run()


if __name__ == '__main__':
    main()
