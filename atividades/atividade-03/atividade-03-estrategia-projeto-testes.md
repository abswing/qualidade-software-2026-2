# Atividade 3: Estratégia e Projeto de Testes do LocalEats


## 1. Identificação

**Turma:** 2026-02   
**Data:** 27/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Antônio B. | @abswing |


**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Validar se as principais funcionalidades da aplicação LocalEats atendem às regras de negócio, usabilidade, garantindo a prevenção de falhas e a entrega de um produto confiável ao usuário final.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| [nome] | Cadastro de Usuário | Validação da força da senha (mínimo de caracteres), bloqueio de senhas simples/inválidas e exibição de mensagens de erro adequadas. |


#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Recuperçao de Senhas | A funcionalidade ainda não foi implementada na aplicação LocalEats, sendo identificada como uma lacuna/débito técnico durante a análise inicial. |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Testes de Sistema | garantir que os fluxos completos do LocalEats (cadastro, login) funcionem do início ao fim |
| Tipos de teste | Testes Funcionais, de Usabilidade e de Segurança. | Para validar se o sistema realiza as regras de negócio esperadas, oferece navegação intuitiva e protege os dados do usuário contra entradas inválidas ou fracas. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Os testes focam nas entradas e saídas através da interface, simulando a experiência real do usuário final sem necessidade de acesso ao código-fonte direto |
| Técnicas de teste | particionamento de equivalência | Para cobrir cenários de borda no cadastro (como tamanho mínimo de senha) |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Navegador web |
| Responsáveis pelo planejamento | Antonio (QA / Tester) |
| Responsáveis pela especificação dos casos | Antonio (QA / Tester) |
| Responsáveis pela futura execução | Antonio (QA / Tester) |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada O sistema precisa estar no ar e a tela de cadastro disponível para uso. |
| Saída | Todos os testes planejados foram executados e os bugs encontrados foram documentados. |
| Suspensão | O sistema cair (ficar fora do ar) |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | [nome] | Cadastro de Usuário | Aceitar senhas fracas ou de 1 único caractere. | O usuário final terá sua conta vulnerável | Alta | Alto | Alta | A falha já foi identificada no sistema e permite cadastrar credenciais totalmente inseguras |

### 3.2 Aplicação das técnicas

> Cada integrante deve aplicar pelo menos uma técnica adequada à funcionalidade e ao risco analisado. A equipe deve utilizar, no conjunto da atividade, pelo menos duas técnicas diferentes.

#### Análise do integrante 1

**Integrante:** [nome]  
**Funcionalidade:** [preencher]  
**Risco relacionado:** [R01]  
**Técnica escolhida:** [particionamento de equivalência, análise de valor limite, tabela de decisão ou transição de estados]

**Por que a técnica foi escolhida:**  
[Expliquem por que a técnica é adequada à regra ou ao risco analisado.]

**Aplicação da técnica:**  
[Apresentem as classes, limites, combinações ou transições identificadas. Utilizem uma tabela ou lista quando necessário.]

**Casos derivados:** [CT01 e CT02]

#### Análise do integrante 2

**Integrante:** [nome]  
**Funcionalidade:** [preencher]  
**Risco relacionado:** [R02]  
**Técnica escolhida:** [preencher]

**Por que a técnica foi escolhida:**  
[preencher]

**Aplicação da técnica:**  
[preencher]

**Casos derivados:** [preencher]

> Repitam ou removam a seção de análise conforme o número de integrantes.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

> No trabalho individual, elabore três casos. No trabalho em equipe, cada integrante deve elaborar pelo menos dois casos relacionados à própria funcionalidade.

### CT01: [Título do caso]

**Integrante responsável:** [nome]  
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [R01 ou descrição do requisito]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[O que precisa existir ou estar preparado antes da execução.]

**Dados de entrada:**  
[Valores ou dados necessários. Caso não sejam necessários, registrem “Não se aplica”.]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[Comportamento observável que indicará que o teste passou.]

---

### CT02: [Título do caso]

**Integrante responsável:** [nome]  
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [preencher]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[preencher]

**Dados de entrada:**  
[preencher]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[preencher]

---

> Copiem o modelo acima e continuem a numeração para criar os demais casos: CT03, CT04, CT05 etc.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| [nome] | [funcionalidade] | [R01 ou requisito] | [técnica] | [CT01 e CT02] |
| [nome] | [funcionalidade] | [R02 ou requisito] | [técnica] | [CT03 e CT04] |

> Acrescentem as linhas necessárias. Verifiquem se todos os riscos selecionados possuem casos de teste relacionados.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Informar a ferramenta ou registrar “não utilizada”.]

**Como foi utilizada:**  
[Descrever brevemente.]

**Uma sugestão que precisou ser alterada ou rejeitada:**  
[Descrever brevemente. Caso nenhuma sugestão tenha sido rejeitada, expliquem como as sugestões foram analisadas criticamente.]

**Como as respostas foram verificadas:**  
[Descrever brevemente.]
