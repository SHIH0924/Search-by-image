# 匯入函式庫
import tkinter as tk
import index
import Search1
def button_Index():
    index.Integrate_Index()
def button_Search():
    Search1.Integrate_Search()
# 宣告
root = tk.Tk()
# 視窗標題
root.title('以圖搜圖')
# 視窗初始大小
root.geometry('290x155')
# 視窗[左右, 上下]是否可拉大拉小，若都為0則視窗右上角的最大化按鈕會無法點擊
root.resizable(1, 1)
lab=tk.Label(root,text='匯入或更新資料庫:')
lab.grid(row=0,column=0,pady=10,padx=10)
mybutton = tk.Button(root, text='Index',width='15', height='2', command=button_Index)
mybutton.grid(row=0,column=1,pady=10)
lab1=tk.Label(root,text='需收尋圖片及收尋資料夾:')
lab1.grid(row=1,column=0,padx=10)
mybutton1 = tk.Button(root, text='Search',width='15', height='2', command=button_Search)
mybutton1.grid(row=1,column=1)
mybutton2 = tk.Button(root, text='Quit',width='10', height='1', command=root.destroy)
mybutton2.grid(row=2,column=0,pady=10,padx=10)

# 自動刷新畫面
root.mainloop()