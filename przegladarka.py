import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PhotoViewer(QMainWindow):
    def __init__(self):
        super(PhotoViewer, self).__init__()

        self.setWindowTitle("Przeglądarka Zdjęć")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QLabel(self)
        # self.central_widget.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.open_button = QPushButton("Otwórz Zdjęcie", self)
        # self.open_button.clicked.connect(self.show_dialog)
        self.layout.addWidget(self.open_button)

        self.layout.addWidget(self.central_widget)

        self.central_widget.setLayout(self.layout)

    # def show_dialog(self):
    #     file_dialog = QFileDialog(self)
    #     file_dialog.setNameFilter("Zdjęcia (*.png *.jpg *.bmp)")
    #     file_dialog.setViewMode(QFileDialog.Detail)
    #     if file_dialog.exec_():
    #         file_path = file_dialog.selectedFiles()[0]
    #         self.load_image(file_path)

    def load_image(self, path):
        pixmap = QPixmap(path)
        self.central_widget.setPixmap(pixmap)
        self.central_widget.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PhotoViewer()
    viewer.show()
    sys.exit(app.exec_())
