import csv
import random

class Cliente:
    def __init__(self, id, nombre, apellido, genero, fecha_nacimiento, rut, email, telefono, domicilio):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__rut = rut
        self.__email = email
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__mascotas = []
        self.__historial = []

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_genero(self):
        return self.__genero

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_rut(self):
        return self.__rut

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    def get_domicilio(self):
        return self.__domicilio

    def get_mascotas(self):
        return self.__mascotas

    def get_historial(self):
        return self.__historial

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_genero(self, genero):
        self.__genero = genero

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_rut(self, rut):
        self.__rut = rut

    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio


def generar_id_unico():
    return random.randint(100, 9999)


def agregar_cliente(nombre, apellido, genero, fecha_nacimiento, rut, email, telefono, domicilio):
    cliente = Cliente(
        id=generar_id_unico(),
        nombre=nombre,
        apellido=apellido,
        genero=genero,
        fecha_nacimiento=fecha_nacimiento,
        rut=rut,
        email=email,
        telefono=telefono,
        domicilio=domicilio
    )

    clientes = []

    while any(cliente.get_id() == c.get_id() for c in clientes):
        cliente.set_id(generar_id_unico())

    clientes.append(cliente)

    try:
        with open('ArchivosCSV/Cliente.csv', mode='x', newline='') as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(['Id', 'Nombre', 'Apellido', 'Genero', 'Fecha de Nacimiento', 'Rut', 'Email', 'Telefono', 'Domicilio'])
    except FileExistsError:
        pass

    agregar_clientes_a_csv(clientes)


def agregar_clientes_a_csv(clientes):
    with open('ArchivosCSV/Cliente.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        for cliente in clientes:
            writer.writerow([
                cliente.get_id(),
                cliente.get_nombre(),
                cliente.get_apellido(),
                cliente.get_genero(),
                cliente.get_fecha_nacimiento(),
                cliente.get_rut(),
                cliente.get_email(),
                cliente.get_telefono(),
                cliente.get_domicilio()
            ])
