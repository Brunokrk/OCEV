from evoAlg import EvolutiveAlgorithm
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from streamlit_plotly_events import plotly_events

TITLE = "OCEV - Computação Evolutiva - Trabalho 2023/2"
SELECTED_PROBLEM = ""
INDIVIDUAL_TYPE = ""
DIMENSION = 0
POPULATION_SIZE = 0
SELECTION_TYPE = ""
CROSSOOVER_TYPE = ""
QTD_GENERATIONS = 0
CROSSOVER = 0.90
MUTATION = 0.05
ELITISMO = True

# Se quisermos mostrar melhores indivíduos de cada geração
# Estrutura de dados deve ser estar aqui

def setProblemDescription(p):
    if p == "N-Queens":
        with open('Problems/N-Queens.txt', 'r') as pDesc:
            return  pDesc.read() 
    if p == "Fábrica de Rádios":
        with open('Problems/Radios.txt', 'r') as pDesc:
            return  pDesc.read() 
    return ""

def plottingGraphs(averageFitness):
    trace = go.Scatter(x=list(range(len(averageFitness))),  # Índices
                    y=averageFitness,  # Valores
                    mode='markers+lines',  # Define o estilo do gráfico
                    marker=dict(size=10))  # Define o tamanho dos marcadores

    data = [trace]  # Coloca o trace em uma lista de dados

    # Layout do gráfico
    layout = go.Layout(title='Gráfico de Convergência',
                   xaxis=dict(title='Geração'),
                   yaxis=dict(title='Fitness Médio'))

    # Cria a figura
    fig = go.Figure(data=data, layout=layout)

    # Exibe o gráfico
    selected_points = plotly_events(fig)


if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.header(TITLE)
    
    configCol, descCol = st.columns(2)
    with configCol:
        st.header("Configuração do Problema")
        #Select Problem
        problemsList=["Fábrica de Rádios","N-Queens",]
        SELECTED_PROBLEM = st.selectbox("Selecione o Problema para Atacar:", problemsList)
        #Select Individual Type
        individualsTypeList=["Inteiro", "Inteiro Permutado", "Binário", "Real"]
        INDIVIDUAL_TYPE = st.selectbox("Selecione a Codificação (Tipo) dos Indivíduos:", individualsTypeList)
        #Tipo de Seleção
        selectionList=["Torneio","Roleta",]
        SELECTION_TYPE = st.selectbox("Selecione o Tipo de Seleção", selectionList)
        #Tipo Crossover
        crossoverList=["1 Ponto","2 Pontos","Unif","PMX"]
        CROSSOVER_TYPE = st.selectbox("Selecione o Tipo de Crossover", crossoverList)
        #Mutation 
        mutationList=["SWAP","BIT-FLIP"]
        MUTATION_TYPE = st.selectbox("Selecione o Tipo de MUtação", mutationList)
        #Elitista
        ELITISMO = st.checkbox("Elitismo?", value=True)
        #Select Individual DIMENSION
        DIMENSION = st.slider("Selecione a Dimensão dos Indivíduos:", max_value=128)
        #Select Population Size
        POPULATION_SIZE = st.slider("Selecione o Tamanho da População Inicial:")
        #Select Gerações
        QTD_GENERATIONS = st.slider("Selecione a Quantidade de Gerações")
        #Executa
        executeAttack = st.button("ATTACK!", use_container_width=True)
    with descCol:
        st.header("Descrição do Problema")
        st.text(setProblemDescription(SELECTED_PROBLEM))

    if executeAttack:
        algorithm = EvolutiveAlgorithm(SELECTED_PROBLEM, POPULATION_SIZE, DIMENSION, INDIVIDUAL_TYPE, QTD_GENERATIONS, SELECTION_TYPE, CROSSOVER_TYPE,MUTATION_TYPE, CROSSOVER, MUTATION, ELITISMO)
        algorithm.apply_problem()
        averageFitness , bestIndividuals,  bestIndividualsFit = algorithm.evolutive_loop()
        col1, col2 = st.columns(2)
        with col1:
            st.header("População")
            for idx, individual in enumerate(algorithm.population):
                st.write(f"Individual {idx+1}: {individual}")
                
        with col2:
            st.header("Score Última População")
            for idx, individual in enumerate(algorithm.population):
                st.write(f"Individual {idx+1}: {individual.score}")

        st.divider()
        st.header("Plotando Gráficos")
        plottingGraphs(bestIndividualsFit)
        

