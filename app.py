import panel as pn
import pandas as pd

# Iniciar a extensão do Panel com suporte ao Tabulator
pn.extension('tabulator')

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

# Criar um widget Tabulator interativo
dataframe_widget = pn.widgets.Tabulator(df, show_index=False)

# Função para atualizar os dados
def update_data(event):
    updated_df = dataframe_widget.value
    print(updated_df)  # Aqui você pode processar ou salvar os dados atualizados
    return updated_df  # Retorna os dados para o painel de saída

# Botão para atualizar os dados
update_button = pn.widgets.Button(name='Atualizar Dados', button_type='primary')
update_button.on_click(update_data)

# Exibir os dados atualizados após o clique no botão
output = pn.pane.DataFrame(df, width=400)

# Função que organiza o layout
def meu_app():
    return pn.Column("### Classificação de Candidatos",
                     dataframe_widget,
                     update_button,
                     output)

# Inicializar o aplicativo Panel
app = meu_app()

# Rodar o Panel no Binder
pn.serve(app, port=5006, address='0.0.0.0', show=False)
