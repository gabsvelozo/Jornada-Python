# Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir sistema -> logar -> importar base de dados dos produtos -> cadastrar 1 produto -> repetir os passos

import pyautogui # Biblioteca de automatização
import time
import pandas

pyautogui.PAUSE = 0.5 

# pyautogui.comando("") (click -> para teclas, press, write, hotkey -> atalho de teclado (ex: ctrl, C))
# pyautogui.hotkey("command", "space")

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=605, y=469)
pyautogui.write("python@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)


for linha in tabela.index:
    pyautogui.click(x=594, y=324)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if obs != "nan": # Vai evitar preencher o valor vazio
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(100000)