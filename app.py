import streamlit as st
import pandas as pd
from fpdf import FPDF
import os

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

# Criar DataFrame com os dados dos candidatos
df = pd.DataFrame(candidatos)

# Função para gerar o PDF com largura ajustada para o nome e matrícula
def gerar_pdf(aprovados, suplentes, desqualificados, ausentes, df_sorted):
    pdf = FPDF()
    pdf.add_page()

    # Definir o tamanho da fonte
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(200, 10, 'Classificação de Candidatos', ln=True, align='C')

    # Função auxiliar para desenhar uma tabela no PDF
    def desenhar_tabela(pdf, header, data):
        pdf.set_font('Arial', 'B', 8)

        # Cabeçalhos da tabela (centralizados)
        for col in header:
            if col == 'Nome':
                pdf.cell(100, 10, col, 1, 0, 'C')  # Aumentar bastante a largura da célula do Nome
            elif col == 'Matrícula':
                pdf.cell(30, 10, col, 1, 0, 'C')  # Diminuir bastante a largura da célula da Matrícula
            else:
                pdf.cell(35, 10, col, 1, 0, 'C')  # Outras colunas com tamanho padrão
        pdf.ln()

        # Linhas da tabela (centralizadas)
        pdf.set_font('Arial', '', 8)
        for row in data:
            for i, item in enumerate(row):
                if i == 1:  # Nome - célula com largura maior
                    pdf.cell(100, 10, str(item), 1, 0, 'C')
                elif i == 2:  # Matrícula - célula com largura menor
                    pdf.cell(30, 10, str(item), 1, 0, 'C')
                else:
                    pdf.cell(35, 10, str(item), 1, 0, 'C')
            pdf.ln()

    # Cabeçalhos da tabela
    header = ['Classificação', 'Nome', 'Matrícula', 'Nota', 'Semestre']

    # Tabela de Candidatos Aprovados
    if not aprovados.empty:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, 'Candidatos Aprovados', ln=True, align='L')
        data = aprovados[['Classificacao', 'Nome', 'Matrícula', 'Nota', 'Semestre']].values.tolist()
        desenhar_tabela(pdf, header, data)

    # Tabela de Candidatos Suplentes
    if not suplentes.empty:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, 'Candidatos Suplentes', ln=True, align='L')
        data = suplentes[['Classificacao', 'Nome', 'Matrícula', 'Nota', 'Semestre']].values.tolist()
        desenhar_tabela(pdf, header, data)

    # Tabela de Candidatos Desqualificados
    if not desqualificados.empty:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, 'Candidatos Desqualificados (Nota < 10)', ln=True, align='L')
        data = desqualificados[['Nome', 'Matrícula', 'Nota', 'Semestre']].values.tolist()
        desenhar_tabela(pdf, ['Nome', 'Matrícula', 'Nota', 'Semestre'], data)

    # Tabela de Candidatos Ausentes
    if not ausentes.empty:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, 'Candidatos Ausentes', ln=True, align='L')
        data = ausentes[['Nome', 'Matrícula', 'Semestre']].values.tolist()
        desenhar_tabela(pdf, ['Nome', 'Matrícula', 'Semestre'], data)

    # Tabela de Classificação Geral
    if not df_sorted.empty:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, 'Classificação Geral', ln=True, align='L')
        data = df_sorted[['Classificacao', 'Nome', 'Matrícula', 'Nota', 'Semestre']].values.tolist()
        desenhar_tabela(pdf, header, data)

    # Gerar PDF e salvar no diretório local
    pdf_output = 'classificacao_candidatos.pdf'
    pdf.output(pdf_output)
    return pdf_output

# Função para salvar o estado da classificação
def salvar_classificacao(aprovados, suplentes, desqualificados, ausentes, df_sorted):
    st.session_state['aprovados'] = aprovados
    st.session_state['suplentes'] = suplentes
    st.session_state['desqualificados'] = desqualificados
    st.session_state['ausentes'] = ausentes
    st.session_state['df_sorted'] = df_sorted

# Função para exibir o aplicativo
def exibir_tabela():
    st.title('Classificação de Candidatos')

    # Iterar sobre o DataFrame de candidatos
    for index, row in df.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(row['Nome'])
        with col2:
            # Limitar a entrada para valores inteiros entre 0 e 20
            df.at[index, 'Nota'] = st.number_input(f'Nota de {row["Nome"]}', min_value=0, max_value=20, value=0, step=1, key=f'nota_{index}')
        with col3:
            df.at[index, 'Ausente'] = st.checkbox('Ausente?', value=row['Ausente'], key=f'ausente_{index}')

    # Botão para exibir os dados atualizados
    if st.button('Classificar Candidatos'):
        # Marcar nota zero para candidatos ausentes
        df.loc[df['Ausente'] == True, 'Nota'] = 0

        # Garantir que o valor da nota seja convertido para inteiro
        df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce').fillna(0).astype(int)

        # Filtrar candidatos com nota >= 10 para serem classificados
        df_classificaveis = df[df['Nota'] >= 10]

        # Classificar candidatos com nota >= 10 em ordem decrescente de notas e em caso de empate, por semestre
        if not df_classificaveis.empty:
            df_sorted = df_classificaveis.sort_values(by=['Nota', 'Semestre'], ascending=[False, False])
            df_sorted = df_sorted.reset_index(drop=True)  # Resetar o índice
            df_sorted['Classificacao'] = df_sorted.index + 1  # Adicionar a classificação geral começando de 1

            # Selecionar os 18 primeiros aprovados
            aprovados = df_sorted.head(18).reset_index(drop=True)
            aprovados['Classificacao'] = aprovados.index + 1

            # Selecionar os 5 próximos como suplentes
            suplentes = df_sorted.iloc[18:23].reset_index(drop=True)
            suplentes['Classificacao'] = suplentes.index + 19

        else:
            aprovados = pd.DataFrame()
            suplentes = pd.DataFrame()

                # Filtrar e exibir candidatos desqualificados (nota abaixo de 10)
        desqualificados = df[df['Nota'] < 10]

        # Filtrar e exibir candidatos ausentes
        ausentes = df[df['Ausente'] == True]

        # Salvar a classificação no estado
        salvar_classificacao(aprovados, suplentes, desqualificados, ausentes, df_sorted if not df_classificaveis.empty else pd.DataFrame())

        # Exibir resultados
        if not df_classificaveis.empty:
            st.write("### Candidatos Aprovados:")
            st.dataframe(aprovados[['Classificacao', 'Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

            st.write("### Candidatos Suplentes:")
            st.dataframe(suplentes[['Classificacao', 'Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

        if not desqualificados.empty:
            st.write("### Candidatos Desqualificados (Nota < 10):")
            st.dataframe(desqualificados[['Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

        if not ausentes.empty:
            st.write("### Candidatos Ausentes:")
            st.dataframe(ausentes[['Nome', 'Matrícula', 'Semestre']], use_container_width=True)

        if not df_classificaveis.empty:
            st.write("### Classificação Geral:")
            st.dataframe(df_sorted[['Classificacao', 'Nome', 'Matrícula', 'Nota', 'Semestre']], use_container_width=True)

    # Botões lado a lado para gerar e baixar PDF
    if 'aprovados' in st.session_state:
        col1, col2 = st.columns([1, 1])
        with col1:
            gerar = st.button('Gerar PDF', key="gerar_pdf")

        # Após gerar o PDF, salvar no estado
        if gerar and not st.session_state['aprovados'].empty:
            pdf_file = gerar_pdf(st.session_state['aprovados'], st.session_state['suplentes'], st.session_state['desqualificados'], st.session_state['ausentes'], st.session_state['df_sorted'])
            st.session_state['pdf_file'] = pdf_file

        with col2:
            # Mostrar o botão de download somente se o PDF já foi gerado
            if 'pdf_file' in st.session_state and st.session_state['pdf_file']:
                with open(st.session_state['pdf_file'], 'rb') as f:
                    st.download_button('Baixar PDF', f, file_name="classificacao_candidatos.pdf", mime="application/pdf")


# Executar o aplicativo
if __name__ == '__main__':
    # Certifique-se de inicializar a variável de estado
    if 'aprovados' not in st.session_state:
        st.session_state['aprovados'] = pd.DataFrame()
        st.session_state['suplentes'] = pd.DataFrame()
        st.session_state['desqualificados'] = pd.DataFrame()
        st.session_state['ausentes'] = pd.DataFrame()
        st.session_state['df_sorted'] = pd.DataFrame()
        st.session_state['pdf_file'] = None

    exibir_tabela()


