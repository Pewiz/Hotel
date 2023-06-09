# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListaClientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaEditarCliente import ventanaEditarCliente
from ventanaMostrarDatosCliente import ventanaMostrarCliente
from ventanaNuevoClinte import ventanaNuevoCliente
from ventanaListaMascota import ventanaListaMascotas
from ventanaListaReservas import ventanaListaReservas
from ventanaBoletas import ventanaBoletas

class ventanaListaCliente(object):
        def __init__(self, cliente_id, habitacion, cont):
                self.cliente_id = cliente_id
                self.habitacion = habitacion
                self.cont = cont
        def setupUi(self, ListaCliente):
                ListaCliente.setObjectName("ListaCliente")
                ListaCliente.resize(802, 602)
                ListaCliente.setMinimumSize(802, 602)
                ListaCliente.setMaximumSize(802, 602)
                font = QtGui.QFont()
                font.setFamily("Arial")
                ListaCliente.setFont(font)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                ListaCliente.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(ListaCliente)
                self.centralwidget.setObjectName("centralwidget")

                #Boton Atras
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
                icon1.addPixmap(QtGui.QPixmap("Recursos/FotoBtnAtras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.BtnAtras.setIcon(icon1)
                self.BtnAtras.setIconSize(QtCore.QSize(50, 50))
                self.BtnAtras.setObjectName("BtnAtras")

                #Accion boton atras
                self.BtnAtras.clicked.connect(self.cambiar_a_ventana_anterior)

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

                #Boton Ver Datos
                self.BtnVerDatos = QtWidgets.QPushButton(self.centralwidget)
                self.BtnVerDatos.setGeometry(QtCore.QRect(32, 460, 141, 31))
                self.BtnVerDatos.setEnabled(False)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnVerDatos.setFont(font)
                self.BtnVerDatos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnVerDatos.setStyleSheet("background-color: rgb(0, 177, 15);\n" "border-radius:15px;")
                self.BtnVerDatos.setObjectName("BtnVerDatos")

                #Accion Boton Ver Datos
                self.BtnVerDatos.clicked.connect(lambda: self.cambiarVentana(ventanaMostrarCliente, self.obtenerClienteSeleccionado()))

                #Boton Editar
                self.BtnEditar = QtWidgets.QPushButton(self.centralwidget)
                self.BtnEditar.setGeometry(QtCore.QRect(196, 460, 151, 31))
                self.BtnEditar.setEnabled(False)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnEditar.setFont(font)
                self.BtnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnEditar.setStyleSheet("background-color: rgb(251, 255, 0);\n" "border-radius:15px;")
                self.BtnEditar.setObjectName("BtnEditar")

                #Accion Boton Editar
                self.BtnEditar.clicked.connect(lambda: self.cambiarVentana(ventanaEditarCliente, self.obtenerClienteSeleccionado()))

                #Boton Eliminar
                self.BtnEliminar = QtWidgets.QPushButton(self.centralwidget)
                self.BtnEliminar.setGeometry(QtCore.QRect(368, 460, 141, 31))
                self.BtnEliminar.setEnabled(False)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnEliminar.setFont(font)
                self.BtnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnEliminar.setStyleSheet("background-color: rgb(255, 0, 0);\n" "border-radius:15px;")
                self.BtnEliminar.setObjectName("BtnEliminar")

                #Accion boton eliminar
                self.BtnEliminar.clicked.connect(lambda: self.eliminarCliente(self.obtenerClienteSeleccionado()))

                #Tabla Clientes
                self.tablaListaClientes = QtWidgets.QTableWidget(self.centralwidget)
                self.tablaListaClientes.setGeometry(QtCore.QRect(30, 160, 481, 291))
                self.tablaListaClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.tablaListaClientes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.tablaListaClientes.setObjectName("tablaListaClientes")
                self.tablaListaClientes.setColumnCount(3)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaListaClientes.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaListaClientes.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaListaClientes.setHorizontalHeaderItem(2, item)
                self.tablaListaClientes.horizontalHeader().setCascadingSectionResizes(True)
                self.tablaListaClientes.horizontalHeader().setDefaultSectionSize(115)
                self.tablaListaClientes.horizontalHeader().setHighlightSections(True)
                self.tablaListaClientes.horizontalHeader().setMinimumSectionSize(58)
                self.tablaListaClientes.horizontalHeader().setSortIndicatorShown(False)
                self.tablaListaClientes.horizontalHeader().setStretchLastSection(True)
                self.tablaListaClientes.verticalHeader().setCascadingSectionResizes(True)
                self.tablaListaClientes.verticalHeader().setHighlightSections(True)
                self.tablaListaClientes.verticalHeader().setSortIndicatorShown(False)
                self.tablaListaClientes.verticalHeader().setVisible(False)

                #Boton Aceptar
                self.BtnAceptar = QtWidgets.QPushButton(self.centralwidget)
                self.BtnAceptar.setGeometry(QtCore.QRect(643, 540, 151, 41))
                self.BtnAceptar.setEnabled(False)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnAceptar.setFont(font)
                self.BtnAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnAceptar.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius:15px;")
                self.BtnAceptar.setObjectName("BtnAceptar")

                #Accion Boton Aceptar
                if self.cont == 0:
                        self.BtnAceptar.clicked.connect(lambda: self.cambiarVentanaReserva(ventanaListaReservas, self.obtenerClienteSeleccionado()))
                else:
                        self.BtnAceptar.clicked.connect(lambda: self.cambiarVentanaMasc(ventanaListaMascotas, self.obtenerClienteSeleccionado()))

                self.labelClientesAgregados = QtWidgets.QLabel(self.centralwidget)
                self.labelClientesAgregados.setGeometry(QtCore.QRect(29, 114, 481, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelClientesAgregados.setFont(font)
                self.labelClientesAgregados.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius: 12px;")
                self.labelClientesAgregados.setAlignment(QtCore.Qt.AlignCenter)
                self.labelClientesAgregados.setObjectName("labelClientesAgregados")

                #Boton Nuevo Cliente
                self.BtnNuevoCliente = QtWidgets.QPushButton(self.centralwidget)
                self.BtnNuevoCliente.setGeometry(QtCore.QRect(516, 160, 31, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(16)
                font.setBold(False)
                font.setWeight(50)
                self.BtnNuevoCliente.setFont(font)
                self.BtnNuevoCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnNuevoCliente.setStyleSheet("background-color: rgb(79, 163, 166);")
                self.BtnNuevoCliente.setObjectName("BtnNuevoCliente")

                #Accion Boton Nuevo Cliente
                self.BtnNuevoCliente.clicked.connect(lambda: self.cambiarVentanaNuevoCliente())

                self.labelTitulo.raise_()
                self.labelFotoPerrito.raise_()
                self.BtnVerDatos.raise_()
                self.BtnEditar.raise_()
                self.BtnEliminar.raise_()
                self.tablaListaClientes.raise_()
                self.BtnAceptar.raise_()
                self.labelClientesAgregados.raise_()
                self.BtnNuevoCliente.raise_()
                self.BtnAtras.raise_()
                ListaCliente.setCentralWidget(self.centralwidget)

                self.retranslateUi(ListaCliente)
                QtCore.QMetaObject.connectSlotsByName(ListaCliente)

                # Cargar Usuarios del CSV
                self.cargarUsuariosCSV()
                print(self.cont)
                self.tablaListaClientes.itemSelectionChanged.connect(self.actualizarBotones)
                self.tablaListaClientes.itemDoubleClicked.connect(lambda: self.cambiarVentana(ventanaBoletas, self.obtenerClienteSeleccionado()))


       
        def retranslateUi(self, ListaCliente):
                _translate = QtCore.QCoreApplication.translate
                ListaCliente.setWindowTitle(_translate("ListaCliente", "Hotel"))
                self.labelTitulo.setText(_translate("ListaCliente", "Lista Clientes "))
                self.BtnVerDatos.setText(_translate("ListaCliente", "Ver datos"))
                self.BtnEditar.setText(_translate("ListaCliente", "Editar"))
                self.BtnEliminar.setText(_translate("ListaCliente", "Eliminar"))
                item = self.tablaListaClientes.horizontalHeaderItem(0)
                item.setText(_translate("ListaCliente", "Rut"))
                item = self.tablaListaClientes.horizontalHeaderItem(1)
                item.setText(_translate("ListaCliente", "Nombre"))
                item = self.tablaListaClientes.horizontalHeaderItem(2)
                item.setText(_translate("ListaCliente", "Apellido"))
                self.BtnAceptar.setText(_translate("ListaCliente", "Aceptar"))
                self.labelClientesAgregados.setText(_translate("ListaCliente", "Clientes agregados"))
                self.BtnNuevoCliente.setText(_translate("ListaCliente", "+"))

        def obtenerClienteSeleccionado(self):
                fila_seleccionada = self.tablaListaClientes.currentRow()
                if fila_seleccionada != -1:
                        id_usuario = self.tablaListaClientes.item(fila_seleccionada, 0).text()
                        self.usuario_seleccionado = id_usuario
                        return id_usuario

        def cambiarVentanaMasc(self, clase, cliente_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.nuevaVentana = QtWidgets.QMainWindow()
                cantidad = 1
                msg1 = QtWidgets.QMessageBox()
                msg1.setWindowTitle("Confirmación.")
                msg1.setText("Eliga cuantas mascotas desea ingresar a la reserva")
                spinbox = QtWidgets.QSpinBox()
                spinbox.setMinimum(1)
                spinbox.setMaximum(int(self.habitacion[1]))
                spinbox.setValue(cantidad)
                
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(spinbox)
                
                widget = QtWidgets.QWidget()
                widget.setLayout(layout)
                msg1.layout().addWidget(widget)
    
                msg1.setStandardButtons(QtWidgets.QMessageBox.Yes)
                msg1.accepted.connect(msg1.close)
                msg1.exec_()
                
                cantidad = spinbox.value()
                self.uiVentanaActual.close()
                self.ui = clase(cliente_id, self.habitacion, cantidad)  # Pasa el idCliente y el habitacion como parámetros
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()
                
        def cambiarVentana(self, clase, cliente_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = clase(self.cont, cliente_id, self.habitacion)  # Pasa el idCliente y el habitacion como parámetros
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()
        
        def cambiarVentanaReserva(self, clase, cliente_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = clase(cliente_id)
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()
                from ventanaAdministracion import ventanaAdministracion
                from ventanaHabitaciones import ventanaHabitaciones  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                if self.cont == 0:
                        self.uiVentanaAnterior = ventanaAdministracion() 
                else:
                        self.uiVentanaAnterior = ventanaHabitaciones()
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()

        def cambiarVentanaNuevoCliente(self):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = ventanaNuevoCliente(self.cont,self.cliente_id,self.habitacion) 
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show() 
        # Abre el archivo CSV y devuelve los datos como una lista de filas
        def leerDatosDesdeCSV(self):
                with open('ArchivosCSV/Cliente.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        return list(reader)


        # Inserta los datos en el widget de la tabla
        def insertarDatosEnTabla(self, datos):
                for fila in datos:
                        posicionFila = self.tablaListaClientes.rowCount()
                        self.tablaListaClientes.insertRow(posicionFila)

                        for columna, value in enumerate(fila):
                                item = QtWidgets.QTableWidgetItem(value)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                self.tablaListaClientes.setItem(posicionFila, columna, item)


 
        # Carga los datos del archivo CSV en el tableWidget
        def cargarUsuariosCSV(self):
                datos = self.leerDatosDesdeCSV()

                if datos:
                        # Seleccionar las columnas "Id", "Rut", "Nombre" y "Apellido" (columnas 0, 7 , 1 y 2) 
                        datos_seleccionados = [[fila[0],fila[5] ,fila[1], fila[2]] for fila in datos]
                        encabezados = datos_seleccionados.pop(0)  
                        self.tablaListaClientes.setColumnCount(len(encabezados))
                        self.tablaListaClientes.setHorizontalHeaderLabels(encabezados)

                        self.insertarDatosEnTabla(datos_seleccionados)
                else:
                        print("La lista de datos está vacía")

        def actualizarBotones(self):
                filasSeleccionada = self.tablaListaClientes.selectedIndexes()

                if filasSeleccionada:
                        # Se seleccionó al menos una fila
                        self.BtnAceptar.setEnabled(True)
                        self.BtnVerDatos.setEnabled(True)
                        self.BtnEditar.setEnabled(True)
                        self.BtnEliminar.setEnabled(True)
                else:
                        # No se seleccionó ninguna fila
                        self.BtnAceptar.setEnabled(False)
                        self.BtnVerDatos.setEnabled(False)
                        self.BtnEditar.setEnabled(False)
                        self.BtnEliminar.setEnabled(False)

        def eliminarCliente(self, usuario_id):
                # Obtener el índice de la fila seleccionada
                fila_seleccionada = self.tablaListaClientes.currentRow()

                # Eliminar la fila de la tabla
                self.tablaListaClientes.removeRow(fila_seleccionada)

                # Eliminar el usuario del archivo CSV
                datos = self.leerDatosDesdeCSV()
                if datos:
                        usuarios_actualizados = [fila for fila in datos if fila[0] != usuario_id]
                with open('ArchivosCSV/Cliente.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerows(usuarios_actualizados)

                # Actualizar los botones
                self.actualizarBotones()
        
        

