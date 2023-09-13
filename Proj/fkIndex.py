from evoAlg import EvolutiveAlgorithm
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from streamlit_plotly_events import plotly_events
import numpy as np



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
EXECS = 1
ALG_EXECS_HIST = []

def plottingGraphs(averageFitness):
    trace = go.Scatter(x=list(range(len(averageFitness))),  # Índices
                    y=averageFitness,  # Valores
                    mode='markers+lines',  # Define o estilo do gráfico
                    marker=dict(size=10))  # Define o tamanho dos marcadores

    data = [trace]  # Coloca o trace em uma lista de dados

    # Layout do gráfico
    layout = go.Layout(title='Gráfico de Convergência',
                   xaxis=dict(title='Geração'),
                   yaxis=dict(title='Fitness do melhor indivíduo'))

    # Cria a figura
    fig = go.Figure(data=data, layout=layout)

    # Exibe o gráfico
    return fig



if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.header(TITLE)
    
    st.header("Configuração do Problema")
    #Select Problem
    problemsList=["Fábrica de Rádios","N-Queens",]
    SELECTED_PROBLEM = st.selectbox("Selecione o Problema para Atacar:", problemsList)

    EXECS = st.slider("Selecione a Quantidade de Exexuções", min_value=1)

    if SELECTED_PROBLEM == "N-Queens":
        #Select Individual Type
        individualsTypeList=["Inteiro Permutado"]
        INDIVIDUAL_TYPE = st.selectbox("Selecione a Codificação (Tipo) dos Indivíduos:", individualsTypeList)
        #Tipo de Seleção
        selectionList=["Torneio","Roleta",]
        SELECTION_TYPE = st.selectbox("Selecione o Tipo de Seleção", selectionList)
        #Tipo Crossover
        crossoverList=["PMX"]
        CROSSOVER_TYPE = st.selectbox("Selecione o Tipo de Crossover", crossoverList)
        #Mutation 
        mutationList=["SWAP"]
        MUTATION_TYPE = st.selectbox("Selecione o Tipo de Mutação", mutationList)
        #Elitista
        ELITISMO = st.checkbox("Elitismo?", value=True)
        #Select Individual DIMENSION
        DIMENSION = st.slider("Selecione a Dimensão dos Indivíduos:")
        #Select Population Size
        POPULATION_SIZE = st.slider("Selecione o Tamanho da População Inicial:")
        #Select Gerações
        QTD_GENERATIONS = st.slider("Selecione a Quantidade de Gerações")
        #Executa
    elif SELECTED_PROBLEM == "Fábrica de Rádios":
        #Select Individual Type
        individualsTypeList=["Binário"]
        INDIVIDUAL_TYPE = st.selectbox("Selecione a Codificação (Tipo) dos Indivíduos:", individualsTypeList)
        #Tipo de Seleção
        selectionList=["Torneio","Roleta",]
        SELECTION_TYPE = st.selectbox("Selecione o Tipo de Seleção", selectionList)
        #Tipo Crossover
        crossoverList=["1 Ponto","2 Pontos","Unif"]
        CROSSOVER_TYPE = st.selectbox("Selecione o Tipo de Crossover", crossoverList)
        #Mutation 
        mutationList=["BIT-FLIP"]
        MUTATION_TYPE = st.selectbox("Selecione o Tipo de Crossover", mutationList)
        #Elitista
        ELITISMO = st.checkbox("Elitismo?", value=True)
        #Select Individual DIMENSION
        DIMENSION = st.slider("Selecione a Dimensão dos Indivíduos:")
        #Select Population Size
        POPULATION_SIZE = st.slider("Selecione o Tamanho da População Inicial:")
        #Select Gerações
        QTD_GENERATIONS = st.slider("Selecione a Quantidade de Gerações")
        #Executa

    executeAttack = st.button("ATTACK!", use_container_width=True)
 
    if executeAttack:
        tabs = st.tabs([f'Exec {i}' for i in range(1, EXECS + 1)])
        for i in range(EXECS):
            algorithm = EvolutiveAlgorithm(SELECTED_PROBLEM, POPULATION_SIZE, DIMENSION, INDIVIDUAL_TYPE, QTD_GENERATIONS, SELECTION_TYPE, CROSSOVER_TYPE,MUTATION_TYPE, CROSSOVER, MUTATION, ELITISMO)
            algorithm.apply_problem()
            averageFitness , bestIndividuals,  bestIndividualsFit = algorithm.evolutive_loop()
            ALG_EXECS_HIST.append(algorithm)
            #print(algorithm.generalBest.cromossome)
        
            with tabs[i]:
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
                plotly_events(plottingGraphs(bestIndividualsFit))

        with st.expander("Estatísticas Gerais"):
            #Média e desvio padrão do valor da função objetivo do melhor indivíduo de cada execução
            st.header("Melhores indivíduos de cada execução")
            for i in ALG_EXECS_HIST:
                st.write(str(i.generalBest.cromossome))
                st.write(i.generalBest.score)
            #Valores das variáveis da melhor solução encontrada dentre todas as execuções
            
            #Valor da Func Objetivo da melhor solução



            

