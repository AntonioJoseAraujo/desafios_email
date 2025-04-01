import smtplib
from email.message import EmailMessage
from time import sleep

# Configuração de login
EMAIL_ADDRESS = 'dev.antonioaraujo@gmail.com'  # E-mail que vai ser o remetente
EMAIL_PASSWORD = 'xxxx xxxxx xxxx xxxxx'   # Senha que o google gera automaticamente na segurança de duas etapas

contatos = ['email_teste01@gmail.com','email_teste02@gmail.com']


# Enviar o email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
    email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    for contato in contatos:
        # Criar e enviar um email
        mail = EmailMessage()
        mail['Subject'] = 'Segue envio de Email em Massa'
        mensagem = '''
        Parabens, você recebeu um email em massa!
        '''
        mail['From'] = EMAIL_ADDRESS
        mail['To'] = contato
        mail.add_header('Content-Type', 'text/html')
        mail.set_payload(mensagem.encode('utf-8'))
        email.send_message(mail)
        sleep(5)