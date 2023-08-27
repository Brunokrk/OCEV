import streamlit as st
from main import *

TITLE = "OCEV - Computação Evolucionária"
SUBTITLE = "Ferramenta Dedicada a aplicações solicitadas na disciplina de Computação Evolucionária da UDESC"
if __name__ == "__main__":
    #Header
    st.set_page_config(TITLE, layout="wide")
    st.divider()
    st.title(TITLE)
    st.subheader(SUBTITLE)
    st.caption("Feito por Bruno Marchi Pires")
    st.divider()
    
    #Select Problem
    problems=["Nenhum","N-Queens",]
    selectedProblem = st.selectbox("Selecione o Problema para Atacar:", problems)
    print(selectedProblem)

    #Select Individual Type

    #Select Individual Dimension

    #Select Population Size

    individual_type, dimension, population_size, problem = ler_arquivo_json()
    createdPopulation = create_pop(individual_type, population_size, dimension)
    createdPopulation = apply_problem(createdPopulation, problem)
    printPopulation(createdPopulation)



