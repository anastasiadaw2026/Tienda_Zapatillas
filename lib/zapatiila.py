# z --> marca, numero, color, precio, stock
#    -- crear, imprimir, modificar

class Zapatilla:
    def __init__(self):
        self._marca: str = ''
        self._numero: float = 0.0
        self._color: str = ''
        self._precio: float = 0
        self._stock: int = 0

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, (float, int)):
            self._numero = valor
        else:
            self._numero = 'Desconocido'

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if isinstance(valor, (float, int)):
            self._precio = valor
        else:
            self._precio = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, valor):
        if valor.isalpha():
            self._color = valor
        else:
            self._color = None

    @property
    def stock(self):
        return self._stock

    def __str__(self):
        return (f"Marca: {self._marca}\n"
                f"Talla: {self._numero}\n"
                f"Color: {self._color}\n"
                f"Precio: {self._precio}€\n"
                f"Stock: {self._stock}")

    def add_stock(self, cantidad_aniadida):
        if isinstance(cantidad_aniadida, int):
            self._stock += cantidad_aniadida

z = Zapatilla()
z.add_stock(3)
z.add_stock(6)
print(z)