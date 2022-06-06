import tkinter as tk
from tkinter import filedialog
def open_file():                            # 開檔函式
    root = tk.Tk()
    root.withdraw()
    sfname = filedialog.askopenfilename(title='選擇要開啟的檔案',
        # 開起對話框，對話框名稱
                                            filetypes=[# 文件能選擇的類型
                                                ('All Files','*'),
                                                ("jpeg files","*.jpg"),
                                                ("png files","*.png"),
                                                ("gif files","*.gif")])
    return sfname

def open_folder():                            # 開啟資料夾
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory(title='選擇要開啟的資料夾')                                      
        return file_path