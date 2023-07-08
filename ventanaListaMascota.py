# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListaMascota.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaMostrarDatosMascota import ventanaMostrarMascota
from ventanaEditarMascota import ventanaEditarMascota
from ventanaNuevaMascota import ventanaNuevaMascota
from PyQt5.QtCore import Qt, pyqtSignal

class ventanaListaMascotas(object):
    
    def __init__(self, cliente_id, idHabitacion):
        self.cliente_id = cliente_id
        self.idHabitacion = idHabitacion
        
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

        #Boton Atras
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

        #Accion Boton Atras
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
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BtnVerDatos.setFont(font)
        self.BtnVerDatos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnVerDatos.setStyleSheet("background-color: rgb(0, 177, 15);\n" "border-radius:15px;")
        self.BtnVerDatos.setObjectName("BtnVerDatos")

        self.BtnVerDatos.clicked.connect(lambda: self.cambiarVentanaMostrarMascota(ventanaMostrarMascota))

        #Boton Editar
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
        
        self.BtnEditar.clicked.connect(lambda: self.cambiarVentanaEditarMascota(ventanaEditarMascota))


        #Boton Eliminar
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

        #Accion boton eliminar
        self.BtnEliminar.clicked.connect(lambda: self.eliminarMascota())

        #Lista Mascota
        self.tablaListaMascotas = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaListaMascotas.setGeometry(QtCore.QRect(30, 160, 481, 291))
        self.tablaListaMascotas.setAutoFillBackground(False)
        self.tablaListaMascotas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaListaMascotas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablaListaMascotas.setObjectName("tablaListaMascotas")
        self.tablaListaMascotas.setColumnCount(3)
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
        self.tablaListaMascotas.verticalHeader().setVisible(False)

        #Boton Aceptar
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

        #Accion Boton Aceptar
        self.BtnAceptar.clicked.connect(self.aceptarClick)


        #Mascota de
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
        


        #Boton Nueva Mascota
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

        #Accion Boton Nueva Mascota
        self.BtnNuevaMascota.clicked.connect(lambda: self.cambiarVentanaNuevaMascota())

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

        # Cargar Mascota del CSV
        self.cargarMascotasCSV()

        


    def retranslateUi(self, ListaMascotas):
        _translate = QtCore.QCoreApplication.translate
        ListaMascotas.setWindowTitle(_translate("ListaMascotas", "Hotel"))
        self.labelTitulo.setText(_translate("ListaMascotas", "Lista Mascotas"))
        self.BtnVerDatos.setText(_translate("ListaMascotas", "Ver datos"))
        self.BtnEditar.setText(_translate("ListaMascotas", "Editar"))
        self.BtnEliminar.setText(_translate("ListaMascotas", "Eliminar"))
        item = self.tablaListaMascotas.horizontalHeaderItem(0)
        item.setText(_translate("ListaMascotas", "Id"))
        item = self.tablaListaMascotas.horizontalHeaderItem(1)
        item.setText(_translate("ListaMascotas", "Nombre"))
        item = self.tablaListaMascotas.horizontalHeaderItem(2)
        item.setText(_translate("ListaMascotas", "Especie"))
        self.BtnAceptar.setText(_translate("ListaMascotas", "Aceptar"))
        self.labelMascotasDe.setText(_translate("ListaMascotas", "Mascotas de "))
        self.BtnNuevaMascota.setText(_translate("ListaMascotas", "+"))

        nombre_cliente = self.obtenerNombreCliente(self.cliente_id)
        if nombre_cliente is not None:
            self.labelNombreDelPropietario.setText(nombre_cliente)
        else:
            self.labelNombreDelPropietario.setText("Cliente ")

    def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()

                from ventanaListaClientes import ventanaListaCliente # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaListaCliente(self.cliente_id,self.idHabitacion,1)
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()

    def cambiarVentanaNuevaMascota(self):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = ventanaNuevaMascota(self.cliente_id,self.idHabitacion) 
                self.ui.setupUi(self.nuevaVentana)

                self.nuevaVentana.show() 
    
    def cambiarVentanaMostrarMascota(self, ventana):
        mascota = self.obtenerMascotaSeleccionada()
        id_usuario = self.obtenerIdSeleccionado()
        
        if mascota and id_usuario is not None:
            
            self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
            self.uiVentanaActual.close()
            self.nuevaVentana = QtWidgets.QMainWindow()
            self.ui = ventana(id_usuario, self.idHabitacion, mascota)
            self.ui.setupUi(self.nuevaVentana)           
            self.nuevaVentana.show()


    def cambiarVentanaEditarMascota(self, ventana):
        mascota = self.obtenerMascotaSeleccionada()
        id_usuario = self.obtenerIdSeleccionado()
        
        if mascota and id_usuario is not None:
            
            self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
            self.uiVentanaActual.close()
            self.nuevaVentana = QtWidgets.QMainWindow()
            self.ui = ventana(id_usuario, self.idHabitacion, mascota)
            self.ui.setupUi(self.nuevaVentana)           
            self.nuevaVentana.show()
   


    def leerDatosDesdeCSV(self):
        with open('ArchivosCSV/Mascotas.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            return list(reader)

    def filtrarMascotasPorCliente(self, mascotas, cliente_id):
        return [mascota for mascota in mascotas if mascota[0] == cliente_id]

    def filtrarMascotasPorTipo(self, mascotas, tipo):
        return [mascota for mascota in mascotas if mascota[2] == tipo]

    def cargarMascotasCSV(self):
        datos = self.leerDatosDesdeCSV()

        if datos:
            datos_filtrados_cliente = self.filtrarMascotasPorCliente(datos, self.cliente_id)
            datos_filtrados_tipo = self.filtrarMascotasPorTipo(datos_filtrados_cliente, self.obtenerTipoAnimalAceptado(self.idHabitacion))

            encabezados = ["Id", "Nombre", "Especie"]

            self.tablaListaMascotas.clearContents()
            self.tablaListaMascotas.setRowCount(0)
            self.tablaListaMascotas.setColumnCount(len(encabezados))
            self.tablaListaMascotas.setHorizontalHeaderLabels(encabezados)

            for fila in datos_filtrados_tipo:
                posicionFila = self.tablaListaMascotas.rowCount()
                self.tablaListaMascotas.insertRow(posicionFila)

                for columna, value in enumerate(fila):
                    item = QtWidgets.QTableWidgetItem(value)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tablaListaMascotas.setItem(posicionFila, columna, item)
        else:
            print("La lista de datos está vacía")
    

    def obtenerTipoAnimalAceptado(self, idHabitacion):
        # Código para obtener el tipo de mascota aceptado por la habitación con el idHabitacion
        with open('ArchivosCSV/Habitacion.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[0] == idHabitacion:
                    return row[3]  # El tipo de mascota aceptado se encuentra en la tercera columna (índice 2)
        return None  # Devuelve None si no se encuentra la habitación con el idHabitacion especificado

    def obtenerIdSeleccionado(self):
        fila_seleccionada = self.tablaListaMascotas.currentRow()
        if fila_seleccionada != -1:
            id_usuario = self.tablaListaMascotas.item(fila_seleccionada, 0).text()
            self.usuario_seleccionado = id_usuario
            return id_usuario

    def obtenerMascotaSeleccionada(self):
        fila_seleccionada = self.tablaListaMascotas.currentRow()
        if fila_seleccionada != -1:
            mascota = self.tablaListaMascotas.item(fila_seleccionada, 1).text()
            self.mascota_seleccionada = mascota
            return mascota

    def actualizarBotones(self):
                filasSeleccionada = self.tablaListaMascotas.selectedIndexes()

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


    def eliminarMascota(self):
        # Obtener el índice de la fila seleccionada
        usuario_id = self.obtenerIdSeleccionado()
        nombre_mascota = self.obtenerMascotaSeleccionada()
        print(nombre_mascota," a ", usuario_id)

        fila_seleccionada = self.tablaListaMascotas.currentRow()

        # Eliminar la fila de la tabla
        self.tablaListaMascotas.removeRow(fila_seleccionada)

        # Eliminar el usuario del archivo CSV
        datos = self.leerDatosDesdeCSV()

        if datos:
            usuarios_actualizados = [fila for fila in datos if fila[0] != usuario_id or fila[1] != nombre_mascota]
            with open('ArchivosCSV/Mascotas.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(usuarios_actualizados)

        # Actualizar los botones
        self.actualizarBotones()



    def obtenerNombreCliente(self, cliente_id):
        with open('ArchivosCSV/Cliente.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            datos_clientes = reader
            for cliente in datos_clientes:
                if cliente[0] == cliente_id:
                    return cliente[1]  # Suponiendo que el nombre del cliente está en la columna 1 del CSV
            return None  # Si no se encuentra el cliente con el cliente_id especificado
    

    def obtenerSizeMascotaSeleccionada(self):
        fila_seleccionada = self.tablaListaMascotas.currentRow()
        if fila_seleccionada != -1:
            nombre_mascota = self.tablaListaMascotas.item(fila_seleccionada, 0).text()
        else:
            print("no selecciono")

        with open('ArchivosCSV/Mascotas.csv', 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if fila[1] == nombre_mascota:
                    size_mascota = fila[6]
                    break
            else:
                size_mascota = ''  # Manejo de casos en los que el nombre de la mascota no se encuentre en el CSV

        print(size_mascota)

        if size_mascota.isdigit():
            return int(size_mascota)
        else:
            return 0  # Otra acción a realizar en caso de que el valor no sea numérico


    def obtenerCapacidadHabitacionSeleccionada(self):
        with open('ArchivosCSV/Habitacion.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[0] == self.idHabitacion:
                    return int(row[1])  # La capacidad está en la columna 1

        return None  # Si no se encuentra la habitación, devuelve None o un valor predeterminado


    def aceptarClick(self):
        print(self.obtenerSizeMascotaSeleccionada())
        size = self.obtenerSizeMascotaSeleccionada()  # Obtener el tamaño de la mascota seleccionada
        capacidad_actual = self.obtenerCapacidadHabitacionSeleccionada()  # Obtener la capacidad actual de la habitación
        capacidad_restante = capacidad_actual - size  # Restar la cantidad correspondiente al tamaño de la mascota

        if capacidad_restante < 0:
            # Si la capacidad restante es menor que 0, mostrar un mensaje de error
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "No hay suficiente capacidad en la habitación.")
        else:
            # Actualizar la capacidad de la habitación en el archivo CSV
            datos = self.leerDatosDesdeCSV()
            for fila in datos:
                if fila[0] == self.idHabitacion:
                    fila[2] = str(capacidad_restante)
                    break

            # Escribir los datos actualizados en el archivo CSV
            with open('ArchivosCSV/Habitaciones.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(datos)

            # Mostrar un mensaje de éxito
            QtWidgets.QMessageBox.information(self.centralwidget, "Éxito", "La capacidad de la habitación se actualizó correctamente.")
    

   
            
        





    


