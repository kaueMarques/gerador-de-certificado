from PIL import Image, ImageDraw, ImageFont
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib, ssl
import pandas as pd
import numpy as np
import os, sys

tabelaCSV      = pd.read_csv('./pessoas.csv')
colunaPessoas  = tabelaCSV['certificadoNome'].values
colunaEmail    = pd.DataFrame(tabelaCSV, columns = ['email'])

image     = Image.open('./assets/referencia.png')
font_type = ImageFont.truetype('./assets/GreatVibes-Regular.ttf', 40)
draw      = ImageDraw.Draw(image)

server         = smtplib.SMTP('smtp.gmail.com', 587)
context        = ssl.create_default_context()
gmail_user     = ''
gmail_password = ''

def gerarCertificado(nome):
    draw.text(xy=(260,170), text=nome, fill='white', font=font_type)
    image.save('./certificados/{nome}.png'.format(nome=nome))

def gerarCertificadosCSV():
    for i in colunaPessoas:
        gerarCertificado(i)


def gerarMensagem():
    print(gmail_user,  'email enviado pelo script')
#server.sendmail

def enviarEmail():
    try:
        server.starttls(context=context)
        server.login(gmail_user, gmail_password)
        gerarMensagem()
    except Exception as e:
        print('erro:\n', e)
    finally:
        server.quit()

gerarCertificadosCSV()
