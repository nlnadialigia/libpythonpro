import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['nlnadialigia@gmail.com', 'email@email.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'nlnadialigia@hotmail.com',
        'Cursos',
        'Primeira turma'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'email']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'nlnadialigia@hotmail.com',
            'Cursos',
            'Primeira turma'
        )
