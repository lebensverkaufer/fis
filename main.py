import tkinter as tk
from tkinter import *

import interface.main_wizard as UI

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.minsize(width=666, height=666)

        # self.variablesInputGroup = LabelFrame(self, text="Новая переменная", padx=5, pady=5)
        # self.showGroup_createNewVar(self.variablesInputGroup)

        self.pack()
        mainWizard = UI.MainWizard(self)
        mainWizard.pack()

    # def showGroup_createNewVar(self, container):   
        # container.pack(padx=10, pady=10)

    #     varName = StringVar()
    #     self.makeEntry(container, "Имя переменной", 10, textvariable = varName)

    #     def callback():
    #         print(varName.get())

    #     createVarBtn = Button(self, text="Создать переменную", width=10, command=callback)
    #     createVarBtn.pack()


    # def makeEntry(self, parent, caption, width=None, **options):
    #     Label(parent, text=caption).pack(side=LEFT)
    #     entry = Entry(parent, **options)
    #     if width:
    #         entry.config(width=width)
    #     entry.pack(side=LEFT)
    #     return entry

    # def createWidgets(self):
    #     newVarBtn = Button(self, text="Добавить переменную", command=self.showGroup_createNewVar(self))
    #     newVarBtn.pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
# 