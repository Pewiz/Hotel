import csv
import random

class Mascota:
    def __init__(self, id, nombre, especie, raza, fecha_nacimiento, sexo, volumen):
        self.__id = id
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
        self.__volumen = volumen
        self.__ficha_medica = []

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_especie(self):
        return self.__especie

    def get_raza(self):
        return self.__raza

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_sexo(self):
        return self.__sexo

    def get_volumen(self):
        return self.__volumen

    def get_ficha_medica(self):
        return self.__ficha_medica

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_especie(self, especie):
        self.__especie = especie

    def set_raza(self, raza):
        self.__raza = raza

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_volumen(self, volumen):
        self.__volumen = volumen

    def agregar_ficha_medica(self, ficha):
        self.__ficha_medica.append(ficha)

def agregar_mascota(nombre, especie, raza, fecha_nacimiento, sexo, volumen, cliente):
    id_mascota = cliente.get_rut()  # Utilizamos el Rut del cliente como ID de la mascota
    mascota = Mascota(
        id=id_mascota,
        nombre=nombre,
        especie=especie,
        raza=raza,
        fecha_nacimiento=fecha_nacimiento,
        sexo=sexo,
        volumen=volumen
    )

    mascotas = []

    mascotas.append(mascota)

    try:
        with open('ArchivosCSV/Mascotas.csv', mode='x', newline='') as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow(['Id', 'Nombre', 'Especie', 'Raza', 'Fecha de Nacimiento', 'Sexo', 'Volumen'])
    except FileExistsError:
        pass

    agregar_mascotas_a_csv(mascotas)


def agregar_mascotas_a_csv(mascotas):
    with open('ArchivosCSV/Mascotas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        for mascota in mascotas:
            writer.writerow([
                mascota.get_id(),
                mascota.get_nombre(),
                mascota.get_especie(),
                mascota.get_raza(),
                mascota.get_fecha_nacimiento(),
                mascota.get_sexo(),
                mascota.get_volumen()
            ])
