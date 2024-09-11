import smtplib
from email.mime.text import MIMEText

def enviar_email(diferencas):
    remetente = 'seuemail@example.com'
    destinatario = 'destinatario@example.com'
    senha = 'senha'

    corpo_email = f"Existem {len(diferencas)} discrepâncias no estoque."
    msg = MIMEText(corpo_email)
    msg['Subject'] = 'Relatório de Estoque Diário'
    msg['From'] = remetente
    msg['To'] = destinatario

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
