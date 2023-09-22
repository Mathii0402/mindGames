import sys
from PyQt5.QtWidgets import QHeaderView,QDialog,QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QButtonGroup, QFrame,QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from pymongo import MongoClient
import pymongo
from PyQt5.QtGui import QPixmap

    # ... (rest of the code remains the same)

class CardContainer(QFrame):
    def __init__(self, content_widget):
        super().__init__()
        self.setStyleSheet(
            "QFrame {"
            "   background-color: #F5DEB3;"  # Set sand-colored background color
            "   border-radius: 16px;"
            "   border: 1px solid rgba(0, 0, 0, 0.2);"
            "   padding: 20px;"  # Add padding
            "}"
        )
        layout = QVBoxLayout()
        layout.addWidget(content_widget)
        self.setLayout(layout)

class QuizWindow(QWidget):
    def __init__(self, name, questions, unique_code):
        super().__init__()

        self.name = name
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.remaining_time = 5
        self.unique_code = unique_code

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timeout)

        view_leaderboard_button = QPushButton('View Leaderboard')
        view_leaderboard_button.clicked.connect(self.view_leaderboard)

        container_layout = QVBoxLayout()
        self.setLayout(container_layout)

        quiz_widget = self.create_quiz_widget()
        card_container = CardContainer(quiz_widget)  # Wrap your quiz UI in the CardContainer
        container_layout.addWidget(card_container)

        container_layout.addWidget(view_leaderboard_button)
        card_container.setStyleSheet(
        "background: rgba(255, 255, 255, 0.17);"
        "border-radius: 16px;"
        "box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);"
        "backdrop-filter: blur(5px);"
        "-webkit-backdrop-filter: blur(5px);"
        "border: 1px solid rgba(255, 255, 255, 0.3);"
)
        # Set the window size
        self.setGeometry(100, 100, 951, 710)

        # Set the container size and position
        card_container.setGeometry(100, 100, 500, 400)
        background_label = QLabel(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')  # Replace with the actual image path
        background_label.setPixmap(pixmap)
        background_label.resize(self.size())  # Resize the label to match the window size
        background_label.move(0, 0)
        background_label.lower()

    def view_leaderboard(self):
    # Fetch scores from MongoDB
    
        try:
            client = MongoClient('mongodb+srv://mathivananmvcs20:qt20232023@cluster0.gl3ocfo.mongodb.net/')
            db = client["Quiz_app_using_QT"]
            results_collection = db["QuizResults"]

            # Query MongoDB to find scores based on the unique_code and sort them in decreasing order
            scores = list(results_collection.find({"unique_code": self.unique_code}).sort("score", pymongo.DESCENDING))

            # Create a new leaderboard window
            leaderboard_window = QDialog(self)
            leaderboard_window.setWindowTitle('Leaderboard')
            leaderboard_window.setGeometry(100, 100, 951, 710)

            # Create a layout for the leaderboard window
            layout = QVBoxLayout()
            ayout = QVBoxLayout()

        # Set the background image for the leaderboard window
            background_label = QLabel()
            background_pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')  # Replace with the path to your background image
            background_label.setPixmap(background_pixmap)
            background_label.setAlignment(Qt.AlignCenter) 
            # Create an image label and add it to the layout
            image_label = QLabel()
            pixmap = QPixmap('/home/mathi/django/pytutorial/sd.png')  # Replace with the path to your image
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)  # Center the image horizontally
            layout.addWidget(image_label)

            # Create a table widget
            table_widget = QTableWidget()
            table_widget.setColumnCount(2)  # Assuming two columns for name and score
            table_widget.setHorizontalHeaderLabels(["Name", "Score"])
            table_widget.setRowCount(len(scores))

            # Populate the table with leaderboard data
            for idx, score_data in enumerate(scores, start=1):
                name_item = QTableWidgetItem(score_data['name'])
                score_item = QTableWidgetItem(str(score_data['score']))
                table_widget.setItem(idx - 1, 0, name_item)
                table_widget.setItem(idx - 1, 1, score_item)

            # Set table properties
            table_widget.horizontalHeader().setStretchLastSection(True)
            table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table_widget.verticalHeader().setVisible(False)

            # Add the table widget to the layout
            layout.addWidget(table_widget)

            # Set the layout for the leaderboard window
            leaderboard_window.setLayout(layout)

            leaderboard_window.exec_()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred while fetching scores: {str(e)}')
    def create_quiz_widget(self):
        quiz_widget = QWidget()
        quiz_widget.setStyleSheet(open('style.css').read())
        quiz_layout = QVBoxLayout(quiz_widget)

        image_label = QLabel()
        pixmap = QPixmap('/home/mathi/django/pytutorial/sd.png')  # Replace 'your_image_path.jpg' with the actual image path
        image_label.setPixmap(pixmap)
        quiz_layout.addWidget(image_label)
        self.question_label = QLabel()
        quiz_layout.addWidget(self.question_label)
        image_label.setAlignment(Qt.AlignCenter)

        self.remaining_time_label = QLabel()
        quiz_layout.addWidget(self.remaining_time_label)

        self.option_buttons = QButtonGroup()

        for idx, option in enumerate(self.questions[self.current_question]["options"]):
            radio_button = QRadioButton(option)
            self.option_buttons.addButton(radio_button, idx)
            quiz_layout.addWidget(radio_button)

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.check_answer)
        quiz_layout.addWidget(submit_button)

        self.update_question()

        return quiz_widget

    def update_question(self):
        # Update the question and options for the current quiz.
        if self.current_question < len(self.questions):
            self.question_label.setText(self.questions[self.current_question]["question"])
            for idx, option in enumerate(self.questions[self.current_question]["options"]):
                self.option_buttons.button(idx).setText(option)
                self.option_buttons.button(idx).setChecked(False)

            self.timer.start(1000)
        else:
            self.show_result()

    def check_answer(self):
        # Check the selected answer, update the score, and move to the next question.
        self.timer.stop()

        selected_button = self.option_buttons.checkedButton()
        if selected_button is not None:
            selected_idx = self.option_buttons.id(selected_button)
            if selected_idx == self.questions[self.current_question]["correct"]:
                self.score += 1
            self.current_question += 1
            self.update_question()

    def on_timeout(self):
        self.remaining_time -= 1
        self.remaining_time_label.setText(f"Time Remaining: {self.remaining_time} seconds")

        if self.remaining_time == 0:
            self.score += 0
            self.remaining_time_label.clear()
            self.current_question += 1
            self.remaining_time = 5
            self.update_question()

    def show_result(self):
        # Display the quiz result, congratulate the user, and show the leaderboard.
        QMessageBox.information(self, 'Quiz Completed', f'Congratulations, {self.name}!\nYour score: {self.score}/{len(self.questions)}')

        # Pass the unique_code to the ScoreDashboard and show it
        leaderboard_window = ScoreDashboard(self.unique_code, self.name, self.score)
        leaderboard_window.show()

def main():
    app = QApplication(sys.argv)

    # You can customize these parameters with your quiz data
    name = "Your Name"
    questions = [
        {
            "question": "Question 1",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct": 0,  # Index of the correct option
        },
        {
            "question": "Question 2",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct": 1,
        },
        # Add more questions here
    ]
    unique_code = "os"

    quiz_window = QuizWindow(name, questions, unique_code)
    quiz_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
