from components.restaurante import Restaurante
from components.avaliacao_restaurante import AvaliacaoRestaurante


def test_adicionar_avaliacao(restaurante_valido, avaliacao_valida):
    tamanho_inicial = len(restaurante_valido._avaliacoes.avaliacoes_individuais)
    restaurante_valido._avaliacoes.avaliacoes_individuais.append(avaliacao_valida)
    tamanho_final = len(restaurante_valido._avaliacoes.avaliacoes_individuais)

    assert tamanho_final == tamanho_inicial + 1
    assert avaliacao_valida in restaurante_valido._avaliacoes.avaliacoes_individuais


def test_adicionar_item_cardapio(restaurante_valido, prato_valido):
    tamanho_inicial = len(restaurante_valido._cardapio)
    restaurante_valido.adicionar_no_cardapio(prato_valido)
    tamanho_final = len(restaurante_valido._cardapio)

    assert tamanho_final == tamanho_inicial + 1
    assert prato_valido in restaurante_valido._cardapio


def test_listar_cardapio(restaurante_com_cardapio):
    assert len(restaurante_com_cardapio._cardapio) > 0


def test_media_avaliacoes(restaurante_com_avaliacoes):
    assert restaurante_com_avaliacoes._avaliacoes.media == 3.0


def test_media_avaliacoes_sem_avaliacoes(restaurante_valido):
    assert len(restaurante_valido._avaliacoes.avaliacoes_individuais) == 0
    assert restaurante_valido._avaliacoes.media == 0