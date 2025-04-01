# Verificar o arquivo send_modularizacao.py com todas as funções
#
from send_modularizacao import Emailer

email = Emailer('dev.antonioaraujo@gmail.com', 'xxxx xxxx xxxxx xxxx')

lista_contatos = ['email_teste_01@gmail.com', 'email_teste_02@gmail.com']

mensagem = '''
Olá seu pacote acaba de chegar nos correios!
'''
email.definir_conteudo(topico='Seu pacote chegou', email_remetente='dev.antonioaraujo@gmail.com',
                       lista_contatos=lista_contatos, conteudo_email=mensagem)

imagens = ['imagens_01.png', 'imagens_03.jpg']
email.anexar_imagem(imagens)

arquivos = ['csv_exemplo.csv', 'PDF_exemplo.pdf', 'ExemploPlanilha.xlsx',
            'exemplo_word.docx', 'Untitled presentation.pptx']
email.anexar_arquivos(arquivos)

email.enviar_email(intervalo_em_segundos=5)
