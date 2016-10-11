import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QTextBrowser, QWidget
from PyQt5.QtCore import Qt

class LogQMainWindow(QMainWindow):

    def __init__(self, parent=None, flags=Qt.Widget):
        super().__init__(parent, flags)
        self.init_ui()

    def init_ui(self):

        table = QTableView()
        text = QTextBrowser()
        text.setText('Test')

        vbox = QVBoxLayout()
        vbox.addWidget(table)
        vbox.addWidget(text)

        widget = QWidget(flags=Qt.Widget)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.setGeometry(300, 300, 300, 150)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = LogQMainWindow()
    sys.exit(app.exec_())
