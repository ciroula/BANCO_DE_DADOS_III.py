from services.usuario_services import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    services = UsuarioService(repository)

    #Solicitando dados para o usuário.
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")

    services.criar_usuario(nome = nome, email = email, senha = senha)

    #Listar todos os usúarios cadastrados.
    print ("\nListando usúarios cadastrados.")
    lista_usuario = services.listar_todos_usuarios()
    for usuario in lista_usuario:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha {usuario.senha}")

if __name__ == "__main__":
    main()
