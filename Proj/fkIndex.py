import streamlit as st
from main import *

TITLE = "OCEV - Computação Evolutiva - Trabalho 2023/2"

if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.header(TITLE, divider='rainbow')
   
    #Select Problem
    problemsList=["Nenhum","N-Queens",]
    selectedProblem = st.selectbox("Selecione o Problema para Atacar:", problemsList)
    print(selectedProblem)

    #Select Individual Type
    individualsTypeList=["Inteiro", "Inteiro Permutado", "Binário", "Real"]
    individualType = st.selectbox("Selecione a Codificação (Tipo) dos Indivíduos:", individualsTypeList)
    print(individualType)

    #Select Individual Dimension
    dimension = st.slider("Selecione a Dimensão dos Indivíduos:")
    print(dimension)

    #Select Population Size
    populationSize = st.slider("Selecione o Tamanho da População Inicial:")
    print(populationSize)
    
    #Executa
    execute = st.button("ATTACK!", use_container_width=True)

    #individual_type, dimension, population_size, selectedProblem = ler_arquivo_json()
    #createdPopulation = create_pop(individual_type, population_size, dimension)
    #createdPopulation = apply_problem(createdPopulation, problem)
    #printPopulation(createdPopulation)



