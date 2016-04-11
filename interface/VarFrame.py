import tkinter as tk
from tkinter import *

from interface.Subframe import Subframe


class VarFrame(Subframe):
  def __init__(self, container, callback):
    super().__init__(containerFrame = container)

    Label(self.frame, text="here be New Variable window").pack(side=LEFT)

    saveVarBtn = Button(self.frame, text = 'save Variable',
        command = lambda: callback('variable content'))
    saveVarBtn.pack()