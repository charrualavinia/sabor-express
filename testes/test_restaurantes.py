import pytest
from components.restaurantes import Restaurantes
from components.restaurante import Restaurante


@pytest.fixture
def gerenciador_restaurantes():
    gerenciador = Restaurantes({'restaurants': []})

    rest_a = Restaurante("Restaurante A", "Tipo 1", [], {'average': 0, 'individual_ratings': []})
    rest_b = Restaurante("Restaurante B", "Tipo 2", [], {'average': 0, 'individual_ratings': []})

    gerenciador._lista_de_restaurantes.append(rest_a)
    gerenciador._lista_de_restaurantes.append(rest_b)
    return gerenciador


def test_adicionar_restaurante(restaurante_valido):
    gerenciador = Restaurantes({'restaurants': []})
    tamanho_inicial = len(gerenciador._lista_de_restaurantes)
    gerenciador._lista_de_restaurantes.append(restaurante_valido)
    tamanho_final = len(gerenciador._lista_de_restaurantes)

    assert tamanho_final == tamanho_inicial + 1
    assert restaurante_valido in gerenciador._lista_de_restaurantes


def test_buscar_por_nome_encontrado(gerenciador_restaurantes):
    restaurante = gerenciador_restaurantes.buscar_por_nome("Restaurante A")
    assert restaurante is not None
    assert restaurante.nome == "Restaurante A"


def test_buscar_por_nome_nao_encontrado(gerenciador_restaurantes):
    restaurante = gerenciador_restaurantes.buscar_por_nome("Restaurante Inexistente")
    assert restaurante is None


def test_listar_restaurantes(gerenciador_restaurantes):
    assert len(gerenciador_restaurantes._lista_de_restaurantes) == 2