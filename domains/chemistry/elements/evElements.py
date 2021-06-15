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
    #row = self.buildCellCol(self.root, [['1', 'H'], ['2', 'He']])
    row = self.buildTableCol(self.root, 2)
    row.pack()

    #a = Label(self.root, text="Hello, world!")
    #a.pack()

  #################### buildCell #################### 

  def buildCell(self, parentWidget, label1, label2):
    cell = Frame(parentWidget, 
                 highlightbackground="gray", highlightthickness=1,
                 width=self.cellWidth, height=self.cellHeight)
    l1   = Label(cell, text=label1, width=self.cellWidth)
    l2   = Label(cell, text=label2, width=self.cellWidth)
    for label in [l1, l2]:
      label.pack()

    return cell

  #################### buildCellCol #################### 

  def buildCellCol(self, parentWidget, cellLabelArray):
    cellRow = Frame(parentWidget)
    for labels in cellLabelArray:
      cell = self.buildCell(cellRow, labels[0], labels[1])
      cell.pack(side=TOP)
    cellRow.pack(side=TOP)
    return cellRow

  #################### buildCellCol #################### 

  def buildCellTable(self, parentWidget, cellLabelArray):
    cellTable = Frame(parentWidget)
    tableDimensions = self.getTableDimensions()
    for colIdx in seq(1,tableDimensions[1]+1):
      col = self.buildTableCol(self.root, colIdx)
      col.pack(side=LEFT)
    cellTable.pack(side=LEFT)
    return cellTable

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

