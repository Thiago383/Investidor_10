from bs4 import BeautifulSoup
import requests
import json
import os

# --- DEFINA O CAMINHO DA PASTA AQUI ---
# Por exemplo: "data", "minha_pasta_de_saida", "/caminho/completo/para/sua/pasta"
OUTPUT_DIRECTORY = "E:\Documentos\Web_scraping\Web_scraping_beautifulsoup4\Investidor_10\data"
# ------------------------------------

def obter_soup_da_url(url, headers=None):
    """
    Realiza uma requisição GET para a URL fornecida e retorna o objeto BeautifulSoup.
    """
    try:
        session = requests.Session()
        if headers:
            session.headers.update(headers)
        response = session.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return None

def extrair_dados_da_tabela(soup):
    """
    Extrai os dados da tabela dentro do elemento <tbody id="rankigns">.
    """
    tbody = soup.select_one("#rankigns > tbody")
    tabela = {}
    linha_atual = None

    if tbody:
        valores = []
        for linha in tbody.find_all('tr'):
            for celula in linha.find_all('td'):
                div_oculta = celula.find('div', style='visibility: hidden')
                if div_oculta and div_oculta.text.strip():
                    valores.append(div_oculta.text.strip())

        for item in valores:
            if item.isupper() and item.isalpha():
                linha_atual = item
                tabela[linha_atual] = []
            elif item.isupper() and item.isalnum():
                linha_atual = item
                tabela[linha_atual] = []
            elif linha_atual is not None:
                tabela[linha_atual].append(item)
    else:
        print("Tbody não encontrado nesta página.")

    return tabela

def main():
    """
    Função principal para executar o processo de scraping e salvamento em arquivos JSON.
    """
    url_fixa = "https://investidor10.com.br/acoes/rankings/"
    urls_relativas = [
        {'href': 'maiores-dividend-yield/'},
        {'href': 'maiores-valor-de-mercado/'},
        {'href': 'maiores-receitas/'},
        {'href': 'maiores-lucros/'},
        {'href': 'maiores-roes/'},
        {'href': 'menores-pls/'},
        {'href': 'maiores-altas-30-dias/'},
        {'href': 'maiores-altas-12-meses/'},
        {'href': 'maiores-crescimento-lucro/'},
        {'href': 'maiores-caixas/'},
        {'href': 'maiores-crescimento-receita/'},
        {'href': 'maiores-margens-liquidas/'}
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Referer": "https://google.com"
    }

    # Cria a pasta de saída se ela não existir
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    for url_info in urls_relativas:
        url_completa = url_fixa + url_info['href']
        print(f"\nProcessando URL: {url_completa}")
        soup = obter_soup_da_url(url_completa, headers)

        if soup:
            json_data = extrair_dados_da_tabela(soup)
            if json_data:
                nome_arquivo = url_info['href'].replace('-', '_').replace('-', '_')+ ".json"
                caminho_completo = os.path.join(OUTPUT_DIRECTORY, nome_arquivo)

                try:
                    with open(caminho_completo, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, ensure_ascii=False, indent=4)
                    print(f"Dados salvos em '{caminho_completo}'")
                except IOError as e:
                    print(f"Erro ao salvar o arquivo {caminho_completo}: {e}")
            else:
                print("Nenhum dado de tabela encontrado nesta URL.")

if __name__ == "__main__":
    main()