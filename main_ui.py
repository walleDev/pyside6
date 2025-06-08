from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui2py.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        # 从文件中加载UI定义
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        if self.ui.lineEdit.text():
            self.ui.webEngineView.load(self.ui.lineEdit.text())
        else:
            QMessageBox.warning(self, 'WARN', '请输入有效的 URL')


app = QApplication()
mainWindow = MainWindow()
mainWindow.show()
app.exec()
