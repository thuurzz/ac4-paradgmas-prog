# AC4 - Paradigmas de Programação (Ciência da Computação)
# Objetivos: Implementação de classes com sobrecarga de operadores em Python.
#
# A seguir, informe o e-mail institucional dos membros do grupo:
# Email Impacta: ______________@aluno.faculdadeimpacta.com.br
# Email Impacta: ______________@aluno.faculdadeimpacta.com.br
# Email Impacta: ______________@aluno.faculdadeimpacta.com.br


"""
Siga atentamente as instruções contidas no arquivo PDF disponibilizado junto
com a atividade.
"""


def mdc_euclides(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


class Fracao:

    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ZeroDivisionError("O denominador não pode ser zero")
        # Implemente o que falta no construtor abaixo:
        mdc = mdc_euclides(numerador, denominador)
        self.n = numerador/mdc
        self.d = denominador/mdc

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, novo_d):
        self._d = int(novo_d)

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, novo_n):
        self._n = int(novo_n)

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __float__(self):
        return self.n / self.d

    def __add__(self, nova_fracao):
        n_numerador = (nova_fracao.d * self.n) + (self.d * nova_fracao.n)
        n_denominador = self.d * nova_fracao.d
        return Fracao(n_numerador, n_denominador)

    def __sub__(self, nova_fracao):
        n_numerador = (nova_fracao.d * self.n) - (self.d * nova_fracao.n)
        n_denominador = self.d * nova_fracao.d
        return Fracao(n_numerador, n_denominador)

    def __mul__(self, nova_fracao):
        n_numerador = nova_fracao.n * self.n
        n_denominador = nova_fracao.d * self.d
        return Fracao(n_numerador, n_denominador)

    def __truediv__(self, nova_fracao):
        n_numerador = self.n * nova_fracao.d
        n_denominador = self.d * nova_fracao.n
        return Fracao(n_numerador, n_denominador)

    def __iadd__(self, nova_fracao):
        n_numerador = (nova_fracao.d * self.n) + (self.d * nova_fracao.n)
        n_denominador = self.d * nova_fracao.d
        mdc = mdc_euclides(n_numerador, n_denominador)
        self.d = n_denominador / mdc
        self.n = n_numerador / mdc
        return self

    def __isub__(self, nova_fracao):
        n_numerador = (nova_fracao.d * self.n) - (self.d * nova_fracao.n)
        n_denominador = self.d * nova_fracao.d
        mdc = mdc_euclides(n_numerador, n_denominador)
        self.d = n_denominador / mdc
        self.n = n_numerador / mdc
        return self

    def __imul__(self, nova_fracao):
        n_numerador = nova_fracao.n * self.n
        n_denominador = nova_fracao.d * self.d
        mdc = mdc_euclides(n_numerador, n_denominador)
        self.d = n_denominador / mdc
        self.n = n_numerador / mdc
        return self

    def __itruediv__(self, nova_fracao):
        n_numerador = self.n * nova_fracao.d
        n_denominador = self.d * nova_fracao.n
        mdc = mdc_euclides(n_numerador, n_denominador)
        self.d = n_denominador / mdc
        self.n = n_numerador / mdc
        return self

    def __lt__(self, nova_fracao):
        return (self.n * nova_fracao.d) < (self.d * nova_fracao.n)

    def __le__(self, nova_fracao):
        return (self.n * nova_fracao.d) <= (self.d * nova_fracao.n)

    def __gt__(self, nova_fracao):
        return (self.n * nova_fracao.d) > (self.d * nova_fracao.n)

    def __ge__(self, nova_fracao):
        return (self.n * nova_fracao.d) >= (self.d * nova_fracao.n)

    def __eq__(self, nova_fracao):
        return (self.n * nova_fracao.d) == (self.d * nova_fracao.n)

    def __ne__(self, nova_fracao):
        return (self.n * nova_fracao.d) != (self.d * nova_fracao.n)

    def __getitem__(self, k):
        if k in ("n", "numerador"):
            return self.n
        elif k in ("d", "denominador"):
            return self.d
        return None

    def __setitem__(self, k, v):
        if k in ("n", "numerador"):
            self.n = v
        elif k in ("d", "denominador"):
            self.d = v
        mdc = mdc_euclides(self.n, self.d)
        self.d = self.d / mdc
        self.n = self.n / mdc
        return None


if __name__ == '__main__':   # não apague ou modifique essa linha
    pass  # não apague ou modifique essa linha
    """
	Caso deseje testar a classe implementada, escreva o seu código INDENTADO
	dentro deste if. Ele só será executado caso você rode o arquivo ac4.py diretamente.

	Quando o arquivo for chamado como módulo (que é o caso quando você executa o
	arquivo test_ac4.py), o código abaixo será ignorado.
	"""
