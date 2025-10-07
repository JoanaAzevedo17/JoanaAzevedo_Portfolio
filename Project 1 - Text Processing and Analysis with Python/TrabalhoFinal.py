import os
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.24kitchen.pt/"
page = requests.get(url)

print(page.text)

# Função para extrair informações de arquivos locais
def extrair_informacoes_pasta(caminho_pasta):
    dados_arquivos = []
    
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                
                # Extrair título
                titulo = re.search(r'Título[:\-]?\s*(.+)', conteudo, re.IGNORECASE)
                titulo = titulo.group(1).strip() if titulo else 'Título não encontrado'
                
                # Extrair autor
                autor = re.search(r'Autor[:\-]?\s*(.+)', conteudo, re.IGNORECASE)
                autor = autor.group(1).strip() if autor else 'Autor não encontrado'
                
                # Extrair data
                data = re.search(r'Data[:\-]?\s*(.+)', conteudo, re.IGNORECASE)
                data = data.group(1).strip() if data else 'Data não encontrada'
                
                # Extrair ingredientes (exemplo para receitas)
                ingredientes = re.findall(r'-\s*(.+)', conteudo)  # Lista de linhas com "-"
                
                # Armazenar em um dicionário
                dados = {
                    'arquivo': arquivo,
                    'titulo': titulo,
                    'autor': autor,
                    'data': data,
                    'ingredientes': ingredientes
                }
                
                dados_arquivos.append(dados)
    
    return dados_arquivos


# Função para extrair informações de um URL
def extrair_texto_de_url(url, pasta_destino):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica erros na requisição
        
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        
        # Extrair título
        titulo = sopa.find('h1').get_text(strip=True) if sopa.find('h1') else 'Título não encontrado'
        
        # Extrair autor (exemplo; depende da estrutura HTML do site)
        autor = sopa.find(class_='author').get_text(strip=True) if sopa.find(class_='author') else 'Autor não encontrado'
        
        # Extrair data (exemplo; depende da estrutura HTML do site)
        data = sopa.find(class_='date').get_text(strip=True) if sopa.find(class_='date') else 'Data não encontrada'
        
        # Extrair conteúdo principal (ex.: lista de ingredientes, modo de preparo)
        conteudo = ''
        for paragrafo in sopa.find_all('p'):
            conteudo += paragrafo.get_text(strip=True) + '\n'
        
        ingredientes = [li.get_text(strip=True) for li in sopa.find_all('li')]
        
        # Salvar em um arquivo .txt
        nome_arquivo = f"{titulo.replace(' ', '_')}.txt"
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
        
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"Título: {titulo}\n")
            f.write(f"Autor: {autor}\n")
            f.write(f"Data: {data}\n")
            f.write("Conteúdo:\n")
            f.write(conteudo)
            f.write("\nIngredientes:\n")
            for ingrediente in ingredientes:
                f.write(f"- {ingrediente}\n")
        
        print(f"✅ Texto extraído com sucesso e salvo em: {caminho_arquivo}")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a URL: {e}")


# Menu principal
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Analisar arquivos .txt na pasta")
        print("2. Extrair texto de uma URL do 24Kitchen")
        print("3. Sair")
        
        escolha = input("Opção: ").strip()
        
        if escolha == '1':
            caminho = './textos_24kitchen'
            resultados = extrair_informacoes_pasta(caminho)
            for resultado in resultados:
                print(f"\nArquivo: {resultado['arquivo']}")
                print(f"Título: {resultado['titulo']}")
                print(f"Autor: {resultado['autor']}")
                print(f"Data: {resultado['data']}")
                print("Ingredientes:")
                for ingrediente in resultado['ingredientes']:
                    print(f" - {ingrediente}")
        
        elif escolha == '2':
            url = input("Insere o URL da receita do 24Kitchen: ").strip()
            pasta_destino = './textos_24kitchen'
            os.makedirs(pasta_destino, exist_ok=True)
            extrair_texto_de_url(url, pasta_destino)
        
        elif escolha == '3':
            print("👋 Programa encerrado. Até breve!")
            break
        
        else:
            print("❌ Opção inválida. Tente novamente.")


# Executar o programa
if __name__ == '__main__':
    main()

