import tkinter as tk
from tkinter import *

from interface.Subframe import Subframe

from fis import Variable


class VarFrame(Subframe):
  def __init__(self, container, callback):
    super().__init__(containerFrame = container)
    self.callback = callback
    varName = StringVar()
    inp = Entry(self.frame, textvariable = varName)
    inp.pack()


    # name, value, leftB, rightB, lterms, mfvalues

    saveVarBtn = Button(self.frame, text = 'save Variable',
        command = lambda: self.saveVar(varName))
    saveVarBtn.pack()

  def saveVar(self, varName):
    var = Variable(
      name = varName.get()
    )
    self.callback(var)
    self.unpack()
