import streamlit as st

# Lista de candidatos com nome e matrícula (obtida da tabela anterior)
candidatos = [
    {"Nome": "Alexandre Amorim Pivetta", "Matrícula": "2022010619"},
    {"Nome": "Artur Ribeiro de Barcellos", "Matrícula": "2022020326"},
    {"Nome": "Brenda Garcia Xavier", "Matrícula": "2022020301"},
    {"Nome": "Cirano Gautier dos Santos", "Matrícula": "2017012023"},
    {"Nome": "Crissie Del'Olmo Soares Barbieri", "Matrícula": "2021020325"},
    {"Nome": "Daniel Muraro", "Matrícula": "2022010630"},
    {"Nome": "Edgar Franchesco Fraga de Souza", "Matrícula": "2022010242"},
    {"Nome": "Eduardo Ferreira Stormovski", "Matrícula": "2023010008"},
    {"Nome": "Gabriel Bertoncello", "Matrícula": "2021020656"},
    {"Nome": "Gabriel Marcon Mognon", "Matrícula": "2021010968"},
    {"Nome": "Giovan Bagolin Bonini", "Matrícula": "2022020298"},
    {"Nome": "Isabel Luisa Rosenbach", "Matrícula": "2022020007"},
    {"Nome": "Joao Otavio Borges Espindola", "Matrícula": "2022010526"},
    {"Nome": "Joao Pedro Pereira Pinto Portella", "Matrícula": "2022020309"},
    {"Nome": "Julia Dall Agnol", "Matrícula": "2024020412"},
    {"Nome": "Liege Dai-Prá Tasqueto", "Matrícula": "2020021248"},
    {"Nome": "Lucca Henrique Moura da Silva", "Matrícula": "2022010625"},
    {"Nome": "Luiz Otavio Wegher Floss", "Matrícula": "2022020316"},
    {"Nome": "Manar Aiman Dib Khaled", "Matrícula": "2024011525"},
    {"Nome": "Matheus Henrique Bergenthal Porto", "Matrícula": "2020010914"},
    {"Nome": "Nicolás Navarro Stiler", "Matrícula": "2024020360"},
    {"Nome": "Pedro Ziegler Dalenogare", "Matrícula": "2023010019"},
    {"Nome": "Rafaela Cougo Rios", "Matrícula": "2022020212"},
    {"Nome": "Roberto Carlan de Oliveira", "Matrícula": "2022020313"},
    {"Nome": "Taina Oliveira Squizani", "Matrícula": "2021010527"},
    {"Nome": "Taina Toaldo Granez", "Matrícula": "2021020462"},
    {"Nome": "Tiago Mann Wastowski", "Matrícula": "2022020377"}
]

# Dicionário para armazenar as notas dos candidatos
notas = {candidato['Matrícula']: 0 for candidato in candidatos}

# Função para classificar os candidatos
def classificar_candidatos(candidatos):
    # Filtrar candidatos com pelo menos 10 pontos
    candidatos_classificados = [c for c in candidatos if c['Nota'] >= 10]

    # Ordenar os candidatos classificados por nota (ordem decrescente)
    candidatos_classificados.sort(key=lambda x: x['Nota'], reverse=True)

    # Selecionar os 18 primeiros aprovados
    aprovados = candidatos_classificados[:18]

    # Selecionar os 5 suplentes
    suplentes = candidatos_classificados[18:23]

    return aprovados, suplentes

# Função principal
def main():
    st.set_page_config(page_title="Classificação de Candidatos", layout="wide")

    # Título
    st.title("Classificação de Candidatos")

    # Seleção de candidato
    opcoes_candidatos = [f"{c['Nome']} (Matrícula: {c['Matrícula']})" for c in candidatos]
    candidato_selecionado = st.selectbox("Selecione um candidato para inserir a nota:", opcoes_candidatos)

    # Extrair a matrícula do candidato selecionado
    matricula_selecionada = candidato_selecionado.split("(Matrícula: ")[-1][:-1]

    # Inserir a nota para o candidato selecionado
    nota = st.number_input(f"Insira a nota de {candidato_selecionado}:", min_value=0.0, max_value=20.0, step=0.5)

    # Atualizar a nota do candidato
    notas[matricula_selecionada] = nota

    # Botão para classificar candidatos
    if st.button("Classificar Candidatos"):
        # Atribuir as notas aos candidatos
        for candidato in candidatos:
            candidato['Nota'] = notas[candidato['Matrícula']]

        # Classificar candidatos
        aprovados, suplentes = classificar_candidatos(candidatos)

        # Exibir aprovados
        st.markdown("### Aprovados:")
        for i, candidato in enumerate(aprovados, start=1):
            st.success(f"{i}. {candidato['Nome']} - Matrícula: {candidato['Matrícula']} - Nota: {candidato['Nota']}")

        # Exibir suplentes
        st.markdown("### Suplentes:")
        for i, candidato in enumerate(suplentes, start=1):
            st.info(f"{i}. {candidato['Nome']} - Matrícula: {candidato['Matrícula']} - Nota: {candidato['Nota']}")

# Executar o aplicativo
if __name__ == "__main__":
    main()
