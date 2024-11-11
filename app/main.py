import os
from app.services.usuario_services import UsuarioService
from app.repositories.usuario_repositories import UsuarioRepository
from app.config.database import Session
import sys

#Adicionna o diretorio 'app' como diretorio padrão.
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

def main():
    session = Session()
    repository = UsuarioRepository(session)
    services = UsuarioService(repository)

    # Solicitando dados para o usuário.
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")

    services.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usúarios cadastrados.
    print("\nListando usúarios cadastrados.")
    lista_usuario = services.listar_todos_usuarios()
    for usuario in lista_usuario:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha {usuario.senha}")


if __name__ == "__main__":
    os.system("cls || clear")
    main()
