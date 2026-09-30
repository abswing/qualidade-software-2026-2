# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** 2026-02   
**Data:** 27/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Antônio B. | @abswing |


**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Ausência de validações básicas no front-end e back-end (ex.: aceitação de senhas de 1 caractere). | perda de dados e vulnerabilidade do produto |
| Falta de fluxos essenciais de suporte ao usuário (ex.: ausência de recuperação de senha). | Frustração do Usuario |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade deve ser uma responsabilidade compartilhada por toda a equipe (desenvolvedores, designers, product owners e QA). Enquanto o QA atua na prevenção, criação de cenários de teste e garantia de processos, os desenvolvedores são responsáveis por escrever código seguro com validações adequadas, o designer pela usabilidade, e o PO por definir regras de negócio claras. Atribuir a qualidade apenas ao QA gera gargalos e não evita que erros estruturais cheguem ao produto.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Antônio | Analista/ Tester de Qualidade | realizar testes | execução de testes funcionais | Pensamento crítico, atenção rigorosa aos detalhes, boa comunicação |
| [nome] | Desenvolvedor Backend/Frontend | Escrever código limpo, implementar validações de regras de negócio | Domínio da linguagem do projeto, segurança de código, desenvolvimento de APIs REST e validação de dados em camada de aplicação. | Resolução de problemas |
| [nome] | PO | Definir critérios de aceite claros, mapear requisitos não funcionais e garantir que necessidades implícitas (como fluxo de recuperação de senha) entrem no planejamento. | Engenharia de requisitos, gestão de backlog, conhecimento da regra de negócio e técnicas de refinamento | visão analítica e capacidade de negociação de prioridades. |
| [nome] | UX | Projetar fluxos intuitivos, garantir prevenção de erros na interface e assegurar usabilidade e acessibilidade no sistema. | Prototipagem de interfaces | escuta ativa e orientação à experiência do usuário. |

---

## 4. Tarefa 3: Matriz de responsabilidades

> Substituam “Papel 1”, “Papel 2”, “Papel 3” e “Papel 4” pelos papéis definidos pela equipe. Acrescentem ou removam colunas conforme necessário.

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Tester | Dev | PO | UX |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | C | C | AR | C |
| Revisar requisitos | R | C | A | R |
| Implementar a funcionalidade | I | AR | I | C |
| Revisar o código | I | AR | I | I |
| Criar testes unitários | I | AR | I | I |
| Planejar e executar testes do sistema | AR | C | I | C |
| Registrar e acompanhar defeitos | AR | C | I | I |
| Priorizar a correção dos defeitos | C | C | AR | I |
| Aprovar a disponibilização da versão | C | C | AR | I |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
O PO ficou centralizando tudo e o Dev ficou fazendo o código e os testes unitários isolado, sem o Tester acompanhar nada nessa parte.

**Consequência:**  
Gera gargalo na equipe, atrasa as entregas e faz passar bug besta pra fase final, custando mais tempo e trabalho pra consertar depois.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| alinhamento prévio antes de codificar | Centralização do PO e critérios de aceite incompletos, evitando que requisitos sem validação de segurança ou usabilidade sigam para dev. | PO, Dev, Tester e UX |
| testes e validação no início do fluxo | Isolamento do Dev e bugs descobertos tarde demais, reduzindo o retrabalho e o custo de correção na fase final. | Tester e Dev |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Gemini (Inteligência Artificial)

**Como foi utilizada:**  
Como suporte na definição dos conceitos teóricos de qualidade

**Como as respostas foram verificadas:**  
Validadas manualmente com base nos testes práticos realizados na aplicação LocalEats e revisão do conteúdo teórico.