import tkinter as tk
from tkinter import *

from interface.Subframe import Subframe


class VarFrame(Subframe):
  def __init__(self, container):
    super().__init__(containerFrame = container)

    Label(self.frame, text="here be New Variable window").pack(side=LEFT)