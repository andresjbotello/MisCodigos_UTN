# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Grabacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 244)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/2x/baseline_mic_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 120, 41, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGrabar = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGrabar.sizePolicy().hasHeightForWidth())
        self.btnGrabar.setSizePolicy(sizePolicy)
        self.btnGrabar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnGrabar.setText("")
        self.btnGrabar.setIcon(icon)
        self.btnGrabar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnGrabar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnGrabar.setObjectName("btnGrabar")
        self.gridLayout.addWidget(self.btnGrabar, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 120, 41, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnParar = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.btnParar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnParar.sizePolicy().hasHeightForWidth())
        self.btnParar.setSizePolicy(sizePolicy)
        self.btnParar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/2x/baseline_stop_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnParar.setIcon(icon1)
        self.btnParar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnParar.setObjectName("btnParar")
        self.gridLayout_2.addWidget(self.btnParar, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(80, 120, 41, 41))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnRepetirGrab = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.btnRepetirGrab.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRepetirGrab.sizePolicy().hasHeightForWidth())
        self.btnRepetirGrab.setSizePolicy(sizePolicy)
        self.btnRepetirGrab.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnRepetirGrab.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/2x/baseline_replay_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRepetirGrab.setIcon(icon2)
        self.btnRepetirGrab.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnRepetirGrab.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnRepetirGrab.setObjectName("btnRepetirGrab")
        self.gridLayout_4.addWidget(self.btnRepetirGrab, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(400, 160, 131, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnGuardar = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout_3.addWidget(self.btnGuardar, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(250, 0, 21, 161))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(270, 20, 261, 21))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.txtBoxNombre = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_6)
        self.txtBoxNombre.setEnabled(False)
        self.txtBoxNombre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtBoxNombre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtBoxNombre.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txtBoxNombre.setPlaceholderText("")
        self.txtBoxNombre.setObjectName("txtBoxNombre")
        self.gridLayout_6.addWidget(self.txtBoxNombre, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(270, 0, 261, 21))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lblNombre = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout_7.addWidget(self.lblNombre, 0, 0, 1, 1)
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(270, 40, 261, 21))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblAutor = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.lblAutor.setObjectName("lblAutor")
        self.gridLayout_8.addWidget(self.lblAutor, 0, 0, 1, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(270, 60, 261, 21))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.txtBoxAutor = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_9)
        self.txtBoxAutor.setEnabled(False)
        self.txtBoxAutor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtBoxAutor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtBoxAutor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txtBoxAutor.setPlaceholderText("")
        self.txtBoxAutor.setObjectName("txtBoxAutor")
        self.gridLayout_9.addWidget(self.txtBoxAutor, 1, 0, 1, 1)
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(270, 80, 261, 21))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lblDescripcion = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.lblDescripcion.setObjectName("lblDescripcion")
        self.gridLayout_10.addWidget(self.lblDescripcion, 0, 0, 1, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 251, 121))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.widgetVideo = QVideoWidget(self.gridLayoutWidget_11)
        self.widgetVideo.setObjectName("widgetVideo")
        self.gridLayout_11.addWidget(self.widgetVideo, 0, 0, 1, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(270, 100, 261, 61))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.txtBoxDescripcion = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_12)
        self.txtBoxDescripcion.setEnabled(False)
        self.txtBoxDescripcion.setObjectName("txtBoxDescripcion")
        self.gridLayout_12.addWidget(self.txtBoxDescripcion, 0, 0, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(130, 120, 41, 41))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.btnReproducir = QtWidgets.QToolButton(self.gridLayoutWidget_13)
        self.btnReproducir.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReproducir.sizePolicy().hasHeightForWidth())
        self.btnReproducir.setSizePolicy(sizePolicy)
        self.btnReproducir.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnReproducir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/2x/baseline_play_circle_filled_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReproducir.setIcon(icon3)
        self.btnReproducir.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnReproducir.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnReproducir.setObjectName("btnReproducir")
        self.gridLayout_13.addWidget(self.btnReproducir, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(170, 120, 41, 41))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.btnPausar = QtWidgets.QToolButton(self.gridLayoutWidget_14)
        self.btnPausar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPausar.sizePolicy().hasHeightForWidth())
        self.btnPausar.setSizePolicy(sizePolicy)
        self.btnPausar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnPausar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/2x/baseline_pause_circle_filled_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPausar.setIcon(icon4)
        self.btnPausar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnPausar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnPausar.setObjectName("btnPausar")
        self.gridLayout_14.addWidget(self.btnPausar, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(210, 120, 41, 41))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.btnRepetirRep = QtWidgets.QToolButton(self.gridLayoutWidget_15)
        self.btnRepetirRep.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRepetirRep.sizePolicy().hasHeightForWidth())
        self.btnRepetirRep.setSizePolicy(sizePolicy)
        self.btnRepetirRep.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnRepetirRep.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/2x/baseline_first_page_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRepetirRep.setIcon(icon5)
        self.btnRepetirRep.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnRepetirRep.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnRepetirRep.setObjectName("btnRepetirRep")
        self.gridLayout_15.addWidget(self.btnRepetirRep, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_16.setGeometry(QtCore.QRect(120, 120, 16, 41))
        self.gridLayoutWidget_16.setObjectName("gridLayoutWidget_16")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget_16)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_16.addWidget(self.line_2, 0, 0, 1, 1)
        self.gridLayoutWidget_17 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_17.setGeometry(QtCore.QRect(0, 160, 401, 41))
        self.gridLayoutWidget_17.setObjectName("gridLayoutWidget_17")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.lblShortcut = QtWidgets.QLabel(self.gridLayoutWidget_17)
        self.lblShortcut.setObjectName("lblShortcut")
        self.gridLayout_17.addWidget(self.lblShortcut, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGrabar_Audio = QtWidgets.QAction(MainWindow)
        self.actionGrabar_Audio.setObjectName("actionGrabar_Audio")
        self.actionAbrir_Audio = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Audio.setObjectName("actionAbrir_Audio")
        self.menuMenu.addAction(self.actionGrabar_Audio)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbrir_Audio)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grabacion"))
        self.btnGrabar.setToolTip(_translate("MainWindow", "Comezar grabación"))
        self.btnGrabar.setShortcut(_translate("MainWindow", "G"))
        self.btnParar.setToolTip(_translate("MainWindow", "Detener Grabación"))
        self.btnParar.setShortcut(_translate("MainWindow", "P"))
        self.btnRepetirGrab.setToolTip(_translate("MainWindow", "Reiniciar Grabación"))
        self.btnRepetirGrab.setShortcut(_translate("MainWindow", "G"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        self.txtBoxNombre.setToolTip(_translate("MainWindow", "Insertar Nombre del Audio"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre del Audio"))
        self.lblAutor.setText(_translate("MainWindow", "Autor del Audio"))
        self.txtBoxAutor.setToolTip(_translate("MainWindow", "Insertar Nombre del Audio"))
        self.lblDescripcion.setText(_translate("MainWindow", "Descripción del Audio"))
        self.txtBoxDescripcion.setToolTip(_translate("MainWindow", "Inserte Descripcion del Audio"))
        self.btnReproducir.setToolTip(_translate("MainWindow", "Iniciar Reproducción"))
        self.btnReproducir.setShortcut(_translate("MainWindow", "G"))
        self.btnPausar.setToolTip(_translate("MainWindow", "Pausar Reproducción"))
        self.btnPausar.setShortcut(_translate("MainWindow", "G"))
        self.btnRepetirRep.setToolTip(_translate("MainWindow", "Reiniciar Reproducción"))
        self.btnRepetirRep.setShortcut(_translate("MainWindow", "G"))
        self.lblShortcut.setText(_translate("MainWindow", "Tambien puede presionar \"G\" para grabar y \"P\" para detener la grabación."))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionGrabar_Audio.setText(_translate("MainWindow", "Grabar Audio"))
        self.actionAbrir_Audio.setText(_translate("MainWindow", "Abrir Audio"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
