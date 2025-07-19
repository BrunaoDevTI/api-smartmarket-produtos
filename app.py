# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Rota inicial
@app.route('/')
def home():
    return {"mensagem": "API SmartMarket está no ar!"}

# Listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([p.to_dict() for p in produtos])

# Obter um produto específico
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produto = Produto.query.get_or_404(id)
    return jsonify(produto.to_dict())

# Criar novo produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    novo = Produto(
        nome=dados['nome'],
        categoria=dados['categoria'],
        preco=dados['preco'],
        quantidade=dados['quantidade']
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

# Atualizar um produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto = Produto.query.get_or_404(id)
    dados = request.get_json()
    produto.nome = dados['nome']
    produto.categoria = dados['categoria']
    produto.preco = dados['preco']
    produto.quantidade = dados['quantidade']
    db.session.commit()
    return jsonify(produto.to_dict())

# Deletar produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return {"mensagem": f"Produto {id} deletado."}

if __name__ == '__main__':
    app.run(debug=True)


# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'categoria': self.categoria,
            'preco': self.preco,
            'quantidade': self.quantidade
        }
    
a = 1 