# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListaMascota.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ventanaListaMascotas(object):
    def setupUi(self, ListaMascotas):
        ListaMascotas.setObjectName("ListaMascotas")
        ListaMascotas.resize(802, 602)
        font = QtGui.QFont()
        font.setFamily("Arial")
        ListaMascotas.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ListaMascotas.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ListaMascotas)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAtras.setGeometry(QtCore.QRect(20, 15, 51, 51))
        self.BtnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAtras.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius: 10px;")
        self.BtnAtras.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Recursos/FotoBtnAtras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnAtras.setIcon(icon1)
        self.BtnAtras.setIconSize(QtCore.QSize(50, 50))
        self.BtnAtras.setObjectName("BtnAtras")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(-20, 0, 831, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelFotoPerrito = QtWidgets.QLabel(self.centralwidget)
        self.labelFotoPerrito.setGeometry(QtCore.QRect(520, 170, 281, 271))
        self.labelFotoPerrito.setText("")
        self.labelFotoPerrito.setPixmap(QtGui.QPixmap("Recursos/FotoPerrito.png"))
        self.labelFotoPerrito.setScaledContents(True)
        self.labelFotoPerrito.setObjectName("labelFotoPerrito")
        self.BtnVerDatos = QtWidgets.QPushButton(self.centralwidget)
        self.BtnVerDatos.setGeometry(QtCore.QRect(32, 460, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnVerDatos.setFont(font)
        self.BtnVerDatos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnVerDatos.setStyleSheet("background-color: rgb(0, 177, 15);\n" "border-radius:15px;")
        self.BtnVerDatos.setObjectName("BtnVerDatos")
        self.BtnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEditar.setGeometry(QtCore.QRect(196, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnEditar.setFont(font)
        self.BtnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEditar.setStyleSheet("background-color: rgb(251, 255, 0);\n" "border-radius:15px;")
        self.BtnEditar.setObjectName("BtnEditar")
        self.BtnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEliminar.setGeometry(QtCore.QRect(368, 460, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnEliminar.setFont(font)
        self.BtnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEliminar.setStyleSheet("background-color: rgb(255, 0, 0);\n" "border-radius:15px;")
        self.BtnEliminar.setObjectName("BtnEliminar")
        self.tablaListaMascotas = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaListaMascotas.setGeometry(QtCore.QRect(30, 160, 481, 291))
        self.tablaListaMascotas.setAutoFillBackground(False)
        self.tablaListaMascotas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaListaMascotas.setObjectName("tablaListaMascotas")
        self.tablaListaMascotas.setColumnCount(3)
        self.tablaListaMascotas.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tablaListaMascotas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tablaListaMascotas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tablaListaMascotas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tablaListaMascotas.setHorizontalHeaderItem(2, item)
        self.tablaListaMascotas.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaListaMascotas.horizontalHeader().setDefaultSectionSize(129)
        self.tablaListaMascotas.horizontalHeader().setHighlightSections(True)
        self.tablaListaMascotas.horizontalHeader().setMinimumSectionSize(117)
        self.tablaListaMascotas.horizontalHeader().setSortIndicatorShown(False)
        self.tablaListaMascotas.horizontalHeader().setStretchLastSection(True)
        self.tablaListaMascotas.verticalHeader().setVisible(True)
        self.tablaListaMascotas.verticalHeader().setCascadingSectionResizes(True)
        self.tablaListaMascotas.verticalHeader().setHighlightSections(True)
        self.tablaListaMascotas.verticalHeader().setSortIndicatorShown(False)
        self.tablaListaMascotas.verticalHeader().setStretchLastSection(False)
        self.BtnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAceptar.setGeometry(QtCore.QRect(642, 541, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnAceptar.setFont(font)
        self.BtnAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAceptar.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius:15px;")
        self.BtnAceptar.setObjectName("BtnAceptar")
        self.labelMascotasDe = QtWidgets.QLabel(self.centralwidget)
        self.labelMascotasDe.setGeometry(QtCore.QRect(29, 114, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelMascotasDe.setFont(font)
        self.labelMascotasDe.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius: 12px;")
        self.labelMascotasDe.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMascotasDe.setIndent(162)
        self.labelMascotasDe.setObjectName("labelMascotasDe")
        self.BtnNuevaMascota = QtWidgets.QPushButton(self.centralwidget)
        self.BtnNuevaMascota.setGeometry(QtCore.QRect(516, 160, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.BtnNuevaMascota.setFont(font)
        self.BtnNuevaMascota.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnNuevaMascota.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.BtnNuevaMascota.setObjectName("BtnNuevaMascota")
        self.labelNombreDelPropietario = QtWidgets.QLabel(self.centralwidget)
        self.labelNombreDelPropietario.setGeometry(QtCore.QRect(281, 119, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelNombreDelPropietario.setFont(font)
        self.labelNombreDelPropietario.setObjectName("labelNombreDelPropietario")
        self.labelTitulo.raise_()
        self.labelFotoPerrito.raise_()
        self.BtnVerDatos.raise_()
        self.BtnEditar.raise_()
        self.BtnEliminar.raise_()
        self.tablaListaMascotas.raise_()
        self.BtnAceptar.raise_()
        self.labelMascotasDe.raise_()
        self.BtnNuevaMascota.raise_()
        self.BtnAtras.raise_()
        self.labelNombreDelPropietario.raise_()
        ListaMascotas.setCentralWidget(self.centralwidget)

        self.retranslateUi(ListaMascotas)
        QtCore.QMetaObject.connectSlotsByName(ListaMascotas)

    def retranslateUi(self, ListaMascotas):
        _translate = QtCore.QCoreApplication.translate
        ListaMascotas.setWindowTitle(_translate("ListaMascotas", "Hotel"))
        self.labelTitulo.setText(_translate("ListaMascotas", "Lista Mascotas"))
        self.BtnVerDatos.setText(_translate("ListaMascotas", "Ver datos"))
        self.BtnEditar.setText(_translate("ListaMascotas", "Editar"))
        self.BtnEliminar.setText(_translate("ListaMascotas", "Eliminar"))
        item = self.tablaListaMascotas.verticalHeaderItem(0)
        item.setText(_translate("ListaMascotas", "Nueva fila"))
        item = self.tablaListaMascotas.horizontalHeaderItem(0)
        item.setText(_translate("ListaMascotas", "Id"))
        item = self.tablaListaMascotas.horizontalHeaderItem(1)
        item.setText(_translate("ListaMascotas", "Nombre"))
        item = self.tablaListaMascotas.horizontalHeaderItem(2)
        item.setText(_translate("ListaMascotas", "Especie"))
        self.BtnAceptar.setText(_translate("ListaMascotas", "Aceptar"))
        self.labelMascotasDe.setText(_translate("ListaMascotas", "Mascotas de "))
        self.BtnNuevaMascota.setText(_translate("ListaMascotas", "+"))
        self.labelNombreDelPropietario.setText(_translate("ListaMascotas", "nombre del dueño"))



