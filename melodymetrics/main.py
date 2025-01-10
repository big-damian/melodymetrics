"""
Main module. Runs the app starting with its main window
"""

from melodymetrics.gui.main_window import MainWindow


def main():
    # Create and run the main window for the app
    app = MainWindow()
    app.run()


if __name__ == '__main__':
    main()
