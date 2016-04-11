import tkinter as tk
from tkinter import *

class Subframe:
  def __init__(self, containerFrame):
    self.subframe = tk.Frame(containerFrame)
    
  def pack(self):
    self.subframe.pack()

  def unpack(self):
    self.subframe.destroy()