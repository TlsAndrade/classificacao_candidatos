import streamlit as st
import pandas as pd

# Lista de 28 candidatos com nome, matrícula, nota, se estão ausentes e semestre
candidatos = [
    {"Nome": "Alexandre Amorim Pivetta", "Matrícula": "2022010619", "Nota": 0, "Ausente": False, "Semestre": 6},
    {"Nome": "Artur Ribeiro de Barcellos", "Matrícula": "2022020326", "Nota": 0, "Ausente": False, "Semestre": 5},
    {"Nome": "Brenda Garcia Xavier", "Matrícula": "2022020301", "Nota": 0, "Ausente": False, "Semestre": 5},
    {"Nome": "Cirano Gautier dos Santos", "Matrícula": "2017012023", "Nota": 0, "Ausente": False, "Semestre": 6},
    {"Nome": "Crissie Del'Olmo Soares Barbieri", "Matrícula": "2021020325", "Nota": 0, "Ausente": False, "Semestre": 7},
    {"Nome": "Daniel Muraro", "Matrícula": "2022010630", "Nota": 0, "Ausente": False, "Semestre": 6},
    {"Nome": "Edgar Franchesco Fraga de Souza", "Matrícula": "2022010242", "Nota": 0, "Ausente": False, "Semestre": 6},
    {"Nome": "Eduardo Ferreira Stormovski", "Matrícula": "2023010008", "Nota": 0, "Ausente": False, "Semestre": 4},
    # Adicione os outros candidatos conforme necessário...
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

        # Classificar candidatos em ordem decrescente de notas e em caso de empate, por semestre decrescente
        df_sorted = df.sort_values(by=['Nota', 'Semestre'], ascending=[False, False])

        # Selecionar os 18 primeiros aprovados
        aprovados = df_sorted.head(18)

        # Selecionar os 5 próximos como suplentes
        suplentes = df_sorted.iloc[18:23]

        # Exibir os candidatos aprovados e suplentes
        st.write("### Candidatos Aprovados:")
        st.dataframe(aprovados[['Nome', 'Matrícula', 'Nota', 'Semestre']])

        st.write("### Candidatos Suplentes:")
        st.dataframe(suplentes[['Nome', 'Matrícula', 'Nota', 'Semestre']])

        # Filtrar e exibir candidatos ausentes
        ausentes = df[df['Ausente'] == True]
        st.write("### Candidatos Ausentes:")
        st.dataframe(ausentes[['Nome', 'Matrícula', 'Semestre']])

# Executar o aplicativo
if __name__ == '__main__':
    exibir_tabela()
