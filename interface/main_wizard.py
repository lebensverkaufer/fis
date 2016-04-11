import tkinter as tk
from tkinter import *
from interface.Subframe import Subframe

from interface.VarFrame import VarFrame
from interface.LTermFrame import LTermFrame



class MainWizard(Subframe):
  def __init__(self, container):
    super().__init__(containerFrame = container)

    Label(self.frame, text="here be main Wizard").pack(side=LEFT)

    new_varFrame = VarFrame(self.frame)
    new_varFrame.pack()
    # это будем делать по кнопке