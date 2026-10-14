import string
import itertools
import time
from hash_utils import gerar_hash

def simular_ataque_forca_bruta(hash_alvo: int, tamanhos: range = range(1, 6)) -> tuple:
    """
    Simula um ataque testando combinações de caracteres até encontrar
    uma senha que gere o mesmo hash alvo.
    """
    # Alfabeto usado para testar as combinações (letras minúsculas e números)
    caracteres = string.ascii_lowercase + string.digits
    tentativas = 0
    tempo_inicio = time.time()
    
    print(f"\n⚡ Iniciando ataque de Força Bruta para o Hash: {hash_alvo}...")
    
    for tamanho in tamanhos:
        print(f"🔎 Testando combinações de tamanho {tamanho}...")
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativas += 1
            senha_teste = "".join(combinacao)
            hash_teste = gerar_hash(senha_teste)
            
            if hash_teste == hash_alvo:
                tempo_decorrido = time.time() - tempo_inicio
                return senha_teste, tentativas, tempo_decorrido
                
    tempo_decorrido = time.time() - tempo_inicio
    return None, tentativas, tempo_decorrido