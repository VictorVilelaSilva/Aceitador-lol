
from time import sleep
import time
import pyautogui

def runScript():
    print("Script rodando")
    while True:
        pyautogui.locateOnScreen("imgs/NaFila.png",minSearchTime=20000)
        print("Buscando partida")
        sleep(1)
        buttonLocation = pyautogui.locateOnScreen("imgs/Aceitar.png",minSearchTime=960)
        print(f"Achou partida {time.strftime('%H:%M:%S', time.localtime())}") 
        buttonPoint = pyautogui.center(buttonLocation)
        pyautogui.click(buttonPoint)
        print(f"Partida aceita com sucesso {time.strftime('%H:%M:%S', time.localtime())}") 
        sleep(1)
        pyautogui.moveTo(0,0)
            
if __name__ == "__main__":
    runScript()
    print("Script finalizado")