import tkinter as tk
from tkinter import *

# import new_variable as varFrame
# import new_lTerm as ltFrame

from interface.Subframe import Subframe


class mainWizard(Subframe):
  def __init__(self, container):
    Subframe.__init__(self, containerFrame = container)

    Label(self.subframe, text="here be main Wizard").pack(side=LEFT)