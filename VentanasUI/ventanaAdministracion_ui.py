# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\asus\OneDrive\Documentos\GitHub\Hotel\VentanasUI\ventanaAdministracion.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Administracion(object):
    def setupUi(self, Administracion):
        Administracion.setObjectName("Administracion")
        Administracion.resize(802, 602)
        Administracion.setMinimumSize(QtCore.QSize(802, 602))
        Administracion.setMaximumSize(QtCore.QSize(802, 602))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        Administracion.setFont(font)
        Administracion.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\Hotel\\VentanasUI\\../Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Administracion.setWindowIcon(icon)
        Administracion.setToolTip("")
        Administracion.setWhatsThis("")
        Administracion.setAccessibleName("")
        Administracion.setAccessibleDescription("")
        Administracion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Administracion)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(-20, 0, 831, 81))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.BtnGestionDeHabitacion = QtWidgets.QPushButton(self.centralwidget)
        self.BtnGestionDeHabitacion.setGeometry(QtCore.QRect(90, 167, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.BtnGestionDeHabitacion.setFont(font)
        self.BtnGestionDeHabitacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnGestionDeHabitacion.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: #4fa3a6;\n"
"}\n"
"QPushButton::hover {\n"
"    background: rgb(181, 181, 181) ;\n"
"}")
        self.BtnGestionDeHabitacion.setObjectName("BtnGestionDeHabitacion")
        self.BtnAdministracionDeUsuarios = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAdministracionDeUsuarios.setGeometry(QtCore.QRect(91, 290, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.BtnAdministracionDeUsuarios.setFont(font)
        self.BtnAdministracionDeUsuarios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAdministracionDeUsuarios.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: #4fa3a6;\n"
"}\n"
"QPushButton::hover {\n"
"    background: rgb(181, 181, 181) ;\n"
"}")
        self.BtnAdministracionDeUsuarios.setObjectName("BtnAdministracionDeUsuarios")
        self.labelFotoPerrito = QtWidgets.QLabel(self.centralwidget)
        self.labelFotoPerrito.setGeometry(QtCore.QRect(419, 142, 371, 321))
        self.labelFotoPerrito.setText("")
        self.labelFotoPerrito.setPixmap(QtGui.QPixmap("c:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\Hotel\\VentanasUI\\../Recursos/FotoPerrito.png"))
        self.labelFotoPerrito.setScaledContents(True)
        self.labelFotoPerrito.setObjectName("labelFotoPerrito")
        self.BtnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAtras.setGeometry(QtCore.QRect(20, 15, 51, 51))
        self.BtnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAtras.setStyleSheet("QPushButton {\n"
"  \n"
"    \n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 20px;\n"
"\n"
"  \n"
"}\n"
"\n"
"\n"
"QPushButton::hover {\n"
"    background: #74b6b6;\n"
"}\n"
"")
        self.BtnAtras.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\Hotel\\VentanasUI\\../Recursos/FotoBtnAtras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnAtras.setIcon(icon1)
        self.BtnAtras.setIconSize(QtCore.QSize(50, 50))
        self.BtnAtras.setObjectName("BtnAtras")
        self.BtnListaUsuarios = QtWidgets.QPushButton(self.centralwidget)
        self.BtnListaUsuarios.setGeometry(QtCore.QRect(90, 420, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.BtnListaUsuarios.setFont(font)
        self.BtnListaUsuarios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnListaUsuarios.setStyleSheet("QPushButton{\n"
"    border-radius: 13px;\n"
"    background-color: #4fa3a6;\n"
"}\n"
"QPushButton::hover {\n"
"    background: rgb(181, 181, 181) ;\n"
"}")
        self.BtnListaUsuarios.setObjectName("BtnListaUsuarios")
        Administracion.setCentralWidget(self.centralwidget)

        self.retranslateUi(Administracion)
        QtCore.QMetaObject.connectSlotsByName(Administracion)

    def retranslateUi(self, Administracion):
        _translate = QtCore.QCoreApplication.translate
        Administracion.setWindowTitle(_translate("Administracion", "Hotel"))
        self.labelTitulo.setText(_translate("Administracion", "Administración"))
        self.BtnGestionDeHabitacion.setText(_translate("Administracion", "Gestion de habitacion"))
        self.BtnAdministracionDeUsuarios.setText(_translate("Administracion", "Administración de usuarios"))
        self.BtnListaUsuarios.setText(_translate("Administracion", "Lista de Reservas de Clientes"))
