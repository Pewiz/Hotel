# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListaUsuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaMostrarDatosUsuario import ventanaMostrarDatosUsuario
from ventanaEditarUsuario import ventanaEditarUsuario
from ventanaNuevoUsuario import ventanaNuevoUsuario

class ventanaListaUsuarios(object):
        def setupUi(self, ListaUsuarios):
                ListaUsuarios.setObjectName("ListaUsuarios")
                ListaUsuarios.resize(802, 602)
                font = QtGui.QFont()
                font.setFamily("Arial")
                ListaUsuarios.setFont(font)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                ListaUsuarios.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(ListaUsuarios)
                self.centralwidget.setObjectName("centralwidget")

                #Boton atras
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

                #Boton ver datos
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

                #Accion boton ver datos
                self.BtnVerDatos.clicked.connect(lambda: self.cambiarVentana(ventanaMostrarDatosUsuario, self.obtenerUsuarioSeleccionado()))



                #Boton editar
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

                #Accion boton editar datos
                self.BtnEditar.clicked.connect(lambda: self.cambiarVentana(ventanaEditarUsuario, self.obtenerUsuarioSeleccionado()))

                #Boton eliminar
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
                self.BtnEliminar.clicked.connect(lambda: self.eliminarUsuario(self.obtenerUsuarioSeleccionado()))

                self.tablaListaUsuarios = QtWidgets.QTableWidget(self.centralwidget)
                self.tablaListaUsuarios.setGeometry(QtCore.QRect(30, 160, 481, 291))
                self.tablaListaUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.tablaListaUsuarios.setObjectName("tablaListaUsuarios")
                self.tablaListaUsuarios.setColumnCount(3)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaListaUsuarios.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaListaUsuarios.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaListaUsuarios.setHorizontalHeaderItem(2, item)
                self.tablaListaUsuarios.horizontalHeader().setCascadingSectionResizes(True)
                self.tablaListaUsuarios.horizontalHeader().setDefaultSectionSize(115)
                self.tablaListaUsuarios.horizontalHeader().setHighlightSections(True)
                self.tablaListaUsuarios.horizontalHeader().setMinimumSectionSize(58)
                self.tablaListaUsuarios.horizontalHeader().setSortIndicatorShown(False)
                self.tablaListaUsuarios.horizontalHeader().setStretchLastSection(True)
                self.tablaListaUsuarios.verticalHeader().setCascadingSectionResizes(True)
                self.tablaListaUsuarios.verticalHeader().setHighlightSections(True)
                self.tablaListaUsuarios.verticalHeader().setSortIndicatorShown(False)
                self.tablaListaUsuarios.verticalHeader().setStretchLastSection(False)


                self.labelUsuariosAgregados = QtWidgets.QLabel(self.centralwidget)
                self.labelUsuariosAgregados.setGeometry(QtCore.QRect(29, 114, 481, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelUsuariosAgregados.setFont(font)
                self.labelUsuariosAgregados.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius: 12px;")
                self.labelUsuariosAgregados.setAlignment(QtCore.Qt.AlignCenter)
                self.labelUsuariosAgregados.setObjectName("labelUsuariosAgregados")

                #Boton nuevo usuario
                self.BtnNuevoUsuario = QtWidgets.QPushButton(self.centralwidget)
                self.BtnNuevoUsuario.setGeometry(QtCore.QRect(516, 160, 31, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(16)
                font.setBold(False)
                font.setWeight(50)
                self.BtnNuevoUsuario.setFont(font)
                self.BtnNuevoUsuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnNuevoUsuario.setStyleSheet("background-color: rgb(79, 163, 166);")
                self.BtnNuevoUsuario.setObjectName("BtnNuevoUsuario")

                #Accion Boton Nuevo Usuario
                self.BtnNuevoUsuario.clicked.connect(lambda: self.cambiarVentanaNuevoUsuario())

                self.labelTitulo.raise_()
                self.labelFotoPerrito.raise_()
                self.BtnVerDatos.raise_()
                self.BtnEditar.raise_()
                self.BtnEliminar.raise_()
                self.tablaListaUsuarios.raise_()
                self.labelUsuariosAgregados.raise_()
                self.BtnNuevoUsuario.raise_()
                self.BtnAtras.raise_()
                ListaUsuarios.setCentralWidget(self.centralwidget)

                self.retranslateUi(ListaUsuarios)
                QtCore.QMetaObject.connectSlotsByName(ListaUsuarios)

                # Cargar Usuarios del CSV
                self.cargarUsuariosCSV()

                self.tablaListaUsuarios.itemSelectionChanged.connect(self.actualizarBotones)
                
                


        def retranslateUi(self, ListaUsuarios):
                _translate = QtCore.QCoreApplication.translate
                ListaUsuarios.setWindowTitle(_translate("ListaUsuarios", "Hotel"))
                self.labelTitulo.setText(_translate("ListaUsuarios", "Lista Usuarios"))
                self.BtnVerDatos.setText(_translate("ListaUsuarios", "Ver datos"))
                self.BtnEditar.setText(_translate("ListaUsuarios", "Editar"))
                self.BtnEliminar.setText(_translate("ListaUsuarios", "Eliminar"))
                item = self.tablaListaUsuarios.horizontalHeaderItem(0)
                item.setText(_translate("ListaUsuarios", "Rut"))
                item = self.tablaListaUsuarios.horizontalHeaderItem(1)
                item.setText(_translate("ListaUsuarios", "Nombre"))
                item = self.tablaListaUsuarios.horizontalHeaderItem(2)
                item.setText(_translate("ListaUsuarios", "Apellido"))
                self.labelUsuariosAgregados.setText(_translate("ListaUsuarios", "Usuarios agregados"))
                self.BtnNuevoUsuario.setText(_translate("ListaUsuarios", "+"))


        

        # Abre el archivo CSV y devuelve los datos como una lista de filas
        def leerDatosDesdeCSV(self):
                with open('ArchivosCSV/Usuarios.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        return list(reader)


        # Inserta los datos en el widget de la tabla
        def insertarDatosEnTabla(self, datos):
                for fila in datos:
                        posicionFila = self.tablaListaUsuarios.rowCount()
                        self.tablaListaUsuarios.insertRow(posicionFila)

                        for columna, value in enumerate(fila):
                                item = QtWidgets.QTableWidgetItem(value)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                self.tablaListaUsuarios.setItem(posicionFila, columna, item)


 
        # Carga los datos del archivo CSV en el tableWidget
        def cargarUsuariosCSV(self):
                datos = self.leerDatosDesdeCSV()

                if datos:
                        # Seleccionar las columnas "Id", "Rut", "Nombre" y "Apellido" (columnas 0, 7 , 1 y 2) 
                        datos_seleccionados = [[fila[0],fila[7] ,fila[1], fila[2]] for fila in datos]
                        encabezados = datos_seleccionados.pop(0)  
                        self.tablaListaUsuarios.setColumnCount(len(encabezados))
                        self.tablaListaUsuarios.setHorizontalHeaderLabels(encabezados)

                        self.insertarDatosEnTabla(datos_seleccionados)
                else:
                        print("La lista de datos está vacía")


        def actualizarBotones(self):
                filasSeleccionada = self.tablaListaUsuarios.selectedIndexes()

                if filasSeleccionada:
                        # Se seleccionó al menos una fila
                        self.BtnVerDatos.setEnabled(True)
                        self.BtnEditar.setEnabled(True)
                        self.BtnEliminar.setEnabled(True)
                else:
                        # No se seleccionó ninguna fila
                        self.BtnVerDatos.setEnabled(False)
                        self.BtnEditar.setEnabled(False)
                        self.BtnEliminar.setEnabled(False)


        def obtenerUsuarioSeleccionado(self):
                fila_seleccionada = self.tablaListaUsuarios.currentRow()
                if fila_seleccionada != -1:
                        id_usuario = self.tablaListaUsuarios.item(fila_seleccionada, 0).text()
                        self.usuario_seleccionado = id_usuario
                        return id_usuario

        def cambiarVentana(self, clase, usuario_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = clase(usuario_id)
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()

                from ventanaAdministracion import ventanaAdministracion  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaAdministracion()
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()

        def cambiarVentanaNuevoUsuario(self):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = ventanaNuevoUsuario() 
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show() 

        def eliminarUsuario(self, usuario_id):
                # Obtener el índice de la fila seleccionada
                fila_seleccionada = self.tablaListaUsuarios.currentRow()

                # Eliminar la fila de la tabla
                self.tablaListaUsuarios.removeRow(fila_seleccionada)

                # Eliminar el usuario del archivo CSV
                datos = self.leerDatosDesdeCSV()
                if datos:
                        usuarios_actualizados = [fila for fila in datos if fila[0] != usuario_id]
                with open('ArchivosCSV/Usuarios.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerows(usuarios_actualizados)

                # Actualizar los botones
                self.actualizarBotones()