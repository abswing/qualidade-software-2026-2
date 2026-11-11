# Atividade 4: Testes Automatizados do LocalEats

---

## 1. Identificação

- **Turma:** [informar]
- **Modalidade:** Individual
- **Repositório:** [colar o link do repositório]
- **Diretório da atividade:** [colar o link direto para este diretório]
- **Data da última execução:** 10/11/2026

### Integrantes

1. Antonio Bernardo

---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Antonio Bernardo | Unitário | Pedido igual ao valor mínimo (R$ 30,00) é aceito | `tests/test_regras_localeats.py::test_aceita_pedido_igual_ao_valor_minimo` |
| TU02 | Antonio Bernardo | Unitário | Pedido abaixo do valor mínimo é rejeitado | `tests/test_regras_localeats.py::test_rejeita_pedido_abaixo_do_valor_minimo` |
| TU03 | Antonio Bernardo | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_valor_negativo_gera_value_error` |
| TF01 | Antonio Bernardo | Funcional | Login com credenciais inválidas exibe mensagem de erro | `tests/test_localeats.py::test_login_com_credenciais_invalidas_exibe_erro` |

---

## 3. Testes unitários

### Regra de Antonio Bernardo

- **Regra escolhida:** Regra 1 — valor mínimo do pedido
- **Função implementada:** `pedido_atingiu_valor_minimo(valor_pedido)`
- **Arquivo da implementação:** [`src/regras_localeats.py`](src/regras_localeats.py)
- **Testes criados:** `test_aceita_pedido_igual_ao_valor_minimo`; `test_rejeita_pedido_abaixo_do_valor_minimo`; `test_valor_negativo_gera_value_error`
- **Comportamentos verificados:**
  - um pedido de exatamente R$ 30,00 (limite da regra) retorna `True`;
  - um pedido de R$ 20,00 (abaixo do mínimo) retorna `False`;
  - um valor negativo (-1) gera `ValueError`.

---

## 4. Aplicação do TDD

### TDD de Antonio Bernardo

- **Regra escolhida:** Regra 1 — valor mínimo do pedido
- **Primeiro teste escrito:** `test_aceita_pedido_igual_ao_valor_minimo`
- **Por que o teste falhou inicialmente:** o teste importava `pedido_atingiu_valor_minimo` de `src/regras_localeats.py`, mas a função ainda não existia, então o pytest gerou `ImportError: cannot import name 'pedido_atingiu_valor_minimo'`.
- **Implementação mínima realizada:** criação da função retornando `valor_pedido >= 30`, o suficiente para o primeiro teste passar.
- **Segundo teste escrito:** `test_rejeita_pedido_abaixo_do_valor_minimo` (e, em seguida, `test_valor_negativo_gera_value_error`, que falhou até ser adicionada a verificação `if valor_pedido < 0: raise ValueError(...)`).
- **Melhoria ou refatoração realizada:** 

---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Teste funcional de Antonio Bernardo

- **ID:** `TF01`
- **Fluxo automatizado:** tentativa de login com credenciais inválidas.
- **Interação realizada:** preenchimento do campo **E-mail** (placeholder `teste@teste.com`) com `naoexiste@teste.com`, do campo **Senha** (placeholder `Sua senha secreta`) com `senhaerrada` e clique no botão **Entrar** do formulário de login (`#loginForm`).
- **Primeira assertion:** a mensagem de erro (`#errorMsg`) é exibida com o texto `Invalid credentials`.
- **Segunda assertion:** a URL continua contendo `login.html`, ou seja, o usuário não foi levado para a página inicial.
- **Arquivo e função:** `tests/test_localeats.py::test_login_com_credenciais_invalidas_exibe_erro`
- **Resultado final:** aprovado

---

## 6. Resultado da execução

Comando executado (no Git Bash, equivalente ao `Tee-Object` do PowerShell):

```bash
python -m pytest -v | tee relatorio-pytest.txt
```

- **Quantidade total de testes:** 4
- **Testes aprovados:** 4
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** Todos os testes foram aprovados. O pytest exibiu um aviso (*warning*) de depreciação interno do plugin `pytest-playwright`, que não afeta o resultado dos testes.

---

## 7. Explicações individuais

### Explicação do teste

- **Teste escolhido:** `test_login_com_credenciais_invalidas_exibe_erro`
- **Comportamento verificado:** o sistema deve recusar um login com e-mail e senha inexistentes e informar o erro ao usuário.
- **Dados ou estado inicial:** navegador sem usuário logado (o Playwright inicia cada teste com um contexto limpo), por isso o LocalEats abre a tela de login. São usados o e-mail `naoexiste@teste.com` e a senha `senhaerrada`, que não correspondem a nenhuma conta.
- **Resultado esperado:** a mensagem `Invalid credentials` aparece na tela e a URL permanece em `login.html`.
- **O que faria o teste falhar:** o sistema aceitar credenciais inválidas e redirecionar para a página inicial; a mensagem de erro não aparecer ou ter outro texto; ou o campo/botão mudar de texto ou identificador, impedindo o locator de encontrá-lo.

---

## 8. Uso de inteligência artificial

- **Ferramenta utilizada:** Claude e ChatGpt
- **Como a ferramenta foi utilizada:** como apoio para organizar a estrutura de pastas, entender o ciclo do TDD, revisar a função implementada,fez o markdown e eu refatorei.
- **Uma sugestão que precisou ser alterada ou rejeitada:**  foi sugerido o uso de ambiente virtual (`.venv`), que foi removido por já haver o pytest instalado na máquina.
- **Motivo da alteração ou rejeição:** o ambiente virtual não era necessário para a entrega.
- **Como o código sugerido foi verificado:** todo o código foi executado com `python -m pytest -v`, incluindo a observação das falhas antes da implementação (TDD) e a execução do teste funcional com `--headed` para acompanhar o navegador. Os textos usados no teste funcional foram conferidos diretamente na interface do LocalEats.

---

## 9. Diferenciais opcionais

- [x] Terceiro teste unitário para caso de borda — [`test_valor_negativo_gera_value_error`](tests/test_regras_localeats.py)
- [x] Uso de `pytest.raises` para verificar exceção — [`test_valor_negativo_gera_value_error`](tests/test_regras_localeats.py)
- [ ] Parametrização com `pytest.mark.parametrize`.
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

- **Terceiro teste unitário (TU03) com `pytest.raises`:** verifica o caso de borda de valor negativo, garantindo que a função `pedido_atingiu_valor_minimo` gera `ValueError` em vez de retornar `True` ou `False`. Arquivo: `tests/test_regras_localeats.py`.
