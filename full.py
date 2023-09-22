# Import the necessary modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget
import fp,co
# Create a custom widget for your main window
print(fp)
class FullScreenApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize a stacked widget
        self.stacked_widget = QStackedWidget(self)

        # Create and add your pages to the stacked widget
        self.page1 = fp.main()
        self.page2 = co.main()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Create buttons to switch between pages
        self.button1 = QPushButton("Page 1")
        self.button2 = QPushButton("Page 2")
        self.button1.clicked.connect(self.showPage1)
        self.button2.clicked.connect(self.showPage2)

        # Create a layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set fullscreen state change event filter
        self.installEventFilter(self)

    def showPage1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def showPage2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def eventFilter(self, obj, event):
        if event.type() == Qt.WindowStateChange:
            # Check if the application is in fullscreen mode
            if self.windowState() == Qt.WindowFullScreen:
                # Apply CSS styles for fullscreen
                self.setStyleSheet("""
                    background-color: #333;
                    color: white;
                    font-size: 24px;
                """)
            else:
                # Apply regular CSS styles
                self.setStyleSheet("")

        return super().eventFilter(obj, event)

# Create your first and second page classes similar to what you already have

if __name__ == "__main__":
    app = QApplication([])

    main_window = FullScreenApp()
    main_window.show()

    app.exec_()
