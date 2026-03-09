# **Organizador Inteligente de Estudos**

Aplicação desktop desenvolvida em **Python** para ajudar estudantes a registrar sessões de estudo, analisar desempenho e receber sugestões de prioridade entre matérias.

O objetivo do projeto é transformar simples registros de estudo em **insights úteis para planejamento**, utilizando lógica de priorização baseada em dificuldade percebida e tempo investido.

---

# **Funcionalidades**

- Cadastro de matérias
 Registro de sessões de estudo (tempo + dificuldade)
- Resumo detalhado por matéria
- Sugestão automática da matéria que merece mais foco
- Interface gráfica simples e intuitiva
- Estrutura de código organizada em módulos

---

# **Lógica da Sugestão Inteligente**

O sistema calcula uma **pontuação de prioridade** para cada matéria considerando:

* média de dificuldade percebida
* tempo total investido

Fórmula utilizada:

```
score = (dificuldade_media * 2) + (1 / (tempo_total + 1)) * 100
```

Isso faz com que:

* matérias **difíceis** ganhem prioridade
* matérias **pouco estudadas** também subam no ranking

Assim o sistema sugere onde o usuário deveria focar seus estudos.

---

# **Interface**

A aplicação possui uma interface gráfica com:

* campo para adicionar matérias
* lista de matérias cadastradas
* registro de sessões de estudo
* visualização de resumo
* sugestão inteligente semanal

## Exemplo da aplicação

https://github.com/user-attachments/assets/cca549de-2dba-499f-ae4b-8281c4f4b139

```
Python
Banco de Dados
Algoritmos
```

---

# **Tecnologias utilizadas**

* Python
* Tkinter
* JSON para persistência de dados
* Programação Orientada a Objetos

---

# ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/organizador-estudos.git
```

### 2️⃣ Entrar na pasta

```
cd organizador-estudos
```

### 3️⃣ Executar o programa

```
python main.py
```

---

# **Autora**

**Larissa Tomé Mussoi**

* LinkedIn: https://www.linkedin.com/in/larissa-mussoi-713217199/
* GitHub: https://github.com/larimussoi

---

Se este projeto te ajudou ou parece interessante, considere deixar uma estrela no repositório.
