from random import randint


class Producto:

    def __init__(self, codigo, descripcion, precio_u):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_u = precio_u

    def show(self):
        print('%d: %s $%d' % (self.codigo, self.descripcion, self.precio_u))

class Venta:

    def __init__(self, fecha, numero_vendedor, codigo_producto, cantidad_venta, forma_pago):
        self.fecha = fecha

        # si el numero de vendedor es mayor que nuevo. Se asigana el default, 0
        if numero_vendedor > 9:
            self.numero_vendedor = 0
        else:
            self.numero_vendedor = numero_vendedor

        self.codigo_producto = codigo_producto
        self.cantidad_venta = cantidad_venta

        if int(forma_pago) > 2 : self.forma_pago = 0
        else: self.forma_pago = forma_pago

    def comprar_Vendedor(self, other):
        if self.numero_vendedor:
            print('comprar_Vendedor')
        

    def show(self):
        print('%-2s: %s -> %s: $%s, %s' % (self.fecha, self.numero_vendedor, self.codigo_producto,
                                         self.cantidad_venta, self.forma_pago))


def get_mayor_venta_credito(ventas):
    mayor_venta = Venta('', '', '', '', '')
    mayor_importe = -1
    for venta in ventas:
        if (venta.forma_pago == 2) and (venta.cantidad_venta > mayor_importe):
            mayor_importe = venta.cantidad_venta
            mayor_venta = venta
    if mayor_importe != -1:
        return mayor_venta
    else:
        return -1


def get_total_ventas(ventas):
    suma_ventas = 0
    for venta in ventas:
        suma_ventas += venta.cantidad_venta
    return suma_ventas


def get_vendedor_top(ventas):
    vendedores = {x: 0 for x in range(0,10)}
    for venta in ventas:
        vendedores[int(venta.numero_vendedor)] += 1

    # Recuperamos al vendedor con el mayor numero de ventas
    vendedor_top = {'id': -1 , 'cant': -1}
    for i in vendedores:
        if vendedores[i] > vendedor_top['cant']:
            vendedor_top['id'] = i
            vendedor_top['cant'] = vendedores[i]

    # Devuelve el index del vendedor mayor y la cantidad
    return vendedor_top['id'], vendedores[vendedor_top['id']]


def bubble_sort(ventas):
    ventas_ordenada = ventas
    """ Implementation of bubble sort """
    for i in range(len(ventas_ordenada)):
        for j in range(len(ventas_ordenada) - 1 - i):
            if ventas_ordenada[j].numero_vendedor > ventas_ordenada[j+1].numero_vendedor:
                ventas_ordenada[j].numero_vendedor, ventas_ordenada[j + 1].numero_vendedor = ventas_ordenada[j + 1].numero_vendedor, ventas_ordenada[j].numero_vendedor

    return ventas_ordenada

def get_precio_producto(id, productos):
    for producto in productos:
        if id == producto.codigo:
            return producto.precio_u
    return -1

def get_lista_debito(ventas, productos):
    ventas_ordenadas = bubble_sort(ventas)
    for venta in ventas_ordenadas:
        if venta.forma_pago == 1:
            print('Id_vendedor: %s -> %s: $%s = $%d' % (venta.numero_vendedor, venta.codigo_producto,
                                                      venta.cantidad_venta,
                                                      venta.cantidad_venta * get_precio_producto(venta.codigo_producto, productos)))
def buscar_vendedor(producto_id, productos, ventas):
    for venta in ventas:
        # print('%s  == %s' %(producto_id, venta.codigo_producto))
        if int(producto_id) == int(venta.codigo_producto):
            print('Fecha: numero_vendedor -> codigo_producto: cantidad_venta, forma_pago')
            venta.show()
            print('Precio Final: %d' %(venta.cantidad_venta * get_precio_producto(venta.codigo_producto, productos)))
            return 0

    print('No se han registrado ventas del producto: %s' % producto_id)




def menu():

    productos = []
    ventas = []
    for i in range(1,99):
        n1= randint(0,10)
        n2= randint(0,9)
        n3= randint(0,2)
        # (fecha, numero_vendedor, codigo_producto, cantidad_venta, forma_pago)
        venta = Venta(n1 + i, n1, n2, n1, n3)

        ventas.append(venta)

        # (codigo, descripcion, precio_u):
        producto = Producto(n2, n3, i)

        productos.append(producto)


    while True:
        print('\n***** Menu *****')
        print('1) Ingresar productos')
        print('2) Registrar Ventas')
        print('3) Vendedor con mayores ventas')
        print('4) Generar Listado, Ventas Debito por Vendedor')
        print('5) Buscar vendedor por producto vendido')
        print('6) Monto total ventas')
        print('7) Mostrar la venta con mayor importe con tarjeta de credito')
        print('8) Listar Productos')
        print('9) Listar Ventas')
        print('99) Salir')
        opc = int(input('> '))
        if opc == 1:
            print('Ingrese un Nuevo producto')
            codigo = float(input('Codigo: > '))
            descripcion = input('Descripcion: > ')
            precio_u = float(input('Precio Unitario: > '))
            producto = Producto(codigo, descripcion, precio_u)
            productos.append(producto)
            print(1)
        elif opc == 2:
            print('Registre una nueva venta')
            fecha = input('fecha: > ')
            numero_vendedor = input('Id Vendedor: > ')
            codigo_producto = input('Código producto: > ')
            cantidad_venta = input('Cantaidad venta: > ')
            forma_pago = input('Forma de pago: > ')

            venta = Venta(fecha, numero_vendedor, codigo_producto, cantidad_venta, forma_pago)
            ventas.append(venta)
        elif opc == 3:
            # Vendedor con Mayores Ventas
            id, cant = get_vendedor_top(ventas)
            print('El vendedor con más ventas es: %d, Realizo %d ventas' % (id, cant))

        elif opc == 4:
            get_lista_debito(ventas,productos)
            # Generar Listado, Ventas Debito por Vendedor
        elif opc == 5:
            # Buscar vendedor por producto vendido
            print('Buscar vendedor por producto vendido')
            codigo_producto = input('Ingrese el código del producto: > ')
            buscar_vendedor(codigo_producto, productos, ventas)
        elif opc == 6:
            total_ventas = get_total_ventas(ventas)
            print('Total vendido: $%d' % total_ventas)
        elif opc == 7:
            venta = get_mayor_venta_credito(ventas)
            if venta != -1:
                venta.show()
            else:
                print('No existen pagos realizados con tarjeta')
        elif opc == 8:
            print('Listar Productos')

            for producto in productos:
                producto.show()
        elif opc == 9:
            print('Listar Ventas')
            print('Fecha: numero_vendedor -> codigo_producto: cantidad_venta, forma_pago')
            for venta in ventas:
                venta.show()

        elif opc == 99:
            print('Finalizando aplicación')
            break
        else:
            print('Opcion NO valida')


menu()