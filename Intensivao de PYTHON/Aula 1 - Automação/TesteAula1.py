import pyautogui
import pyperclip
import time
import pandas as pd

# Escrever passo a passo do que voce faria manualmente

# Traduzir esse passo a passo para o Python

# <!--
# - Passo 1: entrar no sistema (clickar link do relatorio)

pyautogui.pause = 1
pyautogui.click(x=539, y=961)
pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 'V')
pyautogui.write(
    "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.press('enter')
pyautogui.sleep(3)

# - Passo 2: navegar ate o local do relatorio(entrar na pastar exportar)
pyautogui.click(x=540, y=382, clicks=2)
pyautogui.sleep(2)
pyautogui.click()
# - Passo 3: fazer o download do relatorio
pyautogui.click(x=1607, y=200)
pyautogui.sleep(1)
pyautogui.click(x=1282, y=855)
pyautogui.sleep(2)

# - Passo 4: Calcular os indicadores
tabela = pd.read_excel(r"C:\Users\pedro\Downloads\Vendas - Dez.xlsx")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# - Passo 5: Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3)
# - Passo 6: Enviar por email o resultado
pyautogui.click(x=271, y=186)
time.sleep(3)
pyautogui.write("pedrovictor.rveras12@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Pedro Victor"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
