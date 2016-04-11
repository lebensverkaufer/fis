import tkinter as tk
from tkinter import *
from interface.Subframe import Subframe

from interface.VarFrame import VarFrame
from interface.LTermFrame import LTermFrame



class MainWizard(Subframe):
  def __init__(self, container):
    super().__init__(containerFrame = container)

    Label(self.frame, text="here be main Wizard").pack(side=LEFT)

    self.varList = Listbox(self.frame)
    self.varList.pack()

    self.new_varFrame = VarFrame(self.frame, self.saveVar)

    newVarBtn = Button(self.frame, text = 'Add new Variable',
        command=lambda: self.createNewVarFrame(self.new_varFrame))
    newVarBtn.pack()


  def createNewVarFrame(self, oldVarFrame):
    oldVarFrame.unpack()
    self.new_varFrame = VarFrame(self.frame, self.saveVar)
    self.new_varFrame.pack()
    
  def saveVar(self, variable):
    self.varList.insert(END, variable.name)