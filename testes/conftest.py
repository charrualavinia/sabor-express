import pytest
from components.restaurante import Restaurante
from components.avaliacao_restaurante import AvaliacaoRestaurante
from components.cardapio.prato import Prato
from components.cardapio.bebida import Bebida
from components.cardapio.sobremesa import Sobremesa

@pytest.fixture
def restaurante_valido():
    return Restaurante("Chef's Burger", "Hamburgueria", [], {'average': 0, 'individual_ratings': []})

@pytest.fixture
def avaliacao_valida():
    return AvaliacaoRestaurante(media=5.0, avaliacoes_individuais=[])

@pytest.fixture
def avaliacao_invalida_media_alta():
    return AvaliacaoRestaurante(media=10.0, avaliacoes_individuais=[])

@pytest.fixture
def avaliacao_valida_com_individuais():
    return AvaliacaoRestaurante(media=4.0, avaliacoes_individuais=["Avaliacao 1", "Avaliacao 2"])

@pytest.fixture
def prato_valido():
    return Prato("Hambúrguer Clássico", 25.50, "Pão, carne, queijo, alface, tomate")

@pytest.fixture
def bebida_valida():
    return Bebida("Refrigerante", 8.00, "Lata 350ml")

@pytest.fixture
def sobremesa_valida():
    return Sobremesa("Pudim", 12.00, "Doce", "Pequeno")

@pytest.fixture
def restaurante_com_avaliacoes():
    return Restaurante("Pizzaria Boa", "Pizza", [], {'average': 3.0, 'individual_ratings': ["Nota 4", "Nota 2"]})

@pytest.fixture
def restaurante_com_cardapio(prato_valido, bebida_valida):
    restaurante = Restaurante("Cantina Italiana", "Italiana", [], {'average': 0, 'individual_ratings': []})
    restaurante.adicionar_no_cardapio(prato_valido)
    restaurante.adicionar_no_cardapio(bebida_valida)
    return restaurante