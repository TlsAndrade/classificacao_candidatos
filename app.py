import streamlit as st
import pandas as pd
from fpdf import FPDF

# Lista completa de 28 candidatos com nome, matrícula, semestre
candidatos = [
    {"Nome": "Alexandre Amorim Pivetta", "Matrícula": "2022010619", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "Artur Ribeiro de Barcellos", "Matrícula": "2022020326", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Brenda Garcia Xavier", "Matrícula": "2022020301", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Cirano Gautier dos Santos", "Matrícula": "2017012023", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "Crissie Del'Olmo Soares Barbieri", "Matrícula": "2021020325", "Nota": '', "Ausente": False, "Semestre": 7},
    {"Nome": "Daniel Muraro", "Matrícula": "2022010630", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "Edgar Franchesco Fraga de Souza", "Matrícula": "2022010242", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "Eduardo Ferreira Stormovski", "Matrícula": "2023010008", "Nota": '', "Ausente": False, "Semestre": 4},
    {"Nome": "Gabriel Bertoncello", "Matrícula": "2021020656", "Nota": '', "Ausente": False, "Semestre": 7},
    {"Nome": "Gabriel Marcon Mognon", "Matrícula": "2021010968", "Nota": '', "Ausente": False, "Semestre": 8},
    {"Nome": "Giovan Bagolin Bonini", "Matrícula": "2022020298", "Nota": '', "Ausente": False, "Semestre": 7},
    {"Nome": "Isabel Luisa Rosenbach", "Matrícula": "2022020007", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "Joao Otavio Borges Espindola", "Matrícula": "2022010526", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "João Pedro Pereira Pinto Portella", "Matrícula": "2022020309", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Júlia Dall Agnol", "Matrícula": "2024020412", "Nota": '', "Ausente": False, "Semestre": 4},
    {"Nome": "Liege Dai-Prá Tasqueto", "Matrícula": "2020021248", "Nota": '', "Ausente": False, "Semestre": 9},
    {"Nome": "Lucas Do Amaral Gressler", "Matrícula": "2022020195", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Lucca Henrique Moura da Silva", "Matrícula": "2022010625", "Nota": '', "Ausente": False, "Semestre": 6},
    {"Nome": "Luiz Otavio Wegher Floss", "Matrícula": "2022020316", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Manar Aiman Dib Khaled", "Matrícula": "2024011525", "Nota": '', "Ausente": False, "Semestre": 7},
    {"Nome": "Matheus Henrique Bergenthal Porto", "Matrícula": "2020010914", "Nota": '', "Ausente": False, "Semestre": 4},
    {"Nome": "Nicolás Navarro Stiler", "Matrícula": "2024020360", "Nota": '', "Ausente": False, "Semestre": 4},
    {"Nome": "Pedro Ziegler Dalenogare", "Matrícula": "2023010019", "Nota": '', "Ausente": False, "Semestre": 7},
    {"Nome": "Rafaela Cougo Rios", "Matrícula": "2022020212", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Roberto Carlan de Oliveira", "Matrícula": "2022020313", "Nota": '', "Ausente": False, "Semestre": 5},
    {"Nome": "Tainá Oliveira Squizani", "Matrícula": "2021010527", "Nota": '', "Ausente": False, "Semestre": 7},
    {"Nome": "Taína Toaldo Granez", "Matrícula": "2021020462", "Nota": '', "Ausente": False, "Semestre": 8},
    {"Nome": "Tiago Mann Wastowski", "Matrícula": "2022020377", "Nota": '', "Ausente": False, "Semestre": 5}
]

# Função para gerar PDF
def gerar_pdf(aprovados, suplentes, desqualificados, ausentes, df_sorted):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, 'Classificação Geral', ln=True, align='C')

    # Tabela de Classificação Geral
    pdf.cell(200, 10, 'Classificação Geral de Todos os Candidatos', ln=True, align='L')
    for i, row in df_sorted.iterrows():
        pdf.cell(200, 10, f'{i+1}. {row["Nome"]} - Nota: {row["Nota"]} - Semestre: {row["Semestre"]}', ln=True)

    # Aprovados
    pdf.cell(200, 10, 'Candidatos Aprovados', ln=True, align='L')
    for i, row in aprovados.iterrows():
        pdf.cell(200, 10, f'{row["Classificação"]}. {row["Nome"]} - Nota: {row["Nota"]} - Semestre: {row["Semestre"]}', ln=True)

    # Suplentes
    pdf.cell(200, 10, 'Candidatos Suplentes', ln=True, align='L')
    for i, row in suplentes.iterrows():
        pdf.cell(200, 10, f'{row["Classificação"]}. {row["Nome"]} - Nota: {row["Nota"]} - Semestre: {row["Semestre"]}', ln=True)

    # Desqualificados
    pdf.cell(200, 10, 'Candidatos Desqualificados (Nota < 10)', ln=True, align='L')
    for i, row in desqualificados.iterrows():
        pdf.cell(200, 10, f'{row["Nome"]} - Nota: {row["Nota"]} - Semestre: {row["Semestre"]}', ln=True)

    # Ausentes
    pdf.cell(200, 10, 'Candidatos Ausentes', ln=True, align='L')
    for i, row in ausentes.iterrows():
        pdf.cell(200, 10, f'{row["Nome"]} - Semestre: {row["Semestre"]}', ln=True)

    # Gerar PDF
    pdf_output = '/mnt/data/classificacao_candidatos.pdf'
    pdf.output(pdf_output)
    return pdf_output

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
            # Campo de input vazio para digitar a nota
            df.at[index, 'Nota'] = st.text_input(f'Nota de {row["Nome"]}', value=row['Nota'], key=f'nota_{index}')
        with col3:
            df.at[index, 'Ausente'] = st.checkbox('Ausente?', value=row['Ausente'], key=f'ausente_{index}')

    # Botão para exibir os dados atualizados
    if st.button('Classificar Candidatos'):
        # Marcar nota zero para candidatos ausentes
        df.loc[df['Ausente'] == True, 'Nota'] = 0

        # Garantir que o valor da nota seja convertido para inteiro
        df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce').fillna(0).astype(int)

        # Classificar candidatos em ordem decrescente de notas e em caso de empate, por semestre decrescente
        df_sorted = df.sort_values(by=['Nota', 'Semestre'], ascending=[False, False])

        # Selecionar os 18 primeiros aprovados
        aprovados = df_sorted.head(18).reset_index(drop=True)
        aprovados['Classificação'] = aprovados.index + 1

        # Selecionar os 5 próximos como suplentes
        suplentes = df_sorted.iloc[18:23].reset_index(drop=True)
        suplentes['Classificação'] = suplentes.index + 19

        # Filtrar e exibir candidatos desqualificados (nota abaixo de 10)
        desqualificados = df_sorted[df_sorted['Nota'] < 10]

        # Filtrar e exibir candidatos ausentes
        ausentes = df[df['Ausente'] == True]

        # Exibir os candidatos aprovados, suplentes, desqualificados e ausentes
        st.write("### Candidatos Aprovados:")
        st.dataframe(aprovados[['Classificação', 'Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

        st.write("### Candidatos Suplentes:")
        st.dataframe(suplentes[['Classificação', 'Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

        st.write("### Candidatos Desqualificados (Nota < 10):")
        st.dataframe(desqualificados[['Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

        st.write("### Candidatos Ausentes:")
        st.dataframe(ausentes[['Nome', 'Matrícula', 'Semestre']], use_container_width=True)

        st.write("### Classificação Geral:")
        df_sorted['Classificação'] = df_sorted.index + 1  # Adicionar a classificação geral começando de 1
        st.dataframe(df_sorted[['Classificação', 'Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

        # Botão para gerar PDF e download
        if st.button('Gerar PDF'):
            pdf_file = gerar_pdf(aprovados, suplentes, desqualificados, ausentes, df_sorted)
            st.download_button('Baixar PDF', data=open(pdf_file, 'rb').read(), file_name="classificacao_candidatos.pdf", mime="application/pdf")

# Executar o aplicativo
if __name__ == '__main__':
    exibir_tabela()
