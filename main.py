from time import sleep
import time
import pyautogui
from threading import Thread, Event


def handleMatchType():
    import pyautogui

    foundEvent = Event()
    result = [None]

    def search_image(image_path, match_result):
        while not foundEvent.is_set():
            if pyautogui.locateOnScreen(image_path, minSearchTime=20000):
                result[0] = match_result
                foundEvent.set()

    threadLol = Thread(target=search_image, args=("imgs/lol.png", "lol"))
    threadTft = Thread(target=search_image, args=("imgs/tft.png", "tft"))

    threadLol.start()
    threadTft.start()

    foundEvent.wait()

    return result[0]


def runScript():
    print("Script rodando")
    imagsDictionary = {"lol": "imgs/NaFilaLol.png", "tft": "imgs/NaFilaTft.png"}

    while True:
        matchType = handleMatchType()
        print(f"Modo de Jogo: {matchType}")
        pyautogui.locateOnScreen(imagsDictionary[matchType], minSearchTime=20000)
        print("Esta na fila")
        sleep(1)
        buttonLocation = pyautogui.locateOnScreen(
            "imgs/Aceitar.png", minSearchTime=960, confidence=0.8
        )
        print(f"Achou partida {time.strftime('%H:%M:%S', time.localtime())}")
        buttonPoint = pyautogui.center(buttonLocation)
        pyautogui.click(buttonPoint)
        pyautogui.moveTo(0, 0)
        print(
            f"Partida aceita com sucesso {time.strftime('%H:%M:%S', time.localtime())}"
        )
        sleep(5)
        pyautogui.moveTo(0, 0)
        buttonLocation = [0, 0]


if __name__ == "__main__":
    runScript()
    print("Script finalizado")
