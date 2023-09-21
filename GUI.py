import sys
import os
import subprocess
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SIH CHATBOT")
        self.showMaximized()
        # Set the custom icon
        icon_path = "static/assets/REC Logo.png"  # Replace "icon.png" with the actual path to your icon file
        self.setWindowIcon(QIcon(icon_path))

        # Create the web view widget
        self.webview = QWebEngineView(self)
        self.webview.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.webview.urlChanged.connect(self.update_address_bar)  # Connect the urlChanged signal

        # Create a vertical layout to hold the web view
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.webview)

        # Create a central widget to set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        # Create the menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

       # Open Folder action
        open_folder_action = QAction(QIcon("icon_folder.png"), "Check Reports", self)
        open_folder_action.triggered.connect(self.open_folder)
        file_menu.addAction(open_folder_action)

        # Restart action
        restart_action = QAction(QIcon("icon_restart.png"), "Restart", self)
        restart_action.triggered.connect(self.restart_application)
        file_menu.addAction(restart_action)

        # Exit action
        exit_action = QAction(QIcon("icon_exit.png"), "Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Load this link by default
        self.load_url("http://127.0.0.1:5000")

    def load_url(self, url=None):
        if not url:
            url = self.address_bar.text()
        if "http://" not in url and "https://" not in url:
            url = "http://" + url
        self.webview.setUrl(QUrl(url))

    def update_address_bar(self, url):
        pass

    def restart_application(self):
        # Get the current executable and arguments
        executable = sys.executable
        args = sys.argv

        # Start a new instance of the application
        subprocess.Popen([executable] + args)
        self.close()

    def open_folder(self):
        initial_dir = os.getcwd()  # Get the current working directory where the application runs
        initial_dir += "/Reports"
        os.startfile(initial_dir)

if __name__ == "__main__":
    # Run the Flask app in a separate process
    flask_process = subprocess.Popen(["python", "app.py"])

    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.show()
    sys.exit(app.exec_())
