from PIL import Image, ImageDraw, ImageFont
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib, ssl
import pandas as pd
import numpy as np
import os, sys
import random

tabelaCSV       = pd.read_csv('./pessoas.csv')
colunaPessoas   = tabelaCSV['certificadoNome'].values
colunaEmail     = pd.DataFrame(tabelaCSV, columns = ['email'])

image           = Image.open('./assets/referencia.png')
draw            = ImageDraw.Draw(image)

cod             = random.randint(100000, 999999)
cod_img         = str(cod)

font_type       = ImageFont.truetype('./assets/GreatVibes-Regular.ttf', 40)
font_verifier   = ImageFont.truetype('./assets/Cairo-Light.ttf', 18)

server           = smtplib.SMTP('smtp.gmail.com', 587)
context          = ssl.create_default_context()
sender_pass      = ''
sender_address   = ''
gmail_password   = ''
receiver_address = ''

def gerarCertificado(nome, verifier):
    draw.text(xy=(140,200), text=nome, fill='white', font=font_type)
    draw.text(xy=(780,510), text=verifier, fill='white', font=font_verifier)
    image.save('certificado.png')

def gerarCertificadosCSV():
    for i in colunaPessoas:
        gerarCertificado(i)


gerarCertificado('Kauê Marques Barbosa', f'verificador: CN-{cod_img}')
print('Verificador',cod_img)