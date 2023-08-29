import streamlit as st
from auxFunctions import *

TITLE = "OCEV - Computação Evolutiva - Trabalho 2023/2"
SELECTED_PROBLEM = ""
INDIVIDUAL_TYPE = ""
DIMENSION = 0
POPULATION_SIZE = 0

def setProblemDescription(p):
    if p == "N-Queens":
        with open('Problems/N-Queens.txt', 'r') as pDesc:
            return  pDesc.read() 
    if p == "Fábrica de Rádios":
        with open('Problems/Radios.txt', 'r') as pDesc:
            return  pDesc.read() 
    return ""

if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.header(TITLE, divider="rainbow")
    
    configCol, descCol = st.columns(2)
    with configCol:
        st.header("Configuração do Problema", divider =True)
        #Select Problem
        problemsList=["Fábrica de Rádios","N-Queens",]
        SELECTED_PROBLEM = st.selectbox("Selecione o Problema para Atacar:", problemsList)
        #Select Individual Type
        individualsTypeList=["Inteiro", "Inteiro Permutado", "Binário", "Real"]
        INDIVIDUAL_TYPE = st.selectbox("Selecione a Codificação (Tipo) dos Indivíduos:", individualsTypeList)
        #Select Individual DIMENSION
        DIMENSION = st.slider("Selecione a Dimensão dos Indivíduos:")
        #Select Population Size
        POPULATION_SIZE = st.slider("Selecione o Tamanho da População Inicial:")
        #Executa
        executeAttack = st.button("ATTACK!", use_container_width=True)
    with descCol:
        st.header("Descrição do Problema", divider =True)
        st.text(setProblemDescription(SELECTED_PROBLEM))

    if executeAttack:
        createdPopulation = attackButton(INDIVIDUAL_TYPE, POPULATION_SIZE, DIMENSION, SELECTED_PROBLEM)
        col1, col2 = st.columns(2)
        with col1:
            st.header("População", divider=True)
            for idx, individual in enumerate(createdPopulation):
                st.write(f"Individual {idx+1}: {individual}")
                
        with col2:
            st.header("Score", divider=True)
            for idx, individual in enumerate(createdPopulation):
                st.write(f"Individual {idx+1}: {individual.score}")
   

