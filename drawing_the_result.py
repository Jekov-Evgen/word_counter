from tkinter import *
from tkinter import ttk

class DrawRes:
    def __init__(self, res) -> None:
        result = Tk()
        
        Label(result, text=f"{res} слов в тексте", font="30").grid(row=0, column=0, padx=10, pady=10)
        Button(result, text="Выйти", width=50, command=result.destroy).grid(row=1, column=0, padx=10, pady=10)
