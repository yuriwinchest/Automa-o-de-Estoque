from scripts.extrair_estoque import extrair_estoque_mercado_livre, extrair_estoque_bling
from scripts.comparar_estoque import comparar_estoque
from scripts.enviar_relatorio import enviar_relatorio
from routes.route import app
import threading
import time

def executar_processo_diario():
    while True:
        # Extrair estoques
        extrair_estoque_mercado_livre()
        extrair_estoque_bling()
        
        # Comparar os estoques
        diferencas = comparar_estoque()
        
        # Enviar relatório com as diferenças
        enviar_relatorio(diferencas)
        
        # Espera 24 horas antes de rodar o processo novamente
        time.sleep(86400)  # 86400 segundos = 24 horas

# Função para rodar o servidor Flask
def iniciar_servidor_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    # Inicia o servidor Flask em uma thread separada
    flask_thread = threading.Thread(target=iniciar_servidor_flask)
    flask_thread.start()

    # Inicia o processo de automação em outra thread
    automacao_thread = threading.Thread(target=executar_processo_diario)
    automacao_thread.start()
