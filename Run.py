# Mensajes Automaticos a Whatsapp By: Geovas or MartL7
# Recuerda instalar la libreria de Pyautogui desde tu termna con el comando
#     pip install pyautogui

import pyautogui, webbrowser, re
from time import sleep

# Codigo Aplicable ejecutables en Terminales 
def Titulo(texto):
    print("\033[1;31m" + texto + "\033[0m")

def InputVerde(prompt):
    return input("\033[1;32m" + prompt + "\033[0m")

Titulo("MartL7 Scripts")


CodigoPais = InputVerde("Ingresa el código de país (por ejemplo, +1 para EE. UU., Mexico solo pon 52): ")
numero = InputVerde("Ingresa el Número de la Víctima (sin espacios ni caracteres especiales): ")
Texto = InputVerde("Ingresa el Mensaje a Enviar: ")
Cantidad = int(InputVerde("Ingresa la cantidad de mensajes: "))

# Eliminamos cualquier caracter no numérico del número de teléfono
numero = re.sub(r'\D', '', numero)

if CodigoPais == 52:
    webbrowser.open(f'https://web.whatsapp.com/send?phone={CodigoPais}{numero}')

    for i in range(Cantidad):
        pyautogui.typewrite(Texto)
        pyautogui.press('enter')

# Si el codigo de pais no tiene el signo "+"", lo agregamos
if not CodigoPais.startswith('+'):
    CodigoPais = '+' + CodigoPais

Titulo("Comenzando...")
webbrowser.open(f'https://web.whatsapp.com/send?phone={CodigoPais}{numero}')

sleep(10)

for i in range(Cantidad):
    pyautogui.typewrite(Texto)
    pyautogui.press('enter')
