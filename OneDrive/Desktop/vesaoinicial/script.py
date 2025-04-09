import os
import pandas as pd
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# Escopos de permissão para Gmail e Drive
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/drive.file'
]

def obter_credenciais():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def enviar_email(auth_credentials, destinatario, link):
    try:
        service = build('gmail', 'v1', credentials=auth_credentials)
        mensagem = MIMEMultipart()
        mensagem['From'] = 'me'
        mensagem['To'] = destinatario
        mensagem['Subject'] = 'Seu Link de Acesso à Planilha Filtrada'
        corpo_email = f"Olá! Aqui está o link de acesso à sua planilha filtrada: {link}"
        mensagem.attach(MIMEText(corpo_email, 'plain'))

        raw_message = base64.urlsafe_b64encode(mensagem.as_bytes()).decode()
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print(f'✅ E-mail enviado para: {destinatario}')
    except HttpError as error:
        print(f'❌ Erro ao enviar e-mail para {destinatario}: {error}')

def upload_para_drive(credentials, arquivo_local, nome_arquivo):
    try:
        service = build('drive', 'v3', credentials=credentials)
        file_metadata = {'name': nome_arquivo}
        media = MediaFileUpload(arquivo_local, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        file_id = file.get('id')
        service.permissions().create(
            fileId=file_id,
            body={'role': 'reader', 'type': 'anyone'}
        ).execute()
        link = f'https://drive.google.com/file/d/{file_id}/view?usp=sharing'
        return link
    except HttpError as error:
        print(f'Erro ao fazer upload para o Google Drive: {error}')
        return None

def main():
    creds = obter_credenciais()

    nome_arquivo = input("Digite o nome do arquivo Excel (ex: base.xlsx): ")
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    planilha = pd.read_excel(nome_arquivo, engine='openpyxl')

    colunas_disponiveis = list(planilha.columns)
    print(f"\nColunas disponíveis: {', '.join(colunas_disponiveis)}")
    colunas_para_filtrar = input("Digite os nomes das colunas que deseja filtrar (separadas por vírgula): ").split(',')

    colunas_para_filtrar = [col.strip() for col in colunas_para_filtrar]

    if not all(col in colunas_disponiveis for col in colunas_para_filtrar):
        print("Uma ou mais colunas não existem na planilha.")
        return

    coluna_emails = input("Digite o nome da coluna que contém os e-mails dos destinatários: ").strip()
    if coluna_emails not in planilha.columns:
        print("Coluna de e-mails inválida.")
        return

    valores_unicos = planilha[colunas_para_filtrar].drop_duplicates()

    for _, valores in valores_unicos.iterrows():
        filtro = (planilha[colunas_para_filtrar] == valores.values).all(axis=1)
        df_filtrado = planilha[filtro]

        email = df_filtrado[coluna_emails].iloc[0]
        nome_arquivo_filtrado = f"planilha_filtrada_{'_'.join(str(v) for v in valores.values)}.xlsx"
        df_filtrado.to_excel(nome_arquivo_filtrado, index=False)

        link = upload_para_drive(creds, nome_arquivo_filtrado, nome_arquivo_filtrado)
        if link:
            enviar_email(creds, email, link)

if __name__ == '__main__':
    main()
