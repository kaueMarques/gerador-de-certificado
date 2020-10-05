from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv, find_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl, yagmail
import pandas as pd
import numpy as np
import os, sys

image     = Image.open('./assets/referencia.png')
font_type = ImageFont.truetype('./assets/GreatVibes-Regular.ttf', 60)
draw      = ImageDraw.Draw(image)

tabelaCSV     = pd.read_csv('./pessoas.csv')
tabelaPessoas = tabelaCSV['certificadoNome'].values
tabelaEmail   = tabelaCSV['email'].values

serverGmail    = smtplib.SMTP('smtp.gmail.com', 587)
gmail_user     = ''
gmail_password = ''

def geradorDeCertificado(nome):
    draw.text(xy=(510,525), text=nome, fill='black', font=font_type)
    image.save('./certificados/{nome}.png'.format(nome=nome))

def gerarCertificadoDoCSV():
    for i in tabelaPessoas:
        geradorDeCertificado(i)

gerarCertificadoDoCSV()
