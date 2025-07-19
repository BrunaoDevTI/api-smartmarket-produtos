from flask import Flask, request, jsonify
from models import db, Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return {"mensagem": "API SmartMarket está no ar!"}

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([p.to_dict() for p in produtos])

@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produto = Produto.query.get_or_404(id)
    return jsonify(produto.to_dict())

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    novo = Produto(**dados)
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto = Produto.query.get_or_404(id)
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(produto, chave, valor)
    db.session.commit()
    return jsonify(produto.to_dict())

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return {"mensagem": f"Produto {id} deletado."}

if __name__ == '__main__':
    app.run(debug=True)
