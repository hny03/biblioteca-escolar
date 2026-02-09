# Projeto A – Sistema de Biblioteca Escolar 📚

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um **Sistema de Biblioteca Escolar em Python**, executado via terminal, cujo objetivo é auxiliar no gerenciamento de livros, usuários e empréstimos de uma biblioteca.

O sistema resolve o problema do controle manual do acervo e dos empréstimos, permitindo registrar livros, cadastrar usuários, controlar a quantidade disponível de cada obra e acompanhar empréstimos e devoluções de forma simples, organizada e intuitiva.

---

## ⚙️ Funcionalidades Implementadas

O sistema é acessado por meio de um menu interativo e possui as seguintes funcionalidades:

### 📚 Gerenciamento de Livros
- Cadastrar novos livros
- Adicionar ou remover exemplares de livros existentes
- Listar todos os livros cadastrados e suas respectivas disponibilidades

### 👤 Gerenciamento de Usuários
- Cadastrar novos usuários
- Listar todos os usuários cadastrados

### 🔄 Empréstimos e Devoluções
- Registrar empréstimos de livros
- Registrar devoluções
- Listar todos os empréstimos realizados

---

## ▶️ Como Executar o Projeto

### 1️⃣ Pré-requisitos
- **Python 3.8 ou superior**
- Sistema operacional com acesso ao terminal (Windows, Linux ou macOS)

> O projeto não utiliza bibliotecas externas, apenas módulos padrão do Python.

---

### 2️⃣ Clonar o Repositório

git clone https://github.com/seu-usuario/nome-do-repositorio.git 

Acesse o diretório do projeto: cd nome-do-repositório

### 3️⃣ Executar o Sistema 

No terminal, execute o arquivo principal: python main.py 
Após a execução, o menu será exibido e o sistema estará pronto para uso


---

## 🗂️ Estrutura de Diretórios 
```text
.
├── main.py
├── models.py
├── actions/
│   ├── user_actions.py
│   ├── book_actions.py
│   └── loan_actions.py
├── data/
│   ├── users.csv
│   ├── books.csv
│   └── loans.csv
└── README.md
.

