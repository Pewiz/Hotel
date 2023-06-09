# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaNuevoCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class ventanaNuevoCliente(object):
        def __init__(self, cont, id_cliente, idHabitacion):
                self.cont = cont
                self.id_cliente= id_cliente
                self.idHabitacion= idHabitacion
        def setupUi(self, ClienteNuevo):
                ClienteNuevo.setObjectName("ClienteNuevo")
                ClienteNuevo.resize(802, 602)
                ClienteNuevo.setMinimumSize(802, 602)
                ClienteNuevo.setMaximumSize(802, 602)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                ClienteNuevo.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(ClienteNuevo)
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

                #Boto Atras
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

                self.labelDatosNuevoClientes = QtWidgets.QLabel(self.centralwidget)
                self.labelDatosNuevoClientes.setGeometry(QtCore.QRect(40, 130, 381, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(13)
                self.labelDatosNuevoClientes.setFont(font)
                self.labelDatosNuevoClientes.setStyleSheet("background-color: rgb(79, 163, 166);\n"
        "border-radius: 18%;")
                self.labelDatosNuevoClientes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.labelDatosNuevoClientes.setIndent(29)
                self.labelDatosNuevoClientes.setObjectName("labelDatosNuevoClientes")
                self.labelIconFlechaAbajo = QtWidgets.QLabel(self.centralwidget)
                self.labelIconFlechaAbajo.setGeometry(QtCore.QRect(359, 136, 31, 31))
                self.labelIconFlechaAbajo.setText("")
                self.labelIconFlechaAbajo.setPixmap(QtGui.QPixmap("../Recursos/IconFlechaAbajo.png"))
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
                self.labelApellido.setGeometry(QtCore.QRect(244, 200, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelApellido.setFont(font)
                self.labelApellido.setAlignment(QtCore.Qt.AlignCenter)
                self.labelApellido.setObjectName("labelApellido")
                self.inputApellido = QtWidgets.QLineEdit(self.centralwidget)
                self.inputApellido.setGeometry(QtCore.QRect(260, 240, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputApellido.setFont(font)
                self.inputApellido.setText("")
                self.inputApellido.setObjectName("inputApellido")

                #Rut
                self.inputRut = QtWidgets.QLineEdit(self.centralwidget)
                self.inputRut.setGeometry(QtCore.QRect(50, 320, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputRut.setFont(font)
                self.inputRut.setText("")
                self.inputRut.setObjectName("inputRut")
                self.labelRut = QtWidgets.QLabel(self.centralwidget)
                self.labelRut.setGeometry(QtCore.QRect(20, 280, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelRut.setFont(font)
                self.labelRut.setAlignment(QtCore.Qt.AlignCenter)
                self.labelRut.setObjectName("labelRut")
                self.inputRut.textEdited.connect(self.autocompletar_rut)

                #Fecha Nacimiento
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

                #Correo Electronico
                self.inputCorreoElectronico = QtWidgets.QLineEdit(self.centralwidget)
                self.inputCorreoElectronico.setGeometry(QtCore.QRect(50, 479, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputCorreoElectronico.setFont(font)
                self.inputCorreoElectronico.setText("")
                self.inputCorreoElectronico.setObjectName("inputCorreoElectronico")
                self.labelCorreoElectronico = QtWidgets.QLabel(self.centralwidget)
                self.labelCorreoElectronico.setGeometry(QtCore.QRect(54, 439, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelCorreoElectronico.setFont(font)
                self.labelCorreoElectronico.setAlignment(QtCore.Qt.AlignCenter)
                self.labelCorreoElectronico.setObjectName("labelCorreoElectronico")

                #Domicilio
                self.labelDomicilio = QtWidgets.QLabel(self.centralwidget)
                self.labelDomicilio.setGeometry(QtCore.QRect(234, 440, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelDomicilio.setFont(font)
                self.labelDomicilio.setAlignment(QtCore.Qt.AlignCenter)
                self.labelDomicilio.setObjectName("labelDomicilio")
                self.inputDomicilio = QtWidgets.QLineEdit(self.centralwidget)
                self.inputDomicilio.setGeometry(QtCore.QRect(260, 480, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputDomicilio.setFont(font)
                self.inputDomicilio.setText("")
                self.inputDomicilio.setObjectName("inputDomicilio")

                #Telefono
                self.labelTelefono = QtWidgets.QLabel(self.centralwidget)
                self.labelTelefono.setGeometry(QtCore.QRect(258, 360, 71, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelTelefono.setFont(font)
                self.labelTelefono.setAlignment(QtCore.Qt.AlignCenter)
                self.labelTelefono.setObjectName("labelTelefono")
                self.inputTelefono = QtWidgets.QLineEdit(self.centralwidget)
                self.inputTelefono.setGeometry(QtCore.QRect(260, 400, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputTelefono.setFont(font)
                self.inputTelefono.setText("")
                self.inputTelefono.setObjectName("inputTelefono")
                positive_validator = QtGui.QIntValidator(1, 999999999, self.inputTelefono)
                self.inputTelefono.setValidator(positive_validator)

                #Genero
                self.labelGenero = QtWidgets.QLabel(self.centralwidget)
                self.labelGenero.setGeometry(QtCore.QRect(258, 281, 71, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelGenero.setFont(font)
                self.labelGenero.setAlignment(QtCore.Qt.AlignCenter)
                self.labelGenero.setObjectName("labelGenero")
                self.comboBoxGenero = QtWidgets.QComboBox(self.centralwidget)
                self.comboBoxGenero.setGeometry(QtCore.QRect(260, 320, 81, 31))
                self.comboBoxGenero.setObjectName("comboBoxGenero")
                self.comboBoxGenero.addItem("")
                self.comboBoxGenero.addItem("")
                self.comboBoxGenero.addItem("")

                #Boton Agregar Cliente
                self.BtnAgregarCliente = QtWidgets.QPushButton(self.centralwidget)
                self.BtnAgregarCliente.setGeometry(QtCore.QRect(639, 540, 151, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnAgregarCliente.setFont(font)
                self.BtnAgregarCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnAgregarCliente.setStyleSheet("background-color: rgb(79, 163, 166);\n"
        "border-radius:15px;")
                self.BtnAgregarCliente.setObjectName("BtnAgregarCliente")
                
                #Accion Boton Agregar Cliente
                self.BtnAgregarCliente.clicked.connect(self.agregar_cliente)

                ClienteNuevo.setCentralWidget(self.centralwidget)

                self.retranslateUi(ClienteNuevo)
                QtCore.QMetaObject.connectSlotsByName(ClienteNuevo)



                self.inputNombre.textChanged.connect(self.actualizar_estado_boton)
                self.inputApellido.textChanged.connect(self.actualizar_estado_boton)
                self.inputRut.textChanged.connect(self.actualizar_estado_boton)
                self.inputCorreoElectronico.textChanged.connect(self.actualizar_estado_boton)
                self.inputDomicilio.textChanged.connect(self.actualizar_estado_boton)
                self.inputTelefono.textChanged.connect(self.actualizar_estado_boton)
                self.comboBoxGenero.currentIndexChanged.connect(self.actualizar_estado_boton)

        def retranslateUi(self, ClienteNuevo):
                _translate = QtCore.QCoreApplication.translate
                ClienteNuevo.setWindowTitle(_translate("ClienteNuevo", "Hotel"))
                self.labelTitulo.setText(_translate("ClienteNuevo", "Datos Clientes "))
                self.labelDatosNuevoClientes.setText(_translate("ClienteNuevo", "Datos del nuevo cliente"))
                self.labelNombre.setText(_translate("ClienteNuevo", "Nombre"))
                self.labelApellido.setText(_translate("ClienteNuevo", "Apellido"))
                self.labelRut.setText(_translate("ClienteNuevo", "Rut"))
                self.labelFechaNacimiento.setText(_translate("ClienteNuevo", "Fecha de Nacimiento"))
                self.labelCorreoElectronico.setText(_translate("ClienteNuevo", "Correo electronico"))
                self.labelDomicilio.setText(_translate("ClienteNuevo", "Domicilio"))
                self.labelTelefono.setText(_translate("ClienteNuevo", "Teléfono"))
                self.labelGenero.setText(_translate("ClienteNuevo", "Género"))
                self.comboBoxGenero.setItemText(0, _translate("ClienteNuevo", "Elegir"))
                self.comboBoxGenero.setItemText(1, _translate("ClienteNuevo", "Femenino"))
                self.comboBoxGenero.setItemText(2, _translate("ClienteNuevo", "Masculino"))
                self.BtnAgregarCliente.setText(_translate("ClienteNuevo", "Agregar Cliente"))

        def cambiarVentana(self, clase, cliente_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = clase(self.cont,cliente_id, self.idHabitacion)  # Pasa el idCliente y el idHabitacion como parámetros
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()

                from ventanaListaClientes import ventanaListaCliente  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaListaCliente(self.id_cliente,self.idHabitacion,self.cont)
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()
        
        def verificar_campos_llenos(self):
                campos_llenos = all([
                        self.inputNombre.text(),
                        self.inputApellido.text(),
                        self.inputRut.text(),
                        self.dateEditFechaNacimiento.date().isValid(),
                        self.inputCorreoElectronico.text(),
                        self.inputDomicilio.text(),
                        self.inputTelefono.text(),
                        self.comboBoxGenero.currentIndex() != 0,
                ])
                return campos_llenos
        
        def actualizar_estado_boton(self):
                self.BtnAgregarCliente.setEnabled(self.verificar_campos_llenos())


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

        def agregar_cliente(self):
                idCliente= random.randint(100, 9999)
                nombre = self.inputNombre.text()
                apellido = self.inputApellido.text()
                rut = self.inputRut.text()
                fecha_nacimiento = self.dateEditFechaNacimiento.date().toString("dd-MM-yyyy")
                correo = self.inputCorreoElectronico.text()
                domicilio = self.inputDomicilio.text()
                telefono = self.inputTelefono.text()
                genero = self.comboBoxGenero.currentText()
                
                
                # Crear una lista con los datos del nuevo cliente
                nuevo_cliente = [idCliente, nombre, apellido, genero, fecha_nacimiento, rut, correo, telefono, domicilio]
                
                # Abrir el archivo CSV en modo de escritura (append)
                with open('ArchivosCSV/Cliente.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                
                        # Escribir los datos del nuevo cliente en una nueva fila del archivo CSV
                        writer.writerow(nuevo_cliente)
                
                # Mostrar mensaje de éxito
                #QtWidgets.QMessageBox.information(self, "Éxito", "El cliente ha sido agregado correctamente.")
                
                # Limpiar los campos de entrada
                self.inputNombre.setText("")
                self.inputApellido.setText("")
                self.inputRut.setText("")
                self.dateEditFechaNacimiento.setDate(QtCore.QDate.currentDate())
                self.inputCorreoElectronico.setText("")
                self.inputDomicilio.setText("")
                self.inputTelefono.setText("")
                self.comboBoxGenero.setCurrentIndex(0)

                # Mostrar un mensaje de éxito al cliente
                QtWidgets.QMessageBox.information(self.centralwidget, "Éxito", "El cliente fue ingresado correctamente.")

                self.cambiar_a_ventana_anterior()