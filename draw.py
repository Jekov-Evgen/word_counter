from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from drawing_the_result import DrawRes
from logics import count

def error():
    info = Tk()
    
    Label(info, text="Ошибка открытия файла, возможно не тот формат", font="30").grid(row=0, column=0, padx=10, pady=10)
    
    Button(info, text="OK", command=info.destroy, width=50).grid(row=1, column=0, padx=10, pady=10)


class MainWindow:
    def __init__(self) -> None:
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid
        
        ttk.Label(text="Загрузите свой текст и узнайте количество строк в нем", font=30).grid(row=0, column=0, padx=10, pady=10) 
        ttk.Label(text="Формат должен быть txt", font="30").grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Button(text="Выбрать файл", width=50, command=self.word_processing).grid(row=2, column=0 ,padx=10, pady=10)
        
        root.mainloop()
     
    def word_processing(self):
        try:
            self.file_path = filedialog.askopenfilename(
                title="Выберите файл",
                filetypes=[("txt файлы", "*.txt"), ("Все файлы", "*.*")]
            )
        except:
            error()
            
        res = count(self.file_path)
        
        DrawRes(res)
            
        