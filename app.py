import panel as pn
import pandas as pd

# Iniciar a extensão do Panel com suporte ao Tabulator
pn.extension('tabulator')

# Lista de candidatos com nome, matrícula, nota e se estão ausentes
candidatos = [
    {"Nome": "Alexandre Amorim Pivetta", "Matrícula": "2022010619", "Nota": 0, "Ausente": False},
    {"Nome": "Artur Ribeiro de Barcellos", "Matrícula": "2022020326", "Nota": 0, "Ausente": False},
    {"Nome": "Brenda Garcia Xavier", "Matrícula": "2022020301", "Nota": 0, "Ausente": False},
    {"Nome": "Cirano Gautier dos Santos", "Matrícula": "2017012023", "Nota": 0, "Ausente": False},
    # Adicione outros candidatos conforme necessário...
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
