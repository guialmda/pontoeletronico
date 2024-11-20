import streamlit as st
import os

# Definir usuários e senhas
USUARIOS = {
    "usuario1": "msm",
    "usuario2": "isso"
}

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
