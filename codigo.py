import pyautogui
import time
import pandas as pd

pyautogui.PAUSE=1.1
#Passo 1: 
#Clicar na tecla de iniciar;
pyautogui.press("win")
#Digitar na busca o nome do navegador;
pyautogui.write("Google Chrome")
#Clicar enter para abrir o navegador;
pyautogui.press("enter")

#Passo 2:
#Digitar o link no navegador;
link=("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
#Clicar enter para acessar o link;
pyautogui.press("enter")

#Passo 3: 
#Digitar login;
pyautogui.click(x=1945, y=373)
pyautogui.write("python.2024@gmail.com")
#Digitar senha;
pyautogui.press("tab")
pyautogui.write("123456")
#Clicar enter para entrar no site;  
pyautogui.press("enter")
time.sleep(1.8)

#Passo 4:
#Cadastrar a base de dados;
#Passo 5:
#Repetir processo até que toda a base de dados esteja cadastrada;
tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:
  pyautogui.click(x=1930, y=260)
  #codigo
  pyautogui.write(str(tabela.loc[linha, "codigo"]))
  pyautogui.press("tab")
  #marca
  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  #tipo
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  #categoria
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  #preco_unitario
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  #custo
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  #obs
  if not pd.isna(tabela.loc[linha, "obs"]):
    pyautogui.write(str(tabela.loc[linha, "obs"]))
  pyautogui.press("tab")

  pyautogui.press("enter")
  pyautogui.scroll(5000)
