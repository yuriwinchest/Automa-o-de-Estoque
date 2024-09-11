# main.py
from scripts.extrair_estoque import extrair_dados_publicos

# Executar a função de extração de dados da API pública
dados = extrair_dados_publicos()

if dados:
    # Exibir os primeiros 5 itens para teste
    print("Dados da API pública:")
    for item in dados[:5]:
        print(item)
else:
    print("Falha ao extrair os dados.")
