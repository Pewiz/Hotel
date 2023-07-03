# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaAdministracion import ventanaAdministracion




Bandera = None

class ventanaLogin(object):
        def __init__(self, parent=None):
                self.parent = parent
        def setupUi(self, Login):
                Login.setObjectName("Login")
                Login.resize(802, 602)
                Login.setMinimumSize(QtCore.QSize(802, 602))
                Login.setMaximumSize(QtCore.QSize(802, 602))
                font = QtGui.QFont()
                font.setFamily("Arial")
                Login.setFont(font)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Login.setWindowIcon(icon)
                Login.setWindowOpacity(1.0)
                Login.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(79,163,166,1), stop:0.61 rgba(38,98,120,1), stop:1 rgba(0,38,77,1));\n"
        "")
                self.centralwidget = QtWidgets.QWidget(Login)
                self.centralwidget.setObjectName("centralwidget")
                self.labelFondoLogin = QtWidgets.QLabel(self.centralwidget)
                self.labelFondoLogin.setGeometry(QtCore.QRect(235, 239, 341, 261))
                self.labelFondoLogin.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);\n"
        "border-radius: 25px;")
                self.labelFondoLogin.setText("")
                self.labelFondoLogin.setObjectName("labelFondoLogin")
                self.labelIconUser = QtWidgets.QLabel(self.centralwidget)
                self.labelIconUser.setGeometry(QtCore.QRect(346, 151, 121, 131))
                self.labelIconUser.setStyleSheet("background-color: transparent;")
                self.labelIconUser.setText("")
                self.labelIconUser.setPixmap(QtGui.QPixmap("Recursos/IconUser.png"))
                self.labelIconUser.setScaledContents(True)
                self.labelIconUser.setObjectName("labelIconUser")
                self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
                self.labelTitulo.setGeometry(QtCore.QRect(3, 5, 801, 91))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(39)
                font.setBold(True)
                font.setWeight(75)
                self.labelTitulo.setFont(font)
                self.labelTitulo.setStyleSheet("background-color: transparent;\n"
        "color: rgb(255, 255, 255);")
                self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
                self.labelTitulo.setObjectName("labelTitulo")
                self.labelIconUserName = QtWidgets.QLabel(self.centralwidget)
                self.labelIconUserName.setGeometry(QtCore.QRect(276, 300, 41, 41))
                self.labelIconUserName.setText("")
                self.labelIconUserName.setPixmap(QtGui.QPixmap("Recursos/IconUserName.png"))
                self.labelIconUserName.setScaledContents(True)
                self.labelIconUserName.setObjectName("labelIconUserName")
                self.labelIconPassword = QtWidgets.QLabel(self.centralwidget)
                self.labelIconPassword.setGeometry(QtCore.QRect(276, 360, 41, 41))
                self.labelIconPassword.setText("")
                self.labelIconPassword.setPixmap(QtGui.QPixmap("Recursos/IconPassword.png"))
                self.labelIconPassword.setScaledContents(True)
                self.labelIconPassword.setObjectName("labelIconPassword")
                self.BtnIniciarSesion = QtWidgets.QPushButton(self.centralwidget)
                self.BtnIniciarSesion.setGeometry(QtCore.QRect(307, 441, 201, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.BtnIniciarSesion.setFont(font)
                self.BtnIniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnIniciarSesion.setStyleSheet("color: rgb(207, 207, 207);\n"
        "background-color: rgba(0, 38, 77, 0.5);\n"
        "border-radius: 10%;")
                self.BtnIniciarSesion.setObjectName("BtnIniciarSesion")

                #Accion boton iniciar sesion
                self.BtnIniciarSesion.clicked.connect(lambda:self.cambiar_ventana(ventanaAdministracion))


                self.inputUser = QtWidgets.QLineEdit(self.centralwidget)
                self.inputUser.setGeometry(QtCore.QRect(317, 300, 211, 41))
                self.inputUser.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\n"
        "color: rgb(207, 207, 207);\n"
        "")
                self.inputUser.setMaxLength(12)
                self.inputUser.setCursorPosition(4)
                self.inputUser.setDragEnabled(False)
                self.inputUser.setObjectName("inputUser")
                self.inputUser.textEdited.connect(self.autocompletar_rut)
                self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
                self.inputPassword.setGeometry(QtCore.QRect(317, 360, 211, 41))
                self.inputPassword.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\n"
        "color: rgb(207, 207, 207);")
                self.inputPassword.setMaxLength(32768)
                self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
                self.inputPassword.setCursorPosition(11)
                self.inputPassword.setObjectName("inputPassword")
                
                Login.setCentralWidget(self.centralwidget)

                self.retranslateUi(Login)
                QtCore.QMetaObject.connectSlotsByName(Login)

        def retranslateUi(self, Login):
                _translate = QtCore.QCoreApplication.translate
                Login.setWindowTitle(_translate("Login", "Hotel"))
                self.labelTitulo.setText(_translate("Login", "Centro Veterinario Integral"))
                self.BtnIniciarSesion.setText(_translate("Login", "Iniciar Sesión"))
                self.inputUser.setPlaceholderText(_translate("Login","Rut"))
                self.inputPassword.setPlaceholderText(_translate("Login","Contraseña"))


        def verificar_credenciales(self, rut, contraseña):
                self.user = False
                #hay que poner el directorio exacto
                with open('ArchivosCSV/Usuarios.csv', 'r', newline='') as file:
                        reader = csv.reader(file)
                        next(reader) 
                        for row in reader:
                                if row[7] == rut:
                                        self.user = True
                                        if row[6] == contraseña:
                                                return True
                return False
        
        def verificar_admin(self,rut,contraseña):
                global Bandera
                with open('ArchivosCSV/Usuarios.csv', 'r', newline='') as file:
                        reader = csv.reader(file)
                        next(reader)
                        for row in reader:
                                if row[7] == rut and row[6] == contraseña:
                                        if row[10] == "Administrador":
                                                Bandera = True
                                        else:
                                                Bandera = False




        def cambiar_ventana(self, nombreVentana):

                
                rut = self.inputUser.text()
                contraseña = self.inputPassword.text()
                
                if self.verificar_credenciales(rut, contraseña):
                        self.inputUser.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\n"
                        "color: rgb(207, 207, 207);\n")
                        self.inputPassword.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\n"
                        "color: rgb(207, 207, 207);")
                        self.verificar_admin(rut,contraseña)
                        self.uiVentanaActual= QtWidgets.QApplication.activeWindow()
                        self.uiVentanaActual.close()
                        self.nuevaVentana = QtWidgets.QMainWindow()
                        self.ui = nombreVentana()
                        self.ui.setupUi(self.nuevaVentana)
                        self.nuevaVentana.show()
                else:
                        QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'RUT o contraseña incorrectos.')
                        if self.user == False:
                                self.inputUser.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\ncolor: rgb(207, 207, 207);\nborder: 1px solid #ff0000;\n")
                        else:
                                self.inputUser.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\n"
                                "color: rgb(207, 207, 207);\n")
                        self.inputPassword.setStyleSheet("background-color: rgba(0, 38, 77, 0.5);\ncolor: rgb(207, 207, 207);\nborder: 1px solid #ff0000;\n")

        
        def autocompletar_rut(self, rut):
                rut_limpio = rut.replace(".", "").replace("-", "")
                rut_formateado = self.formatear_rut(rut_limpio)
                self.inputUser.blockSignals(True)
                self.inputUser.setText(rut_formateado)
                self.inputUser.setCursorPosition(len(rut_formateado))
                self.inputUser.blockSignals(False)
        
        def formatear_rut(self, rut):
                rut_formateado = ""
                if len(rut) > 1:
                        parte_entera = rut[:-1]
                        digito_verificador = rut[-1]
                        parte_entera_formateada = "{:,}".format(int(parte_entera)).replace(",", ".")
                        rut_formateado = f"{parte_entera_formateada}-{digito_verificador}"
                elif len(rut) == 1:
                        rut_formateado = rut
                return rut_formateado
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = ventanaLogin()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
