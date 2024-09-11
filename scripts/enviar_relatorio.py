from utils.email_utils import enviar_email
from scripts.comparar_estoque import comparar_estoques


def enviar_relatorio_diferencas():
    diferencas = comparar_estoques()
    if diferencas:
        # Envia um e-mail com as diferenças
        enviar_email(diferencas)
