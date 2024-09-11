import requests

def extrair_dados_publicos():
    """
    Função para extrair dados de uma API pública (JSONPlaceholder) para teste.
    :return: Lista de dados ou uma mensagem de erro.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'  # URL de exemplo da API pública

    try:
        response = requests.get(url)
        
        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Exibir a resposta completa para depuração
            print("Resposta da API pública:", response.json())
            
            # Retorna os dados da resposta
            return response.json()
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar à API pública: {e}")
        return None

# Teste a função
dados = extrair_dados_publicos()

if dados:
    for item in dados[:5]:  # Exibir os primeiros 5 itens para teste
        print(item)
else:
    print("Falha ao extrair os dados.")
