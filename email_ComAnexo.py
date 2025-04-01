import smtplib
from email.message import EmailMessage
from PIL import Image

# Configuração de login
EMAIL_ADDRESS = 'dev.antonioaraujo@gmail.com'  # E-mail que vai ser o remetente
# Senha que o google gera automaticamente na segurança de duas etapas
EMAIL_PASSWORD = 'werwrwe qerewrw adasda wadaada'

# Criar e enviar um email
mail = EmailMessage()
mail['Subject'] = 'Favor baixar estes arquivos'
mensagem = '''
Baixe seus arquivos em anexo.
'''
mail['From'] = EMAIL_ADDRESS
mail['To'] = 'email_que_vai_receber@gmail.com'
mail.add_header('Content-Type', 'text/html')
mail.set_payload(mensagem.encode('utf-8'))

# Anexo de arquivos
imagens = ['4147330.jpg', 'thumb-1920.png',
           'C:\\Users\\anton\\Pictures\\Saved Pictures\\brinqOver.jpg']
for imagem in imagens:
    for imagem in imagens:
        with open(imagem, 'rb') as arquivo:
            dados = arquivo.read()
            img = Image.open(arquivo)
            # Obtém extensão da imagem (jpeg, png, etc.)
            extensao_imagem = img.format.lower()
            nome_arquivo = arquivo.name
            mail.add_attachment(dados, maintype='image',
                                subtype=extensao_imagem, filename=nome_arquivo)

# Anexar qualquer tipo de arquivo (que não seja imagem)
arquivos = ['csv_exemplo.csv', 'exemplo_word.docx',
            'ExemploPlanilha.xlsx', 'PDF_Exemplo.pdf', 'Untitled presentation.pptx']

for arquivo in arquivos:
    with open(arquivo, 'rb') as arquivo:
        dados = arquivo.read()
        nome_arquivo = arquivo.name
        mail.add_attachment(dados, maintype='application',
                            subtype='octet-stream', filename=nome_arquivo)

# Enviar o email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
    email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    email.send_message(mail)
