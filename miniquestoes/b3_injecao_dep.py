# Exercicio 08 - Aula 08 - Injeção de Dependencia
class BancoMySQL:
    def salvar(self, dados: str) -> None:
        print(f"Salvando '{dados}' no banco MySQL...")

class BancoPostgreSQL:
    def salvar(self, dados: str) -> None:
        print(f"Salvando '{dados}' no banco PostgreSQL...")

class UsuarioService:
    def __init__(self, banco):
        self.banco = banco
    
    def registrar_usuario(self, nome: str) -> None:
        self.banco.salvar(f"Usuário {nome}")

um = BancoMySQL()
up = BancoPostgreSQL()

us1 = UsuarioService(um)
us1.registrar_usuario("Higor")
us2 = UsuarioService(up)
us2.registrar_usuario("Diego")