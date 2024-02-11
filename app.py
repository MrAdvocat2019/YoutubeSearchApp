import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QVBoxLayout, QPushButton, QWidget

from response import search_response
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube search")
        self.setGeometry(100,100,500,300)
        self.search_line=QTextEdit()
        line_height = self.search_line.fontMetrics().lineSpacing()
        extra_vertical_space = self.search_line.frameWidth() * 2
        self.search_line.setFixedHeight(line_height+extra_vertical_space)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_line)
        self.button=QPushButton("Search")
        self.button.clicked.connect(self.search_clicked)
        self.layout.addWidget(self.button)
        self.label_widgets = []

        self.create_labels()

        self.setLayout(self.layout)
    def create_labels(self):
        labels_layout = QVBoxLayout()

        # Buttons for digits 0 to 9
        for i in range(5):
            label = QLabel()
            labels_layout.addWidget(label)
            self.label_widgets.append(label)
        self.layout.addLayout(labels_layout)
    def search_clicked(self):
        search_request=self.search_line.toPlainText()
        resp =  search_response(search_request)
        data = resp.json()
        sample_url = "https://www.youtube.com/watch?v="
        for i in range(5):
            video_id = data['items'][i]['id']['videoId']
            title = data['items'][i]['snippet']['title']
            url = f"{sample_url}{video_id}"

            # Set text as clickable URL
            self.label_widgets[i].setText(f'<a href="{url}">{title}</a>')
            self.label_widgets[i].setTextFormat(Qt.TextFormat.RichText)
            self.label_widgets[i].setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
            self.label_widgets[i].setOpenExternalLinks(True)
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_Return:
            self.search_clicked()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()