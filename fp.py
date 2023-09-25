import sys
from PyQt5.QtWidgets import QTextEdit,QScrollArea,QHeaderView,QDialog,QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QButtonGroup, QFrame,QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog,QFrame,QComboBox,QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QStackedWidget, QMessageBox, QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout
import pymongo
import subprocess
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIntValidator,QPixmap,QPainter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pymongo import MongoClient
from PyQt5.QtCore import Qt
import webview

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

class GlassCardWidget(QWidget):
    def __init__(self, question, answer):
        super().__init__()
        self.initUI(question, answer)

    def initUI(self, question, answer):
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        card_widget = QWidget(self)
        card_widget.setObjectName("GlassCard")
        card_widget.setStyleSheet(
            """
            #GlassCard {
                background-color: rgba(255, 255, 255, 0.2);
                border: 2px solid rgba(255, 255, 255, 0.4);
                border-radius: 10px;
                padding: 10px;
            }
            """
        )

        question_label = QLabel(question, self)
        question_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(question_label)

        answer_label = QLabel(answer, self)
        answer_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(answer_label)

       
       
        card_widget.setLayout(card_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(card_widget)
        self.setLayout(main_layout)


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
        create_quiz_button.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")


        start_quiz_button = QPushButton('Start Quiz', self)
        start_quiz_button.setFixedSize(380, 60)
        start_quiz_button.clicked.connect(self.start_quiz)
        start_quiz_button.setObjectName("startQuizButton")
        start_quiz_button.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")


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
        # Create a container widget for the main content
        container = QWidget(self)
        container.setGeometry(100, 100, 500, 440)  # Set the container's size and position
        container.setObjectName("contentContainer")

        # Create a layout for the container
        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignCenter)  # Center align the content vertically

        # Load the image sd.png
        pixmap = QPixmap('/home/mathi/django/pytutorial/sd.png')
        image_label = QLabel(container)
        image_height = 200
        image_label.setPixmap(pixmap.scaledToHeight(image_height))
        container_layout.addWidget(image_label)
        background_label = QLabel(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')  # Replace with the actual image path
        background_label.setPixmap(pixmap)
        background_label.resize(self.size()) 
        background_label.setGeometry(100,100,951,720) # Resize the label to match the window size
        background_label.move(0, 0)
        background_label.lower()
        # Create input widgets and buttons
        self.name_label = QLabel('Enter Your Name:', container)
        self.name_label.setObjectName("titleLabel")
        self.name_label.setFixedHeight(40)
        self.name_label.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")  # Set text color and font
        self.name_input = QLineEdit(container)
        self.name_input.setFixedHeight(40)
        self.name_input.setStyleSheet("border-radius: 10px; border: 2px solid #ccc; padding: 5px;")


        self.category_label = QLabel('Select Quiz Category:', container)
        self.category_label.setObjectName("titleLabel")
        self.category_label.setFixedHeight(40)
        self.category_label.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")  # Set text color and font
        self.category_dropdown = QComboBox(container)    
        self.category_dropdown.addItem('os')
        self.category_dropdown.addItem('Networks')
        self.category_dropdown.addItem('Aptitude')
        self.category_dropdown.addItem('Verbal')
        self.category_dropdown.setFixedHeight(40)
        self.category_dropdown.setStyleSheet("border-radius: 10px; border: 2px solid #ccc; padding: 5px;")


        
        start_button = QPushButton('Start Quiz', container)
        start_button.setObjectName("startQuizButton")
        start_button.setStyleSheet("color: white; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px; background-color: #e042f5; border: none; border-radius: 10px; padding: 10px 20px;")
        start_button.clicked.connect(self.start_quiz)
        start_button.setFixedHeight(40)

        self.start_button = start_button
        # Add input widgets and buttons to the container layout
        container_layout.addWidget(self.name_label)
        container_layout.addWidget(self.name_input)
        container_layout.addWidget(self.category_label)
        container_layout.addWidget(self.category_dropdown)
        container_layout.addWidget(start_button)

        # Create a horizontal layout to center the container horizontally
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(1)  # Add a stretchable space before the container
        horizontal_layout.addLayout(container_layout)  # Add the centered container
        horizontal_layout.addStretch(1)  # Add a stretchable space after the container

        # Set the horizontal layout for the main widget
        self.setLayout(horizontal_layout)

        # Set the background color and styles for the container
        

        self.setWindowTitle('Image Display')
        self.show()

    def start_quiz(self):
         # Start the quiz based on user inputs like name and category.
        name = self.name_input.text()
        category = self.category_dropdown.currentText()
         # Change the text of the Start Quiz button
        self.start_button.setText("Loading QuiZzz..")

    # Manually force the button to update its appearance
        self.start_button.repaint()

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
                       
        #Execute a Python script named "co.py" when "Create Quiz" is clicked.
                        try:
                            subprocess.Popen(["python3", "input.py"])
                        except Exception as e:
                            QMessageBox.critical(self, 'Error', f'An error occurred while executing co.py: {str(e)}')

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
        container = QWidget(self)
        container.setGeometry(100, 100, 500, 440)
        container.setObjectName("contentContainer")

        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap('/home/mathi/django/pytutorial/sd.png')
        image_label = QLabel(container)
        image_height = 200
        image_label.setPixmap(pixmap.scaledToHeight(image_height))
        container_layout.addWidget(image_label)

        background_label = QLabel(self)
        pixmap = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')
        background_label.setPixmap(pixmap)
        background_label.resize(self.size())
        background_label.setGeometry(100, 100, 951, 720)
        background_label.move(0, 0)
        background_label.lower()

        self.name_label = QLabel('Enter Your Name:', container)
        self.name_label.setObjectName("titleLabel")
        self.name_label.setFixedHeight(40)
        self.name_label.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")


        self.name_input = QLineEdit(container)
        self.name_input.setFixedHeight(40)
        self.name_input.setStyleSheet("border-radius: 10px; border: 2px solid #ccc; padding: 5px;")
    

        self.code_label = QLabel('Enter Code:', container)
        self.code_label.setObjectName("titleLabel")
        self.code_label.setFixedHeight(40)
        self.code_label.setStyleSheet("color: black; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px")

        self.code_input = QLineEdit(container)  # Create a QTextEdit widget for code input
        self.code_input.setFixedHeight(40) 
         # Set an appropriate height for code input'
        self.code_input.setStyleSheet("border-radius: 10px; border: 2px solid #ccc; padding: 5px;")
       

        start_button = QPushButton('Start Quiz', container)
        start_button.setObjectName("startQuizButton")
        start_button.setStyleSheet("color: white; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px; background-color: #e042f5; border: none; border-radius: 10px; padding: 10px 20px;")
        start_button.clicked.connect(self.start_quiz)
        start_button.setFixedHeight(40)

        self.start_button = start_button
        container_layout.addWidget(self.name_label)
        container_layout.addWidget(self.name_input)
        container_layout.addWidget(self.code_label)
        container_layout.addWidget(self.code_input)  # Add the code input field
        container_layout.addWidget(start_button)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(container_layout)
        horizontal_layout.addStretch(1)

        self.setLayout(horizontal_layout)

        self.setWindowTitle('Image Display')
        self.show()

    def start_quiz(self):
         # Start the quiz based on user inputs like name and category.
        name = self.name_input.text()
        category = self.code_input.text()
        self.start_button.setText("Loading QuiZzz..")
        self.start_button.repaint()
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
                       
        #Execute a Python script named "co.py" when "Create Quiz" is clicked.
                        try:
                            subprocess.Popen(["python3", "input.py"])
                        except Exception as e:
                            QMessageBox.critical(self, 'Error', f'An error occurred while executing co.py: {str(e)}')

                    else:
                        QMessageBox.warning(self, 'No Questions', 'No quiz questions found for the entered code.')
                else:
                    QMessageBox.warning(self, 'Invalid Code', 'No document found for the entered code.')

            except Exception as e:
                QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')
        else:
            QMessageBox.warning(self, 'Incomplete Information', 'Please enter your Name and Code.')
class ReviewSolutionWindow(QDialog):
    def __init__(self, questions, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Review Solutions')
        self.setGeometry(100, 100, 951, 710)
        
        # Background image
        background_label = QLabel(self)
        pixmap_background = QPixmap('/home/mathi/django/pytutorial/magicpattern-mesh-gradient-1695381891730.jpeg')  # Replace with your background image path
        background_label.setPixmap(pixmap_background)
        background_label.resize(self.size())

        layout = QVBoxLayout()
        centered_label = QLabel(self)
        pixmap_centered = QPixmap('/home/mathi/django/pytutorial/sd.png')  # Replace with your centered image path
        centered_label.setPixmap(pixmap_centered)
        centered_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(centered_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        content_layout = QVBoxLayout(content_widget)
        content_widget.setAutoFillBackground(True)
        content_widget.setStyleSheet("background-color: transparent;")  # Set to transparent background
        for question_data in questions:
            question_label = QLabel(question_data["question"])
            answer_label = QLabel(f"Correct Answer: {question_data['options'][question_data['correct']]}")

            content_layout.addWidget(question_label)
            content_layout.addWidget(answer_label)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        layout.addWidget(scroll_area)

        # Centered image
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

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
        self.questions_answered = 0
        view_leaderboard_button = QPushButton('View Leaderboard')
        view_leaderboard_button.setStyleSheet("color: white; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px; background-color: #edb672; border: none; border-radius: 10px; padding: 10px 20px;")
        
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
        submit_button.setStyleSheet("color: white; font-family: 'Special Elite', cursive; font-weight: bold; font-size: 16px; background-color: #e042f5; border: none; border-radius: 10px; padding: 10px 20px;")
        
        
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
            self.remaining_time = 6
            self.timer.start(1000)
        else:
            self.show_result()
    def show_feedback(self):
        # Create a FeedbackWindow and pass the questions list to it
        
        app = QApplication([])  # Create a temporary application to display the dialog
        review_window = ReviewSolutionWindow(self.questions)
        review_window.exec_()
        self.view_leaderboard()
        print("1")
    def check_answer(self):
         # Check the selected answer, update the score, and move to the next question.
        self.timer.stop()

        selected_button = self.option_buttons.checkedButton()
        if selected_button is not None:
            selected_idx = self.option_buttons.id(selected_button)
            if selected_idx == self.questions[self.current_question]["correct"]:
                self.score += 1

            self.questions_answered += 1  # Increment the questions answered counter

            if self.questions_answered == len(self.questions):
                # All questions have been answered, open the leaderboard
                self.show_result()
                self.show_feedback()
            

            else:
                self.current_question += 1
                self.update_question()
    
    def on_timeout(self):
        self.remaining_time -= 1
        self.remaining_time_label.setText(f"Time Remaining: {self.remaining_time} seconds")

        if self.remaining_time == 0:
            self.score += 0
            self.remaining_time_label.clear()
            self.current_question += 1
            self.remaining_time = 20
            self.update_question()

    def show_result(self):
        print("hi")
        # Display the quiz result, congratulate the user, and show the leaderboard.
        if self.score / len(self.questions) > len(self.questions) - 2:
            QMessageBox.information(self, 'Quiz Completed',
                                    f'Congratulations! You are good at this subject, {self.name}!\nYour score: {self.score}/{len(self.questions)}')
        elif self.score / len(self.questions) < 2:
            QMessageBox.information(self, 'Quiz Completed',
                                    f' You need to focus on this subject more! , {self.name}!\nYour score: {self.score}/{len(self.questions)}')
        else:
            QMessageBox.information(self, 'Quiz Completed',
                                    f'You need to improve a lot in this subject!, {self.name}!\nYour score: {self.score}/{len(self.questions)}')
        
        
        # Pass the unique_code to the ScoreDashboard and show it
        leaderboard_window = ScoreDashboard(self.unique_code, self.name, self.score)
        # leaderboard_window.show()
        self.show_feedback()
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