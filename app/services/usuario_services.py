from app.models.usuario_models import Usuario
from app.repositories.usuario_repositories import UsuarioRepository


class UsuarioService:

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:

            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)

            if novo_usuario:
                print("usuário ja cadastrado!")
                return

            usuario = Usuario(nome=nome, email=email, senha=senha)

            self.repository.salvar_usuario(usuario)
            print("Usuario cadastrado com sucesso")
        except TypeError as erro:
            print(f"Erro ao salvar o usuario: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
