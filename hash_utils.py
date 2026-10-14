def gerar_hash(texto: str, limite_modulo: int = 1000000) -> int:
    """
    Gera um hash numérico customizado baseado na ordem dos caracteres e Tabela ASCII.
    A ordem altera o resultado devido ao peso (multiplicação por posição/índice).
    O operador módulo (%) garante um tamanho limitado e padronizado.
    """
    hash_valor = 0
    prime_multiplier = 31
    
    for indice, caractere in enumerate(texto):
        codigo_ascii = ord(caractere)
        # A posição (indice + 1) garante que a ordem das letras mude o hash final
        peso_posicao = (indice + 1) * prime_multiplier
        hash_valor += (codigo_ascii * peso_posicao)
        
    return hash_valor % limite_modulo