import re
from lib.perfil import Perfil


class PerfilVendedor(Perfil):
    PATTERN_DNI= re.compile(r'^\d{8}[TRWAGMYFPDXBNJZSQVHLCKE]$')

    def __init__(self):
        super().__init__()
        self._dni: str = ''

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if PerfilVendedor.PATTERN_DNI.match(valor):
            self._dni = valor
        else:
            self._dni = None

    def __str__(self):
        return super().__str__() + f'DNI: {self._dni}'

# v = PerfilVendedor()
# v.dni = '12345678t'
# print(v)