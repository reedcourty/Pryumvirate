#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from PySide import QtGui, QtCore

import gui
import controller
        
def main(args):
    app = QtGui.QApplication(args)
    app_controller = controller.Controller()
    win = gui.MainWindow(app_controller)
    app_controller.gui = win
    app_controller.init_services()
    win.show()
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
                app, QtCore.SLOT("quit()"))
    app.exec_()

if __name__=="__main__":
    main(sys.argv)
