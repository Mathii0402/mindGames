import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CodeMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Code Monitor')
        self.setGeometry(100, 100, 400, 300)

        self.output_browser = QTextBrowser()
        self.start_button = QPushButton('Start Monitoring')
        self.stop_button = QPushButton('Stop Monitoring')

        layout = QVBoxLayout()
        layout.addWidget(self.output_browser)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.start_button.clicked.connect(self.start_monitoring)
        self.stop_button.clicked.connect(self.stop_monitoring)

        self.monitoring = False
        self.observer = None

    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.output_browser.clear()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

            script_path = '/home/mathi/django/pytutorial/fp.py'  # Replace with the path to your Python script
            self.observer = Observer()
            self.observer.schedule(CodeChangeHandler(script_path, self.output_browser), path='.')
            self.observer.start()
        else:
            self.output_browser.append('Monitoring is already running.')

    def stop_monitoring(self):
        if self.monitoring:
            self.monitoring = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

            self.observer.stop()
            self.observer.join()
        else:
            self.output_browser.append('Monitoring is not running.')

class CodeChangeHandler(FileSystemEventHandler):
    def __init__(self, script_path, output_browser):
        super().__init__()
        self.script_path = script_path
        self.output_browser = output_browser

    def on_modified(self, event):
        if event.src_path == self.script_path:
            self.output_browser.append('Script modified. Reloading...')
            process = subprocess.Popen(['python', self.script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True, shell=False)
            stdout, stderr = process.communicate()
            self.output_browser.append(stdout)
            self.output_browser.append(stderr)

def main():
    app = QApplication(sys.argv)
    window = CodeMonitor()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
