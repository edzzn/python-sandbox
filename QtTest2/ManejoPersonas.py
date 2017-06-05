class Persona:
    def __init__(self, id, nombre, apellido):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido

    def edit(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

class Registro(Persona):
    def __init__(self):
        self.__registro_personas = []

    def add(self, Persona):
        self.__registro_personas.append(Persona)

    def __str__(self):
        print(self.__registro_personas)

    def get_registro(self):
        return self.__registro_personas

    def edit_persona(self, id):
        print('edit_persona')

    def delete_persona(self, id):
        print('edit_persona')