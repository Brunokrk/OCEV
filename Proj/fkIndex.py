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
FULL_CONVERGENCE_DATA = []

def plottingGraphs(averageFitness):
    """Convergence for one execution"""
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

def dispersion():
    fig = go.Figure()  # Cria uma figura vazia

    num_generations = len(FULL_CONVERGENCE_DATA[0])  # Assume que todas as execuções têm o mesmo número de gerações

    # Calcula a média para cada coluna (geração) separadamente
    column_means = [np.mean([FULL_CONVERGENCE_DATA[i][j] for i in range(len(FULL_CONVERGENCE_DATA))]) for j in range(num_generations)]

    for index, averageFitness in enumerate(FULL_CONVERGENCE_DATA):
        trace = go.Scatter(
            x=list(range(len(averageFitness))),  # Índices
            y=averageFitness,  # Valores
            mode='lines',  # Define o estilo dos pontos como marcadores
            marker=dict(size=5),  # Define o tamanho dos marcadores
            name=f'Execução {index + 1}'  # Define o nome da série
        )
        fig.add_trace(trace)  # Adiciona a série de pontos à figura

    # Adiciona uma linha de média que liga os pontos de média de cada coluna (geração)
    trace_column_means = go.Scatter(
        x=list(range(num_generations)),
        y=column_means,
        mode='lines',  # Define o estilo da linha
        line=dict(color='black', dash='dash'),  # Define a linha vermelha tracejada
        name='Média das Gerações'
    )
    fig.add_trace(trace_column_means)

    # Layout do gráfico
    layout = go.Layout(
        title='Gráfico de Convergência com Média das Colunas',
        xaxis=dict(title='Geração'),
        yaxis=dict(title='Fitness do Melhor Indivíduo')
    )
    
    fig.update_layout(layout)

    # Exibe o gráfico
    fig.show()

    return fig

def boxplot():
    best_scores = []  # Lista para armazenar os melhores scores de cada execução
    for i in range(EXECS):
        algorithm = ALG_EXECS_HIST[i]
        best_score = algorithm.generalBest.score
        best_scores.append(best_score)

    st.header("Plotando Gráficos")
    fig = go.Figure()
    fig.add_trace(go.Box(y=best_scores, name="Geração"))
    fig.update_layout(
        title="Boxplot dos Melhores Scores",
        yaxis=dict(title="Score"),
    )
    return fig

if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.header(TITLE)
    
    st.header("Configuração do Problema")
    #Select Problem
    problemsList=["Fábrica de Rádios","N-Queens", "N-Queens with ScoreBoard"]
    SELECTED_PROBLEM = st.selectbox("Selecione o Problema para Atacar:", problemsList)

    EXECS = st.slider("Selecione a Quantidade de Exexuções", min_value=1)

    if SELECTED_PROBLEM == "N-Queens" or SELECTED_PROBLEM == "N-Queens with ScoreBoard":
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
        DIMENSION = st.slider("Selecione a Dimensão dos Indivíduos:", max_value=128)
        #Select Population Size
        POPULATION_SIZE = st.slider("Selecione o Tamanho da População Inicial:")
        #Select Gerações
        QTD_GENERATIONS = st.slider("Selecione a Quantidade de Gerações",max_value=3500)
        #Executa
    elif SELECTED_PROBLEM == "Fábrica de Rádios":
        print("entrou aqui")
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
        DIMENSION = st.slider("Selecione a Dimensão dos Indivíduos:", max_value=128)
        #Select Population Size
        POPULATION_SIZE = st.slider("Selecione o Tamanho da População Inicial:")
        #Select Gerações
        QTD_GENERATIONS = st.slider("Selecione a Quantidade de Gerações",max_value=3500)
        #Executa

    executeAttack = st.button("ATTACK!", use_container_width=True)
 
    if executeAttack:
        tabs = st.tabs([f'Exec {i}' for i in range(1, EXECS + 1)])
        for i in range(EXECS):
            algorithm = EvolutiveAlgorithm(SELECTED_PROBLEM, POPULATION_SIZE, DIMENSION, INDIVIDUAL_TYPE, QTD_GENERATIONS, SELECTION_TYPE, CROSSOVER_TYPE,MUTATION_TYPE, CROSSOVER, MUTATION, ELITISMO)
            #algorithm.apply_problem()
            averageFitness , bestIndividuals,  bestIndividualsFit = algorithm.evolutive_loop()
            ALG_EXECS_HIST.append(algorithm)
            FULL_CONVERGENCE_DATA.append(bestIndividualsFit)
            #print(algorithm.generalBest.cromossome)
        
            with tabs[i]:
                col1, col2 = st.columns(2)
                with st.expander("Gráfico Convergência"):
                    with col1:
                        with st.expander("População Última Geração"):
                            st.header("População")
                            for idx, individual in enumerate(algorithm.population):
                                st.write(f"Individual {idx+1}: {individual}")                    
                    with col2:
                        with st.expander("Score Ultima Geração"):
                            st.header("Score Última População")
                            for idx, individual in enumerate(algorithm.population):
                                st.write(f"Individual {idx+1}: {individual.score}")
                    st.header("Plotando Gráficos")
                    #plotly_events(plottingGraphs(bestIndividualsFit))

        with st.expander("Estatísticas Gerais"):
            #Média e desvio padrão do valor da função objetivo do melhor indivíduo de cada execução
            st.plotly_chart(boxplot(), use_container_width=True)
            #Valores das variáveis da melhor solução encontrada dentre todas as execuções
            #st.divider()
            st.plotly_chart(dispersion(), use_container_width=True)
            st.header("Melhores soluções encontradas")
            for idx, execution in enumerate(ALG_EXECS_HIST):
                st.write(f"Exec {idx+1}: {execution.generalBest.cromossome} -> {execution.generalBest.score} FO: {execution.generalBest.fo}")
            
            



            

