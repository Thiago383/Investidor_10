# 📈 Scraper de Rankings de Ações - Investidor10

Este projeto realiza a raspagem de dados do site [Investidor10](https://investidor10.com.br/acoes/rankings/) para extrair rankings de ações listadas na bolsa de valores brasileira (B3). O script utiliza as bibliotecas `requests`, `BeautifulSoup` e `pandas` para coletar e organizar os dados em DataFrames.

---

## 📑 Sumário

- [📦 Pré-requisitos](#-pré-requisitos)
- [⚙️ Instalação](#️-instalação)
- [🚀 Como Executar](#-como-executar)
- [🧠 Explicação do Código](#-explicação-do-código)
  - [1. `obter_soup_da_url`](#1-obter_soup_da_url)
  - [2. `extrair_dados_da_tabela`](#2-extrair_dados_da_tabela)
  - [3. `main`](#3-main)
- [📊 Exemplo de Saída](#-exemplo-de-saída)
- [📝 Licença](#-licença)

---

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Pacotes necessários:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `IPython`

---

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt

