# Projeto Python RPA: Automação de Tarefas e Criação de Bots 

Projeto realizado com o auxílio das aulas ministradas pela Hashtag Treinamentos, durante a semana de jornada Python.

## Objetivo: 

Criar Bot, com linguagem Python, capaz de acessar página web e realizar o cadastro de informações, presentes em uma base de dados, de forma automatizada.

## 🛠️Ferramentas utilizadas
### Pandas:
Biblioteca de software criada para a linguagem Python para manipulação e análise de dados.

### Pyautogui:
Biblioteca tem como principal foco a automação de processos repetitivos e fornece meios para se controlar o mouse e o teclado.

### Time: 
Biblioteca padrão do Python (não necessita de instalação) que fornece várias funcionalidades relacionadas ao tempo, permite manipular, formatar e exibir datas, horários e intervalos de tempo.

## 🔧 Pré-requisitos

### Instalar Python

Seguir o tutorial disponível no link abaixo:

    https://python.org.br/instalacao-windows/

### Instalar Pandas

Para realizar sua instalação, basta executar o seguinte comando no terminal do Visual Studio Code (VSCode) : 

    pip install pandas 

### Instalar Pyautogui

Para realizar sua instalação, basta executar o seguinte comando no terminal do Visual Studio Code (VSCode) : 

    pip install pyautogui 

## 📋Conteúdo 

### produtos.csv
Arquivo no formato csv que contém a base de dados dos produtos que serão cadastrados na página web.

### passo_a_passo1.ipynb
Arquivo jupyter notebook que contém o passo a passo mais detalhado do processo de automação, as etapas estão divididas em blocos individuais de execução. 

### codigo.py: 
Código completo, ao executar irá abrir de forma automática o navegador, irá acessar a página web que consta no código e inicializará o processo de cadastro de todos produtos de forma automática.

Obs.: As coordenadas x e y, utilizadas para realizar o clique no campo de busca, podem sofrer alterações de acordo com o tamanho do monitor que será executado.

    pyautogui.click(x=1945, y=373)
    pyautogui.click(x=1930, y=260)

  ATENÇÃO: caso deseje interroper o processo de automação basta colocar o cursor do mouse na parte superior esquerda do seu monitor e aguardar alguns segundos.





