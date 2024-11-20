import streamlit as st
import urllib3
from urllib3 import request

# Definir usuários e senhas
USUARIOS = {
    "VINI": "VINI321",
    "WILL": "WILL321"
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
def Botao_Colorido(rotulo, cor = "#7e7b7b"):
    Botao_Colorido.cor = cor
    st.markdown("""<style>  .element-container:has(style){display: none;} #button-after {display: none;}
                            .element-container:has(#button-after) {display: none;}
                            .element-container:has(#button-after) + div button {background-color: %s;font-weight: bolder; color:black;}
                </style>"""%(Botao_Colorido.cor), unsafe_allow_html=True)
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    respBTNColor = st.button(rotulo)
    return respBTNColor
    
# Função principal
def app():
    if "usuario" not in st.session_state:
        fazer_login()
    else:
        st.title(f"Batedor de Ponto Eletrônico - {st.session_state.usuario}")

        # Opção para registrar o ponto
        if st.button("Registrar Ponto ENTRADA"):
            http = urllib3.PoolManager()
            link = "https://docs.google.com/forms/d/e/1FAIpQLScjfglFk9DS7OSntG9ORwPB6EqLWYRUq6SbEyRNBBbFAceFNg/formResponse?&submit=Submit?usp=pp_url&entry.1959026244={usuario}&entry.1020301816=ES" 
            r = http.request('GET', link)
            r.status
            st.write(r.status)
            
        # Opção para registrar o ponto
        if st.button("Registrar Ponto SAIDA"):
            http = urllib3.PoolManager()
            link = "https://docs.google.com/forms/d/e/1FAIpQLScjfglFk9DS7OSntG9ORwPB6EqLWYRUq6SbEyRNBBbFAceFNg/formResponse?&submit=Submit?usp=pp_url&entry.1959026244={usuario}&entry.1020301816=ES" 
            r = http.request('GET', link)
            r.status
            st.write(r.status)
                

# Executar o app
if __name__ == "__main__":
    app()
