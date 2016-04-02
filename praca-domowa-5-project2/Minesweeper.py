from GameWindow import GameWindow

from PyQt4 import QtGui

import sys

if __name__ == "__main__":
    application = QtGui.QApplication(sys.argv)
    window = GameWindow()
    window.newGame()
    sys.exit(application.exec_())
