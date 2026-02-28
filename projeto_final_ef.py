# ==========================================================
# A DIVERSIDADE E VARIEDADE DAS ATIVIDADES FÍSICAS
# ==========================================================

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Recomendação Personalizada de Atividade Física", layout="wide")

# ==========================================================
# FUNÇÕES
# ==========================================================

def calcular_imc(peso, altura):
    imc = peso / ((altura/100) ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Excesso de peso"
    else:
        categoria = "Obesidade"
    return imc, categoria


def classificar_perfil(energia, competitividade, social, bem_estar):
    if competitividade >= 7:
        return "Competitivo"
    elif social >= 7:
        return "Social"
    elif bem_estar >= 7:
        return "Wellness"
    elif energia >= 8:
        return "Aventura"
    else:
        return "Equilibrado"


def gerar_recomendacao(perfil, imc_categoria, tecnologia):
    if perfil == "Competitivo":
        principal = "Futebol federado ou Atletismo"
        alternativa = "Basquetebol ou Natação competitiva"
        tipo = "Formal"

    elif perfil == "Social":
        principal = "Dança ou Aulas de Grupo"
        alternativa = "Desporto Escolar ou Trail em grupo"
        tipo = "Não Formal"

    elif perfil == "Wellness":
        principal = "Yoga ou Pilates"
        alternativa = "Hidroginástica ou Caminhada orientada"
        tipo = "Não Formal"

    elif perfil == "Aventura":
        principal = "Escalada ou Surf"
        alternativa = "Trail Running ou BTT"
        tipo = "Informal"

    else:
        principal = "Treino Funcional"
        alternativa = "Ginásio ou Caminhada Regular"
        tipo = "Não Formal"

    if imc_categoria in ["Excesso de peso", "Obesidade"]:
        principal = "Caminhada progressiva ou Hidroginástica"
        alternativa = "Treino de baixo impacto"
        tipo = "Informal"

    if tecnologia:
        alternativa += " com apoio de aplicações móveis ou smartwatch"

    return principal, alternativa, tipo


def gerar_justificacao(nome, perfil, energia, dias, bem_estar, competitividade, social):
    texto = f"{nome}, com base nas tuas respostas, identificaste-te como uma pessoa "

    if perfil == "Competitivo":
        texto += "competitiva, o que indica que procuras desafios e superação pessoal. "
    elif perfil == "Social":
        texto += "social, valorizando o convívio e a interação em grupo. "
    elif perfil == "Wellness":
        texto += "focada no bem-estar e equilíbrio corpo-mente. "
    elif perfil == "Aventura":
        texto += "aventureira, procurando experiências intensas e contacto com a natureza. "
    else:
        texto += "equilibrada, com interesses variados na prática física. "

    texto += f"Apresentas um nível de energia de {energia}/10 e tens disponibilidade para {dias} dias por semana. "

    if dias >= 4:
        texto += "Esta disponibilidade permite uma prática estruturada e regular. "
    else:
        texto += "Uma prática flexível adapta-se melhor à tua rotina. "

    if bem_estar >= 7:
        texto += "Demonstras também grande interesse no bem-estar, o que reforça a importância de atividades equilibradas. "

    if competitividade >= 7:
        texto += "O teu espírito competitivo favorece modalidades com objetivos claros e progressão de desempenho. "

    if social >= 7:
        texto += "O gosto por atividades em grupo aumenta a motivação e a adesão à prática. "

    texto += "Assim, a recomendação apresentada ajusta-se ao teu perfil psicológico, físico e social, promovendo motivação, inclusão e benefícios para a saúde."

    return texto


# ==========================================================
# INTERFACE
# ==========================================================

st.title("Recomendação Personalizada de Atividade Física")

col1, col2 = st.columns(2)

with col1:
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", 10, 100, 17)
    altura = st.number_input("Altura (cm)", 120, 220, 170)
    peso = st.number_input("Peso (kg)", 30, 200, 70)

with col2:
    energia = st.slider("Nível de energia", 1, 10, 5)
    competitividade = st.slider("Grau de competitividade", 1, 10, 5)
    social = st.slider("Gosto por atividades em grupo", 1, 10, 5)
    bem_estar = st.slider("Procura de bem-estar/relaxamento", 1, 10, 5)
    dias = st.slider("Dias disponíveis por semana", 1, 7, 3)
    tecnologia = st.checkbox("Utilizas aplicações ou smartwatch?")

# ==========================================================
# RESULTADOS
# ==========================================================

if st.button("Gerar Recomendação Personalizada"):

    imc, categoria_imc = calcular_imc(peso, altura)
    perfil = classificar_perfil(energia, competitividade, social, bem_estar)
    principal, alternativa, tipo = gerar_recomendacao(perfil, categoria_imc, tecnologia)
    justificacao = gerar_justificacao(nome, perfil, energia, dias, bem_estar, competitividade, social)

    st.subheader("Resultados")

    st.write(f"IMC: {imc:.1f} ({categoria_imc})")
    st.write(f"Perfil identificado: {perfil}")
    st.write(f"Tipo de prática recomendada: {tipo}")

    st.success(f"Atividade principal recomendada: {principal}")
    st.info(f"Alternativa recomendada: {alternativa}")

    # 🔥 NOVO – Panorama completo de diversidade
    st.subheader("Outras possibilidades dentro da diversidade de atividades físicas")

    st.write("**Desportos Coletivos:** Futebol, Basquetebol, Andebol, Voleibol")
    st.write("**Atividades de Ginásio:** Musculação, Treino Funcional, Crossfit")
    st.write("**Atividades Informais:** Caminhada, Corrida, Bicicleta")
    st.write("**Atividades de Wellness:** Yoga, Pilates, Alongamentos")
    st.write("**Atividades de Aventura:** Escalada, Surf, Skate, Trail Running")

    # 🔥 Justificação personalizada
    st.subheader("Justificação Personalizada")
    st.write(justificacao)

    # Gráfico
    categorias = ["Formal", "Não Formal", "Informal"]
    valores = [0, 0, 0]

    if tipo == "Formal":
        valores = [60, 25, 15]
    elif tipo == "Não Formal":
        valores = [20, 60, 20]
    else:
        valores = [15, 25, 60]

    fig, ax = plt.subplots()
    ax.pie(valores, labels=categorias, autopct='%1.1f%%')
    ax.set_title("Compatibilidade por Tipo de Prática")
    st.pyplot(fig)

    st.subheader("Justificação Científica")

    st.write("""
    A recomendação baseia-se na diversidade das atividades físicas existentes na sociedade contemporânea,
    considerando fatores físicos, psicológicos, sociais e tecnológicos.

    A prática regular contribui para:
    - Melhoria da condição cardiorrespiratória
    - Redução do stress e ansiedade
    - Promoção da integração social
    - Aumento da motivação e autoestima

    Este modelo demonstra como a personalização pode aumentar a adesão à atividade física,
    respondendo às necessidades individuais de cada pessoa.
    """)
