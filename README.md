# To-Do List CRUD com FastAPI

Este projeto é uma API para gerenciamento de uma lista de tarefas (To-Do List) que permite aos usuários criar, visualizar, atualizar e deletar tarefas. Construí esse projeto usando Python e FastAPI como framework principal, oferecendo uma experiência rápida e eficiente aos usuários.

## Tecnologias Utilizadas

- **FastAPI**: Escolhi por ser um framework web moderno, eficiente, e do qual estou concentrando minhas forças em aprender.
- **Uvicorn**: Um servidor ASGI que usei por ser leve e rápido, perfeito para servir à aplicação e explorar a documentação interativa Swagger UI em sua versão mais recente.
- **SQLite3**: Foi meu sistema de gerenciamento de banco de dados inicial para o armazenamento das tabelas.
- **PostgreSQL**: Optei por migrar para essa DataBase ao longo do projeto, visto que almejei adquirir uma experiência com um Banco de Dados Relacional.
- **Alembic**: Usei para realizar a migração do SQLite3 para o PostgreSQL de forma fluida e facilitada.
- **JSON Web Tokens (JWT)**: Implementei para autenticação de usuários, buscando adquirir uma experiência com segurança de dados e autenticação.

## Funcionalidades Do Projeto

- **Autenticação de Usuários**: Implementei o cadastro e login usando JWT para proteger as rotas e assegurar que apenas usuários autenticados possam gerenciar seus To-Do's.
- **Gerenciamento de To-Do's**:
  - **Criação**: Adição de novos To-Do's com título, descrição, prioridade e status.
  - **Visualização**: Exibição dos To-Do's em uma lista, com a possibilidade de filtrá-los por status, prioridade ou ID.
  - **Atualização**: Edição de To-Do's existentes através de seu ID, seja em seu título, descrição, prioridade ou status.
  - **Deleção**: Remoção de To-Do's existentes.

- **Cadastro de Usuários**: A aplicação permite que novos usuários se cadastrem com informações pessoais básicas, como : username, primeiro e último nome, e-mail, número de telefone e seu cargo (admin, user...).
- **Atualização de Senha**: O projeto permite que o usuário não só tenha a sua senha criptografada como também o permite editá-la.

## Como Rodar o Projeto na sua Máquina

Para executar o projeto em sua máquina, siga estes passos:

1. Clone o repositório do projeto.
2. Configure a conexão com a base de dados seguindo os passos abaixo:

    - 2.1 Crie um servidor local no PostgreSQL
    - 2.2 No arquivo 'database.py' modifique a URL de acordo com os dados referentes à sua conta (atente-se à senha e ao nome do servidor)
  
4. Para iniciar a aplicação com Uvicorn, execute `uvicorn main:app --reload` no terminal. Isso vai iniciar a documentação interativa Swagger UI automaticamente.
5. Acesse `http://localhost:8000/docs` no navegador para ver a documentação da API e experimentar os endpoints.

## Minha experiência com esse projeto 

- Com esse projeto, consegui ter uma boa curva de aprendizado no que diz respeito à criação de operações CRUD.

- Isso se deve não só à todos os _endpoints_ que criei, mas também à experiência enriquecedora de configurar todo o _setup_ desse projeto, utilizando diversas bibliotecas diferentes e ferramentas novas para fins específicos.

- Além disso, a experiência de migração de base de dados usando o Alembic me deu a oportunidade de adquirir uma primeira experiência com um Banco de Dados Relacional, que nesse projeto foi o PostgreSQL.

- Ainda nesse contexto, a experiência de criar um segundo projeto CRUD com FastAPI me deu mais familiaridade com essa excelente framework e me motivou à continuar estudando e praticando por meio de projetos.
