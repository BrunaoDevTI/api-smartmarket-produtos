# app.py
from flask import Flask, request, jsonify
from models import db, Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
