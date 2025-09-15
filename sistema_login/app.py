from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
CORS(app)

# --- CONFIGURE AQUI: altere se necessário ---
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "sua_senha",
    "database": "sistema_usuarios",
}
# ---------------------------------------------

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    username = data.get('username', '').strip()
    senha = data.get('senha', '').strip()

    if not username or not senha:
        return jsonify({"error": "username e senha são obrigatórios"}), 400

    hashed = generate_password_hash(senha)

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
    if cursor.fetchone():
        cursor.close()
        db.close()
        return jsonify({"error": "Usuário já existe"}), 400

    cursor.execute("INSERT INTO usuarios (username, senha) VALUES (%s, %s)", (username, hashed))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '').strip()
    senha = data.get('senha', '').strip()

    if not username or not senha:
        return jsonify({"error": "username e senha são obrigatórios"}), 400

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    db.close()

    if user and check_password_hash(user['senha'], senha):
        return jsonify({"message": "Login realizado com sucesso!"}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def frontend_files(filename):
    return send_from_directory('frontend', filename)

if __name__ == '__main__':
    # Apenas para desenvolvimento. Em produção, use um WSGI server.
    app.run(debug=True)
