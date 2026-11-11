# Regras de negócio do LocalEats
# Responsável: Antonio Bernardo

VALOR_MINIMO_PEDIDO = 30


def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= VALOR_MINIMO_PEDIDO
