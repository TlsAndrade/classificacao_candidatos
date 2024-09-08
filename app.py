import streamlit as st

# Classe para armazenar informações dos candidatos
class Candidato:
    def __init__(self, matricula, nome, nota):
        self.matricula = matricula
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.matricula} - {self.nome}: {self.nota}"

# Função para classificar e exibir resultados
def classificar_candidatos(candidatos):
    # Desclassificar quem tirou menos de 50% (nota mínima)
    candidatos_classificados = [c for c in candidatos if c.nota >= 50]
    
    # Ordenar em ordem decrescente de nota
    candidatos_classificados.sort(key=lambda x: x.nota, reverse=True)

    aprovados = "Aprovados:\n" + "\n".join([f"{i+1}. {c}" for i, c in enumerate(candidatos_classificados[:18])])
    suplentes = "Suplentes:\n" + "\n".join([f"{i+1}. {c}" for i, c in enumerate(candidatos_classificados[18:23])])
    
    desclassificados = [c for c in candidatos if c.nota < 50]
    desclassificados_txt = "Desclassificados (nota abaixo de 50%):\n" + "\n".join([str(c) for c in desclassificados]) if desclassificados else "Nenhum candidato foi desclassificado."
    
    resultado = aprovados + "\n\n" + suplentes + "\n\n" + desclassificados_txt
    return resultado

# Lista de candidatos
candidatos = []

# Interface Gráfica usando Streamlit
st.title("Sistema de Classificação de Candidatos")

# Entrada de dados
matricula = st.text_input("Matrícula:")
nome = st.text_input("Nome:")
nota = st.number_input("Nota:", min_value=0.0, max_value=100.0, step=0.1)

# Botão para adicionar candidato
if st.button("Adicionar Candidato"):
    if matricula and nome and nota >= 0:
        candidatos.append(Candidato(matricula, nome, nota))
        st.success(f"Candidato {nome} adicionado com sucesso!")
    else:
        st.error("Preencha todos os campos corretamente.")

# Botão para exibir a classificação
if st.button("Exibir Classificação"):
    if candidatos:
        resultado = classificar_candidatos(candidatos)
        st.text_area("Classificação", value=resultado, height=300)
    else:
        st.warning("Nenhum candidato cadastrado ainda.")
