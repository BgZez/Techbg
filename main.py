# Sistema básico de login
usuarios = {}

def registrar():
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    usuarios[nome] = senha
    print("Usuário registrado!")

def login():
    nome = input("Usuário: ")
    senha = input("Senha: ")
    
    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

# Menu principal
while True:
    print("\n1. Registrar\n2. Login\n3. Sair")
    opcao = input("Escolha: ")
    
    if opcao == "1":
        registrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        break