from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app  # declare an app member
        self.setWindowTitle("Custom MainWindow")

        # setup menu bar and menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # add an edit menu and its actions
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # add other menu options, for fun
        menu_bar.addMenu("&Window")
        menu_bar.addMenu("&Settings")
        menu_bar.addMenu("&Help")

        # create the toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar) # add the toolbar to this window

        toolbar.addAction(quit_action)

        # add a custom action to the toolbar
        some_action = QAction("Some Action", self)  # parent is this window
        some_action.setStatusTip("Status message for some action") # shows on hover
        some_action.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(some_action)

    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        print("Action triggered")

