import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import json
import os

# Definir usuários e senhas (em um ambiente real, isso seria mais seguro)
USUARIOS = {
    "usuario1": "issomsm",
    "usuario2": "issomsm"
}

# Função para autenticar no Google Sheets
def autenticar_google_sheets():
    try:
        # Carregar chave JSON diretamente dos secrets
        chave_json = st.secrets["GOOGLE_SHEETS_KEY"]
        chave_dict = json.loads(chave_json)
        
        # Escopo da autenticação
       scope = ["https://www.googleapis.com/auth/spreadsheets"]
        
        # Autenticar usando as credenciais
        creds = ServiceAccountCredentials.from_json_keyfile_dict(chave_dict, scope)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error("Erro ao autenticar com o Google Sheets.")
        st.error(f"Detalhes do erro: {e}")
        return None

def registrar_ponto(nome):
    # Acessa a planilha
    client = autenticar_google_sheets()
    if client is None:
        return  # Se não conseguiu autenticar, não faz o registro

    try:
        # Acessa a planilha específica usando o ID (substitua pelo ID da sua planilha)
        planilha_id = "1eUhbqDqZPuV6lhlm0zCkEPZ_0hZarMneZnGgCicU3X8"  
        sheet = client.open_by_key(planilha_id).sheet1

        # Pega a data e hora atual
        data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

        # Adiciona os dados na planilha
        sheet.append_row([nome, data_atual, hora_atual])
        st.success(f"Ponto registrado com sucesso para {nome}!")
    except Exception as e:
        st.error(f"Erro ao registrar ponto: {e}")

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
            st.success(f"Ponto registrado com sucesso para {st.session_state.usuario}!")

# Executar o app
if __name__ == "__main__":
    app()


