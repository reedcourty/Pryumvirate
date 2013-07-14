#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PySide import QtGui, QtCore

class MyError(Exception):
    pass

class MainWindow(QtGui.QMainWindow):
    controller = None

    def __init__(self, controller, *args):
        apply(QtGui.QMainWindow.__init__, (self,) + args)
        self.resize(420, 450)
        self.setWindowTitle('Pryumvirate')
        self.setWindowIcon(QtGui.QIcon('resources/icons/pryumvirate.png'))

        self.groupBox_Services = QtGui.QGroupBox(self)
        self.groupBox_Services.setGeometry(QtCore.QRect(10, 340, 401, 51))
        self.groupBox_Services.setTitle(u"Szolgáltatások")
        
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_Services)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 381, 31))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        
        self.checkBox_twitter = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_twitter.setText(u"Twitter")
        self.checkBox_twitter.setCheckState(QtCore.Qt.Checked)
        self.horizontalLayout.addWidget(self.checkBox_twitter)
        
        self.checkBox_plurk = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_plurk.setText(u"Plurk")
        self.checkBox_plurk.setCheckState(QtCore.Qt.Checked)
        self.horizontalLayout.addWidget(self.checkBox_plurk)
        
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 400, 401, 41))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_OK = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_OK.setText(u"Mehet!")
        self.connect(self.pushButton_OK, QtCore.SIGNAL('clicked()'), self.OK_klikk)
        
        self.horizontalLayout_2.addWidget(self.pushButton_OK)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_Quit = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Quit.setText(u"Hagyjuk!")
        self.connect(self.pushButton_Quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        
        self.horizontalLayout_2.addWidget(self.pushButton_Quit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.groupBox_output = QtGui.QGroupBox(self)
        self.groupBox_output.setGeometry(QtCore.QRect(10, 10, 401, 191))
        self.groupBox_output.setTitle(u"Eredmény")
        
        self.plainTextEdit_output = QtGui.QPlainTextEdit(self.groupBox_output)
        self.plainTextEdit_output.setGeometry(QtCore.QRect(10, 20, 381, 161))
        self.plainTextEdit_output.setReadOnly(True)
        
        self.groupBox_input = QtGui.QGroupBox(self)
        self.groupBox_input.setGeometry(QtCore.QRect(10, 200, 401, 131))
        self.groupBox_input.setTitle(u"Post")
        
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox_input)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 381, 107))
        
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        
        self.plainTextEdit_input = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_input.setMaximumBlockCount(0)
        self.plainTextEdit_input.setPlainText(u"Na mesélj valamit! :)")
        self.plainTextEdit_input.selectAll()
        self.plainTextEdit_input.setFocus() 
        
        self.gridLayout.addWidget(self.plainTextEdit_input, 0, 0, 1, 6)
        self.label_jelenleg = QtGui.QLabel(self.gridLayoutWidget)
        self.label_jelenleg.setText(str(len(self.plainTextEdit_input.toPlainText().encode('utf-8'))))
        self.connect(self.plainTextEdit_input, QtCore.SIGNAL('textChanged()'), self.ChangeLimits)
        self.gridLayout.addWidget(self.label_jelenleg, 2, 1, 1, 1)
        
        self.label_hatravan = QtGui.QLabel(self.gridLayoutWidget)
        self.label_hatravan.setText(str(140-len(self.plainTextEdit_input.toPlainText().encode('utf-8'))))
        self.gridLayout.addWidget(self.label_hatravan, 2, 3, 1, 1)
        
        self.pushButton_Clear = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Clear.setText(u"Töröld!")
        self.connect(self.pushButton_Clear, QtCore.SIGNAL('clicked()'), self.ClearTextFields)
        self.gridLayout.addWidget(self.pushButton_Clear, 2, 5, 1, 1)
        
        
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 4, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.controller = controller

    def ChangeLimits(self):
        self.label_jelenleg.setText(str(len(self.plainTextEdit_input.toPlainText())))
        self.label_hatravan.setText(str(140-len(self.plainTextEdit_input.toPlainText())))
        
    def ClearTextFields(self):
        self.plainTextEdit_input.clear()
        self.plainTextEdit_output.clear()
        
    def OK_klikk(self):
        self.setWindowTitle('Pryumvirate - Dolgozom...')
        if (len(self.plainTextEdit_input.toPlainText()) < 141):
            post = str(self.plainTextEdit_input.toPlainText().encode('utf-8'))
            post = post.replace(":)", "ツ")
            self.controller.send(post)
        else:
            limiterror_str = u"Ha jól számolom, ez több, mint 140 karakter. Próbálj meg tömörebben fogalmazni!"
            limiterror = QtGui.QMessageBox.critical(self, u'Hm...', limiterror_str)
        self.setWindowTitle('Pryumvirate')