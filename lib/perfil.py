import re


class Perfil:
    # suponemos que el formato permitido para la direccion es: (Calle,
    # Avenida, Plaza, Paseo) nombre nº, (portal, escalera, casa) nº, piso n.º
    # letra, el piso siendo no obligatorio
    PATTERN_DIRECCION = re.compile(r'^[Cc]alle\s+[A-Za-z]+\s+\d{1,3}$|'
    r'^[Cc]alle\s+[A-Za-z]+\s+\d{1,3},\s*(portal|escalera|casa)\s*\d{1,3}$|'
    r'^[Cc]alle\s+[A-Za-z]+\s+\d{1,3},\s*piso\s*\d{1,3}[A-Za-z]?$|' 
    r'^[Pp]laza\s+[A-Za-z]+\s+\d{1,3}$|'
    r'^[Aa]venida\s+[A-Za-z]+\s+\d{1,3}$|'
    r'^[Pp]aseo\s+[A-Za-z]+\s+\d{1,3}$')
    """ no va """
    # re.compile(r'^[Cc]alle|[Pp]laza|[Aa]venida|['
    #            r'Pp]aseo\b[a-zA-Z]+\b\d{1,3},'
    #            r'?\bportal|escalera|casa\b\d{1,3},'
    #            r'?\b(piso\b\d{1,3}\b?[a-zA-Z])?$')

    def __init__(self):
        self._nombre: str = ''
        self._direccion: str = ''

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.isalpha():
            self._nombre = valor
        else:
            self._nombre = 'Desconocido'

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        if Perfil.PATTERN_DIRECCION.match(valor):
            self._direccion = valor
        else:
            self._direccion = None

    def __str__(self):
        return (f"Nombre: {self._nombre}\n"
                f"Dirección: {self._direccion}\n")