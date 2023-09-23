import sys
from PyQt5.QtWidgets import QScrollArea,QHeaderView,QDialog,QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QButtonGroup, QFrame,QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog,QFrame,QComboBox,QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QStackedWidget, QMessageBox, QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout
import pymongo
import subprocess
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIntValidator,QPixmap,QPainter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pymongo import MongoClient
from PyQt5.QtCore import Qt

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



class StartQuizPage(QWidget):
    def __init__(self, stacked_widget=None):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        
        self.setGeometry(100, 100, 951, 710)
        self.setWindowTitle('Background Image Example')

        
        self.setStyleSheet(open('style.css').read())
        
        pixmap = QPixmap(r'/home/mathi/django/pytutorial/sd.png')
        
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)

        create_quiz_button = QPushButton('Room Mode', self)
        create_quiz_button.setFixedSize(380, 60)
        create_quiz_button.clicked.connect(self.room_mode)
        create_quiz_button.setObjectName("Domain Mode")

        start_quiz_button = QPushButton('Domain Mode', self)
        start_quiz_button.setFixedSize(380, 60)
        start_quiz_button.clicked.connect(self.domain_mode)
        start_quiz_button.setObjectName("startQuizButton")

        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        v_layout.addWidget(create_quiz_button)
        v_layout.addWidget(start_quiz_button)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout)

        container = QWidget(self)
        container.setLayout(h_layout)
        
        # Set the background color of the container to sandy brown
        container.setStyleSheet(
        "background: rgba(255, 255, 255, 0.17);"
        "border-radius: 16px;"
        "box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);"
        "backdrop-filter: blur(5px);"
        "-webkit-backdrop-filter: blur(5px);"
        "border: 1px solid rgba(255, 255, 255, 0.3);"
)

        # Center the container horizontally and vertically
        h_center_layout = QHBoxLayout()
        h_center_layout.addStretch(1)
        h_center_layout.addWidget(container)
        h_center_layout.addStretch(1)

        v_center_layout = QVBoxLayout(self)
        v_center_layout.addStretch(1)
        v_center_layout.addLayout(h_center_layout)
        v_center_layout.addStretch(1)

        self.setLayout(v_center_layout)

        self.setGeometry(100, 100, pixmap.width(), pixmap.height())
        self.setWindowTitle('Image Display')
        self.show()
    def paintEvent(self, event):
        # Paint the background image
        painter = QPainter(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')
        painter.drawPixmap(self.rect(), pixmap)

        # Create your content (buttons, labels, etc.)
        pixmap = QPixmap('/home/mathi/django/pytutorial/sd.png')
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.move(100, 100)

        create_quiz_button = QPushButton('Create Quiz', self)
        create_quiz_button.setFixedSize(345, 60)
        create_quiz_button.clicked.connect(self.room_mode)
        create_quiz_button.setObjectName("startQuizButton")
        create_quiz_button.move(100, 200)

        start_quiz_button = QPushButton('Start Quiz', self)
        start_quiz_button.setFixedSize(345, 60)
        start_quiz_button.clicked.connect(self.domain_mode)
        start_quiz_button.setObjectName("startQuizButton")
        start_quiz_button.move(100, 300)
 
    # Switch to the QuizInputPage for "Room Mode."
    def room_mode(self):
        quiz_input_page = QuizInputPage(self.stacked_widget)
        self.stacked_widget.addWidget(quiz_input_page)
        self.stacked_widget.setCurrentWidget(quiz_input_page)
    # Switch to the QuizInputPage for "Domain Mode."
    def domain_mode(self):
        
        quiz_input_page2 = QuizInputPage2(self.stacked_widget)
        self.stacked_widget.addWidget(quiz_input_page2)
        self.stacked_widget.setCurrentWidget(quiz_input_page2)

class HomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.initUI()
    def initUI(self):
        
        
        self.setGeometry(100, 100, 951, 710)
        self.setWindowTitle('Background Image Example')

        
        self.setStyleSheet(open('style.css').read())
        
        pixmap = QPixmap(r'/home/mathi/django/pytutorial/sd.png')
        
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)

        create_quiz_button = QPushButton('Create Quiz', self)
        create_quiz_button.setFixedSize(380, 60)
        create_quiz_button.clicked.connect(self.create_quiz)
        create_quiz_button.setObjectName("startQuizButton")

        start_quiz_button = QPushButton('Start Quiz', self)
        start_quiz_button.setFixedSize(380, 60)
        start_quiz_button.clicked.connect(self.start_quiz)
        start_quiz_button.setObjectName("startQuizButton")

        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        v_layout.addWidget(create_quiz_button)
        v_layout.addWidget(start_quiz_button)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout)

        container = QWidget(self)
        container.setLayout(h_layout)
        
        # Set the background color of the container to sandy brown
        container.setStyleSheet(
        "background: rgba(255, 255, 255, 0.17);"
        "border-radius: 16px;"
        "box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);"
        "backdrop-filter: blur(5px);"
        "-webkit-backdrop-filter: blur(5px);"
        "border: 1px solid rgba(255, 255, 255, 0.3);"
)

        # Center the container horizontally and vertically
        h_center_layout = QHBoxLayout()
        h_center_layout.addStretch(1)
        h_center_layout.addWidget(container)
        h_center_layout.addStretch(1)

        v_center_layout = QVBoxLayout(self)
        v_center_layout.addStretch(1)
        v_center_layout.addLayout(h_center_layout)
        v_center_layout.addStretch(1)

        self.setLayout(v_center_layout)

        self.setGeometry(100, 100, pixmap.width(), pixmap.height())
        self.setWindowTitle('Image Display')
        self.show()
    def paintEvent(self, event):
        # Paint the background image
        painter = QPainter(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')
        painter.drawPixmap(self.rect(), pixmap)

        # Create your content (buttons, labels, etc.)
        pixmap = QPixmap('/home/mathi/django/pytutorial/sd.png')
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.move(100, 100)

        create_quiz_button = QPushButton('Create Quiz', self)
        create_quiz_button.setFixedSize(345, 60)
        create_quiz_button.clicked.connect(self.create_quiz)
        create_quiz_button.setObjectName("startQuizButton")
        create_quiz_button.move(100, 200)

        start_quiz_button = QPushButton('Start Quiz', self)
        start_quiz_button.setFixedSize(345, 60)
        start_quiz_button.clicked.connect(self.start_quiz)
        start_quiz_button.setObjectName("startQuizButton")
        start_quiz_button.move(100, 300)
    def execute_co_script(self):
        #Execute a Python script named "co.py" when "Create Quiz" is clicked.
        try:
            subprocess.Popen(["python3", "co.py"])
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred while executing co.py: {str(e)}')

    def create_quiz(self):
        self.execute_co_script()

    def start_quiz(self):
         # Switch to the StartQuizPage when "Start Quiz" is clicked.
        start_quiz_page = StartQuizPage(self.stacked_widget)
        self.stacked_widget.addWidget(start_quiz_page)
        self.stacked_widget.setCurrentWidget(start_quiz_page)
class QuizInputPage2(QWidget):
    def __init__(self, stacked_widget=None):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 951, 710)
        self.setStyleSheet(open('style.css').read())
        pixmap = QPixmap(r'/home/mathi/django/pytutorial/sd.png')

        # Create a background image label
        background_label = QLabel(self)
        pixmap_background = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')
        background_label.setPixmap(pixmap_background)
        background_label.setGeometry(0, 0, self.width(), self.height())

        # Create a container widget for the main content
        container = QWidget(self)
        container.setObjectName("contentContainer")

        # Create a layout for the container
        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignCenter)  # Center align the content

        # Create a label for the image
        image_label = QLabel(container)
        image_height = 200
        image_label.setPixmap(pixmap.scaledToHeight(image_height))
        container_layout.addWidget(image_label)

        # Create input widgets and buttons
        self.name_label = QLabel('Enter Your Name:')
        self.name_label.setObjectName("titleLabel")
        self.name_label.setFixedHeight(40)
        self.name_label.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")  # Set text color and font
        self.name_input = QLineEdit()
        self.name_input.setFixedHeight(40)

        self.category_label = QLabel('Select Quiz Category:')
        self.category_label.setObjectName("titleLabel")
        self.category_label.setFixedHeight(40)
        self.category_label.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")  # Set text color and font
        self.category_dropdown = QComboBox()    
        self.category_dropdown.addItem('os')
        self.category_dropdown.addItem('Networks')
        self.category_dropdown.addItem('Aptitude')
        self.category_dropdown.addItem('Verbal')
        self.category_dropdown.setFixedHeight(40)

        start_button = QPushButton('Start Quiz')
        start_button.setObjectName("startQuizButton")
        start_button.clicked.connect(self.start_quiz)
        start_button.setFixedHeight(40)  # Increase button height

        # Add input widgets and buttons to the container layout
        container_layout.addWidget(self.name_label)
        container_layout.addWidget(self.name_input)
        container_layout.addWidget(self.category_label)
        container_layout.addWidget(self.category_dropdown)
        container_layout.addWidget(start_button)

        # Set the container layout
        container.setLayout(container_layout)

        # Create a scroll area to contain the content
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)  # Allow the content to be scrollable

        # Set the background color and styles for the container
        container.setStyleSheet(
            "background: rgba(255, 255, 255, 0.17);"
            "border-radius: 16px;"
            "box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);"
            "backdrop-filter: blur(5px);"
            "-webkit-backdrop-filter: blur(5px);"
            "border: 1px solid rgba(255, 255, 255, 0.3);")

        # Create a layout for the main widget and add the scroll area
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setWindowTitle('Image Display')
        self.show()

        self.name_label = QLabel('Enter Your Name:')
        self.name_label.setObjectName("titleLabel")
        self.name_label.setFixedHeight(40)
        self.name_label.setStyleSheet("color: black;     font-family: 'Special Elite', cursive;font-weight: bold; font-size: 16px")  # Set text color and font
        self.name_input = QLineEdit()
        self.name_input.setFixedHeight(40)

        self.category_label = QLabel('Select Quiz Category:')
        self.category_label.setObjectName("titleLabel")
        self.category_label.setFixedHeight(40)
        self.category_label.setStyleSheet("color: black;     font-family: 'Special Elite', cursive;font-weight: bold; font-size: 16px")  # Set text color and font
        self.category_dropdown = QComboBox()    
      
        self.category_dropdown.addItem('os')
        self.category_dropdown.addItem('Networks')
        self.category_dropdown.addItem('Aptitude')
        self.category_dropdown.addItem('Verbal')
        self.category_dropdown.setFixedHeight(40)

        start_button = QPushButton('Start Quiz')
        start_button.setObjectName("startQuizButton")
        start_button.clicked.connect(self.start_quiz)
        start_button.setFixedHeight(40)  # Increase button height
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.name_label)
        v_layout.addWidget(self.name_input)
        v_layout.addWidget(self.category_label)
        v_layout.addWidget(self.category_dropdown)
        v_layout.addWidget(start_button)

        # Center the form vertically within the container
        form_container = QWidget(self)
        form_container.setLayout(v_layout)
        v_container_layout = QVBoxLayout()
        v_container_layout.addStretch(1)
        v_container_layout.addWidget(form_container)
        v_container_layout.addStretch(1)
        container.layout().addLayout(v_container_layout)



    def start_quiz(self):
         # Start the quiz based on user inputs like name and category.
        name = self.name_input.text()
        category = self.category_dropdown.currentText()
        
        if name and category:
            try:
                client = pymongo.MongoClient("mongodb+srv://mathivananmvcs20:qt20232023@cluster0.gl3ocfo.mongodb.net/")
                db = client["Quiz_app_using_QT"]
                questions_collection = db["Questions"]

                # Filter the database based on the selected category and search term
                
                document = questions_collection.find_one({"unique_code": category})

                # documents = questions_collection.find({"category": category})
                if document:
                    questions = document.get("questions", [])
                    if questions:
                        self.stacked_widget.removeWidget(self)
                        quiz_window = QuizWindow(name, questions, category)
                        self.stacked_widget.addWidget(quiz_window)
                        self.stacked_widget.setCurrentWidget(quiz_window)
                    else:
                        QMessageBox.warning(self, 'No Questions', 'No quiz questions found for the entered code.')
                else:
                    QMessageBox.warning(self, 'Invalid Code', 'No document found for the entered code.')

            except Exception as e:
                QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')
        else:
            QMessageBox.warning(self, 'Incomplete Information', 'Please enter your Name and Code.')

class QuizInputPage(QWidget):
    def __init__(self, stacked_widget=None):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 951, 710)
        self.setStyleSheet(open('style.css').read())
        pixmap = QPixmap(r'/home/mathi/django/pytutorial/sd.png')

        image_label = QLabel(self)
        # Set a fixed height for the image (e.g., 200 pixels)
        image_height = 200
        image_label.setPixmap(pixmap.scaledToHeight(image_height))

        # Create a background image label
        background_label = QLabel(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())
        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout)
        container = QWidget(self)
        container.setLayout(h_layout)

        # Set the background color and styles for the container
        container.setStyleSheet(
            "background: rgba(255, 255, 255, 0.17);"
            "border-radius: 16px;"
            "box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);"
            "backdrop-filter: blur(5px);"
            "-webkit-backdrop-filter: blur(5px);"
            "border: 1px solid rgba(255, 255, 255, 0.3);")

        # Center the container horizontally and vertically
        h_center_layout = QHBoxLayout(self)
        h_center_layout.addStretch(1)
        h_center_layout.addWidget(container)
        h_center_layout.addStretch(1)

        v_center_layout = QVBoxLayout(self)
        v_center_layout.addStretch(1)
        v_center_layout.addLayout(h_center_layout)
        v_center_layout.addStretch(1)

        self.setLayout(v_center_layout)

        self.setWindowTitle('Image Display')
        self.show()

        self.name_label = QLabel('Enter Your Name:')
        self.name_label.setObjectName("titleLabel")
        self.name_label.setFixedHeight(40)
        self.name_label.setStyleSheet("color: black;     font-family: 'Special Elite', cursive;font-weight: bold; font-size: 16px")  # Set text color and font
        self.name_input = QLineEdit()
        self.name_input.setFixedHeight(40)

        self.category_label = QLabel('Enter Quiz Category:')
        self.category_label.setObjectName("titleLabel")
        self.category_label.setFixedHeight(40)
        self.category_label.setStyleSheet("color: black;     font-family: 'Special Elite', cursive;font-weight: bold; font-size: 16px")  # Set text color and font
        # Replace the dropdown with a regular input box
        self.code_input = QLineEdit()
        self.code_input.setFixedHeight(40)

        start_button = QPushButton('Start Quiz')
        start_button.setObjectName("startQuizButton")
        start_button.clicked.connect(self.start_quiz)
        start_button.setFixedHeight(40)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.name_label)
        v_layout.addWidget(self.name_input)
        v_layout.addWidget(self.category_label)
        v_layout.addWidget(self.code_input)
        v_layout.addWidget(start_button)

        # Center the form vertically within the container
        form_container = QWidget(self)
        form_container.setLayout(v_layout)
        v_container_layout = QVBoxLayout()
        v_container_layout.addStretch(1)
        v_container_layout.addWidget(form_container)
        v_container_layout.addStretch(1)
        container.layout().addLayout(v_container_layout)
    def start_quiz(self):
        name = self.name_input.text()
        code = self.code_input.text()
        if name and code:
            try:
                client = pymongo.MongoClient("mongodb+srv://mathivananmvcs20:qt20232023@cluster0.gl3ocfo.mongodb.net/")
                db = client["Quiz_app_using_QT"]
                questions_collection = db["Questions"]
                document = questions_collection.find_one({"unique_code": code})

                if document:
                    questions = document.get("questions", [])
                    if questions:
                        self.stacked_widget.removeWidget(self)
                        quiz_window = QuizWindow(name, questions, code)
                        self.stacked_widget.addWidget(quiz_window)
                        self.stacked_widget.setCurrentWidget(quiz_window)
                    else:
                        QMessageBox.warning(self, 'No Questions', 'No quiz questions found for the entered code.')
                else:
                    QMessageBox.warning(self, 'Invalid Code', 'No document found for the entered code.')

            except Exception as e:
                QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')
        else:
            QMessageBox.warning(self, 'Incomplete Information', 'Please enter your Name and Code.')

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
            

        # Set the background image for the leaderboard window
            background_label = QLabel()
            pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')  # Replace with the actual image path
            background_label.setPixmap(pixmap)
            background_label.resize(self.size())  # Resize the label to match the window size
            background_label.move(0, 0)
            background_label.lower()
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

        submit_button = QPushButton('Next')
        submit_button.clicked.connect(self.check_answer)
        quiz_layout.addWidget(submit_button)

        self.update_question()

        return quiz_widget

    def update_question(self):
        #Update the question and options for the current quiz.
        if self.current_question < len(self.questions):
            self.question_label.setText(self.questions[self.current_question]["question"])
            for idx, option in enumerate(self.questions[self.current_question]["options"]):
                self.option_buttons.button(idx).setText(option)
                self.option_buttons.button(idx).setChecked(False)
            self.remaining_time = 6
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

class ScoreDashboard(QWidget):
    def __init__(self, unique_code, name, score):
        super().__init__()

        self.unique_code = unique_code
        self.name = name
        self.score = score
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Score Dashboard')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(open('style.css').read())

        # Fetch scores from MongoDB
        try:
            client = MongoClient('mongodb+srv://mathivananmvcs20:qt20232023@cluster0.gl3ocfo.mongodb.net/')
            db = client["Quiz_app_using_QT"]
            results_collection = db["QuizResults"]

            # Insert the current player's score
            results_collection.insert_one({"unique_code": self.unique_code, "name": self.name, "score": self.score})

            # Query MongoDB to find scores based on the unique_code and sort them in decreasing order
            scores = list(results_collection.find({"unique_code": self.unique_code}).sort("score", pymongo.DESCENDING))

            score_label = QLabel('Leaderboard ')
            score_text = ''
            for idx, score_data in enumerate(scores, start=1):
                score_text += f"{idx}. {score_data['name']}: {score_data['score']}\n"

            score_display = QLabel(score_text)

            layout = QVBoxLayout()
            layout.addWidget(score_label)
            layout.addWidget(score_display)
            self.setLayout(layout)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred while fetching scores: {str(e)}')
def main():
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    home_page = HomePage(stacked_widget)
    stacked_widget.addWidget(home_page)
    stacked_widget.setGeometry(100, 100, 951, 710)
    stacked_widget.setObjectName("centered-container")
    
    stacked_widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()