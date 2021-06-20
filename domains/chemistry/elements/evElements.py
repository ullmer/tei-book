# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

from   edElements import *
from   tkinter    import *
import yaml

######################################################################### 
#################### Enodia Visual : Chemical Elements #################### 

class evElements(edElements):
  root = None
  cellWidth  = 5
  cellHeight = 5
  blockColorYaml = '{s: RosyBrown2, p: LightSkyBlue1, d: khaki1, f: PaleGreen1}'
  blockColorHash = None
  # https://en.wikipedia.org/wiki/Periodic_table#/media/File:Simple_Periodic_Table_Chart-blocks.svg
  # http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png

  #################### build GUI #################### 
  def buildGui(self):
    self.root = Tk()
    self.blockColorHash = yaml.safe_load(self.blockColorYaml)

    table = self.buildCellTable(self.root)
    table.pack()

  #################### buildCell #################### 

  def buildCell(self, parentWidget, label1, label2, cellBg='white'):
    cell = Frame(parentWidget, 
                 highlightbackground="gray", highlightthickness=1, bg=cellBg,
                 width=self.cellWidth, height=self.cellHeight)
    l1   = Label(cell, text=label1, width=self.cellWidth, bg=cellBg)
    l2   = Label(cell, text=label2, width=self.cellWidth, bg=cellBg)
    for label in [l1, l2]:
      label.pack()
      label.bind("<Button>", self.buttonCB)

    return cell

  #################### button event callback #################### 
  def buttonCB(self, element):
    print("Element clicked")

  #################### buildCellCol #################### 

  def buildCellCol(self, parentWidget, cellLabelArray):
    cellRow = Frame(parentWidget)
    for labels in cellLabelArray:
      cell = self.buildCell(cellRow, labels[0], labels[1], labels[2])
      cell.pack(side=TOP)
    cellRow.pack(side=TOP)
    return cellRow

  #################### buildTableCol #################### 
  def buildTableCol(self, parentWidget, selectedRow):
    tableDimensions = self.getTableDimensions()
  
    rowLabels = []
    x = selectedRow
    #for y in range(1,9):
    for y in range(1,tableDimensions[1]):
      elFullname = self.getElementByTableIdx(x, y)
      elSymbol   = self.getSymbolByFullname(elFullname)
      elId       = self.getIdByFullname(elFullname)

      cellBlock  = self.getBlockByElName(elFullname)
      if cellBlock == None: cellColor = 'white'
      else:                 cellColor  = self.blockColorHash[cellBlock]

      labels     = [elId, elSymbol, cellColor]
      rowLabels.append(labels)
    row = self.buildCellCol(parentWidget, rowLabels)
    return row

  #################### buildCellTable #################### 

  def buildCellTable(self, parentWidget):
    cellTable = Frame(parentWidget)
    for colIdx in range(1,19):
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

