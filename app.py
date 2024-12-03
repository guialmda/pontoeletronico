import streamlit as st
import urllib3

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

# Função para criar botões coloridos
def Botao_Colorido(rotulo, cor="#FFFFFF"):
    st.markdown(f"""
        <style>
            div.stButton > button {{
                background-color: {cor};
                color: black;
                font-weight: bold;
            }}
        </style>
    """, unsafe_allow_html=True)
    return st.button(rotulo)

# Função principal
def app():
    if "usuario" not in st.session_state:
        fazer_login()
    else:
        usuario = st.session_state.usuario
        st.title(f"Batedor de Ponto Eletrônico - {usuario}")

        # Links personalizados para cada usuário
        if usuario == "VINI":
            link_entrada = "https://docs.google.com/forms/d/e/1FAIpQLSeb8wPZbax0WyFKS9IO6Dl4xPdTeiav4uuEUUOtA6GaISdTEA/formResponse?&submit=Submit?usp=pp_url&entry.1189838164=Vinicius&entry.1914771938=Entrada"
            link_saida = "https://docs.google.com/forms/d/e/1FAIpQLSeb8wPZbax0WyFKS9IO6Dl4xPdTeiav4uuEUUOtA6GaISdTEA/formResponse?&submit=Submit?usp=pp_url&entry.1189838164=Vinicius&entry.1914771938=Saida"
            link_arquivo = "https://docs.google.com/spreadsheets/d/1QoGflMc1sOeIE7uCys9CLWrMeB0I1vDe90T8AKnbCy0/edit?usp=sharing"
        elif usuario == "WILL":
            link_entrada = "https://docs.google.com/forms/d/e/1FAIpQLSf2MxkTM-kxsxWeU52OwP2EMZMbGFdrfg3Jwj5N0dbNU6YGlQ/formResponse?&submit=Submit?usp=pp_url&entry.1615807504=Willam&entry.624774481=Entrada"
            link_saida = "https://docs.google.com/forms/d/e/1FAIpQLSf2MxkTM-kxsxWeU52OwP2EMZMbGFdrfg3Jwj5N0dbNU6YGlQ/formResponse?&submit=Submit?usp=pp_url&entry.1615807504=William&entry.624774481=Saida"
            link_arquivo = "https://docs.google.com/spreadsheets/d/1NAIXOo2WSAoByDAkwsf_n2eCrxh-dFV7d-Ev4e68jyg/edit?usp=sharing" 

        # Botões personalizados
        if Botao_Colorido("REGISTRAR ENTRADA", cor="#FFFFFF"):
            http = urllib3.PoolManager()
            r = http.request('GET', link_entrada)
            st.write(f"Status da solicitação: {r.status}")

        if Botao_Colorido("REGISTRAR SAÍDA", cor="#FFFFFF"):
            http = urllib3.PoolManager()
            r = http.request('GET', link_saida)
            st.write(f"Status da solicitação: {r.status}")

        # Botão "Baixar Folha de Ponto"
        if Botao_Colorido("FOLHA DE PONTO", cor="#4CAF50"):
            # Criar o link para baixar o arquivo
            st.markdown(f'<a href="{link_arquivo}" download> Clique aqui para vizualizar a Folha de Ponto </a>', unsafe_allow_html=True)

# Executar o app
if __name__ == "__main__":
    app()

