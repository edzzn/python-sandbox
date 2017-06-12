# trabajando conjuntos utilizando listas


def fun_union(lista1, lista2):
    lista_aux = list(lista1)
    lista_aux.extend([e for e in lista2 if e not in lista1])
    return lista_aux


def fun_interseccion(lista1, lista2):
    return [e for e in lista1 if e in lista2]


def fun_diferencia(lista1, lista2):
    return [e for e in lista1 if e not in lista2]


if __name__ == '__main__':
    lista1 = [1, 2, 3, 4, 6, 8, 10, 12]
    lista2 = [2, 3, 5, 6, 9, 11, 13]

    union = fun_union(lista1, lista2)
    print('Union')
    print(union)

    # lista1 = [1, 2, 3, 4, 6, 8, 10, 12]
    # lista2 = [2, 3, 5, 6, 9, 11, 13]
    interseccion = fun_interseccion(lista1, lista2)
    print('Interseccion')
    print(interseccion)

    # lista1 = [1, 2, 3, 4, 6, 8, 10, 12]
    # lista2 = [2, 3, 5, 6, 9, 11, 13]
    diferencia = fun_diferencia(lista1, lista2)
    print('Diferencia')
    print(diferencia)



# Utilizando Conjuntos

# conj1 = {1, 2, 3, 4, 6, 8, 10, 12}
# conj2 = {2, 3, 5, 6, 9, 11, 13}
#
# union = conj1 | conj2
#
# interseccion = conj1 & conj2
#
# diferencia = conj1 - conj2
#
# print('Union')
# print(union)
# print('Interseccion')
# print(interseccion)
# print('Diferencia')
# print(diferencia)
