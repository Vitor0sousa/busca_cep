import requests

def validar_cep(cep):
    # Remove caracteres não numéricos
    cep = "".join(filter(str.isdigit, str(cep)))
    
    # Valida formato básico (8 dígitos)
    if len(cep) != 8:
        return {"erro": "CEP deve conter 8 dígitos numéricos"}

    # Chamada à API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        # Verifica se o CEP é inexistente
        if "erro" in dados:
            return {"erro": "CEP não encontrado"}
        
        return dados # Retorna logradouro, bairro, localidade, uf
    
    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro na conexão: {e}"}

# Exemplo de uso
cep_input = input("qual o cep") # Exemplo válido
resultado = validar_cep(cep_input)
print(resultado)
