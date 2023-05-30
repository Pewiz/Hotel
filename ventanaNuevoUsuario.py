# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaNuevoUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from Clases.Usuario import Usuario

class ventanaNuevoUsuario(object):
        def setupUi(self, UsuarioNuevo):
                UsuarioNuevo.setObjectName("UsuarioNuevo")
                UsuarioNuevo.resize(802, 602)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                UsuarioNuevo.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(UsuarioNuevo)
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

                #Boton atras
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

                #Accion boton atras
                self.BtnAtras.clicked.connect(self.cambiar_a_ventana_anterior)

                self.labelDatosNuevoUsuario = QtWidgets.QLabel(self.centralwidget)
                self.labelDatosNuevoUsuario.setGeometry(QtCore.QRect(40, 130, 381, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(13)
                self.labelDatosNuevoUsuario.setFont(font)
                self.labelDatosNuevoUsuario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
        "border-radius: 18%;")
                self.labelDatosNuevoUsuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.labelDatosNuevoUsuario.setIndent(29)
                self.labelDatosNuevoUsuario.setObjectName("labelDatosNuevoUsuario")
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
                self.labelNombre.setGeometry(QtCore.QRect(35, 176, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelNombre.setFont(font)
                self.labelNombre.setAlignment(QtCore.Qt.AlignCenter)
                self.labelNombre.setObjectName("labelNombre")
                self.inputNombre = QtWidgets.QLineEdit(self.centralwidget)
                self.inputNombre.setGeometry(QtCore.QRect(50, 216, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputNombre.setFont(font)
                self.inputNombre.setText("")
                self.inputNombre.setObjectName("inputNombre")
                self.labelApellido = QtWidgets.QLabel(self.centralwidget)
                self.labelApellido.setGeometry(QtCore.QRect(245, 175, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelApellido.setFont(font)
                self.labelApellido.setAlignment(QtCore.Qt.AlignCenter)
                self.labelApellido.setObjectName("labelApellido")
                self.inputApellido = QtWidgets.QLineEdit(self.centralwidget)
                self.inputApellido.setGeometry(QtCore.QRect(260, 215, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputApellido.setFont(font)
                self.inputApellido.setText("")
                self.inputApellido.setObjectName("inputApellido")
                
                #Rut
                self.inputRut = QtWidgets.QLineEdit(self.centralwidget)
                self.inputRut.setGeometry(QtCore.QRect(50, 296, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputRut.setFont(font)
                self.inputRut.setText("")
                self.inputRut.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.inputRut.textEdited.connect(self.autocompletar_rut)
                self.inputRut.setObjectName("inputRut")
                self.labelRut = QtWidgets.QLabel(self.centralwidget)
                self.labelRut.setGeometry(QtCore.QRect(20, 256, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelRut.setFont(font)
                self.labelRut.setAlignment(QtCore.Qt.AlignCenter)
                self.labelRut.setObjectName("labelRut")
                self.inputRut.setMaxLength(12)

                self.labelFechaNacimiento = QtWidgets.QLabel(self.centralwidget)
                self.labelFechaNacimiento.setGeometry(QtCore.QRect(53, 335, 151, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelFechaNacimiento.setFont(font)
                self.labelFechaNacimiento.setAlignment(QtCore.Qt.AlignCenter)
                self.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
                self.dateEditFechaNacimiento = QtWidgets.QDateEdit(self.centralwidget)
                self.dateEditFechaNacimiento.setGeometry(QtCore.QRect(50, 375, 151, 31))
                self.dateEditFechaNacimiento.setObjectName("dateEditFechaNacimiento")
                self.inputCorreoElectronico = QtWidgets.QLineEdit(self.centralwidget)
                self.inputCorreoElectronico.setGeometry(QtCore.QRect(50, 454, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputCorreoElectronico.setFont(font)
                self.inputCorreoElectronico.setText("")
                self.inputCorreoElectronico.setObjectName("inputCorreoElectronico")
                self.labelCorreoElectronico = QtWidgets.QLabel(self.centralwidget)
                self.labelCorreoElectronico.setGeometry(QtCore.QRect(54, 414, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelCorreoElectronico.setFont(font)
                self.labelCorreoElectronico.setAlignment(QtCore.Qt.AlignCenter)
                self.labelCorreoElectronico.setObjectName("labelCorreoElectronico")
                self.labelDomicilio = QtWidgets.QLabel(self.centralwidget)
                self.labelDomicilio.setGeometry(QtCore.QRect(234, 340, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelDomicilio.setFont(font)
                self.labelDomicilio.setAlignment(QtCore.Qt.AlignCenter)
                self.labelDomicilio.setObjectName("labelDomicilio")
                self.inputDomicilio = QtWidgets.QLineEdit(self.centralwidget)
                self.inputDomicilio.setGeometry(QtCore.QRect(260, 380, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputDomicilio.setFont(font)
                self.inputDomicilio.setText("")
                self.inputDomicilio.setObjectName("inputDomicilio")

                #Telefono
                self.labelTelefono = QtWidgets.QLabel(self.centralwidget)
                self.labelTelefono.setGeometry(QtCore.QRect(258, 260, 71, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelTelefono.setFont(font)
                self.labelTelefono.setAlignment(QtCore.Qt.AlignCenter)
                self.labelTelefono.setObjectName("labelTelefono")
                self.inputTelefono = QtWidgets.QLineEdit(self.centralwidget)
                self.inputTelefono.setGeometry(QtCore.QRect(260, 300, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputTelefono.setFont(font)
                self.inputTelefono.setText("")
                self.inputTelefono.setObjectName("inputTelefono")
                positive_validator = QtGui.QIntValidator(1, 999999999, self.inputTelefono)
                self.inputTelefono.setValidator(positive_validator)

                self.labelGenero = QtWidgets.QLabel(self.centralwidget)
                self.labelGenero.setGeometry(QtCore.QRect(258, 414, 71, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelGenero.setFont(font)
                self.labelGenero.setAlignment(QtCore.Qt.AlignCenter)
                self.labelGenero.setObjectName("labelGenero")
                self.comboBoxGenero = QtWidgets.QComboBox(self.centralwidget)
                self.comboBoxGenero.setGeometry(QtCore.QRect(260, 450, 81, 31))
                self.comboBoxGenero.setObjectName("comboBoxGenero")
                self.comboBoxGenero.addItem("")
                self.comboBoxGenero.addItem("")
                self.comboBoxGenero.addItem("")

                #Boton agregar usuario
                self.BtnAgregarUsuario = QtWidgets.QPushButton(self.centralwidget)
                self.BtnAgregarUsuario.setGeometry(QtCore.QRect(639, 543, 151, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnAgregarUsuario.setFont(font)
                self.BtnAgregarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnAgregarUsuario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
        "border-radius:15px;")
                self.BtnAgregarUsuario.setObjectName("BtnAgregarUsuario")

                self.BtnAgregarUsuario.clicked.connect(self.agregar_usuario)

                self.labelPassword = QtWidgets.QLabel(self.centralwidget)
                self.labelPassword.setGeometry(QtCore.QRect(52, 490, 91, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelPassword.setFont(font)
                self.labelPassword.setAlignment(QtCore.Qt.AlignCenter)
                self.labelPassword.setObjectName("labelPassword")
                self.inputNewPassword = QtWidgets.QLineEdit(self.centralwidget)
                self.inputNewPassword.setGeometry(QtCore.QRect(50, 530, 151, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.inputNewPassword.sizePolicy().hasHeightForWidth())
                self.inputNewPassword.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputNewPassword.setFont(font)
                self.inputNewPassword.setText("")
                self.inputNewPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.inputNewPassword.setObjectName("inputNewPassword")
                self.comboBoxCargo = QtWidgets.QComboBox(self.centralwidget)
                self.comboBoxCargo.setGeometry(QtCore.QRect(261, 526, 81, 31))
                self.comboBoxCargo.setObjectName("comboBoxCargo")
                self.comboBoxCargo.addItem("")
                self.comboBoxCargo.addItem("")
                self.comboBoxCargo.addItem("")
                self.labelCargo = QtWidgets.QLabel(self.centralwidget)
                self.labelCargo.setGeometry(QtCore.QRect(259, 492, 71, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelCargo.setFont(font)
                self.labelCargo.setAlignment(QtCore.Qt.AlignCenter)
                self.labelCargo.setObjectName("labelCargo")
                UsuarioNuevo.setCentralWidget(self.centralwidget)

                self.retranslateUi(UsuarioNuevo)
                QtCore.QMetaObject.connectSlotsByName(UsuarioNuevo)


                self.inputNombre.textChanged.connect(self.actualizar_estado_boton)
                self.inputApellido.textChanged.connect(self.actualizar_estado_boton)
                self.inputRut.textChanged.connect(self.actualizar_estado_boton)
                self.inputNewPassword.textChanged.connect(self.actualizar_estado_boton)
                self.inputCorreoElectronico.textChanged.connect(self.actualizar_estado_boton)
                self.inputDomicilio.textChanged.connect(self.actualizar_estado_boton)
                self.inputTelefono.textChanged.connect(self.actualizar_estado_boton)
                self.comboBoxGenero.currentIndexChanged.connect(self.actualizar_estado_boton)
                self.comboBoxCargo.currentIndexChanged.connect(self.actualizar_estado_boton)

        def retranslateUi(self, UsuarioNuevo):
                _translate = QtCore.QCoreApplication.translate
                UsuarioNuevo.setWindowTitle(_translate("UsuarioNuevo", "Hotel"))
                self.labelTitulo.setText(_translate("UsuarioNuevo", "Datos Usuario"))
                self.labelDatosNuevoUsuario.setText(_translate("UsuarioNuevo", "Datos del nuevo usuario"))
                self.labelNombre.setText(_translate("UsuarioNuevo", "Nombre"))
                self.labelApellido.setText(_translate("UsuarioNuevo", "Apellido"))
                self.labelRut.setText(_translate("UsuarioNuevo", "Rut"))
                self.labelFechaNacimiento.setText(_translate("UsuarioNuevo", "Fecha de Nacimiento"))
                self.labelCorreoElectronico.setText(_translate("UsuarioNuevo", "Correo electronico"))
                self.labelDomicilio.setText(_translate("UsuarioNuevo", "Domicilio"))
                self.labelTelefono.setText(_translate("UsuarioNuevo", "Teléfono"))
                self.labelGenero.setText(_translate("UsuarioNuevo", "Género"))
                self.comboBoxGenero.setItemText(0, _translate("UsuarioNuevo", "Elegir"))
                self.comboBoxGenero.setItemText(1, _translate("UsuarioNuevo", "Femenino"))
                self.comboBoxGenero.setItemText(2, _translate("UsuarioNuevo", "Masculino"))
                self.BtnAgregarUsuario.setText(_translate("UsuarioNuevo", "Agregar Usuario"))
                self.labelPassword.setText(_translate("UsuarioNuevo", "Contraseña"))
                self.comboBoxCargo.setItemText(0, _translate("UsuarioNuevo", "Elegir"))
                self.comboBoxCargo.setItemText(1, _translate("UsuarioNuevo", "Administrador"))
                self.comboBoxCargo.setItemText(2, _translate("UsuarioNuevo", "Recepcionista"))
                self.labelCargo.setText(_translate("UsuarioNuevo", "Cargo"))

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()
                from ventanaAdministracion import ventanaAdministracion  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaAdministracion()
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()


        def verificar_campos_llenos(self):
                campos_llenos = all([
                        self.inputNombre.text(),
                        self.inputApellido.text(),
                        self.inputRut.text(),
                        self.inputNewPassword.text(),
                        self.dateEditFechaNacimiento.date().isValid(),
                        self.inputCorreoElectronico.text(),
                        self.inputDomicilio.text(),
                        self.inputTelefono.text(),
                        self.comboBoxGenero.currentIndex() != 0,
                        self.comboBoxCargo.currentIndex() != 0
                ])
                return campos_llenos
        
        def actualizar_estado_boton(self):
                self.BtnAgregarUsuario.setEnabled(self.verificar_campos_llenos())



        def autocompletar_rut(self, rut):
                rut_limpio = rut.replace(".", "").replace("-", "")
                rut_formateado = self.formatear_rut(rut_limpio)
                self.inputRut.blockSignals(True)
                self.inputRut.setText(rut_formateado)
                self.inputRut.setCursorPosition(len(rut_formateado))
                self.inputRut.blockSignals(False)

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

        def agregar_usuario(self):
                usuario_id= random.randint(100, 9999)
                nombre = self.inputNombre.text()
                apellido = self.inputApellido.text()
                rut = self.inputRut.text()
                fecha_nacimiento = self.dateEditFechaNacimiento.date().toString("dd-MM-yyyy")
                correo = self.inputCorreoElectronico.text()
                domicilio = self.inputDomicilio.text()
                telefono = self.inputTelefono.text()
                genero = self.comboBoxGenero.currentText()
                password = self.inputNewPassword.text()
                cargo = self.comboBoxCargo.currentText()
                
                
                # Crear una lista con los datos del nuevo usuario
                nuevo_usuario = [usuario_id, nombre, apellido, genero, fecha_nacimiento, correo, password, rut, telefono, domicilio , cargo]
                
                # Abrir el archivo CSV en modo de escritura (append)
                with open('ArchivosCSV/Usuarios.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                
                        # Escribir los datos del nuevo usuario en una nueva fila del archivo CSV
                        writer.writerow(nuevo_usuario)
                
                # Mostrar mensaje de éxito
                #QtWidgets.QMessageBox.information(self, "Éxito", "El usuario ha sido agregado correctamente.")
                
                # Limpiar los campos de entrada
                self.inputNombre.setText("")
                self.inputApellido.setText("")
                self.inputRut.setText("")
                self.dateEditFechaNacimiento.setDate(QtCore.QDate.currentDate())
                self.inputCorreoElectronico.setText("")
                self.inputDomicilio.setText("")
                self.inputTelefono.setText("")
                self.comboBoxGenero.setCurrentIndex(0)
                self.inputNewPassword.setText("")
                self.comboBoxCargo.setCurrentIndex(0)

                # Mostrar un mensaje de éxito al usuario
                QtWidgets.QMessageBox.information(self.centralwidget, "Éxito", "El usuario fue ingresado correctamente.")

                self.cambiar_a_ventana_anterior()