from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QMessageBox, QPushButton
from tkinter import filedialog
from logics import count

def error():
    info = QMessageBox()
    info.setWindowTitle("ОШИБКА")
    info.setText("Ошибка открытия файла")
    info.exec()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        title = QLabel("Выберите свой файл для считывания(txt)")
        opening = QPushButton("Выбрать файл")
        
        opening.clicked.connect(self.word_processing)
        
        control_UI.addWidget(title)
        control_UI.addWidget(opening)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
     
    def word_processing(self):
        try:
            self.file_path = filedialog.askopenfilename(
                title="Выберите файл",
                filetypes=[("txt файлы", "*.txt"), ("Все файлы", "*.*")]
            )
        except:
            error()
        
        try:
            if self.file_path == '':
                raise
        except:
            error()
        
        res = count(self.file_path)    
        self.draw_result(res)
    
    
    def draw_result(self, res):
            result_window = QMessageBox()
            result_window.setWindowTitle("Результат")
            result_window.setText(f"{res} слов в тексте")
            result_window.exec()
            
        
            
        