import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

class ExcelViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.loadButton = QPushButton('Load Excel File', self)
        self.loadButton.clicked.connect(self.loadExcel)
        self.layout.addWidget(self.loadButton)

        self.resultLabel = QLabel('Value will be displayed here', self)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)
        self.setWindowTitle('Excel Viewer')
        self.show()

    def loadExcel(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xls *.xlsx);;All Files (*)", options=options)
        if fileName:
            df = pd.read_excel(fileName)
            if not df.empty:
                value = df.iloc[0, 0]
                self.resultLabel.setText(f'First row, first column value: {value}')
            else:
                self.resultLabel.setText('The Excel file is empty')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExcelViewer()
    sys.exit(app.exec_())