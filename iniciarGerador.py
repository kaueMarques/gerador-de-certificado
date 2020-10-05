from PIL import Image, ImageDraw, ImageFont
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib, ssl
import pandas as pd
import numpy as np
import os, sys 

image     = Image.open('./assets/referencia.png')
font_type = ImageFont.truetype('./assets/GreatVibes-Regular.ttf', 60)
draw      = ImageDraw.Draw(image)

tabelaCSV     = pd.read_csv('./pessoas.csv')
tabelaPessoas = tabelaCSV['certificadoNome'].values
tabelaEmail   = tabelaCSV['email'].values

server         = smtplib.SMTP('smtp.gmail.com', 587)
context        = ssl.create_default_context()
destinatario   = ''
gmail_user     = ''
gmail_password = ''

def geradorDeCertificado(nome):
    draw.text(xy=(510,528), text=nome, fill='black', font=font_type)
    image.save('./certificados/{nome}.png'.format(nome=nome))

def gerarCertificadoDoCSV():
    for i in tabelaPessoas:
        geradorDeCertificado(i)

def gerarMensagem():
    server.sendmail(gmail_user, 'mbkaue@gmail.com', 'email enviado pelo scrpt\nass,\nkaue')

def enviarEmail():
    try:
        server.starttls(context=context)
        server.login(gmail_user, gmail_password)
        gerarMensagem()
    except Exception as e:
        print('erro:\n', e)
    finally:
        server.quit()

def main():
    print('message')
