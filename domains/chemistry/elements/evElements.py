# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

from edElements import *
from tkinter    import *

######################################################################### 
#################### Enodia Visual : Chemical Elements #################### 

class evElements(edElements):
  root = None
  cellWidth  = 5
  cellHeight = 5

  #################### build GUI #################### 
  def buildGui(self):
    self.root = Tk()
    cell = self.buildCell(self.root, '1', 'H')
    cell.pack()

    #a = Label(self.root, text="Hello, world!")
    #a.pack()

  #################### mainloop/event handler #################### 
  def buildCell(self, parentWidget, label1, label2):
    cell = Frame(parentWidget, borderwidth = 1, width=self.cellWidth, height=self.cellHeight)
    l1   = Label(cell, text=label1, width=self.cellWidth)
    l2   = Label(cell, text=label2, width=self.cellWidth)
    for label in [l1, l2]:
      #label.pack(expand=1, fill=BOTH)
      label.pack()

    return cell

  #################### mainloop/event handler #################### 
  def mainloop(self):
    self.root.mainloop()

############################################## 
#################### main #################### 

def main():
  ev = evElements()
  ev.buildGui()
  ev.mainloop()

if __name__ == "__main__":
  main()

### end ###

