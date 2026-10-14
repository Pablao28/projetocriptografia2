from hash_utils import gerar_hash

class SistemaAutenticacao:
    def __init__(self):
        # "Banco de dados" em memória armazenando {usuario: hash_da_senha}
        self._banco_dados = {}

    def cadastrar_usuario(self, usuario: str, senha: str) -> bool:
        if usuario in self._banco_dados:
            print("⚠️ Usuário já cadastrado!")
            return False
            
        hash_senha = gerar_hash(senha)
        self._banco_dados[usuario] = hash_senha
        print(f"✅ Usuário '{usuario}' cadastrado com sucesso!")
        print(f"🔒 Hash salvo no banco: {hash_senha} (A senha real nunca é armazenada)")
        return True

    def verificar_login(self, usuario: str, senha: str) -> bool:
        if usuario not in self._banco_dados:
            print("❌ Usuário não encontrado!")
            return False
            
        hash_tentativa = gerar_hash(senha)
        hash_salvo = self._banco_dados[usuario]
        
        if hash_tentativa == hash_salvo:
            print("🔓 Login realizado com sucesso!")
            return True
        else:
            print("❌ Senha incorreta!")
            return False

    def obter_hash_usuario(self, usuario: str):
        return self._banco_dados.get(usuario, None)