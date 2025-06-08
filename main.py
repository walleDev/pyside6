from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = QUiLoader().load('ui/main.ui')
        # 使用 QWebEngineView 作为中心部件
        self.setCentralWidget(QWebEngineView())
        self.ui.pushButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        if self.ui.lineEdit.text():
            self.ui.webEngineView.load(self.ui.lineEdit.text())
        else:
            QMessageBox.warning(self.ui, 'WARN', '请输入有效的 URL')


app = QApplication()
mainWindow = MainWindow()
mainWindow.ui.show()
app.exec()
