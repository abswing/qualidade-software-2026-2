import pytest

from src.pedido import calcular_taxa_entrega


def test_cobra_taxa_base_ate_3_km():
    # Arrange
    distancia_km = 2
    total_pedido = 50

    # Act
    taxa = calcular_taxa_entrega(distancia_km, total_pedido)

    # Assert
    assert taxa == 5


def test_acrescenta_2_reais_por_km_excedente():
    # Arrange
    distancia_km = 4
    total_pedido = 50

    # Act
    taxa = calcular_taxa_entrega(distancia_km, total_pedido)

    # Assert
    assert taxa == 7


def test_entrega_gratuita_para_pedido_a_partir_de_100():
    # Arrange
    distancia_km = 5
    total_pedido = 100

    # Act
    taxa = calcular_taxa_entrega(distancia_km, total_pedido)

    # Assert
    assert taxa == 0
