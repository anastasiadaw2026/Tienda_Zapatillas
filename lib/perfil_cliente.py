import re
from lib.perfil import Perfil


class PerfilCliente(Perfil):
    PATTERN_TELEFONO = re.compile(r'^\(\+34\)[ ]?\d{3}[ ]?\d{3}[ ]?\d{3}$')
    PATTERN_EMAIL = re.compile(r'[a-zA-Z0-9._%+-ñÑ]+@[a-zA-Z0-9.-ñÑ]+\.es')

    def __init__(self):
        super().__init__()
        self._telefono: str = ''
        self._email: str = ''

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if PerfilCliente.PATTERN_TELEFONO.match(valor):
            self._telefono = valor
        else:
            self._telefono = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if PerfilCliente.PATTERN_EMAIL.match(valor):
            self._email = valor
        else:
            self._email = None

    def __str__(self):
        return super().__str__() + (f'Telefono: {self._telefono}\n'
                                    f'Email: {self._email}')

c = PerfilCliente()
c.telefono = '(+34)777 777 777'
c.email = 'hbgewvbñ@fe.es'
print(c)