class Persona:
    def __init__(self, id, nombre, apellido):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido

    def __str__(self):
        return (self.get_id() + " " + self.get_nombre() + " " + self.get_apellido())

    def print_persona(self):
        return (self.get_id() + " " + self.get_nombre() + " " + self.get_apellido())

    def edit(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido


class Registro():
    def __init__(self):
        self.__registro_personas = []

    def add(self, Persona):
        self.__registro_personas.append(Persona)

    def mostrar(self):
        for persona in self.__registro_personas:
            print(persona)

    def get_registro(self):
        return self.__registro_personas

    def edit_persona(self, persona_id, persona):
        position_list = self.get_peronsa_loc(persona_id)
        self.__registro_personas[position_list] = persona

    def delete_persona(self, persona_id):
        position_list = self.get_peronsa_loc(persona_id)
        del self.__registro_personas[position_list]

    def get_peronsa_loc(self, id):
        for i, persona in enumerate(self.__registro_personas):
            if persona.get_id() == id:
                return i
        else:
            return None

    def encontrar_persona(self, persona_id):
        for persona in self.__registro_personas:
            if persona.get_id() == persona_id:
                return persona
        else:
            return None



if __name__ == '__main__':
    pers = Persona('12', 'Nombre12', 'Apellido1')
    # print (pers)
    pers2 = Persona('13', 'Nombre', 'Apellido')

    registro = Registro()

    registro.add(pers)
    registro.add(pers2)

    a = registro.encontrar_persona('12')
    print(a)