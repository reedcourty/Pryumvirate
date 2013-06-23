#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from PySide import QtGui, QtCore

import gui
        
def main(args):
    app = QtGui.QApplication(args)
    win = gui.MainWindow()
    win.show()
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
                app, QtCore.SLOT("quit()"))
    app.exec_()

if __name__=="__main__":
    main(sys.argv)
