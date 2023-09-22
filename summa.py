import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QSizePolicy

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Responsive App Example")
        self.setGeometry(100, 100, 800, 600)  # Set an initial window size

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create widgets
        label = QLabel("This is a responsive app.")
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        button = QPushButton("Click Me!")
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Add widgets to the layout
        layout.addWidget(label)
        layout.addWidget(button)
		v_layout = QVBoxLayout(self)
        v_layout.addStretch(1)  # Add vertical stretch to center the button
        v_layout.addWidget(button)
        v_layout.addStretch(1)  # Add more vertical stretch to center the button

        # Create a horizontal layout
        h_layout = QHBoxLayout(self)
        h_layout.addStretch(1)  # Add horizontal stretch to center the button
        h_layout.addLayout(v_layout)  # Add the vertical layout with the button
        h_layout.addStretch(1)  # Add more horizontal stretch to center the button

        self.setLayout(h_layout)
        # Connect button signal
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button Clicked!")

    def resizeEvent(self, event):
        # Handle window resize events here
        print(f"Window Resized to {event.size()}")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
