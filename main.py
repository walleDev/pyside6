from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtUiTools import QUiLoader


class MyWindow:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/main.ui')
        self.ui.webEngineView.load('https://www.baidu.com')
        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        # https://www.baidu.com
        # QMessageBox.about(self.ui,'box', self.ui.box.currentText())
        # QMessageBox.about(self.ui,'box', self.ui.line.text())
        # self.ui.webview.load(self.ui.line.text())
        if self.ui.line.text():
            self.ui.webEngineView.load(self.ui.line.text())

app = QApplication()
myWindow = MyWindow()
myWindow.ui.show()
app.exec()