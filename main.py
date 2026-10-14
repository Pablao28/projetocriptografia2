from autenticacao import SistemaAutenticacao
from forca_bruta import simular_ataque_forca_bruta

def exibir_menu():
    print("\n" + "="*40)
    print(" SISTEMA DE AUTENTICAÇÃO E FORÇA BRUTA")
    print("="*40)
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Simular Ataque por Força Bruta")
    print("4. Sair")
    return input("Escolha uma opção (1-4): ").strip()

def main():
    sistema = SistemaAutenticacao()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            user = input("\nNome de usuário: ").strip()
            senha = input("Senha: ").strip()
            sistema.cadastrar_usuario(user, senha)
            
        elif opcao == "2":
            user = input("\nNome de usuário: ").strip()
            senha = input("Senha: ").strip()
            sistema.verificar_login(user, senha)
            
        elif opcao == "3":
            user = input("\nDigite o nome do usuário a ser atacado: ").strip()
            hash_alvo = sistema.obter_hash_usuario(user)
            
            if hash_alvo is None:
                print("❌ Usuário não existe no sistema. Cadastre-o primeiro!")
            else:
                senha_encontrada, tentativas, tempo = simular_ataque_forca_bruta(hash_alvo)
                
                if senha_encontrada:
                    print("\n🎯 ATAQUE BEM-SUCEDIDO!")
                    print(f"🔑 Senha/Combinação encontrada: '{senha_encontrada}'")
                    print(f"📊 Total de tentativas: {tentativas:,}")
                    print(f"⏱️ Tempo decorrido: {tempo:.4f} segundos")
                else:
                    print("\n🛡️ O ataque falhou em encontrar a combinação no limite de caracteres pré-definido.")
                    print(f"📊 Total de tentativas executadas: {tentativas:,}")
                    print(f"⏱️ Tempo decorrido: {tempo:.4f} segundos")
                    
        elif opcao == "4":
            print("\nEncerrando a aplicação... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()