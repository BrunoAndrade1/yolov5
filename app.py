from pathlib import Path
import streamlit as st
from PIL import Image
import base64
import openai
openai.api_key = st.secrets["openai"]["api_key"]
#st.secrets["auth_token"]
# teste no github
#### teste pagians ##############################
######## Github branch bDASSDSA
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

#[data-testid="stHeader"]{
#background-color:rgba(0,0,0,0);
#}

page_bg_img = """
<style>
:root {
  --grad: radial-gradient(at 88% 80%, hsla(200,74%,61%,1) 0px, transparent 50%),
          radial-gradient(at 93% 46%, hsla(200,99%,66%,1) 0px, transparent 50%),
          radial-gradient(at 59% 14%, hsla(200,93%,78%,1) 0px, transparent 50%),
          radial-gradient(at 53% 53%, hsla(200,99%,67%,1) 0px, transparent 50%),
          radial-gradient(at 36% 11%, hsla(200,85%,67%,1) 0px, transparent 50%);
}

[data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stToolbar"] {
  background-color: hsla(200,100%,80%,0.1);
  background-image: var(--grad);
} 
</style>
"""



st. markdown(page_bg_img,unsafe_allow_html=True)
###############################muda #############################
# Configuraçoes Estruturais #
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#arquivo_css = diretorio / 'styles'/'geral.css'
arquivo_pdf = diretorio / 'assets' / 'BrunoAndrade_23.pdf'  # corrected folder name
arquivo_img = diretorio /'assets'/ 'curriculo.jpg'

# onfiguração geral das impormaçoes #

TITULO ='Curriculum | Bruno Andrade'
NOME = 'Bruno Andrade'
DESCRICAO = ''' Data Science , Projetos'''
EMAIL = 'brunoandrade@usp.br'
MIDIA_SOCIAL = {'LinkedIn':"https://www.linkedin.com/in/bruno-andrade-de-luna/",
                "GitHub": "https://github.com/BrunoAndrade1"}

PROJETOS = {"🚀 Projeto X":"Analise",
            '📊Projeto y':'x',
            '📈 Projeto B':'Z'
            }




# carregando asset
# with open(arquivo_css) as c:
#     st.markdown('<style>{}</style>'.format(c.read()),unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_img)

col1, col2 =st.columns(2, gap='small')
with col1:
    st.image(imagem,width=250)

with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label='Download Curriculum',
        data=pdfLeitura,
        file_name= arquivo_pdf.name,
        mime='application/octet-stream'
    )
    st.write('📧',EMAIL)

# Midias  Sociais#
st.write('#')
colunas =st.columns(len(MIDIA_SOCIAL))
for indice,(plataforma,link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].write(f'[{plataforma}]({link})')

st.write("#")
st.write(    
    """
    ## Minhas Experiências Profissionais
    - 💼 **Analista Financeiro**
        - 💰 Realização de pagamentos e controle de fluxo de caixa
        - 🔧 Implementação de processos de melhoria contínua no departamento financeiro
        - 📈 Desenvolvimento e implementação de estratégias de negócios
        - 👥 Gestão de relações com clientes e fornecedores
        
    - 🧠 **Data Scientist:**
        - 🤖 Tenho experiência com modelos de aprendizado de máquina e séries temporais. Minha abordagem é focada na aplicação prática da ciência dos dados para resolver problemas reais.

    - 📊 **Analista de Dados:** 
        - 🐍 Desenvolvo análises usando Python, com foco especial em bibliotecas como Pandas, Numpy, Ploty e Matplotlib. Eu procuro sempre contar uma história com os dados e fornecer insights que podem informar a tomada de decisão.
    
    ## Competências Técnicas
    
    - 💻 **Linguagens de Programação:** Python.
    - 📈 **Bibliotecas de Data Science:** Pandas, Numpy, Scikit-Learn, Ploty, Matplotlib, Seaborn.
    - 🚀 **Big Data Tools:** H2o.ai, Spark.
    - 🛠️ **Outras Ferramentas:** Git, Docker, Jenkins.
    - 📈 **Visualização de Dados**: Proficiência em ferramentas de visualização de dados como Streamlit, Matplotlib e Seaborn.

    ## Projetos Relevantes

    - 🤖 **Projeto de Previsão de Demanda:** Desenvolvi um modelo de aprendizado de máquina para prever a demanda de produtos em um varejista de grande escala. 
   
    ## Formação
    - 🎓  **Tecnólogo em Mecatrônica** 
    - 🎓  **Graduação em Matemática Aplicada Computacional** 
 
    """)
# softskill #

st.write("#")
st.subheader('Certificados')
st.markdown(
    """
       - 📊 **H2O.ai**: [Ver Certificado](https://seu-link-aqui.com)
       - ☁️ **AZURE DP203**: [Ver Certificado](https://seu-link-aqui.com)
    """
)
##############################
# Configuração das credenciais do OpenAI GPT-3
# openai.api_key = "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"


# def chat_with_gpt3(prompt, max_tokens=200):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  #modelo de chat mais recente.
#         messages=[
#             {"role": "system", "content": "Você é um assistente útil que responde a perguntas."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=max_tokens,
#     )
#     return response.choices[0].message['content']
# def caixa_de_dialogo():
#     # CSS personalizado
#     custom_css = """
#     <style>
#         body {
#             background-color: #282C34;  # Substitua com a cor que você deseja
#         }
#         .stTextInput .stTextInput>div>div>input {
#             background-color: #282C34;  # Substitua com a cor que você deseja
#         }
#     </style>
#     """
#     user_input = st.text_area("Digite sua pergunta aqui. Por exemplo: 'Como foram nossas vendas no último trimestre?'", value="", height=100,)
#     if st.button("Enviar"):
#         if user_input:
#             st.write("Você:", user_input)
#             response = chat_with_gpt3(user_input)  # Chamada à função chat_with_gpt3
#             st.write("ChatGPT:", response)

# #$$$$$$$$$$$$$$$


# caixa_de_dialogo()