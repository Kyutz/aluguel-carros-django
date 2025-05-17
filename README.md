# Sistema de Aluguel de Carros

Este repositório contém um sistema web de aluguel de carros desenvolvido com o framework Django. O projeto foi criado como parte da disciplina GAC116 – Programação Web da Universidade Federal de Lavras (UFLA).

## Objetivo

Desenvolver uma aplicação web funcional com foco no backend utilizando Django, implementando um modelo de banco de dados para gerenciamento de clientes, carros e aluguéis, além da visualização e controle dos dados via Django Admin.

## Funcionalidades (Checkpoint 1)

- Definição completa dos modelos de dados
- Interface administrativa via Django Admin

## Tecnologias utilizadas

- Python 3.10+
- Django 4.x

## Requisitos do sistema

- Python 3.10 ou superior
- Virtualenv (recomendado)

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Kyutz/aluguel-carros-django.git
cd aluguel-carros
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o banco de dados e aplique as migrações:

```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o Django Admin:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor local:

```bash
python manage.py runserver
```

7. Acesse o painel administrativo em:

```
http://127.0.0.1:8000/admin/
```

## Estrutura do projeto

```
aluguel-carros-django/
├── aluguel_carros/        # Diretório do projeto Django (configurações principais)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Configurações do Django
│   ├── urls.py
│   └── wsgi.py
├── locadora/              # Aplicativo principal com os modelos
│   ├── __init__.py
│   ├── admin.py           # Registro dos modelos no admin
│   ├── apps.py
│   ├── models.py          # Definição das entidades
│   ├── tests.py
│   └── views.py
│   └── ...
├── db.sqlite3             # Banco de dados SQLite
├── manage.py              # Script de gerenciamento do Django
├── README.md              # Arquivo de documentação do projeto
└── requirements.txt       # Dependências do projeto
```

## Regras de commit

Para manter a organização e facilitar a leitura do histórico de alterações, utilize mensagens de commit padronizadas no seguinte formato:

```
<tipo>: <descrição breve da mudança>
```

### Tipos de commit

- **feat**: Adição de nova funcionalidade ao sistema.
  - Exemplo: `feat: adicionar modelo de Cliente`

- **fix**: Correção de bug ou comportamento inesperado.
  - Exemplo: `fix: corrigir erro na criação de Aluguel`

- **docs**: Alterações na documentação (README, comentários, etc.).
  - Exemplo: `docs: atualizar instruções de execução`

- **style**: Alterações de formatação que não afetam a lógica do código (espaços, quebras de linha, etc.).
  - Exemplo: `style: ajustar identação do views.py`

- **refactor**: Refatoração de código (reestruturação interna sem alterar comportamento).
  - Exemplo: `refactor: separar lógica de validação em função auxiliar`

- **test**: Criação ou modificação de testes.
  - Exemplo: `test: adicionar testes para modelo de Carro`

- **chore**: Tarefas de manutenção que não afetam a lógica do sistema (atualização de dependências, configs, etc.).
  - Exemplo: `chore: atualizar .gitignore`

## Autores

- Thallys Henrique Martins
- Gabriel Marcos Lopes
- Bruno de Almeida de Paula

Curso de Ciência da Computação - Universidade Federal de Lavras (UFLA)
