import os
import re
import csv
import json
import glob
import requests
from bs4 import BeautifulSoup
from collections import Counter
import xml.etree.ElementTree as ET

# URL base para teste
url = "https://www.24kitchen.pt/"
page = requests.get(url)
#print(page.text)

# Função para extrair informações de arquivos locais

# Temos que por para escolher que receita queremos fazer em vez de aparecer logo a informação toda

def extrair_informacoes_pasta(caminho_pasta):
    dados_arquivos = []
    
    # Iterar pelos arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".txt"):  # Processar apenas arquivos .txt
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            
            # Ler o conteúdo do arquivo
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()  # Ler todas as linhas do arquivo
                
                # Usar a primeira linha como título
                titulo = linhas[0].strip() if linhas else "Título não encontrado"
                
                # Unir todas as linhas para busca de autor, ingredientes e preparação
                conteudo = "".join(linhas)
                
                # Extrair o autor ou "Receita"
                autor = re.search(r"Receita de[:\-]?\s*(.+)", conteudo, re.IGNORECASE)
                autor = autor.group(1).strip() if autor else "Autor não encontrado"
                
                # Extrair ingredientes (texto entre "Ingredientes" e "Preparação")
                ingredientes = re.search(r"Ingredientes[:\-]?\s*(.*?)(?=\n\s*Preparação)", conteudo, re.IGNORECASE | re.DOTALL)
                
                # Se ingredientes foram encontrados, dividir em itens por linha
                if ingredientes:
                    ingredientes_texto = ingredientes.group(1).strip()
                    ingredientes_lista = [item.strip() for item in ingredientes_texto.split("\n") if item.strip()]
                else:
                    ingredientes_lista = []
                
                # Captura todo o conteúdo após a palavra "Preparação" até o final do arquivo
                preparacao = re.search(r"Preparação[:\-]?\s*(.*)", conteudo, re.IGNORECASE | re.DOTALL)
            
                # Se preparação foi encontrada, pegar o conteúdo
                if preparacao:
                    preparacao_texto = preparacao.group(1).strip()
                    preparacao_lista = [item.strip() for item in preparacao_texto.split("\n") if item.strip()]
                    #preparacao_lista = preparacao_texto.splitlines()
                else:
                    preparacao_lista = []
            
                # Armazenar as informações num dicionário
                dados = {
                    "arquivo": arquivo,
                    "titulo": titulo,
                    "autor": autor,
                    "ingredientes": ingredientes_lista,
                    "preparacao": preparacao_lista,
                }
                
                dados_arquivos.append(dados)
    
    return dados_arquivos

caminho = r"C:\Users\joana\Desktop\Joana\Universidade\UMinho\HD\FPLN\Trabalho_Final\receitas"
informacoes = extrair_informacoes_pasta(caminho)

#for info in informacoes:
    #print("info:", info)


# Função para extrair informações de um URL

def extrair_texto_de_url(url, pasta_destino):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica erros na requisição
        
        sopa = BeautifulSoup(resposta.text, "html.parser")
        
        # Extrair título

        elemento_titulo = sopa.find("h2", class_="page-header__title")
        titulo = elemento_titulo.get_text(strip=True) if elemento_titulo else "Título não encontrado"

        # Extrair autor
        elemento_autor = sopa.find("a", class_="page-header__link")
        autor = elemento_autor.get_text(strip=True) if elemento_autor else "Autor não encontrado"

        # Extrair ingredientes (título e lista)
        elemento_titulo_ingredientes = sopa.find("h3", class_="recipe-ingredients__title")
        titulo_ingredientes = elemento_titulo_ingredientes.get_text(strip=True) if elemento_titulo_ingredientes else "Título Ingredientes não encontrado"

        elementos_ingredientes = sopa.find_all("li", class_="recipe-ingredients__item")
        ingredientes = [item.get_text(strip=True) for item in elementos_ingredientes] if elementos_ingredientes else ["Ingredientes não encontrados"]

        # Extrair preparação (título e lista)
        elemento_titulo_preparacao = sopa.find("h3", class_="recipe-steps__title")
        titulo_preparacao = elemento_titulo_preparacao.get_text(strip=True) if elemento_titulo_preparacao else "Título Preparação não encontrado"

        elementos_preparacao = sopa.find_all("li", class_="recipe-steps__item")
        preparacao = [item.get_text(strip=True) for item in elementos_preparacao] if elementos_preparacao else ["Preparação não encontrada"]
        
        # Salvar em um arquivo .txt
        nome_arquivo = f"{titulo.replace(" ", "_")}.txt"
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
        
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(f"{titulo}\n")
            f.write(f"Receita de: {autor}\n")
            f.write(f"\n{titulo_ingredientes}\n")
            for ingrediente in ingredientes:
                f.write(f"{ingrediente}\n")
            f.write(f"\n{titulo_preparacao}\n")
            for passo in preparacao:
                f.write(f"{passo}\n")
        
        print(f"Texto extraído com sucesso e salvo em: {caminho_arquivo}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao encontar a URL: {e}")

# Função para analisar o texto dos arquivos .txt

def analise_texto(arquivo):
    with open(arquivo, "r") as f:
        texto = f.read()
    
    palavras = re.findall(r"\b\w+\b", texto.lower())
    linhas = texto.splitlines()
    
    # 1. Número de palavras e linhas
    num_palavras = len(palavras)
    num_linhas = len(linhas)
    
    # 2. Frequência de uma palavra no texto
    palavra_alvo = input("Digite uma palavra para calcular a frequência: ").strip().lower()
    freq_palavra = palavras.count(palavra_alvo)
    
    # 3. Determinar as 10 palavras mais comuns
    frequencias = Counter(palavras)
    palavras_comuns = frequencias.most_common(10)
    
    # 4. Encontrar nomes próprios no texto, no padrão "Receita de"
    nomes_proprios = re.findall(r"(?<=Receita de: )([A-Za-z ]+)", texto)
    
    # 5. Calcular o comprimento médio das frases
    frases = re.split(r"[.!?]", texto)
    frases_limpa = [frase.strip() for frase in frases if frase.strip()]
    comprimento_medio_frases = sum(len(frase.split()) for frase in frases_limpa) / len(frases_limpa) if frases_limpa else 0
    
    return {
        "arquivo": arquivo,
        "freq_palavra": freq_palavra,
        "num_palavras": num_palavras,
        "num_linhas": num_linhas,
        "palavras_comuns": palavras_comuns,
        "nomes_proprios": nomes_proprios,
        "comprimento_medio_frases": comprimento_medio_frases
    }

# Função para exportar os resultados

def exportar_resultados(resultados, formato):
    # Definir o diretório "dados exportados" no caminho desejado
    diretorio_destino = r"C:\Users\joana\Desktop\Joana\Universidade\UMinho\HD\FPLN\Trabalho_Final\receitas"
    
    # Criar o diretório caso não exista
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)
    
    # Nome base do arquivo (sem extensão)
    nome_base = os.path.splitext(os.path.basename(resultados["arquivo"]))[0]
    
    # Exportar para o formato escolhido
    if formato == "json":
        with open(f"{diretorio_destino}/{nome_base}.json", "w") as f:
            json.dump(resultados, f, indent=4)
        print(f"Resultados exportados para {diretorio_destino}/{nome_base}.json")
    
    elif formato == "csv":
        with open(f"{diretorio_destino}/{nome_base}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(resultados.keys())
            writer.writerow(resultados.values())
        print(f"Resultados exportados para {diretorio_destino}/{nome_base}.csv")
    
    elif formato == "xml":
        root = ET.Element("Resultados")
        for key, value in resultados.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(f"{diretorio_destino}/{nome_base}.xml")
        print(f"Resultados exportados para {diretorio_destino}/{nome_base}.xml")
    
    else:
        print("Formato inválido. Exportação não realizada.")

# Função principal para o menu

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Ler os arquivos .txt na pasta")
        print("2. Extrair infromações de uma URL do 24Kitchen")
        print("3. Analisar os arquivos .txt na pasta")
        print("4. Sair")
        
        escolha = input("Opção: ").strip()
        
        if escolha == "1":
            caminho = r"C:\Users\joana\Desktop\Joana\Universidade\UMinho\HD\FPLN\Trabalho_Final\receitas"
            if not os.path.exists(caminho):
                print("Caminho não encontrado. Verifique e tente novamente.")
                continue
            
            arquivos_txt = [arq for arq in os.listdir(caminho) if arq.endswith(".txt")]
            if not arquivos_txt:
                print("A pasta não contém arquivos .txt.")
                continue
            
            print("\nArquivos disponíveis:")
            for i, arquivo in enumerate(arquivos_txt, start=1):
                print(f"{i}. {arquivo}")
            
            escolha_arquivo = input("\nEscolha o número do arquivo para analisar: ").strip()
            if not escolha_arquivo.isdigit() or int(escolha_arquivo) < 1 or int(escolha_arquivo) > len(arquivos_txt):
                print("Escolha inválida. Tente novamente.")

            resultados = extrair_informacoes_pasta(caminho)
            for resultado in resultados:
                print(f"\nArquivo: {resultado["arquivo"]}")
                print(f"Título: {resultado["titulo"]}")
                print(f"Autor: {resultado["autor"]}")
                print("Ingredientes:")
                for ingrediente in resultado["ingredientes"]:
                    print(f" - {ingrediente}")
                print("Preparação:")
                for passo in resultado["preparacao"]:
                    print(f" - {passo}")

        elif escolha == "2":
            url = input("Insere a URL da receita do 24Kitchen: ").strip()
            pasta_destino = "./textos_24kitchen"
            os.makedirs(pasta_destino, exist_ok=True)
            extrair_texto_de_url(url, pasta_destino)
        
        elif escolha == "3": 
            caminho = r"C:\Users\joana\Desktop\Joana\Universidade\UMinho\HD\FPLN\Trabalho_Final\receitas"
            if not os.path.exists(caminho):
                print("Caminho não encontrado. Verifique e tente novamente.")
                continue
            
            arquivos_txt = [arq for arq in os.listdir(caminho) if arq.endswith(".txt")]
            if not arquivos_txt:
                print("A pasta não contém arquivos .txt.")
                continue
            
            print("\nArquivos disponíveis:")
            for i, arquivo in enumerate(arquivos_txt, start=1):
                print(f"{i}. {arquivo}")
            
            escolha_arquivo = input("\nEscolha o número do arquivo para analisar: ").strip()
            if not escolha_arquivo.isdigit() or int(escolha_arquivo) < 1 or int(escolha_arquivo) > len(arquivos_txt):
                print("Escolha inválida. Tente novamente.")
                continue
            
            caminho_arquivo = os.path.join(caminho, arquivos_txt[int(escolha_arquivo) - 1])
            print(f"\nAnalisando o arquivo: {arquivos_txt[int(escolha_arquivo) - 1]}")
            resultados = analise_texto(caminho_arquivo)
            
            print(f"\nFrequência da palavra escolhida: {resultados["freq_palavra"]}")

            print(f"\nNúmero de palavras: {resultados["num_palavras"]}")
            print(f"Número de linhas: {resultados["num_linhas"]}")

            print("\n10 palavras mais comuns:")

            for palavra, freq in resultados["palavras_comuns"]:
                print(f" - {palavra}: {freq}")
            
            print("\nNomes próprios encontrados:", end=" ")
            print(", ".join(resultados["nomes_proprios"]) if resultados["nomes_proprios"] else "Nenhum nome próprio encontrado.")

            print(f"\nComprimento médio das frases: {resultados["comprimento_medio_frases"]:.2f} palavras.")
            
            # Exportar resultados
            exportar = input("\nDeseja exportar os resultados? (Sim/Não): ").strip().lower()
            if exportar == "Sim":
                formato = input("Escolha o formato (json/csv/xml): ").strip().lower()
                if formato in ["json", "csv", "xml"]:
                    exportar_resultados(resultados, formato)
                else:
                    print("Formato inválido. Exportação não realizada.")
            else:
                print("Exportação ignorada.") 

        elif escolha == "4":
            print("Programa encerrado. Até breve!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para calcular a frequência de uma palavra no texto
def calcular_frequencia_palavra(conteudo, palavra):
    palavras = conteudo.lower().split()
    return palavras.count(palavra.lower())

# Função para calcular o número de palavras e linhas no texto
def contar_palavras_linhas(conteudo):
    linhas = conteudo.splitlines()
    palavras = conteudo.split()
    return len(palavras), len(linhas)

# Função para determinar as 10 palavras mais comuns no texto
def palavras_mais_comuns(conteudo):
    palavras = re.findall(r"\b\w+\b", conteudo.lower())
    frequencia = Counter(palavras)
    return frequencia.most_common(10)

# Função para encontrar todos os nomes próprios no texto
def encontrar_nomes_proprios(conteudo):
    palavras = conteudo.split()
    nomes = [palavra for palavra in palavras if palavra.istitle()]
    return nomes

# Função para calcular o comprimento médio das frases no texto
def comprimento_medio_frases(conteudo):
    frases = re.split(r"[.!?]", conteudo)
    frases = [frase.strip() for frase in frases if frase.strip()]
    if not frases:
        return 0
    total_palavras = sum(len(frase.split()) for frase in frases)
    return total_palavras / len(frases)

# Função para encontrar palavras comuns entre textos, excluindo palavras simples
def palavras_comuns(textos):
    palavras_simples = {"não", "e", "ou", "o", "a", "os", "as", "um", "uma", "de", "da", "do", "em", "no", "na", "para", "com", "por", "como", "quando", "onde", "que", "se", "mas"}
    conjuntos_palavras = [set(palavra for palavra in re.findall(r"\b\w+\b", texto.lower()) if palavra not in palavras_simples) for texto in textos]
    palavras_comuns = set.intersection(*conjuntos_palavras)
    return palavras_comuns

# Função principal para análise textual
def analisar_texto(arquivos):
    resultados = []

    for arquivo in arquivos:
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        num_palavras, num_linhas = contar_palavras_linhas(conteudo)
        palavras_comuns_lista = palavras_mais_comuns(conteudo)
        nomes = encontrar_nomes_proprios(conteudo)
        comprimento_frases = comprimento_medio_frases(conteudo)

        resultado = {
            "arquivo": arquivo,
            "num_palavras": num_palavras,
            "num_linhas": num_linhas,
            "palavras_mais_comuns": palavras_comuns_lista,
            "nomes_proprios": nomes,
            "comprimento_medio_frases": comprimento_frases
        }

        resultados.append(resultado)

    textos = [open(arquivo, "r", encoding="utf-8").read() for arquivo in arquivos]
    palavras_comuns_entre_textos = palavras_comuns(textos)

    return resultados, palavras_comuns_entre_textos

if __name__ == "__main__":
    main()
