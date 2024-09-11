# comparar_estoque.py
from api.google_sheets_api import autenticar_google_sheets

# Função para carregar os dados das planilhas
def carregar_planilhas_google(planilha_ml_nome, planilha_bling_nome):
    client = autenticar_google_sheets()
    planilha_ml = client.open(planilha_ml_nome)
    planilha_bling = client.open(planilha_bling_nome)
    dados_ml = planilha_ml.sheet1.get_all_records()
    dados_bling = planilha_bling.sheet1.get_all_records()
    return dados_ml, dados_bling

# Função para comparar estoques entre Mercado Livre e Bling
def comparar_estoques(mercado_livre, bling):
    diferencas = []

    for item_ml in mercado_livre:
        sku = item_ml['SKU']
        estoque_ml = item_ml['Quantidade']
        estoque_bling = next((item['Estoque Bling'] for item in bling if item['SKU'] == sku), None)

        if estoque_bling is not None and estoque_ml != estoque_bling:
            diferenca = abs(estoque_ml - estoque_bling)
            diferencas.append([sku, estoque_ml, estoque_bling, diferenca])
    
    return diferencas

# Função para salvar as diferenças no Google Sheets
def salvar_diferencas_no_google_sheets(planilha_nome, diferencas):
    client = autenticar_google_sheets()
    planilha = client.open(planilha_nome)
    worksheet = planilha.sheet1
    worksheet.clear()  # Limpa os dados antigos
    worksheet.append_row(['SKU', 'Quantidade ML', 'Estoque Bling', 'Diferença'])  # Cabeçalho

    for item in diferencas:
        worksheet.append_row(item)
