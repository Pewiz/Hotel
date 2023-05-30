import csv
import random

class Usuario:
    def __init__(self, id, nombre, apellido, genero, fecha_nacimiento, rut, email, telefono, domicilio, cargo):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__rut = rut
        self.__email = email
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__cargo=cargo
    
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

    def get_cargo(self):
        return self.__cargo

    # Setters
    def set_id(self):
        self.__id = generar_id_unico()

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
    
    def set_cargo(self, cargo):
        self.__cargo = cargo


def generar_id_unico():
    return random.randint(100, 9999)


def agregar_usuario(nombre, apellido, genero, fecha_nacimiento, rut, email, telefono, domicilio, cargo):
    usuario = Usuario(
        id=generar_id_unico(),
        nombre=nombre,
        apellido=apellido,
        genero=genero,
        fecha_nacimiento=fecha_nacimiento,
        rut=rut,
        email=email,
        telefono=telefono,
        domicilio=domicilio,
        cargo=cargo
    )

    usuarios = []

    while any(usuario.get_id() == c.get_id() for c in usuarios):
        usuario.set_id(generar_id_unico())

    usuarios.append(usuario)

    try:
        with open('ArchivosCSV/Usuarios.csv', mode='x', newline='') as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(['Id', 'Nombre', 'Apellido', 'Genero', 'Fecha de Nacimiento', 'Rut', 'Email', 'Telefono', 'Domicilio', 'Cargo'])
    except FileExistsError:
        pass

    agregar_usuarios_a_csv(usuarios)


def agregar_usuarios_a_csv(usuarios):
    with open('ArchivosCSV/Usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        for usuario in usuarios:
            writer.writerow([
                usuario.get_id(),
                usuario.get_nombre(),
                usuario.get_apellido(),
                usuario.get_genero(),
                usuario.get_fecha_nacimiento(),
                usuario.get_rut(),
                usuario.get_email(),
                usuario.get_telefono(),
                usuario.get_domicilio(),
                usuario.get_cargo()
            ])
