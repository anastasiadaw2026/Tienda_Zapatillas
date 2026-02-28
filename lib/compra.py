from lib.perfil_cliente import PerfilCliente
from lib.perfil_vendedor import PerfilVendedor
from lib.zapatilla import Zapatilla


class Compra:
    IVA: float = 0.21

    def __init__(self):
        self.perfil_cliente: PerfilCliente = PerfilCliente()
        self.perfil_vendedor: PerfilVendedor = PerfilVendedor()
        self.zapatilla: list[Zapatilla] = []
        self.cantidad: int = 0


    def add_linea_compra(self, numero):
        linea_compra: list = [self.perfil_cliente, self.perfil_vendedor,
                              self.zapatilla[numero], self.cantidad]
        return linea_compra

    def crear_factura(self):
        precio_total: float = 0.0
        compras: list[list] = []

        for numero1 in range (len(self.zapatilla)):
            compras += [self.add_linea_compra(numero1)]

        for a in compras:
            precio_total += a[2].precio

        print(f"Factura:\n"
              f"_____________")

        for compra in compras:
            print(f"{compra[3]} - {compra[2].marca}, {compra[2].numero}, "
                  f"{compra[2].color} ......... {compra[2].precio}€\n"
                  f"--------------")

        print(f"Total a pagar: ........ {precio_total}€\n"
              f"Base IVA .............. "
              f"{round (precio_total * Compra.IVA, 2)}€\n"
              f"------------\n"
              f"Cliente: {compra[0].nombre}\n"
              f"Vendedor: {compra[1].nombre}")

    def pagar(self):
        print("Pagando...")
        # liberar carrito
        self.zapatilla = []
        self.cantidad = 0




z = Zapatilla()
z.marca = 'Adidas'
z.precio = 50.6

z1 = Zapatilla()
z1.marca = 'Nike'
z1.precio = 78

v = PerfilVendedor()
v.nombre = 'Ana'

cl = PerfilCliente()
cl.nombre = 'Daniel'

c = Compra()
c.zapatilla += [z]
c.zapatilla += [z1]
c.perfil_vendedor = v
c.perfil_cliente = cl

print(c.zapatilla)
c.crear_factura()