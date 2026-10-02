import pyautogui
import pandas as pd
import time

#importar a base de produtos
# tabela = pd.read_csv("produtos.csv")
# print(tabela)

#Definir o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 1.5

#abrir sistema (no nosso caso o chrome)
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")
time.sleep(1.5)
# pyautogui.click(x=958, y=592)
time.sleep(1.5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera carregar
time.sleep(5)

#fazer login (aqui pode preencher com willy.oliver13@gmail.com  suasenhaqualquer dado de login)
pyautogui.click(x=796, y=456)
pyautogui.write("willy.oliver13@gmail.com")
pyautogui.press("tab")
pyautogui.write("suasenha")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=847, y=322)

#importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#cadastrar produto
for linha in tabela.index:
    #clicar no campo de codigo
    pyautogui.click(x=852, y=320)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    marca = pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    tipo = pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    categoria = pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    preco_unitario = pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    custo = pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
    