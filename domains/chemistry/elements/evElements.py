# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

from edElements import *
from tkinter    import *

######################################################################### 
#################### Enodia Visual : Chemical Elements #################### 

class evElements(edElements):
  root = None
  cellWidth  = 100
  cellHeight = 100

  #################### build GUI #################### 
  def buildGui(self):
    self.root = Tk()
    cell = self.buildCell(self.root)
    cell.pack()

    #a = Label(self.root, text="Hello, world!")
    #a.pack()

  #################### mainloop/event handler #################### 
  def buildCell(self, parentWidget):
    cell = Frame(parentWidget, borderwidth = 1, width=self.cellWidth, height=self.cellHeight)
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

