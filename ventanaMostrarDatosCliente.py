# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaMostrarDatosCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class ventanaMostrarCliente(object):
        def __init__(self, cont, id_cliente, idHabitacion):
                self.cont = cont
                self.id_cliente= id_cliente
                self.idHabitacion= idHabitacion

        def setupUi(self, MostrarCliente):
            MostrarCliente.setObjectName("MostrarCliente")
            MostrarCliente.resize(802, 602)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MostrarCliente.setWindowIcon(icon)
            self.centralwidget = QtWidgets.QWidget(MostrarCliente)
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

            #Boton Atras
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

            #Accion Boton Atras
            self.BtnAtras.clicked.connect(self.cambiar_a_ventana_anterior)


            self.labelDatosClientes = QtWidgets.QLabel(self.centralwidget)
            self.labelDatosClientes.setGeometry(QtCore.QRect(40, 130, 381, 41))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(13)
            self.labelDatosClientes.setFont(font)
            self.labelDatosClientes.setStyleSheet("background-color: rgb(79, 163, 166);\n"
    "border-radius: 18%;")
            self.labelDatosClientes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.labelDatosClientes.setIndent(29)
            self.labelDatosClientes.setObjectName("labelDatosClientes")
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
            self.labelApellido = QtWidgets.QLabel(self.centralwidget)
            self.labelApellido.setGeometry(QtCore.QRect(244, 200, 101, 41))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.labelApellido.setFont(font)
            self.labelApellido.setAlignment(QtCore.Qt.AlignCenter)
            self.labelApellido.setObjectName("labelApellido")
            self.labelRut = QtWidgets.QLabel(self.centralwidget)
            self.labelRut.setGeometry(QtCore.QRect(20, 280, 101, 41))
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
            self.labelCorreoElectronico = QtWidgets.QLabel(self.centralwidget)
            self.labelCorreoElectronico.setGeometry(QtCore.QRect(54, 439, 131, 41))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.labelCorreoElectronico.setFont(font)
            self.labelCorreoElectronico.setAlignment(QtCore.Qt.AlignCenter)
            self.labelCorreoElectronico.setObjectName("labelCorreoElectronico")
            self.labelDomicilio = QtWidgets.QLabel(self.centralwidget)
            self.labelDomicilio.setGeometry(QtCore.QRect(234, 440, 131, 41))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.labelDomicilio.setFont(font)
            self.labelDomicilio.setAlignment(QtCore.Qt.AlignCenter)
            self.labelDomicilio.setObjectName("labelDomicilio")
            self.labelTelefono = QtWidgets.QLabel(self.centralwidget)
            self.labelTelefono.setGeometry(QtCore.QRect(258, 360, 71, 41))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.labelTelefono.setFont(font)
            self.labelTelefono.setAlignment(QtCore.Qt.AlignCenter)
            self.labelTelefono.setObjectName("labelTelefono")
            self.labelGenero = QtWidgets.QLabel(self.centralwidget)
            self.labelGenero.setGeometry(QtCore.QRect(258, 281, 71, 41))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.labelGenero.setFont(font)
            self.labelGenero.setAlignment(QtCore.Qt.AlignCenter)
            self.labelGenero.setObjectName("labelGenero")
            self.outputNombre = QtWidgets.QLabel(self.centralwidget)
            self.outputNombre.setEnabled(False)
            self.outputNombre.setGeometry(QtCore.QRect(50, 240, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputNombre.setFont(font)
            self.outputNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputNombre.setText("")
            self.outputNombre.setObjectName("outputNombre")
            self.outputApellido = QtWidgets.QLabel(self.centralwidget)
            self.outputApellido.setEnabled(False)
            self.outputApellido.setGeometry(QtCore.QRect(260, 240, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputApellido.setFont(font)
            self.outputApellido.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputApellido.setText("")
            self.outputApellido.setObjectName("outputApellido")
            self.outputRut = QtWidgets.QLabel(self.centralwidget)
            self.outputRut.setEnabled(False)
            self.outputRut.setGeometry(QtCore.QRect(50, 320, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputRut.setFont(font)
            self.outputRut.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputRut.setText("")
            self.outputRut.setObjectName("outputRut")
            self.outputGenero = QtWidgets.QLabel(self.centralwidget)
            self.outputGenero.setEnabled(False)
            self.outputGenero.setGeometry(QtCore.QRect(260, 320, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputGenero.setFont(font)
            self.outputGenero.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputGenero.setText("")
            self.outputGenero.setObjectName("outputGenero")
            self.outputFechaDeNacimiento = QtWidgets.QLabel(self.centralwidget)
            self.outputFechaDeNacimiento.setEnabled(False)
            self.outputFechaDeNacimiento.setGeometry(QtCore.QRect(50, 400, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputFechaDeNacimiento.setFont(font)
            self.outputFechaDeNacimiento.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputFechaDeNacimiento.setText("")
            self.outputFechaDeNacimiento.setObjectName("outputFechaDeNacimiento")
            self.outputTelefono = QtWidgets.QLabel(self.centralwidget)
            self.outputTelefono.setEnabled(False)
            self.outputTelefono.setGeometry(QtCore.QRect(260, 400, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputTelefono.setFont(font)
            self.outputTelefono.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputTelefono.setText("")
            self.outputTelefono.setObjectName("outputTelefono")
            self.outputCorreoElectronico = QtWidgets.QLabel(self.centralwidget)
            self.outputCorreoElectronico.setEnabled(False)
            self.outputCorreoElectronico.setGeometry(QtCore.QRect(50, 480, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputCorreoElectronico.setFont(font)
            self.outputCorreoElectronico.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputCorreoElectronico.setText("")
            self.outputCorreoElectronico.setObjectName("outputCorreoElectronico")
            self.outputDomicilio = QtWidgets.QLabel(self.centralwidget)
            self.outputDomicilio.setEnabled(False)
            self.outputDomicilio.setGeometry(QtCore.QRect(260, 480, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            self.outputDomicilio.setFont(font)
            self.outputDomicilio.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.outputDomicilio.setText("")
            self.outputDomicilio.setObjectName("outputDomicilio")
            MostrarCliente.setCentralWidget(self.centralwidget)

            self.retranslateUi(MostrarCliente)
            QtCore.QMetaObject.connectSlotsByName(MostrarCliente)
            print(self.cont)
            self.obtener_datos_usuario()

        def retranslateUi(self, MostrarCliente):
            _translate = QtCore.QCoreApplication.translate
            MostrarCliente.setWindowTitle(_translate("MostrarCliente", "Hotel"))
            self.labelTitulo.setText(_translate("MostrarCliente", "Cliente"))
            self.labelDatosClientes.setText(_translate("MostrarCliente", "Datos del cliente"))
            self.labelNombre.setText(_translate("MostrarCliente", "Nombre"))
            self.labelApellido.setText(_translate("MostrarCliente", "Apellido"))
            self.labelRut.setText(_translate("MostrarCliente", "Rut"))
            self.labelFechaNacimiento.setText(_translate("MostrarCliente", "Fecha de Nacimiento"))
            self.labelCorreoElectronico.setText(_translate("MostrarCliente", "Correo electronico"))
            self.labelDomicilio.setText(_translate("MostrarCliente", "Domicilio"))
            self.labelTelefono.setText(_translate("MostrarCliente", "Teléfono"))
            self.labelGenero.setText(_translate("MostrarCliente", "Género"))

        def cambiarVentana(self, clase, cliente_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = clase(self.cont, cliente_id, self.idHabitacion)  # Pasa el idCliente y el idHabitacion como parámetros
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()
        
        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()

                from ventanaListaClientes import ventanaListaCliente  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaListaCliente(self.cont, self.id_cliente, self.idHabitacion)
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()

        def obtener_datos_usuario(self):
            with open('ArchivosCSV/Cliente.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == self.id_cliente:
                        self.outputNombre.setText(row[1])
                        self.outputNombre.setAlignment(QtCore.Qt.AlignCenter)  
                        self.outputApellido.setText(row[2])
                        self.outputApellido.setAlignment(QtCore.Qt.AlignCenter)  
                        self.outputGenero.setText(row[3])
                        self.outputGenero.setAlignment(QtCore.Qt.AlignCenter)  
                        self.outputFechaDeNacimiento.setText(row[4])
                        self.outputFechaDeNacimiento.setAlignment(QtCore.Qt.AlignCenter)  
                        self.outputRut.setText(row[5])
                        self.outputRut.setAlignment(QtCore.Qt.AlignCenter) 
                        self.outputCorreoElectronico.setText(row[6])
                        self.outputCorreoElectronico.setAlignment(QtCore.Qt.AlignCenter)   
                        self.outputTelefono.setText(row[7])
                        self.outputTelefono.setAlignment(QtCore.Qt.AlignCenter)  
                        self.outputDomicilio.setText(row[8])
                        self.outputDomicilio.setAlignment(QtCore.Qt.AlignCenter)  
                        break
