"""Regras de negocio relacionadas ao calculo de pedidos."""


def validar_item(item: dict) -> None:
    """Valida preco e quantidade de um item.

    Raises:
        ValueError: se o preco ou a quantidade nao forem positivos.
    """
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    """Calcula o total do pedido.

    Uma lista vazia resulta em total igual a zero.
    """
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total



TAXA_BASE = 5
KM_BASE = 3
VALOR_KM_EXTRA = 2
PEDIDO_FRETE_GRATIS = 100


def calcular_taxa_entrega(distancia_km: float, total_pedido: float) -> float:
    """Calcula a taxa de entrega.

    - ate 3 km, a taxa e R$ 5;
    - acima de 3 km, acrescenta R$ 2 por quilometro excedente;
    - pedidos a partir de R$ 100 possuem entrega gratuita.

    Raises:
        ValueError: se a distancia for negativa.
    """
    if distancia_km < 0:
        raise ValueError("A distancia nao pode ser negativa.")

    if total_pedido >= PEDIDO_FRETE_GRATIS:
        return 0

    km_extra = max(0, distancia_km - KM_BASE)
    return TAXA_BASE + km_extra * VALOR_KM_EXTRA
