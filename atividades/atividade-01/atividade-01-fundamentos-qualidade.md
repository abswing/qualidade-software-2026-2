# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** 2026-02   
**Data:** 27/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Antônio B. | @abswing |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Realizar autenticação informando apenas usuário/e-mail e senha cadastrados. | Usuário | Bloqueio de acesso |
| Explícita | Direcionar o usuário para landing page após validar o acesso. | Usuário | Falha |
| Implícita | Validar a força e regras mínimas de senha (ex.: bloquear senhas triviais como "123" ou "1"). | Segurança e Negócio | Criação de contas vulneráveis, facilitando ataques de invasão e roubo de contas. |
| Implícita | Garantir a consistência das validações do formulário e oferecer mecanismo de recuperação de acesso. | Usuário | Burlar regras do próprio sistema (aceitar 1 caractere quando exige 3) e perda definitiva da conta ao esquecer a senha. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. Um sistema que permite cadastrar e logar normalmente (cumprindo o requisito explícito) pode apresentar péssima qualidade por ignorar necessidades implícitas. Por exemplo, ao aceitar senhas fracas como "123" ou apenas "1" por falta de validação de força de senha, o sistema expõe todas as contas dos clientes a invasões fáceis. A falta de segurança implícita compromete a confiabilidade de toda a plataforma.

---

## 3. Tarefa 2: Exploração da aplicação

> Cada integrante deve explorar uma funcionalidade, realizando uma utilização esperada e uma utilização alternativa, inválida ou incompleta. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| [nome] | [funcionalidade] | [uso esperado e uso alternativo] | [comportamento observado] | [ver evidência](evidencias/nome-do-arquivo.png) |
| [nome] | [funcionalidade] | [uso esperado e uso alternativo] | [comportamento observado] | [ver evidência](evidencias/nome-do-arquivo.png) |
| [nome] | [funcionalidade] | [uso esperado e uso alternativo] | [comportamento observado] | [ver evidência](evidencias/nome-do-arquivo.png) |
| [nome] | [funcionalidade] | [uso esperado e uso alternativo] | [comportamento observado] | [ver evidência](evidencias/nome-do-arquivo.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

> Cada integrante deve formular um requisito de qualidade relacionado à mesma funcionalidade explorada na Tarefa 2. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| [nome] | [preencher] | [preencher] | [preencher] | [o que observar, medir, contar ou comparar] |
| [nome] | [preencher] | [preencher] | [preencher] | [o que observar, medir, contar ou comparar] |
| [nome] | [preencher] | [preencher] | [preencher] | [o que observar, medir, contar ou comparar] |
| [nome] | [preencher] | [preencher] | [preencher] | [o que observar, medir, contar ou comparar] |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Informar a ferramenta ou registrar “não utilizada”.]

**Como foi utilizada:**  
[Descrever brevemente.]

**Como as respostas foram verificadas:**  
[Descrever brevemente.]
