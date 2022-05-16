import pytest
import os.path
import ac4

"""
NÃO entregue nem modifique esse arquivo.
Ele serve somente para que você teste a sua atividade.
"""

def test_uso_modulos():
	if os.path.exists('ac4.py'):
		with open('ac4.py', 'r') as arq:
			conteudo = arq.read()
			if ('import ' in conteudo or 'from ' in conteudo):
				pytest.exit('Não é permitido importar nenhuma biblioteca. Remova os imports!')


@pytest.mark.parametrize('valores', [(3,5,1), (88,33,11), (128,256,128), (27429,71583,669)])
def test_mdc_euclides(valores):
	try:
		a, b, esperado = valores
		obtido = ac4.mdc_euclides(a, b)
		assert esperado == obtido
	except Exception:
		raise AssertionError('Erro ao calcular o mdc')
	

@pytest.mark.parametrize('atributo', ['_n', '_d'])
def test_cria_fracao(atributo):
	try:
		f = ac4.Fracao(1, 2)
	except Exception:
		raise AssertionError('Erro no construtor da classe Fracao')
	else:
		mensagens_atributos = {'_n': 'Não criou o atributo protegido _n',
		'_d':'Não criou o atributo protegido _d'}
		assert hasattr(f, atributo), mensagens_atributos[atributo]


@pytest.mark.parametrize('numerador', [1, 5])
def test_fracao_numerador(numerador):
	try:
		f = ac4.Fracao(numerador, 1)
		assert f._n == numerador and type(f._n) == int
	except Exception:
		raise AssertionError('Erro ao inicializar o atributo protegido _n')


@pytest.mark.parametrize('denominador', [1, 5])
def test_fracao_denominador(denominador):
	try:
		f = ac4.Fracao(1, denominador)
		assert f._d == denominador and type(f._d) == int
	except Exception:
		raise AssertionError('Erro ao inicializar o atributo protegido _d')


@pytest.mark.parametrize('valores', [(1,2,1,2), (4,8,1,2), (495,297,5,3)])
def test_fracao_string(valores):
	try:
		n, d, n_esperado, d_esperado = valores
		f = ac4.Fracao(n, d)
		assert str(f) == '{0}/{1}'.format(n_esperado, d_esperado)
	except Exception:
		raise AssertionError('Erro ao converter a Fracao para string')


@pytest.mark.parametrize('valores', [(1,2), (4,8), (495,297)])
def test_fracao_float(valores):
	try:
		n, d = valores
		esperado = n/d
		f = ac4.Fracao(n, d)
		assert float(f) == esperado
	except Exception:
		raise AssertionError('Erro ao converter a Fracao para float')


@pytest.mark.parametrize('valores', [(1,2,1,2,1,1), (2,4,128,256,1,1), (3,5,4,64,53,80)])
def test_fracao_soma(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		f3 = f1 + f2
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and f3._n == n_esperado and f3._d == d_esperado
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() + Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,0,1), (2,4,128,256,0,1), (3,5,4,64,43,80)])
def test_fracao_subtracao(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		f3 = f1 - f2
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and f3._n == n_esperado and f3._d == d_esperado
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() - Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,1,4), (2,4,128,256,1,4), (3,5,4,64,3,80)])
def test_fracao_multiplicacao(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		f3 = f1 * f2
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and f3._n == n_esperado and f3._d == d_esperado
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() * Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,1,1), (2,4,128,256,1,1), (3,5,4,64,48,5)])
def test_fracao_divisao(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		f3 = f1 / f2
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and f3._n == n_esperado and f3._d == d_esperado
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() / Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,1,1), (20,8,10,6,25,6), (3,5,4,64,53,80)])
def test_fracao_soma_aumentada(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		id1 = id(f1)
		n2, d2 = f2._n, f2._d
		f1 += f2
		id2 = id(f1)
		assert f1._n == n_esperado and f1._d == d_esperado and f2._n == n2 and f2._d == d2 and id1 == id2
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() += Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,0,1), (20,8,10,6,5,6), (3,5,4,64,43,80)])
def test_fracao_subtracao_aumentada(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		id1 = id(f1)
		n2, d2 = f2._n, f2._d
		f1 -= f2
		id2 = id(f1)
		assert f1._n == n_esperado and f1._d == d_esperado and f2._n == n2 and f2._d == d2 and id1 == id2
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() -= Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,1,4), (20,8,10,6,25,6), (3,5,4,64,3,80)])
def test_fracao_multiplicacao_aumentada(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		id1 = id(f1)
		n2, d2 = f2._n, f2._d
		f1 *= f2
		id2 = id(f1)
		assert f1._n == n_esperado and f1._d == d_esperado and f2._n == n2 and f2._d == d2 and id1 == id2
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() *= Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,1,1), (20,8,10,6,3,2), (3,5,4,64,48,5)])
def test_fracao_divisao_aumentada(valores):
	try:
		n1, d1, n2, d2, n_esperado, d_esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		id1 = id(f1)
		n2, d2 = f2._n, f2._d
		f1 /= f2
		id2 = id(f1)
		assert f1._n == n_esperado and f1._d == d_esperado and f2._n == n2 and f2._d == d2 and id1 == id2
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() /= Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,False), (2,4,128,256,False), (1,3,512,1024,True)])
def test_fracao_menor_que(valores):
	try:
		n1, d1, n2, d2, esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and ((f1.__lt__(f2)) == esperado)
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() < Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,True), (2,3,128,256,False), (512,1537,1,3,True)])
def test_fracao_menor_ou_igual(valores):
	try:
		n1, d1, n2, d2, esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and ((f1.__le__(f2)) == esperado)
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() <= Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,False), (2,4,128,256,False), (1,3,512,1537,True)])
def test_fracao_maior_que(valores):
	try:
		n1, d1, n2, d2, esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and ((f1.__gt__(f2)) == esperado)
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() > Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,True), (2,4,128,255,False), (512,1535,1,3,True)])
def test_fracao_maior_ou_igual(valores):
	try:
		n1, d1, n2, d2, esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and ((f1.__ge__(f2)) == esperado)
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() >= Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,True), (2,4,128,255,False), (1,3,512,1536,True)])
def test_fracao_igual(valores):
	try:
		n1, d1, n2, d2, esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and ((f1.__eq__(f2)) == esperado)
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() == Fracao()')


@pytest.mark.parametrize('valores', [(1,2,1,2,False), (2,4,128,255,True), (1,3,512,1537,True)])
def test_fracao_diferente(valores):
	try:
		n1, d1, n2, d2, esperado = valores
		f1 = ac4.Fracao(n1, d1)
		f2 = ac4.Fracao(n2, d2)
		n1, d1 = f1._n, f1._d
		n2, d2 = f2._n, f2._d
		assert f1._n == n1 and f1._d == d1 and f2._n == n2 and f2._d == d2 and ((f1.__ne__(f2)) == esperado)
	except Exception:
		raise AssertionError('Erro ao executar: Fracao() != Fracao()')


@pytest.mark.parametrize('valores', [('n',1,2), ('d',27,15), ('numerador',1,2), ('denominador',27,15), ('nd',30,45)])
def test_fracao_colchete_leitura(valores):
	try:
		k, n, d = valores
		f = ac4.Fracao(n, d)
		n, d = f._n, f._d
		esperado = None
		if k == 'n' or k == 'numerador':
			esperado = n
		elif k == 'd' or k == 'denominador':
			esperado = d
		assert f._n == n and f._d == d and f[k] == esperado
	except Exception:
		raise AssertionError('Erro ao executar: f[]')


@pytest.mark.parametrize('valores', [('n',1,2,5,5,2), ('d',27,15,18,1,2), ('numerador',1,2,5,5,2), ('denominador',27,15,18,1,2)])
def test_fracao_colchete_escrita(valores):
	try:
		k, n1, d1, v, n2, d2 = valores
		f = ac4.Fracao(n1, d1)
		f[k] = v
		assert f._n == n2 and f._d == d2
	except Exception:
		raise AssertionError('Erro ao executar: f[] = valor')


if __name__ == "__main__":
	pytest.main()

