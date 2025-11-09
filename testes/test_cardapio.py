def test_prato_str(prato_valido):
    resultado_str = str(prato_valido)
    assert prato_valido._nome in resultado_str
    assert str(prato_valido._preco) in resultado_str
    assert prato_valido._descricao in resultado_str
    assert "Descrição:" in resultado_str

def test_bebida_str(bebida_valida):
    resultado_str = str(bebida_valida)
    assert bebida_valida._nome in resultado_str
    assert str(bebida_valida._preco) in resultado_str
    assert bebida_valida._tamanho in resultado_str
    assert "Tamanho:" in resultado_str

def test_sobremesa_str(sobremesa_valida):
    resultado_str = str(sobremesa_valida)
    assert sobremesa_valida._nome in resultado_str
    assert str(sobremesa_valida._preco) in resultado_str
    assert sobremesa_valida._tipo in resultado_str
    assert sobremesa_valida._tamanho in resultado_str
    assert "Tipo:" in resultado_str