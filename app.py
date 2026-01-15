from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
USERS_FILE = "users.json"

def load_users():
    """Carrega usuários do arquivo JSON"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    """Salva usuários no arquivo JSON"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

@app.route('/')
def home():
    """Página inicial"""
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Processa login"""
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    users = load_users()
    
    if username in users and users[username] == password:
        return f'''
        <html>
        <head><title>Login Bem-sucedido</title></head>
        <body style="font-family: Arial; padding: 40px;">
            <h1>🎉 Login Bem-sucedido!</h1>
            <p>Bem-vindo(a), <strong>{username}</strong>!</p>
            <p>✅ Autenticação realizada com sucesso.</p>
            <a href="/" style="color: blue;">← Voltar ao login</a>
        </body>
        </html>
        '''
    else:
        return '''
        <html>
        <head><title>Erro no Login</title></head>
        <body style="font-family: Arial; padding: 40px;">
            <h1>❌ Erro no Login</h1>
            <p>Usuário ou senha incorretos.</p>
            <a href="/" style="color: blue;">← Tentar novamente</a>
        </body>
        </html>
        '''

@app.route('/register', methods=['POST'])
def register():
    """Processa registro"""
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    if not username or not password:
        return "Erro: Preencha todos os campos!"
    
    users = load_users()
    
    if username in users:
        return f"Erro: Usuário '{username}' já existe!"
    
    users[username] = password
    save_users(users)
    
    return f'''
    <html>
    <head><title>Registro Bem-sucedido</title></head>
    <body style="font-family: Arial; padding: 40px;">
        <h1>✅ Registro Bem-sucedido!</h1>
        <p>Usuário <strong>{username}</strong> criado com sucesso.</p>
        <p>Total de usuários no sistema: {len(users)}</p>
        <a href="/" style="color: blue;">← Fazer login</a>
    </body>
    </html>
    '''

@app.route('/users')
def list_users():
    """Lista todos os usuários (para demonstração)"""
    users = load_users()
    user_list = "<br>".join([f"- {user}" for user in users.keys()])
    
    return f'''
    <html>
    <head><title>Usuários Registrados</title></head>
    <body style="font-family: Arial; padding: 40px;">
        <h1>👥 Usuários Registrados</h1>
        <p>Total: {len(users)} usuário(s)</p>
        <div>{user_list}</div>
        <br>
        <a href="/" style="color: blue;">← Voltar ao login</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 SISTEMA DE LOGIN ÁGIL INICIANDO...")
    print("👉 Acesse: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)