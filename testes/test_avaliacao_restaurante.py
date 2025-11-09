import pytest
from components.avaliacao_restaurante import AvaliacaoRestaurante

def test_init_media_valida(avaliacao_valida):
    assert avaliacao_valida.media == 5.0

def test_init_media_invalida(avaliacao_invalida_media_alta):
    assert avaliacao_invalida_media_alta.media > 5

def test_init_com_avaliacoes(avaliacao_valida_com_individuais):
    assert len(avaliacao_valida_com_individuais.avaliacoes_individuais) == 2