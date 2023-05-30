from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget, QPushButton
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formatear RUT")

        layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        self.lineEdit.textEdited.connect(self.autocompletar_rut)
        layout.addWidget(self.lineEdit)

        button_accept = QPushButton("Aceptar")
        button_accept.clicked.connect(self.mostrar_rut)
        layout.addWidget(button_accept)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def autocompletar_rut(self, rut):
        rut_limpio = rut.replace(".", "").replace("-", "")
        rut_formateado = self.formatear_rut(rut_limpio)
        self.lineEdit.blockSignals(True)
        self.lineEdit.setText(rut_formateado)
        self.lineEdit.setCursorPosition(len(rut_formateado))
        self.lineEdit.blockSignals(False)

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

    def mostrar_rut(self):
        rut = self.lineEdit.text()
        rut_sin_caracteres = rut.replace(".", "").replace("-", "")
        self.imprimir_rut(rut_sin_caracteres)

    def imprimir_rut(self, rut):
        print(rut)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

