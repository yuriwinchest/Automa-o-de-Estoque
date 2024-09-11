# mercado_livre_api.py
import requests

def extrair_dados_mercado_livre(conta_id, access_token):
    """
    Função para extrair dados de estoque do Mercado Livre via API.
    :param conta_id: ID da conta do Mercado Livre.
    :param access_token: Token de acesso à API.
    :return: Lista de produtos ou uma mensagem de erro.
    """
    url = f'https://api.mercadolibre.com/users/{conta_id}/items/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    
    try:
        response = requests.get(url, headers=headers)
        
        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            produtos = response.json().get('results', [])
            return produtos
        else:
            print(f"Erro {response.status_code}: {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar à API do Mercado Livre: {e}")
        return None
