import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.extrair_estoque import processar_estoque, extrair_dados_publicos

# Função para carregar dados do arquivo de log
def ler_arquivo_log(log_file):
    with open(log_file, 'r') as file:
        return file.read()

# Função para carregar os dados fictícios de uma planilha no Google Sheets (ou outro lugar)
def carregar_dados_google_sheets(planilha_nome):
    # Para simplificação, usaremos dados fictícios aqui em vez de conectar ao Google Sheets.
    # Exemplo fictício de dados retornados:
    dados = {
        'SKU': ['Produto 1', 'Produto 2', 'Produto 3'],
        'Quantidade': [100, 150, 200],
        'Diferença': [5, -10, 0]
    }
    return pd.DataFrame(dados)

# Título da aplicação
st.title("Dashboard de Estoques: Mercado Livre e Bling")

# Botão para processar os estoques
if st.button('Processar Estoques'):
    processar_estoque('Estoque Mercado Livre', 'Estoque Bling', 'Diferencas Estoque')
    st.success("Estoque processado e diferenças salvas no Google Sheets!")

# Carregar os dados do Google Sheets ou de uma fonte simulada
dados_mercado_livre = carregar_dados_google_sheets('Estoque Mercado Livre')
dados_bling = carregar_dados_google_sheets('Estoque Bling')
diferencas = carregar_dados_google_sheets('Diferencas Estoque')

# Mostrar os dados em tabelas
st.subheader("Tabela de Estoque Mercado Livre")
st.dataframe(dados_mercado_livre)

st.subheader("Tabela de Estoque Bling")
st.dataframe(dados_bling)

st.subheader("Tabela de Diferenças de Estoque")
st.dataframe(diferencas)

# Gráficos
st.subheader("Gráfico de Estoque por SKU (Mercado Livre)")
fig_ml = px.bar(dados_mercado_livre, x='SKU', y='Quantidade', title="Estoque Mercado Livre por SKU")
st.plotly_chart(fig_ml)

st.subheader("Gráfico de Estoque por SKU (Bling)")
fig_bling = px.bar(dados_bling, x='SKU', y='Quantidade', title="Estoque Bling por SKU")
st.plotly_chart(fig_bling)

st.subheader("Diferenças de Estoque entre Mercado Livre e Bling")
fig_diferencas = px.bar(diferencas, x='SKU', y='Diferença', title="Diferenças de Estoque")
st.plotly_chart(fig_diferencas)

# Ler e exibir o conteúdo do arquivo de log
log_content = ler_arquivo_log('logs/estoque_automacao.log')
st.subheader("Log de Extração de Dados")
st.text_area("Conteúdo do Log", log_content, height=300)
