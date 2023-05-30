import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class ventanaEditarUsuario(object):
        def __init__(self, usuario_id):
                self.usuario_id = usuario_id
        def setupUi(self, EditarUsuario):
                EditarUsuario.setObjectName("EditarUsuario")
                EditarUsuario.resize(802, 602)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Recursos/HotelMascota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                EditarUsuario.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(EditarUsuario)
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

                self.labelEditarDatosUsuario = QtWidgets.QLabel(self.centralwidget)
                self.labelEditarDatosUsuario.setGeometry(QtCore.QRect(40, 130, 381, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(13)
                self.labelEditarDatosUsuario.setFont(font)
                self.labelEditarDatosUsuario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
        "border-radius: 18%;")
                self.labelEditarDatosUsuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.labelEditarDatosUsuario.setIndent(29)
                self.labelEditarDatosUsuario.setObjectName("labelEditarDatosUsuario")
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
                self.inputRut = QtWidgets.QLineEdit(self.centralwidget)
                self.inputRut.setEnabled(False)
                self.inputRut.setGeometry(QtCore.QRect(50, 296, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                self.inputRut.setFont(font)
                self.inputRut.setText("")
                self.inputRut.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.inputRut.setObjectName("inputRut")
                self.labelRut = QtWidgets.QLabel(self.centralwidget)
                self.labelRut.setGeometry(QtCore.QRect(20, 256, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.labelRut.setFont(font)
                self.labelRut.setAlignment(QtCore.Qt.AlignCenter)
                self.labelRut.setObjectName("labelRut")
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

                #Boton guardar usuario editado
                self.BtnGuardarUsuarioEditado = QtWidgets.QPushButton(self.centralwidget)
                self.BtnGuardarUsuarioEditado.setGeometry(QtCore.QRect(639, 543, 151, 41))
                self.BtnGuardarUsuarioEditado.setEnabled(False)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.BtnGuardarUsuarioEditado.setFont(font)
                self.BtnGuardarUsuarioEditado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.BtnGuardarUsuarioEditado.setStyleSheet("background-color: rgb(79, 163, 166);\n"
        "border-radius:15px;")
                self.BtnGuardarUsuarioEditado.setObjectName("BtnGuardarUsuarioEditado")

                #Accion boton guardar usuario editado
                self.BtnGuardarUsuarioEditado.clicked.connect(self.guardar_usuario_editado)

                #Label password
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
                EditarUsuario.setCentralWidget(self.centralwidget)

                self.retranslateUi(EditarUsuario)
                QtCore.QMetaObject.connectSlotsByName(EditarUsuario)

                self.obtener_datos_usuario()
                self.inputNombre.textChanged.connect(self.actualizar_estado_boton)
                self.inputApellido.textChanged.connect(self.actualizar_estado_boton)
                self.inputRut.textChanged.connect(self.actualizar_estado_boton)
                self.inputNewPassword.textChanged.connect(self.actualizar_estado_boton)
                self.inputCorreoElectronico.textChanged.connect(self.actualizar_estado_boton)
                self.inputDomicilio.textChanged.connect(self.actualizar_estado_boton)
                self.inputTelefono.textChanged.connect(self.actualizar_estado_boton)
                self.comboBoxGenero.currentIndexChanged.connect(self.actualizar_estado_boton)
                self.comboBoxCargo.currentIndexChanged.connect(self.actualizar_estado_boton)
                
                

        def retranslateUi(self, EditarUsuario):
                _translate = QtCore.QCoreApplication.translate
                EditarUsuario.setWindowTitle(_translate("EditarUsuario", "Hotel"))
                self.labelTitulo.setText(_translate("EditarUsuario", "Editar Usuario"))
                self.labelEditarDatosUsuario.setText(_translate("EditarUsuario", "Datos del usuario a editar"))
                self.labelNombre.setText(_translate("EditarUsuario", "Nombre"))
                self.labelApellido.setText(_translate("EditarUsuario", "Apellido"))
                self.labelRut.setText(_translate("EditarUsuario", "Rut"))
                self.labelFechaNacimiento.setText(_translate("EditarUsuario", "Fecha de Nacimiento"))
                self.labelCorreoElectronico.setText(_translate("EditarUsuario", "Correo electronico"))
                self.labelDomicilio.setText(_translate("EditarUsuario", "Domicilio"))
                self.labelTelefono.setText(_translate("EditarUsuario", "Teléfono"))
                self.labelGenero.setText(_translate("EditarUsuario", "Género"))
                self.comboBoxGenero.setItemText(0, _translate("EditarUsuario", "Elegir"))
                self.comboBoxGenero.setItemText(1, _translate("EditarUsuario", "Femenino"))
                self.comboBoxGenero.setItemText(2, _translate("EditarUsuario", "Masculino"))
                self.BtnGuardarUsuarioEditado.setText(_translate("EditarUsuario", "Aceptar"))
                self.labelPassword.setText(_translate("EditarUsuario", "Contraseña"))
                self.comboBoxCargo.setItemText(0, _translate("EditarUsuario", "Elegir"))
                self.comboBoxCargo.setItemText(1, _translate("EditarUsuario", "Administrador"))
                self.comboBoxCargo.setItemText(2, _translate("EditarUsuario", "Recepcionista"))
                self.labelCargo.setText(_translate("EditarUsuario", "Cargo"))

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()
                from ventanaAdministracion import ventanaAdministracion  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = ventanaAdministracion()
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()

        def obtener_datos_usuario(self):
        # Abrir y leer el archivo CSV
                with open('ArchivosCSV/Usuarios.csv', 'r') as file:
                        reader = csv.reader(file)
                        next(reader)  # Saltar la primera línea si contiene encabezados

                        # Buscar el usuario correspondiente al usuario_id
                        for row in reader:
                                if row[0] == str(self.usuario_id):
                                        # Obtener los datos del usuario
                                        nombre = row[1]
                                        apellido = row[2]
                                        genero = row[3]
                                        fecha_nacimiento = row[4]
                                        correo_electronico = row[5]
                                        password=row[6]
                                        rut = row[7]
                                        telefono = row[8]
                                        domicilio = row[9]
                                        cargo = row[10]

                                        # Establecer los datos en los labels
                                        self.inputNombre.setText(nombre)
                                        self.inputApellido.setText(apellido)
                                        self.inputRut.setText(rut)
                                        self.inputNewPassword.setText(password)
                                        # Establecer el valor de la fecha de nacimiento en el dateEdit
                                        self.dateEditFechaNacimiento.setDate(QtCore.QDate.fromString(fecha_nacimiento, "yyyy-MM-dd"))
                                        self.inputCorreoElectronico.setText(correo_electronico)
                                        self.inputDomicilio.setText(domicilio)
                                        self.inputTelefono.setText(telefono)

                                        # Establecer el valor del género en el comboBoxGenero
                                        if genero == "Femenino":
                                                self.comboBoxGenero.setCurrentIndex(1)
                                        elif genero == "Masculino":
                                                self.comboBoxGenero.setCurrentIndex(2)

                                        # Establecer el valor del cargo en el comboBoxCargo
                                        if cargo == "Administrador":
                                                self.comboBoxCargo.setCurrentIndex(1)
                                        elif cargo == "Recepcionista":
                                                self.comboBoxCargo.setCurrentIndex(2)

                                        # Salir del bucle después de encontrar el usuario
                                        break
                                       
                
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
                self.BtnGuardarUsuarioEditado.setEnabled(self.verificar_campos_llenos())
                


        def guardar_usuario_editado(self):
                nombre = self.inputNombre.text()
                apellido = self.inputApellido.text()
                rut = self.inputRut.text()
                fecha_nacimiento = self.dateEditFechaNacimiento.date().toString(QtCore.Qt.ISODate)
                correo = self.inputCorreoElectronico.text()
                domicilio = self.inputDomicilio.text()
                telefono = self.inputTelefono.text()
                genero = self.comboBoxGenero.currentText()
                cargo = self.comboBoxCargo.currentText()
                password = self.inputNewPassword.text()

                # Aquí puedes realizar la actualización de los datos del usuario en el archivo CSV
                # Por ejemplo, puedes abrir el archivo CSV, leer los datos, actualizar los datos del usuario específico
                # y luego guardar los cambios en el archivo

                with open('ArchivosCSV/Usuarios.csv', 'r') as archivo_csv:
                        # Leer los datos del archivo CSV
                        csv_reader = csv.reader(archivo_csv)
                        lineas = list(csv_reader)

                        # Encontrar la línea correspondiente al usuario_id
                        for i, linea in enumerate(lineas):
                                if linea[0] == self.usuario_id:
                                        # Actualizar los datos en la línea correspondiente
                                        lineas[i] = [self.usuario_id, nombre, apellido, genero, fecha_nacimiento, correo, password, rut, telefono, domicilio , cargo]
                                        break

                # Guardar los cambios en el archivo CSV
                with open('ArchivosCSV/Usuarios.csv', 'w', newline='') as archivo_csv:
                        csv_writer = csv.writer(archivo_csv)
                        csv_writer.writerows(lineas)

                # Mostrar un mensaje de éxito al usuario
                QtWidgets.QMessageBox.information(self.centralwidget, "Éxito", "Los datos del usuario han sido actualizados correctamente.")

                self.cambiar_a_ventana_anterior()
