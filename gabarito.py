# Curso online de 4 dias de python a neste curso foi ensinado que a forma melhor de começar qualquer código é escrendo do nosso jeito mesmo cada passo a passo do processo que queremos fazer ou obter neste projeto.

# Outro ponto para eu saber, existem, assim como a maioria das linguagens, bibliotecas que facilitam na hora de criar os código, uma delas do python é a pyautogui e outra o pandas.

# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# to import pyautogui we should use the prompt python -m pip install pyautogui  and pandas python -m pip install pandas

import pyautogui
import time

pyautogui.FAILSAFE = True #Isso significa que se você mover o mouse para o canto superior esquerdo da tela (0,0), o pyautogui dispara um erro e interrompe imediatamente a automação.

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.7 # neste caso aqui significa que para cada novo comando o sistema vai esperar 7 segundos.

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(3) 
pyautogui.press("enter")

time.sleep(5)  # <<< dá tempo para o Chrome abrir

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # já neste ele diz que apenas a partir deste ponto eu quero essa pausa de 3 segundos.


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=471, y=382) # esta coordenada pode ser adquirida pelo navegador quando eu rodo o comando e vou la no local que quero fazer o clique e coloco o mouse, seriam os eixos. 

# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo 1
pyautogui.write("sua senha")
pyautogui.click(x=680, y=538) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar. O pandas é uma biblioteca que é bastante usada em python, principalmente quando vamos associar com o uso de banco de dado, tabelas etc. 

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index: # em python qundo eu quero dizer que as linhas seguintes estão relacionados a linha de cima eu preciso colocar todas essas linhas com esse espaço que está logo abaixo, ou seja, esse comando for linha in tabela.index: vai englobar os demais comandos abaixo, pois estes estão com esse espaçamento maior. 

    # clicar no campo de código
    pyautogui.click(x=520, y=258)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) # essa string vai transformar tudo o que não está em formato de texto em texto para o código, ou seja, se for um campo que tenha um número sem o comando str vai dar erro pq é um número, já com o str ele da essa opção do código ver como uma letra e transferir para número. 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botão enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim. Esse scroll vai fazer a tela voltar para o inicio e começar novamente o processo de cadastro. essa numeração é baseado no tamanho da tela contudo o macete pe colocar um valor muito alto, pois uma vez que a barra de rolagem atinge o topo ela não continua rolando mais. E outro ponto é, se for positivo rola para cima, se for negativo para baixo. 