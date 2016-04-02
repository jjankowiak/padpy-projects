from PyQt4 import QtGui

blankPalette = QtGui.QPalette(QtGui.QColor(222, 222, 222))
flaggedPalette = QtGui.QPalette(QtGui.QColor(222, 255, 222))
mineString = "M"
blankString = ""


class Field(QtGui.QPushButton):
    def __init__(self, row, column):
        super().__init__()
        self.setFundamentalParameters(column, row)
        self.resetField()

    def setFundamentalParameters(self, column, row):
        self.setFixedSize(30, 30)
        self.row = row
        self.column = column

    def resetField(self):
        self.setPalette(QtGui.QPalette(QtGui.QColor(222, 222, 222)))
        self.setText(blankString)
        self.setEnabled(True)
        self.isMine = False
        self.isRevealed = False
        self.isFlagged = False

    def setGameWindow(self, window):
        self.gameWindow = window

    def contextMenuEvent(self, event):
        self.updateField()
        self.gameWindow.updateMineCounter()

    def updateField(self):
        if not self.isFlagged:
            self.setFlaggedField()
        else:
            self.setBlankField()

    def setBlankField(self):
        self.isFlagged = False
        self.setText(blankString)
        self.setPalette(blankPalette)
        self.gameWindow.markedMines -= 1

    def setFlaggedField(self):
        self.isFlagged = True
        self.setText(mineString)
        self.setPalette(flaggedPalette)
        self.gameWindow.markedMines += 1
