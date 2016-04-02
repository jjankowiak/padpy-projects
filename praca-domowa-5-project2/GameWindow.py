from Field import Field

from PyQt4 import QtCore, QtGui

import random
import itertools

aboutHeader = "About Minesweeper"
aboutText = "This is a minesweeper game. Find all mines staying alive!"


class GameWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setInitialBoardSize()
        self.setWindowTitle("Minesweeper")
        self.setMenuBar(self.createMenuBar())
        self.setCentralWidget(self.createCentralWidget())
        self.statusBar()
        self.show()
        self.setupTimer()

    def setInitialBoardSize(self):
        self.rowsNumber = 6
        self.columnsNumber = 6
        self.minesNumber = 10

    def createMenuBar(self):
        menuBar = QtGui.QMenuBar()

        fileMenu = menuBar.addMenu("&File")
        exitAction = self.createExitAction()
        fileMenu.addAction(exitAction)
        exitToolbar = self.addToolBar("Exit")
        exitToolbar.addAction(exitAction)

        optionsAction = self.createOptionsAction()
        fileMenu.addAction(optionsAction)
        optionsToolbar = self.addToolBar("Options")
        optionsToolbar.addAction(optionsAction)

        helpMenu = menuBar.addMenu("&Help")
        aboutAction = self.createAboutAction()
        helpMenu.addAction(aboutAction)
        aboutToolbar = self.addToolBar("About")
        aboutToolbar.addAction(aboutAction)

        return menuBar

    def createExitAction(self):
        exitAction = QtGui.QAction(QtGui.QIcon("images/exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)
        return exitAction

    def createOptionsAction(self):
        optionsAction = QtGui.QAction(QtGui.QIcon("images/options.png"),
                                      "Options", self)
        optionsAction.setShortcut("Ctrl+O")
        optionsAction.setStatusTip("Options")
        optionsAction.triggered.connect(self.popupOptionsBox)
        return optionsAction

    def popupOptionsBox(self):
        self.optionWidget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout()

        choices = []
        for i in range(10):
            choices.append("%i" % ((i + 1) * 2))

        rowsLabel = QtGui.QLabel("Choose rows number")
        layout.addWidget(rowsLabel)
        rowsComboBox = QtGui.QComboBox()
        rowsComboBox.addItems(choices)
        layout.addWidget(rowsComboBox)
        self.connect(rowsComboBox, QtCore.SIGNAL("activated(QString)"),
                     self.setRowsNumber)

        columnsLabel = QtGui.QLabel("Choose columns number")
        layout.addWidget(columnsLabel)
        columnsComboBox = QtGui.QComboBox()
        columnsComboBox.addItems(choices)
        layout.addWidget(columnsComboBox)
        self.connect(columnsComboBox, QtCore.SIGNAL("activated(QString)"),
             self.setColumnsNumber)


        mineNumberChoices = []
        for i in range(self.rowsNumber * self.columnsNumber):
            mineNumberChoices.append("%i" % (i + 1))
        minesLabel = QtGui.QLabel("Choose mines number")
        layout.addWidget(minesLabel)
        minesComboBox = QtGui.QComboBox()
        minesComboBox.addItems(mineNumberChoices)
        layout.addWidget(minesComboBox)
        self.connect(minesComboBox, QtCore.SIGNAL("activated(QString)"),
                     self.setMinesNumber)

        self.optionWidget.setLayout(layout)
        self.optionWidget.show()

    def setRowsNumber(self, chosenOption):
        self.rowsNumber = int(chosenOption)
        self.clearLayout(self.boardLayout)
        self.drawBoard()
        self.newGame()

    def setColumnsNumber(self, chosenOption):
        self.columnsNumber = int(chosenOption)
        self.clearLayout(self.boardLayout)
        self.drawBoard()
        self.newGame()

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def setMinesNumber(self, chosenOption):
        self.minesNumber = int(chosenOption)
        self.clearLayout(self.boardLayout)
        self.drawBoard()
        self.newGame()

    def createAboutAction(self):
        aboutAction = QtGui.QAction(QtGui.QIcon("images/about.png"),
                                    "About", self)
        aboutAction.setShortcut("Ctrl+I")
        aboutAction.setStatusTip("About application")
        aboutAction.triggered.connect(self.popupAboutBox)
        return aboutAction

    def popupAboutBox(self):
        QtGui.QMessageBox.information(self, aboutHeader, aboutText)

    def createCentralWidget(self):
        widget = QtGui.QWidget()
        widget.setLayout(self.createWidgetLayout())
        return widget

    def createWidgetLayout(self):
        layout = QtGui.QGridLayout()
        layout.addLayout(self.createTopLayout(), 0 ,0)
        layout.addLayout(self.createBoardLayout(), 1, 0)
        return layout

    def createTopLayout(self):
        topLayout = QtGui.QVBoxLayout()
        topLayout.addWidget(self.createMineCounter())
        topLayout.addWidget(self.createTimeLabel())
        topLayout.addWidget(self.createNewGameButton())
        return topLayout

    def createMineCounter(self):
        self.mineCounter = QtGui.QLabel()
        return self.mineCounter

    def createTimeLabel(self):
        self.timeLabel = QtGui.QLabel("0.0 seconds")
        self.timeLabel.setStyleSheet("background-color:rgb(0, 0, 0);"
                                     "color:rgb(0,255,0)")
        return self.timeLabel

    def createNewGameButton(self):
        newGameButton = QtGui.QPushButton("&New Game")
        newGameButton.setEnabled(True)
        newGameButton.clicked.connect(self.newGame)
        return newGameButton

    def createBoardLayout(self):
        self.boardLayout = QtGui.QGridLayout()
        self.setupFieldsLayout()
        self.drawBoard()
        return self.boardLayout

    def setupFieldsLayout(self):
        self.boardLayout.setMargin(5)
        self.boardLayout.setSpacing(5)

    def drawBoard(self):
        self.fields = [None] * self.rowsNumber
        for row in range(self.rowsNumber):
            self.fields[row] = [None] * self.columnsNumber
            for column in range(self.columnsNumber):
                self.emplaceField(row, column)

    def emplaceField(self, row, column):
        field = Field(row, column)
        field.setGameWindow(self)
        field.clicked.connect(self.revealFieldWrapper)
        self.boardLayout.addWidget(field, row, column)
        self.fields[row][column] = field

    def setupTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime)

    # Game segment
    def newGame(self):
        self.gameStarted = False
        self.timer.stop()
        self.time = QtCore.QTime(0, 0, 0)
        self.unrevealedFields = self.rowsNumber * self.columnsNumber
        self.markedMines = 0
        self.updateMineCounter()
        self.resetFields()
        self.deployMines()

    def resetFields(self):
        for row in self.fields:
            for field in row:
                field.resetField()

    def updateMineCounter(self):
        self.mineCounter.setText("Mine Counter: {}/{}".format(
            self.markedMines, self.minesNumber))

    def deployMines(self):
        for i in random.sample(range(self.rowsNumber * self.columnsNumber), self.minesNumber):
            row, column = divmod(i, self.columnsNumber)
            self.fields[row][column].isMine = True

    #Event handlers
    def updateTime(self):
        self.timeLabel.setText("{:.2f} seconds".format(
            self.time.elapsed() / 1000))

    def revealFieldWrapper(self):
        if not self.gameStarted:
            self.time.start()
            self.timer.start(100)
            self.gameStarted = True
        field = self.sender()
        self.revealField(field)

    def revealField(self, field):
        if field.isMine: # lose
            txt = "X"
            color = QtGui.QColor(222, 0, 0)
            self.timer.stop()
            self.disableAll()
        else: # reveal field
            txt = str(self.countAdjacentMines(field.row, field.column))
            color = QtGui.QColor(0, 0, 222)

        field.isRevealed = True
        self.unrevealedFields -= 1
        field.setText(txt)
        field.setEnabled(False)
        field.setPalette(QtGui.QPalette(color))

        if txt == "0": # no adjacent mines
            for r, c in self.getAdjacentFieldCoordinates(field.row,
                                                         field.column):
                if not self.fields[r][c].isRevealed:
                    self.revealField(self.fields[r][c])
        if self.unrevealedFields == self.minesNumber: # win
            self.timer.stop()

    def disableAll(self):
        for row in self.fields:
            for field in row:
                field.setEnabled(False)

    def countAdjacentMines(self, row, column):
        return sum(self.fields[r][c].isMine for r, c
                   in self.getAdjacentFieldCoordinates(row, column))

    def getAdjacentFieldCoordinates(self, row, col):
        rowsBorder = {0: (0, 1),
            self.rowsNumber - 1: (self.rowsNumber - 2, self.rowsNumber - 1)}
        columnsBorder = {0: (0, 1),
            self.columnsNumber - 1: (self.columnsNumber - 2, self.columnsNumber - 1)}
        rows = rowsBorder.get(row, (row - 1, row, row + 1))
        columns = columnsBorder.get(col, (col - 1, col, col + 1))
        return list(itertools.product(rows, columns))
