# coding=utf-8
# para python >= 3.5
# Edisson Reinozo
# 12/06/2017

def verificar_cedula(cedula):
    """
    Algoritmo para la verificación de una cedula Ecuatoriana
    Basado en: http://telesjimenez.blogspot.com/2011/05/algoritmo-de-verificacion-de-cedula.html
    
        
    :param cedula: 
    :return: Boolean
    """
    # La cedula debe tener 10 digitos
    if len(cedula) != 10:
        return false   
    
    multi_a = [2, 1, 2, 1, 2, 1, 2, 1, 2]

    # Convertimos el string cedula a una lista de enteros
    # No se ingresa el ultimo digito
    lista_verficadora = list(filter(str.isdigit, cedula[:-1]))

    # Transformamos la lista a enteros
    lista_verficadora = [int(i) for i in lista_verficadora]
    
    # Los primeros dos digitos deben ser menores a 25
    if (lista_verficadora[0] + lista_verficadora[1]) > 25:
        return false

    # Multiplicamos la lista de los digitos de la cedula con multi_a
    lista_verficadora = [a * b for a, b in zip(lista_verficadora, multi_a)]

    # Si un elemento es mayor que 10, se resta 9
    lista_verficadora = map(lambda x: x-9 if x >= 10 else x, lista_verficadora)

    # Sumamos todos los elementos de la lista.
    # 10 menos el modulo de 10 de la suma debe ser igual al ultimo digito de la cedula
    valor = 10 - (sum(lista_verficadora) % 10)

    try:
        if valor == int(cedula[-1]):
            return True
        else:
            return False
    except:
        return False

if __name__ == '__main__':
    cedula = input('Ingrese la cedula: > ')
    if verificar_cedula(cedula):
        print('La cedula es real')
    else:
        print('Cedula equivocada')



