import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        for row, button_row in enumerate(self.buttons):
            for col, button_text in enumerate(button_row):
                button = QPushButton(button_text)
                self.grid_layout.addWidget(button, row, col)
                button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except Exception:
                self.result_display.setText("Error")
        else:
            self.result_display.setText(self.result_display.text() + button_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
