import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QFileDialog, QMessageBox, QGroupBox
from pymongo import MongoClient
from PyQt5.QtGui import QIntValidator, QPixmap, QPainter
from PyQt5 import QtCore

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize MongoDB connection
        self.client = MongoClient('mongodb+srv://mathivananmvcs20:qt20232023@cluster0.gl3ocfo.mongodb.net/')  # Replace with your MongoDB URL
        self.db = self.client['Quiz_app_using_QT']  # Replace with your database name

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quiz App')
        self.setGeometry(100, 100, 951, 710)

        self.setStyleSheet(open('style.css').read())

        pixmap = QPixmap(r'/home/mathi/django/pytutorial/sd.png')

        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignCenter)  # Center-align the image

        container = QGroupBox()  # Create a container group box
        container_layout = QVBoxLayout()
        container.setGeometry(100, 100, 500, 400)

        self.name_label = QLabel('Name:')
        self.name_field = QLineEdit()

        self.code_label = QLabel('Unique Code:')
        self.code_field = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        self.upload_button = QPushButton('Upload JSON File')
        self.upload_button.clicked.connect(self.upload_json)

        
        container_layout.addWidget(image_label)
        container_layout.addWidget(self.name_label)
        container_layout.addWidget(self.name_field)
        container_layout.addWidget(self.code_label)
        container_layout.addWidget(self.code_field)
        container_layout.addWidget(self.password_label)
        container_layout.addWidget(self.password_field)
        container_layout.addWidget(self.upload_button)
        

        container.setLayout(container_layout)

        main_layout = QVBoxLayout()
        main_layout.addSpacing(100)  # Add 20 pixels of spacing above the container
        main_layout.addWidget(container)  # Add the container to the main layout
        main_layout.addSpacing(100)  # Add 20 pixels of spacing below the container
        main_layout.setContentsMargins(50, 50, 50, 50)  # Left, Top, Right, Bottom margins
        self.setLayout(main_layout)

    def paintEvent(self, event):
        # Paint the background image
        painter = QPainter(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')
        painter.drawPixmap(self.rect(), pixmap)

    def upload_json(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Upload JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)

        if file_name:
            try:
                with open(file_name, "r") as json_file:
                    quiz_data = json.load(json_file)

                # Extract the questions from the loaded JSON
                questions = quiz_data.get("questions", [])
                if questions:
                    password = self.password_field.text()
                    if password == "admin":
                        # Check if unique_code already exists in the database
                        unique_code = self.code_field.text()
                        if self.is_unique_code_valid(unique_code):
                            # Save questions in MongoDB
                            collection = self.db['Questions']
                            name = self.name_field.text()

                            if name and unique_code:
                                quiz_data['name'] = name
                                quiz_data['unique_code'] = unique_code
                                collection.insert_one(quiz_data)
                                QMessageBox.information(self, 'Quiz Created', 'Quiz questions have been stored in MongoDB.')
                            else:
                                QMessageBox.warning(self, 'Missing Information', 'Please enter your Name and Unique Code.')
                        else:
                            QMessageBox.warning(self, 'Duplicate Unique Code', 'A quiz with this Unique Code already exists in the database.')
                    else:
                        QMessageBox.warning(self, 'Invalid Password', 'Password is incorrect. Only "admin" is allowed.')
                else:
                    QMessageBox.warning(self, 'No Questions Found', 'No quiz questions found in the uploaded JSON file.')

                self.upload_button.setText("JSON Uploaded")
            except Exception as e:
                print("Error loading JSON file:", e)

    def is_unique_code_valid(self, code):
        # Check if the unique_code already exists in the database
        collection = self.db['Questions']
        existing_quiz = collection.find_one({'unique_code': code})
        return existing_quiz is None

    def create_quiz(self):
        pass  # No need to create quiz here

def main():
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
