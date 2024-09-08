import streamlit as st
from PIL import Image
import pytesseract
import re

# Configurar o pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Caminho do executável do Tesseract

# Classe para armazenar informações dos candidatos
class Candidato:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.nota = None  # Inicializar nota como None

    def adicionar_nota(self, nota):
        self.nota = nota

    def __repr__(self):
        return f"{self.nome} - {self.matricula} - Nota: {self.nota}"

# Função para processar a imagem e extrair dados dos candidatos
def processar_imagem(imagem_path):
    imagem = Image.open(imagem_path)
    texto = pytesseract.image_to_string(imagem)
    candidatos = []
    linhas = texto.split("\n")
    for linha in linhas:
        match = re.match(r'^(\d+)\s+([\w\s]+)\s+(\d+)', linha)
        if match:
            nome = match.group(2).strip()
            matricula = match.group(3).strip()
            candidatos.append(Candidato(nome, matricula))
    return candidatos

# Lista de candidatos (simulação da extração)
candidatos = processar_imagem("/path/to/image.jpeg")  # Substituir pelo caminho correto

# Interface Gráfica usando Streamlit
st.title("Sistema de Classificação de Candidatos")

# Exibir candidatos e campos para adicionar notas
for candidato in candidatos:
    nota = st.number_input(f"Nota para {candidato.nome}:", min_value=0.0, max_value=20.0, step=0.5, key=candidato.matricula)
    candidato.adicionar_nota(nota)

# Botão para processar a classificação
if st.button("Classificar Candidatos"):
    resultado = classificar_candidatos([c for c in candidatos if c.nota is not None])
    st.text_area("Resultados", resultado, height=300)

# Função para classificar candidatos
def classificar_candidatos(candidatos):
    # Ordenar candidatos pela nota
    candidatos.sort(key=lambda x: x.nota, reverse=True)
    return "\n".join([str(c) for c in candidatos])

