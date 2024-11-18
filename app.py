import streamlit as st
import gspread
import json
import datetime
from google.oauth2.service_account import Credentials
import os

# Definir usuários e senhas
USUARIOS = {
    "usuario1": "msm",
    "usuario2": "isso"
}

# Função para obter as credenciais do Google Secret Manager
def get_google_credentials():
    try:
        # Acessa o segredo armazenado no GitHub (variável de ambiente)
        google_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON')

        if google_credentials is None:
            raise Exception("Credenciais do Google não encontradas!")

        # Carrega as credenciais a partir do JSON armazenado
        creds_dict = json.loads(google_credentials)
        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        return creds
    except Exception as e:
        st.error(f"Erro ao carregar credenciais do Google Secret Manager: {str(e)}")
        return None

# Função para autenticar no Google Sheets
def autenticar_google_sheets():
    try:
        creds = get_google_credentials()
        if creds is None:
            return None  # Se as credenciais não puderem ser carregadas, não continua
        
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error(f"Erro ao autenticar com o Google Sheets: {str(e)}")
        return None

# Função para registrar o ponto na planilha
def registrar_ponto(nome):
    try:
        # Acessa a planilha
        client = autenticar_google_sheets()
        if client is None:
            return  # Se falhar na autenticação, não continua
        
        sheet = client.open("Ponto Eletrônico").sheet1  # Acessa a primeira aba da planilha
        
        # Pega a data e hora atual
        data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

        # Adiciona os dados na planilha
        sheet.append_row([nome, data_atual, hora_atual])
        st.success(f"Ponto registrado com sucesso para {nome}!")
    
    except gspread.exceptions.SpreadsheetNotFound as e:
        st.error(f"Erro ao encontrar a planilha: {str(e)}")
    except gspread.exceptions.APIError as e:
        st.error(f"Erro na API do Google Sheets: {str(e)}")
    except Exception as e:
        st.error(f"Erro inesperado ao registrar o ponto: {str(e)}")

# Função de login
def fazer_login():
    st.title("Login - Batedor de Ponto Eletrônico")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state.usuario = usuario
            st.success(f"Bem-vindo, {usuario}!")
        else:
            st.error("Usuário ou senha inválidos!")

# Função principal
def app():
    if "usuario" not in st.session_state:
        fazer_login()
    else:
        st.title(f"Batedor de Ponto Eletrônico - {st.session_state.usuario}")
        
        # Opção para registrar o ponto
        if st.button("Registrar Ponto"):
            registrar_ponto(st.session_state.usuario)

# Executar o app
if __name__ == "__main__":
    app()
