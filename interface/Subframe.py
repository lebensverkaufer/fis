import tkinter as tk
from tkinter import *

class Subframe:
  ## use self.frame as inner container
  def __init__(self, containerFrame, border = 1, bg = 'white', pady = 10, padx = 10):
    self.frame = tk.Frame(containerFrame, 
      relief      = 'groove', 
      borderwidth = border, 
      bg          = bg, 
      pady        = pady, 
      padx        = padx
    )

  def pack(self):
    self.frame.pack()

  def unpack(self):
    self.frame.pack_forget()