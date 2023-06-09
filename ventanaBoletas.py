# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaBoletasReservas.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class ventanaBoletas(object):
        def __init__(self, cont, cliente_id, habitacion):
                self.cont = cont
                self.cliente_id = cliente_id
                self.habitacion = habitacion
        def setupUi(self, ListaBoletas):
                ListaBoletas.setObjectName("ListaBoletas")
                ListaBoletas.resize(802, 602)
                ListaBoletas.setMinimumSize(802, 602)
                ListaBoletas.setMaximumSize(802, 602)
                font = QtGui.QFont()
                font.setFamily("Arial")
                ListaBoletas.setFont(font)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                ListaBoletas.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(ListaBoletas)
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

                #Tabla Clientes
                self.tablaBoletasReservas = QtWidgets.QTableWidget(self.centralwidget)
                self.tablaBoletasReservas.setGeometry(QtCore.QRect(30, 160, 481, 291))
                self.tablaBoletasReservas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.tablaBoletasReservas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.tablaBoletasReservas.setObjectName("tablaBoletasReservas")
                self.tablaBoletasReservas.setColumnCount(3)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaBoletasReservas.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaBoletasReservas.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablaBoletasReservas.setHorizontalHeaderItem(2, item)
                self.tablaBoletasReservas.horizontalHeader().setCascadingSectionResizes(True)
                self.tablaBoletasReservas.horizontalHeader().setDefaultSectionSize(115)
                self.tablaBoletasReservas.horizontalHeader().setHighlightSections(True)
                self.tablaBoletasReservas.horizontalHeader().setMinimumSectionSize(39)
                self.tablaBoletasReservas.horizontalHeader().setSortIndicatorShown(False)
                self.tablaBoletasReservas.horizontalHeader().setStretchLastSection(True)
                self.tablaBoletasReservas.verticalHeader().setCascadingSectionResizes(True)
                self.tablaBoletasReservas.verticalHeader().setHighlightSections(True)
                self.tablaBoletasReservas.verticalHeader().setSortIndicatorShown(False)
                self.tablaBoletasReservas.verticalHeader().setStretchLastSection(False)
                self.tablaBoletasReservas.verticalHeader().setVisible(False)

                #Boletas de
                self.labelBoletasDe = QtWidgets.QLabel(self.centralwidget)
                self.labelBoletasDe.setGeometry(QtCore.QRect(29, 114, 481, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelBoletasDe.setFont(font)
                self.labelBoletasDe.setStyleSheet("background-color: rgb(79, 163, 166);\n" "border-radius: 12px;")
                self.labelBoletasDe.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.labelBoletasDe.setIndent(162)
                self.labelBoletasDe.setObjectName("labelBoletasDe")
                
                self.labelNombreDelPropietario = QtWidgets.QLabel(self.centralwidget)
                self.labelNombreDelPropietario.setGeometry(QtCore.QRect(281, 119, 121, 21))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelNombreDelPropietario.setFont(font)
                self.labelNombreDelPropietario.setObjectName("labelNombreDelPropietario")
                
                self.labelTitulo.raise_()
                self.labelFotoPerrito.raise_()
                self.tablaBoletasReservas.raise_()
                self.labelBoletasDe.raise_()
                self.BtnAtras.raise_()
                self.labelNombreDelPropietario.raise_()
                ListaBoletas.setCentralWidget(self.centralwidget)

                self.retranslateUi(ListaBoletas)
                QtCore.QMetaObject.connectSlotsByName(ListaBoletas)
                

                # Cargar Usuarios del CSV
                self.cargarReservasCSV()


       
        def retranslateUi(self, ListaBoletas):
                _translate = QtCore.QCoreApplication.translate
                ListaBoletas.setWindowTitle(_translate("ListaBoletas", "Hotel"))
                self.labelTitulo.setText(_translate("ListaBoletas", "Lista Boletas "))
                item = self.tablaBoletasReservas.horizontalHeaderItem(0)
                item.setText(_translate("ListaBoletas", "Rut"))
                item = self.tablaBoletasReservas.horizontalHeaderItem(1)
                item.setText(_translate("ListaBoletas", "Nombre"))
                item = self.tablaBoletasReservas.horizontalHeaderItem(2)
                item.setText(_translate("ListaBoletas", "Apellido"))
                self.labelBoletasDe.setText(_translate("ListaBoletas", "Boletas de "))
                
                nombre_cliente = self.obtenerNombreCliente(self.cliente_id)
                if nombre_cliente is not None:
                        self.labelNombreDelPropietario.setText(nombre_cliente)
                else:
                        self.labelNombreDelPropietario.setText("Cliente ")
                        
                
        def obtenerNombreCliente(self, cliente_id):
                with open('ArchivosCSV/Cliente.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        datos_clientes = reader
                        for cliente in datos_clientes:
                                if cliente[0] == cliente_id:
                                        return cliente[1]  # Suponiendo que el nombre del cliente está en la columna 1 del CSV
                        return None  # Si no se encuentra el cliente con el cliente_id especificado

        def cambiarVentana(self, clase, cliente_id):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = clase(cliente_id, self.habitacion)  # Pasa el idCliente y el habitacion como parámetros
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()
                from ventanaListaClientes import ventanaListaCliente  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaListaCliente(None, self.habitacion, self.cont)
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()
                
        # Abre el archivo CSV y devuelve los datos como una lista de filas
        def leerDatosDesdeCSV(self):
                with open('ArchivosCSV/Habitaciones.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        return list(reader)
                
        def leerHabitacionCsv(self):
                with open('ArchivosCSV/Habitacion.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        return list(reader)


        def filtrarReservas(self, reservas, cliente_id):
                lista = []
                for r in reservas:
                        if r[0] == cliente_id and r[5] != "None":
                                lista.append(r)
                return lista
        
        
        # Carga los datos del archivo CSV en el tableWidget
        def cargarReservasCSV(self):
                datos = self.leerDatosDesdeCSV()

                if datos:
                        reservas = self.filtrarReservas(datos, self.cliente_id)
                        encabezados = ["Id Habitacion", "Especie Mascota", "Cantidad", "Fecha Inicio", "Fecha Termino", "Dias", "Total"]

                        self.tablaBoletasReservas.clearContents()
                        self.tablaBoletasReservas.setRowCount(0)
                        self.tablaBoletasReservas.setColumnCount(len(encabezados))
                        self.tablaBoletasReservas.setHorizontalHeaderLabels(encabezados)
                        
                        self.tablaBoletasReservas.setRowCount(len(reservas))

                        for i, dato in enumerate(reservas):
                            idH = QtWidgets.QTableWidgetItem(dato[1])
                            self.tablaBoletasReservas.setItem(i, 0, idH)
                            
                            especie = QtWidgets.QTableWidgetItem(dato[3])
                            self.tablaBoletasReservas.setItem(i, 1, especie)
                            
                            fecha = QtWidgets.QTableWidgetItem(dato[2])
                            self.tablaBoletasReservas.setItem(i, 2, fecha)
                            
                            fecha = QtWidgets.QTableWidgetItem(dato[4])
                            self.tablaBoletasReservas.setItem(i, 3, fecha)
                            
                            fechafin = QtWidgets.QTableWidgetItem(dato[5])
                            self.tablaBoletasReservas.setItem(i, 4, fechafin)
                            
                            dias = QtWidgets.QTableWidgetItem(str(dato[6]))
                            self.tablaBoletasReservas.setItem(i, 5, dias)
                            
                            fecha = datetime.datetime.strptime(dato[4], "%d/%m/%Y").date()
                            fecha1 = datetime.datetime.strptime(dato[5], "%d/%m/%Y").date()
                            res = (fecha1 - fecha)
                            cant = res.days
                            datoss = self.leerHabitacionCsv()
                            for a in datoss:
                                    if dato[1] == a[0]:
                                            precio = a[4]
                            sub = (int(precio) * int(dato[6]))
                            subt = (sub * int(dato[2]))
                            if cant > 7:
                                    descuento1 = (subt * 0.3)
                                    self.flagDesc1 = True
                            else:
                                    descuento1 = 0
                                    self.flagDesc1 = False
                            if int(dato[2]) > 1:
                                    descuento2 = (subt * 0.4)
                                    self.flagDesc2 = True
                            else:
                                    descuento2 = 0
                                    self.flagDesc2 = False
                            subt = (subt - descuento1 - descuento2)
                            total = QtWidgets.QTableWidgetItem(str(subt))
                            self.tablaBoletasReservas.setItem(i, 6, total)
        
        

