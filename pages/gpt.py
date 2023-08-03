import streamlit as st
import openai
from fuzzywuzzy import process
# lista de perguntas e respostas
faq = {
    "Qual é a sua formação acadêmica?": "Eu tenho um bacharelado em Ciência da Computação e um mestrado em Ciência de Dados.",
    "Quais são seus projetos recentes?": "Recentemente, trabalhei em um projeto de análise de sentimentos usando machine learning.",
    "Quais são suas habilidades técnicas?": "Eu tenho habilidades em Python, R, SQL, TensorFlow, PyTorch e muito mais.",
    "Quais são seus hobbies ou interesses fora do trabalho?": "Eu amo fazer caminhadas, ler e cozinhar.",
    "Como você se mantém atualizado com as novas tendências e tecnologias em ciência de dados?": "Eu leio blogs, assisto a webinars e participo de workshops e conferências.",
    "Quais são suas aspirações de carreira?": "Eu espero se tornar um líder de equipe de ciência de dados em uma empresa de tecnologia inovadora.",
    "Quais são as conquistas profissionais das quais você mais se orgulha?": "Eu me orgulho de ter liderado um projeto que resultou em uma economia significativa para minha empresa.",
    "Quais são suas áreas de especialização em ciência de dados?": "Eu me especializo em machine learning, processamento de linguagem natural e análise preditiva."
}


def chat_with_gpt3(prompt, max_tokens=200):
        
        best_match, score = process.extractOne(prompt, faq.keys())
        if score > 90:  # você pode ajustar esse limite conforme necessário
            return faq[best_match]
        if prompt in faq:
             return faq[prompt]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  #modelo de chat mais recente.
            messages=[
                {"role": "system", "content": "Posso também respon der outras perguntas"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
        )
        return response.choices[0].message['content']



def caixa_de_dialogo():
    # CSS personalizado
    custom_css = """
    <style>
        body {
            background-color: #282C34;  # Substitua com a cor que você deseja
        }
        .stTextInput .stTextInput>div>div>input {
            background-color: #282C34;  # Substitua com a cor que você deseja
        }
    </style>
    """
    st.markdown("<h4 style='text-align: center; color: black;'>Digite sua pergunta aqui. Quais são suas habilidades técnicas? Também posso responder a outras perguntas de outros assuntos.</h3>", unsafe_allow_html=True)
    user_input = st.text_area("", value="", height=100)
    if st.button("Enviar"):
        if user_input:
            st.write("Você:", user_input)
            response = chat_with_gpt3(user_input)  # Chamada à função chat_with_gpt3
            st.write("ChatGPT:", response)

#$$$$$$$$$$$$$$$


caixa_de_dialogo()
