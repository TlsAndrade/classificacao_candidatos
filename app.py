import streamlit as st
import pandas as pd

# Lista de 28 candidatos com nome, matrícula, nota e se estão ausentes
candidatos = [
    {"Nome": "Alexandre Amorim Pivetta", "Matrícula": "2022010619", "Nota": 0, "Ausente": False},
    {"Nome": "Artur Ribeiro de Barcellos", "Matrícula": "2022020326", "Nota": 0, "Ausente": False},
    {"Nome": "Brenda Garcia Xavier", "Matrícula": "2022020301", "Nota": 0, "Ausente": False},
    {"Nome": "Cirano Gautier dos Santos", "Matrícula": "2017012023", "Nota": 0, "Ausente": False},
    {"Nome": "Crissie Del'Olmo Soares Barbieri", "Matrícula": "2021020325", "Nota": 0, "Ausente": False},
    {"Nome": "Daniel Muraro", "Matrícula": "2022010630", "Nota": 0, "Ausente": False},
    {"Nome": "Edgar Franchesco Fraga de Souza", "Matrícula": "2022010242", "Nota": 0, "Ausente": False},
    {"Nome": "Eduardo Ferreira Stormovski", "Matrícula": "2023010008", "Nota": 0, "Ausente": False},
    {"Nome": "Gabriel Bertoncello", "Matrícula": "2021020656", "Nota": 0, "Ausente": False},
    {"Nome": "Gabriel Marcon Mognon", "Matrícula": "2021010968", "Nota": 0, "Ausente": False},
    {"Nome": "Giovan Bagolin Bonini", "Matrícula": "2022020298", "Nota": 0, "Ausente": False},
    {"Nome": "Isabel Luisa Rosenbach", "Matrícula": "2022020007", "Nota": 0, "Ausente": False},
    {"Nome": "Joao Otavio Borges Espindola", "Matrícula": "2022010526", "Nota": 0, "Ausente": False},
    {"Nome": "Joao Pedro Pereira Pinto Portella", "Matrícula": "2022020309", "Nota": 0, "Ausente": False},
    {"Nome": "Julia Dall Agnol", "Matrícula": "2024020412", "Nota": 0, "Ausente": False},
    {"Nome": "Liege Dai-Prá Tasqueto", "Matrícula": "2020021248", "Nota": 0, "Ausente": False},
    {"Nome": "Lucca Henrique Moura da Silva", "Matrícula": "2022010625", "Nota": 0, "Ausente": False},
    {"Nome": "Luiz Otavio Wegher Floss", "Matrícula": "2022020316", "Nota": 0, "Ausente": False},
    {"Nome": "Manar Aiman Dib Khaled", "Matrícula": "2024011525", "Nota": 0, "Ausente": False},
    {"Nome": "Matheus Henrique Bergenthal Porto", "Matrícula": "2020010914", "Nota": 0, "Ausente": False},
    {"Nome": "Nicolás Navarro Stiler", "Matrícula": "2024020360", "Nota": 0, "Ausente": False},
    {"Nome": "Pedro Ziegler Dalenogare", "Matrícula": "2023010019", "Nota": 0, "Ausente": False},
    {"Nome": "Rafaela Cougo Rios", "Matrícula": "2022020212", "Nota": 0, "Ausente": False},
    {"Nome": "Roberto Carlan de Oliveira", "Matrícula": "2022020313", "Nota": 0, "Ausente": False},
    {"Nome": "Taina Oliveira Squizani", "Matrícula": "2021010527", "Nota": 0, "Ausente": False},
    {"Nome": "Taina Toaldo Granez", "Matrícula": "2021020462", "Nota": 0, "Ausente": False},
    {"Nome": "Tiago Mann Wastowski", "Matrícula": "2022020377", "Nota": 0, "Ausente": False},
    {"Nome": "Matheus Augusto Schuch", "Matrícula": "2023020194", "Nota": 0, "Ausente": False}
]

# Criar DataFrame
df = pd.DataFrame(candidatos)

# Função para exibir o aplicativo
def exibir_tabela():
    st.title('Classificação de Candidatos')

    # Criar colunas para edição de nota e checkbox de "Ausente"
    for index, row in df.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(row['Nome'])
        with col2:
            df.at[index, 'Nota'] = st.number_input(f'Nota de {row["Nome"]}', min_value=0, max_value=20, value=row['Nota'], key=f'nota_{index}')
        with col3:
            df.at[index, 'Ausente'] = st.checkbox('Ausente?', value=row['Ausente'], key=f'ausente_{index}')

    # Botão para exibir os dados atualizados
    if st.button('Classificar Candidatos'):
        # Marcar nota zero para candidatos ausentes
        df.loc[df['Ausente'] == True, 'Nota'] = 0

        # Classificar candidatos em ordem decrescente
        df_sorted = df.sort_values(by='Nota', ascending=False)

        # Selecionar os 18 primeiros aprovados
        aprovados = df_sorted.head(18)

        # Selecionar os 5 próximos como suplentes
        suplentes = df_sorted.iloc[18:23]

        # Exibir os candidatos aprovados e suplentes
        st.write("### Candidatos Aprovados:")
        st.dataframe(aprovados[['Nome', 'Matrícula', 'Nota']])

        st.write("### Candidatos Suplentes:")
        st.dataframe(suplentes[['Nome', 'Matrícula', 'Nota']])

# Executar o aplicativo
if __name__ == '__main__':
    exibir_tabela()
