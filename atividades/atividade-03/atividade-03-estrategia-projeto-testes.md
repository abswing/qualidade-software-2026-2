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
| R01 | Antonio | Cadastro de Usuário | Aceitar senhas fracas ou de 1 único caractere. | O usuário final terá sua conta vulnerável | Alta | Alto | Alta | A falha já foi identificada no sistema e permite cadastrar credenciais totalmente inseguras |

### 3.2 Aplicação das técnicas

> Cada integrante deve aplicar pelo menos uma técnica adequada à funcionalidade e ao risco analisado. A equipe deve utilizar, no conjunto da atividade, pelo menos duas técnicas diferentes.

#### Análise do integrante 1

**Integrante:** Antonio  
**Funcionalidade:** Cadastro de Usuário
**Risco relacionado:** R01 (Aceitar senhas fracas ou de 1 único caractere)  
**Técnica escolhida:** Análise de Valor Limite

**Por que a técnica foi escolhida:**  
A regra de negócio exige que a senha tenha um tamanho mínimo de caracteres. A Análise de Valor Limite é a técnica ideal para testar exatamente os pontos de fronteira onde o sistema deve aceitar ou recusar a entrada, que é onde a maioria dos bugs de validação acontece.

**Aplicação da técnica:**  
Considerando a regra de tamanho mínimo de senha igual a 3 caracteres:


## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste


### CT01: R01 Cadastro de Usuário

**Integrante responsável:** Antonio
**Funcionalidade:**  Cadastro de Usuário
**Risco ou requisito relacionado:** R01 (Aceitar senhas fracas ou de 1 único caractere)    
**Técnica utilizada:** AVL

**Pré-condição:**  
Aplicação LocalEats aberta no navegador na página de cadastro de usuário.

**Dados de entrada:**  
Nome: Antonio Silva, E-mail: antonio.teste@email.com, Senha: 123 (3 caracteres).

**Passos:**

1. Acessar a tela de cadastro do LocalEats.
2. Preencher os campos de Nome e E-mail com dados válidos.
3. Digitar a senha de 2 caracteres no campo de Senha.
4. Clicar no botão "Registrar".

**Resultado esperado:**  
O cadastro não deve ser realizado. O sistema deve exibir uma mensagem informando que a senha precisa ter no mínimo 3 caracteres.


### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Antonio | Cadastro de Usuario | R01 (Senha abaixo do limite de segurança) | AVL | CT01 |
---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Gemini (Inteligência Artificial)

**Como foi utilizada:**  
Como suporte na definição dos conceitos teóricos de qualidade

**Como as respostas foram verificadas:**  
Validadas manualmente com base nos testes práticos realizados na aplicação LocalEats e revisão do conteúdo teórico.
