import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        question1 = "What is the capital of France?"
        answer1 = "Paris"
        question2 = "What is 2 + 2?"
        answer2 = "4"

        card1 = GlassCardWidget(question1, answer1)
        card2 = GlassCardWidget(question2, answer2)

        main_layout.addWidget(card1)
        main_layout.addWidget(card2)

        self.setLayout(main_layout)
        self.setWindowTitle('Glass Card UI')
        self.setGeometry(100, 100, 800, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(
        """
        QWidget {
            background-image: url('background.jpg');  # Replace with your background image path
        }
        """
    )
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
