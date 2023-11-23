# export QT_DEBUG_PLUGINS=1
import sys
from PyQt5 import QtWidgets
from views import View


app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
view = View(mainWindow)
view.draw()
sys.exit(app.exec_())
