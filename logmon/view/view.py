import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QTableView, QTextBrowser, QWidget,
    QDesktopWidget
)
from PyQt5.QtCore import Qt, QAbstractTableModel


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None, *args, **kwargs):
        super().rowCount(parent, *args, **kwargs)

    def columnCount(self, parent=None, *args, **kwargs):
        super().columnCount(parent, *args, **kwargs)

    def data(self, QModelIndex, role=None):
        super().data(QModelIndex, role)


class LogQMainWindow(QMainWindow):

    def __init__(self, parent=None, flags=Qt.Widget):
        super().__init__(parent, flags)
        self.init_ui()
        self._table = QTableView()
        self._text = QTextBrowser()


    def init_ui(self):

        self._text.setText('Test')

        vbox = QVBoxLayout()
        vbox.addWidget(self._table)
        vbox.addWidget(self._text)

        widget = QWidget(flags=Qt.Widget)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.setGeometry(500, 200, 1000, 700)
        # self.resize(1000, 700)
        # frame_geom = self.centralWidget().frameGeometry()
        # frame_geom.moveCenter(QDesktopWidget().availableGeometry().center())
        # self.move(frame_geom.topLeft())

    def loadData(self, data):
        self._table.setModel(TableModel(data))


def main():
    app = QApplication(sys.argv)
    w = LogQMainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
