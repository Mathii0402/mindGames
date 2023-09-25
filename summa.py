import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class ContentFetcher(QThread):
    finished_signal = pyqtSignal(str)

    def run(self):
        # Simulate a delay for content fetching (replace this with actual content fetching logic)
        time.sleep(3)
        self.finished_signal.emit("Content fetched!")

class LoadingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Loading Logo Example")
        self.setGeometry(100, 100, 400, 200)

        self.loading_label = QLabel(self)
        self.loading_movie = QMovie("loading.gif")  # Replace "loading.gif" with your loading animation file
        self.loading_label.setMovie(self.loading_movie)

        self.loading_movie.start()
        self.loading_label.hide()

        self.layout = QVBoxLayout()
        self.button = QPushButton("Fetch Content")
        self.button.clicked.connect(self.fetch_content)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.loading_label)
        self.setLayout(self.layout)

    def fetch_content(self):
        self.button.setEnabled(False)
        self.button.setText("Loading...")
        self.loading_label.show()

        self.worker = ContentFetcher()
        self.worker.finished_signal.connect(self.on_content_fetched)
        self.worker.start()

    def on_content_fetched(self, content):
        self.loading_label.hide()
        self.button.setEnabled(True)
        self.button.setText("Fetch Content")
        print(content)  # Replace with the code to handle the fetched content

def main():
    app = QApplication(sys.argv)
    window = LoadingWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
