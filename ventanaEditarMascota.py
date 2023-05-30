# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaEditarMascota.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditarMascota(object):
    def setupUi(self, EditarMascota):
        EditarMascota.setObjectName("EditarMascota")
        EditarMascota.resize(802, 602)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditarMascota.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(EditarMascota)
        self.centralwidget.setObjectName("centralwidget")
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
        self.BtnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAtras.setGeometry(QtCore.QRect(20, 15, 51, 51))
        self.BtnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAtras.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-radius: 10px;")
        self.BtnAtras.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Recursos/FotoBtnAtras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnAtras.setIcon(icon1)
        self.BtnAtras.setIconSize(QtCore.QSize(50, 50))
        self.BtnAtras.setObjectName("BtnAtras")
        self.labelEditarDatosMascota = QtWidgets.QLabel(self.centralwidget)
        self.labelEditarDatosMascota.setGeometry(QtCore.QRect(40, 130, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.labelEditarDatosMascota.setFont(font)
        self.labelEditarDatosMascota.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-radius: 18%;")
        self.labelEditarDatosMascota.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelEditarDatosMascota.setIndent(29)
        self.labelEditarDatosMascota.setObjectName("labelEditarDatosMascota")
        self.labelIconFlechaAbajo = QtWidgets.QLabel(self.centralwidget)
        self.labelIconFlechaAbajo.setGeometry(QtCore.QRect(359, 136, 31, 31))
        self.labelIconFlechaAbajo.setText("")
        self.labelIconFlechaAbajo.setPixmap(QtGui.QPixmap("Recursos/IconFlechaAbajo.png"))
        self.labelIconFlechaAbajo.setScaledContents(True)
        self.labelIconFlechaAbajo.setObjectName("labelIconFlechaAbajo")
        self.labelFotoPerrito = QtWidgets.QLabel(self.centralwidget)
        self.labelFotoPerrito.setGeometry(QtCore.QRect(507, 191, 281, 271))
        self.labelFotoPerrito.setText("")
        self.labelFotoPerrito.setPixmap(QtGui.QPixmap("Recursos/FotoPerrito.png"))
        self.labelFotoPerrito.setScaledContents(True)
        self.labelFotoPerrito.setObjectName("labelFotoPerrito")
        self.labelNombre = QtWidgets.QLabel(self.centralwidget)
        self.labelNombre.setGeometry(QtCore.QRect(35, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelNombre.setFont(font)
        self.labelNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNombre.setObjectName("labelNombre")
        self.inputNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNombre.setGeometry(QtCore.QRect(50, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inputNombre.setFont(font)
        self.inputNombre.setText("")
        self.inputNombre.setObjectName("inputNombre")
        self.labelApellido = QtWidgets.QLabel(self.centralwidget)
        self.labelApellido.setGeometry(QtCore.QRect(254, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelApellido.setFont(font)
        self.labelApellido.setAlignment(QtCore.Qt.AlignCenter)
        self.labelApellido.setObjectName("labelApellido")
        self.inputEspecie = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEspecie.setGeometry(QtCore.QRect(270, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inputEspecie.setFont(font)
        self.inputEspecie.setText("")
        self.inputEspecie.setObjectName("inputEspecie")
        self.inputRaza = QtWidgets.QLineEdit(self.centralwidget)
        self.inputRaza.setGeometry(QtCore.QRect(50, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inputRaza.setFont(font)
        self.inputRaza.setText("")
        self.inputRaza.setObjectName("inputRaza")
        self.labelRut = QtWidgets.QLabel(self.centralwidget)
        self.labelRut.setGeometry(QtCore.QRect(51, 280, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelRut.setFont(font)
        self.labelRut.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRut.setObjectName("labelRut")
        self.labelFechaNacimiento = QtWidgets.QLabel(self.centralwidget)
        self.labelFechaNacimiento.setGeometry(QtCore.QRect(53, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelFechaNacimiento.setFont(font)
        self.labelFechaNacimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
        self.dateEditFechaNacimiento = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEditFechaNacimiento.setGeometry(QtCore.QRect(50, 400, 151, 31))
        self.dateEditFechaNacimiento.setObjectName("dateEditFechaNacimiento")
        self.labelPeso = QtWidgets.QLabel(self.centralwidget)
        self.labelPeso.setGeometry(QtCore.QRect(266, 451, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelPeso.setFont(font)
        self.labelPeso.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPeso.setObjectName("labelPeso")
        self.inputPeso = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPeso.setGeometry(QtCore.QRect(309, 456, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inputPeso.setFont(font)
        self.inputPeso.setText("")
        self.inputPeso.setObjectName("inputPeso")
        self.labelSize = QtWidgets.QLabel(self.centralwidget)
        self.labelSize.setGeometry(QtCore.QRect(268, 360, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelSize.setFont(font)
        self.labelSize.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSize.setObjectName("labelSize")
        self.labelSexo = QtWidgets.QLabel(self.centralwidget)
        self.labelSexo.setGeometry(QtCore.QRect(268, 281, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelSexo.setFont(font)
        self.labelSexo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSexo.setObjectName("labelSexo")
        self.comboBoxSexo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSexo.setGeometry(QtCore.QRect(270, 320, 81, 31))
        self.comboBoxSexo.setObjectName("comboBoxSexo")
        self.comboBoxSexo.addItem("")
        self.comboBoxSexo.addItem("")
        self.comboBoxSexo.addItem("")
        self.BtnGuardarMascotaEditada = QtWidgets.QPushButton(self.centralwidget)
        self.BtnGuardarMascotaEditada.setGeometry(QtCore.QRect(638, 545, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnGuardarMascotaEditada.setFont(font)
        self.BtnGuardarMascotaEditada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnGuardarMascotaEditada.setStyleSheet("background-color: rgb(79, 163, 166);\n"
"border-radius:15px;")
        self.BtnGuardarMascotaEditada.setObjectName("BtnGuardarMascotaEditada")
        self.comboBoxSize = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSize.setGeometry(QtCore.QRect(270, 400, 81, 31))
        self.comboBoxSize.setObjectName("comboBoxSize")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.labelKg = QtWidgets.QLabel(self.centralwidget)
        self.labelKg.setGeometry(QtCore.QRect(336, 452, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelKg.setFont(font)
        self.labelKg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelKg.setObjectName("labelKg")
        EditarMascota.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditarMascota)
        QtCore.QMetaObject.connectSlotsByName(EditarMascota)

    def retranslateUi(self, EditarMascota):
        _translate = QtCore.QCoreApplication.translate
        EditarMascota.setWindowTitle(_translate("EditarMascota", "Hotel"))
        self.labelTitulo.setText(_translate("EditarMascota", "Editar Mascota"))
        self.labelEditarDatosMascota.setText(_translate("EditarMascota", "Datos del nueva mascota"))
        self.labelNombre.setText(_translate("EditarMascota", "Nombre"))
        self.labelApellido.setText(_translate("EditarMascota", "Especie"))
        self.labelRut.setText(_translate("EditarMascota", "Raza"))
        self.labelFechaNacimiento.setText(_translate("EditarMascota", "Fecha de Nacimiento"))
        self.labelPeso.setText(_translate("EditarMascota", "Peso"))
        self.labelSize.setText(_translate("EditarMascota", "Tamaño"))
        self.labelSexo.setText(_translate("EditarMascota", "Sexo"))
        self.comboBoxSexo.setItemText(0, _translate("EditarMascota", "Elegir"))
        self.comboBoxSexo.setItemText(1, _translate("EditarMascota", "Hembra"))
        self.comboBoxSexo.setItemText(2, _translate("EditarMascota", "Macho"))
        self.BtnGuardarMascotaEditada.setText(_translate("EditarMascota", "Aceptar"))
        self.comboBoxSize.setItemText(0, _translate("EditarMascota", "Elegir"))
        self.comboBoxSize.setItemText(1, _translate("EditarMascota", "Pequeño"))
        self.comboBoxSize.setItemText(2, _translate("EditarMascota", "Mediano"))
        self.comboBoxSize.setItemText(3, _translate("EditarMascota", "Grande"))
        self.labelKg.setText(_translate("EditarMascota", "kg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarMascota = QtWidgets.QMainWindow()
    ui = Ui_EditarMascota()
    ui.setupUi(EditarMascota)
    EditarMascota.show()
    sys.exit(app.exec_())
