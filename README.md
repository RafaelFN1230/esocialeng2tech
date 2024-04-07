# Ficha Financeira Extractor
builde constroi dataset
controller modifica data set
use_case usa dataser

## Overview

Este programa foi desenvolvido com o objetivo de automatizar a extração da "Ficha Financeira" da cópia integral de um processo. Ele é desenvolvido considerando que o usuário já tenha conhecimento das páginas iniciais e finais da ficha financeira. 

Ao coletar as informações da ficha, o programa remove os dados bancários e realiza a transposição dos dados, convertendo linhas em colunas e vice-versa. O período é sempre mantido na coluna "A", seguido pelas informações dos proventos, descontos e, por fim, os totais.

Os dados extraídos são salvos em um arquivo Excel (.xlsx) na mesma pasta onde se encontra a aplicação, seguindo o seguinte padrão de nomenclatura: "{nome do arquivo enviado} Ficha Financeira pg({página inicial} - {página final}).xlsx".

O código foi desenvolvido inteiramente em [Python](https://www.python.org/).

## Inicialização do Projeto
- Passo 1: Clone o Repositório

```bash
$ git clone https://github.com/CloudEducationBrazil/esocialeng2tech.git
$ cd esocialeng2tech
```
- Passo 2: Criação do Ambiente Virtual
    - Para isolar as dependências do projeto, crie um ambiente virtual:

```bash
Copy code
$ python -m venv .venv
```
- Passo 3: Ativação do Ambiente Virtual
    - Ative o ambiente virtual:

No Windows:
```bash
.venv\Scripts\activate
```
No Linux/macOS:
```bash
source .venv/bin/activate
```
- Passo 4: Instalação das Dependências

    - Instale as bibliotecas necessárias: [pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide), [openpyxl](https://openpyxl.readthedocs.io/en/stable/tutorial.html) e [pdfplumber](https://pypi.org/project/pdfplumber/).

```bash
$ pip install pandas openpyxl pdfplumber
```
- Executando a Aplicação:
    - Após ativar o ambiente virtual, execute a aplicação normalmente utilizando o arquivo main.py.

## Funcionalidades

- [x] Interface grafica para interação com o usuário.
- [x] Coleta do usuário arquivo do tipo pdf, coleta pagina inicial e final da ficha.
- [x] Identificação do tipo de arquivo enviado.
- [x] Verificação do número de páginas no arquivo enviado e se o número de página está dentro do alcance do arquivo.
- [x] Identificação tabelas dentro de um arquivo .pdf.
- [x] Coleta apenas os dados das tabelas dentro do intervalo especificado.
    - [x] Separação dos dados em quatro grupos: Periodo, Proventos, Descontos e Totais.
    - [x] Organização dos dados dentro dos grupos por centro de custos.
    - [x] Concatenação dos dados do mesmo grupo e centro de custo.
- [x] Tratamento dos dados coletados.
    - [x] Remoção de informações bancárias.
    - [x] Eliminação de linhas em branco.
- [x] Transposição dos dadoss.
- [x] Criação de um arquivo Excel seguindo a ordem: Período, Proventos, Descontos e Totais.
- [x] Salvamento do arquivo na mesma pasta onde o programa está localizado.
