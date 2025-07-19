API de Produtos - SmartMarket

Este projeto é uma API RESTful construída com **Python + Flask + SQLite** para simular o gerenciamento de produtos de uma loja fictícia. Ideal para fins de aprendizado e portfólio como desenvolvedor back-end.

---

##  Funcionalidades da API

-  Listar todos os produtos
-  Obter um produto por ID
-  Criar um novo produto
-  Atualizar um produto existente
-  Deletar um produto

---

##  Tecnologias utilizadas

- Python 3.11
- Flask
- Flask SQLAlchemy
- SQLite (banco de dados leve e local)

---

##  Estrutura do Projeto

```plaintext
smartmarket_api/
├── app.py              # Arquivo principal com as rotas da API
├── models.py           # Definição da tabela Produto (ORM)
├── requirements.txt    # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Documentação do projeto
└── database.db         # Banco de dados SQLite (criado automaticamente)
▶️ Como rodar localmente
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/BrunaoDevTI/api-smartmarket-produtos.git
cd api-smartmarket-produtos
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a aplicação:

bash
Copiar
Editar
python app.py
Acesse a API em:

arduino
Copiar
Editar
http://localhost:5000/
📬 Exemplos de uso
🔹 GET /produtos
Retorna todos os produtos cadastrados.

🔹 GET /produtos/1
Retorna o produto com ID 1.

🔹 POST /produtos
json
Copiar
Editar
{
  "nome": "Notebook",
  "categoria": "Eletrônicos",
  "preco": 3500,
  "quantidade": 5
}
🔹 PUT /produtos/1
json
Copiar
Editar
{
  "nome": "Notebook Gamer",
  "categoria": "Eletrônicos",
  "preco": 4200,
  "quantidade": 3
}
🔹 DELETE /produtos/1
Remove o produto com ID 1 do banco.

👨‍💻 Desenvolvido por
Bruno Damasceno
🔗 linkedin.com/in/bruno-damasceno-964a1b25b

🚀 Este projeto faz parte do meu portfólio como desenvolvedor back-end. Feedbacks são bem-vindos!

yaml
Copiar
Editar
