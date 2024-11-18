import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import datetime

# Definir usuários e senhas
USUARIOS = {
    "usuario1": "msm",
    "usuario2": "isso"
}

# Função para autenticar no Google Sheets
def autenticar_google_sheets():
    try:
        # Definir o escopo e carregar as credenciais
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file("chave.json", scopes=scope)
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
            return  # Se falhar na autenticação, não continue
        
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
