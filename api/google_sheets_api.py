import requests
import gspread
from google.oauth2.service_account import Credentials
import gspread







# Função para autenticar no Google Sheets
def autenticar_google_sheets():
    """
    Autentica o cliente do Google Sheets usando credenciais de serviço.
    :return: Objeto client para interagir com as planilhas do Google Sheets.
    """
    SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file('credenciais.json', scopes=SCOPE)
    client = gspread.authorize(creds)
    return client

# Função para extrair dados do Mercado Livre (usando duas contas)
def extrair_dados_mercado_livre(conta_id, access_token):
    url = f'https://api.mercadolibre.com/users/{conta_id}/items/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Fazer a requisição
    response = requests.get(url, headers=headers)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Verificar o conteúdo da resposta
        print("Resposta da API do Mercado Livre:", response.json())  # Depuração
        
        # Tenta acessar a chave 'results'
        try:
            return response.json()['results']  # Retorna os itens encontrados
        except KeyError:
            print("Chave 'results' não encontrada na resposta da API.")
            return None
    else:
        # Caso a requisição falhe, mostrar o código de status e a mensagem de erro
        print(f"Erro na requisição. Status code: {response.status_code}")
        print("Conteúdo da resposta:", response.json())
        return None

# Função para extrair dados do Mercado Livre (usando duas contas)
def extrair_dados_mercado_livre(conta_id, access_token):
    url = f'https://api.mercadolibre.com/users/{conta_id}/items/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()['results']  # Retorna os itens encontrados

# Função para enviar dados ao Google Sheets
def salvar_no_google_sheets(planilha_nome, dados):
    try:
        client = autenticar_google_sheets()  # Autenticar
        planilha = client.open(planilha_nome)  # Abrir a planilha pelo nome
        worksheet = planilha.sheet1  # Selecionar a primeira aba (sheet1)
        
        worksheet.clear()  # Limpa os dados antigos
        worksheet.append_row(['Nome da Conta', 'SKU', 'MLB', 'Quantidade'])  # Cabeçalho

        for item in dados:
            worksheet.append_row([item['conta'], item['sku'], item['mlb'], item['quantidade']])
        
        print("Dados salvos com sucesso no Google Sheets")
    
    except Exception as e:
        print(f"Erro ao salvar no Google Sheets: {e}")

# Executa a extração de dados de duas contas do Mercado Livre
def extrair_e_salvar_mercado_livre():
    conta1_dados = extrair_dados_mercado_livre(conta_id='123456', access_token='TOKEN_CONTA1')
    conta2_dados = extrair_dados_mercado_livre(conta_id='654321', access_token='TOKEN_CONTA2')
    
    # Combine os dados das duas contas
    dados_combinados = conta1_dados + conta2_dados
    salvar_no_google_sheets('Estoque Mercado Livre', dados_combinados)

# Chamar a função principal para rodar o processo
extrair_e_salvar_mercado_livre()
