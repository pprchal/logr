from project.core.Config import Config;
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.tbLog = None
        self.master = master
        self.levelButtons = list()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")
        
        col = 0
        for level in Config.getLevelDefs():
            color = Config.getLevelDefs()[level]
            button = self.createButton(level, color)
            self.levelButtons.append(button)
            button.grid(column=col, row=0)
            col = col + 1

        self.tbLog = tk.Text(self, height=20, width=300)
        self.tbLog.insert(tk.END,'\nWilliam Shakespeare\n', 'big')

    def createButton(self, level, color):
        bt = tk.Button(self, text=level, bg=color)
        bt["command"] = "bt_log_level-{}".format(level)
        return bt


def createGUI():
    root = tk.Tk()
    root.title("PAT 1.0")
    root.geometry('800x600')
    app = Application(master=root)
    return app

