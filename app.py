import streamlit as st
import pandas as pd

# Lista de candidatos com nome e matrícula
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

# Dicionário para armazenar as notas e status de ausência dos candidatos
notas = {candidato['Matrícula']: 0 for candidato in candidatos}
ausentes = {candidato['Matrícula']: False for candidato in candidatos}

# Função para classificar os candidatos
def classificar_candidatos(candidatos):
    # Filtrar candidatos com pelo menos 10 pontos e que não estão ausentes
    candidatos_classificados = [c for c in candidatos if c['Nota'] >= 10 and not ausentes[c['Matrícula']]]
    ausentes_candidatos = [c for c in candidatos if ausentes[c['Matrícula']]]

    # Ordenar os candidatos classificados por nota (ordem decrescente)
    candidatos_classificados.sort(key=lambda x: x['Nota'], reverse=True)

    # Candidatos desclassificados por nota insuficiente
    desclassificados = [c for c in candidatos if c['Nota'] < 10 and not ausentes[c['Matrícula']]]

    return candidatos_classificados, desclassificados, ausentes_candidatos

# Função para gerar DataFrame com notas
def gerar_tabela_parcial(candidatos):
    data = [{"Nome": c['Nome'], "Matrícula": c['Matrícula'], "Nota": notas[c['Matrícula']], "Ausente": ausentes[c['Matrícula']]} for c in candidatos]
    df = pd.DataFrame(data)
    return df

# Função para verificar se todas as notas foram preenchidas
def notas_preenchidas(notas, ausentes):
    return all(nota > 0 or ausentes[matricula] for matricula, nota in notas.items())

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

    # Checkbox para marcar ausência
    ausente = st.checkbox(f"{candidato_selecionado} está ausente?", key=matricula_selecionada)

    # Inserir a nota para o candidato selecionado (somente inteiros)
    if ausente:
        nota = 0  # Se o candidato estiver ausente, a nota é automaticamente 0
    else:
        nota = st.number_input(f"Insira a nota de {candidato_selecionado}:", min_value=0, max_value=20, step=1)

    # Atualizar a nota e o status de ausência do candidato
    if st.button("Salvar Nota"):
        notas[matricula_selecionada] = nota
        ausentes[matricula_selecionada] = ausente
        st.success(f"Nota salva para {candidato_selecionado}!")

        # Mostrar tabela parcial com as notas atuais
        st.markdown("### Tabela Parcial de Notas")
        df_parcial = gerar_tabela_parcial(candidatos)
        st.dataframe(df_parcial)

        # Mostrar classificação parcial
        for candidato in candidatos:
            candidato['Nota'] = notas[candidato['Matrícula']]
        classificados, desclassificados, ausentes_candidatos = classificar_candidatos(candidatos)

        st.markdown("### Classificação Parcial")
        
        st.markdown("#### Candidatos Classificados:")
        if classificados:
            for i, candidato in enumerate(classificados, start=1):
                st.success(f"{i}. {candidato['Nome']} - Matrícula: {candidato['Matrícula']} - Nota: {candidato['Nota']}")
        else:
            st.info("Nenhum candidato classificado até o momento.")

        st.markdown("#### Candidatos Desclassificados:")
        if desclassificados:
            for candidato in desclassificados:
                st.warning(f"{candidato['Nome']} - Matrícula: {candidato['Matrícula']} - Nota: {candidato['Nota']}")
        else:
            st.info("Nenhum candidato desclassificado até o momento.")

        st.markdown("#### Candidatos Ausentes:")
        if ausentes_candidatos:
            for candidato in ausentes_candidatos:
                st.error(f"{candidato['Nome']} - Matrícula: {candidato['Matrícula']}")
        else:
            st.info("Nenhum candidato ausente até o momento.")

    # Botão para classificar candidatos (final)
    if st.button("Classificar Candidatos"):
        # Verificar se todas as notas foram preenchidas
        if notas_preenchidas(notas, ausentes):
            # Atribuir as notas aos candidatos
            for candidato in candidatos:
                candidato['Nota'] = notas[candidato['Matrícula']]

            # Classificar candidatos
            classificados, desclassificados, ausentes_candidatos = classificar_candidatos(candidatos)

            # Exibir classificados
            st.markdown("### Classificação Final")
            st.markdown("#### Candidatos Classificados:")
            if classificados:
                for i, candidato in enumerate(classificados, start=1):
                    st.success(f"{i}. {candidato['Nome']} - Matrícula: {candidato['Matrícula']} - Nota: {candidato['Nota']}")
            else:
                st.info("Nenhum candidato classificado.")

            # Exibir desclassificados
            st.markdown("#### Candidatos Desclassificados:")
            if desclassificados:
                for candidato in desclassificados:
                    st.warning(f"{candidato['Nome']} - Matrícula: {candidato['Matrícula']} - Nota: {candidato['Nota']}")
            else:
                st.info("Nenhum candidato desclassificado até o momento")
