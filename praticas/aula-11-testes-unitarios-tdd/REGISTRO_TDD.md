# Registro do ciclo de TDD

## Comportamento escolhido

Cobrar a taxa inicial de R$ 5 para uma entrega de ate 3 km
(cenario: 2 km e pedido de R$ 50 -> taxa de R$ 5).

## Red

**Teste criado:** `test_cobra_taxa_base_ate_3_km` (em `tests/test_taxa_entrega.py`)

```python
assert calcular_taxa_entrega(2, 50) == 5
```

**Motivo da falha:** a funcao `calcular_taxa_entrega` ainda nao existia em `src/pedido.py`.

```
E   ImportError: cannot import name 'calcular_taxa_entrega' from 'src.pedido'
ERROR tests/test_taxa_entrega.py
1 error in 0.06s
```

## Green

**Implementacao realizada:** a menor implementacao possivel, retornando o valor fixo esperado:

```python
def calcular_taxa_entrega(distancia_km, total_pedido):
    return 5
```

Suite completa executada: `5 passed`.

## Refactor

**Melhoria realizada:** nao foi necessaria neste ciclo, pois o codigo tinha uma unica linha.
A refatoracao foi feita ao final de todos os ciclos (ver abaixo).

**Resultado final:** `5 passed` (4 testes ja existentes + 1 novo).

---

## Ciclos seguintes (resumo)

| Ciclo | Teste (Red) | Falha observada | Implementacao minima (Green) | Suite |
|---|---|---|---|---|
| 2 | `calcular_taxa_entrega(4, 50) == 7` | `assert 5 == 7` | se `distancia_km > 3`, retorna `5 + (distancia_km - 3) * 2` | 6 passed |
| 3 | `calcular_taxa_entrega(5, 100) == 0` | `assert 9 == 0` | se `total_pedido >= 100`, retorna `0` (verificado antes da distancia) | 7 passed |
| 4 (desafio) | `calcular_taxa_entrega(-1, 50)` gera `ValueError` | `Failed: DID NOT RAISE ValueError` | se `distancia_km < 0`, lanca `ValueError` | 8 passed |

## Refactor final

**Melhoria realizada:**
- numeros magicos substituidos por constantes nomeadas (`TAXA_BASE`,
  `KM_BASE`, `VALOR_KM_EXTRA`, `PEDIDO_FRETE_GRATIS`);
- os dois `return` da regra de distancia unificados com `max(0, distancia_km - 3)`;
- docstring e type hints no mesmo padrao das outras funcoes de `src/pedido.py`.

**Resultado final:** `8 passed` — comportamento preservado, toda a suite verde.
