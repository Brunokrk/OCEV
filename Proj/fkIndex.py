import streamlit as st
from main import *
import pandas as pd

TITLE = "OCEV - Computação Evolutiva - Trabalho 2023/2"

if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.header(TITLE, divider='rainbow')
    #Select Problem
    problemsList=["Nenhum","N-Queens",]
    selectedProblem = st.selectbox("Selecione o Problema para Atacar:", problemsList)
    #Select Individual Type
    individualsTypeList=["Inteiro", "Inteiro Permutado", "Binário", "Real"]
    individualType = st.selectbox("Selecione a Codificação (Tipo) dos Indivíduos:", individualsTypeList)
    #Select Individual Dimension
    dimension = st.slider("Selecione a Dimensão dos Indivíduos:")
    #Select Population Size
    populationSize = st.slider("Selecione o Tamanho da População Inicial:")
    #Executa
    executeAttack = st.button("ATTACK!", use_container_width=True)
    if executeAttack:
        createdPopulation = attackButton(individualType, populationSize, dimension, selectedProblem)
        col1, col2 = st.columns(2)
        with col1:
            st.header("População", divider = True)
            for idx, individual in enumerate(createdPopulation):
                st.write(f"Individual {idx+1}: {individual}")
                
        with col2:
            st.header("Score", divider = True)
            for idx, individual in enumerate(createdPopulation):
                st.write(f"Individual {idx+1}: {individual.score}")
        
        
    
    #individual_type, dimension, population_size, selectedProblem = ler_arquivo_json()
    #createdPopulation = create_pop(individual_type, population_size, dimension)
    #createdPopulation = apply_problem(createdPopulation, problem)
    #printPopulation(createdPopulation)



