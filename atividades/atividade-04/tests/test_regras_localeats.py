# Testes unitários das regras do LocalEats
# Responsável: Antonio Bernardo
import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


# TU01 - comportamento válido no limite exato da regra
def test_aceita_pedido_igual_ao_valor_minimo():
    assert pedido_atingiu_valor_minimo(30) is True


# TU02 - comportamento inválido: abaixo do mínimo
def test_rejeita_pedido_abaixo_do_valor_minimo():
    assert pedido_atingiu_valor_minimo(20) is False


# TU03 - caso de borda: valor negativo gera exceção
def test_valor_negativo_gera_value_error():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-1)
