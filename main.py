import time
import pyautogui
from time import sleep
from threading import Thread, Event


def handleMatchType(stop_event):
    """
    Executa duas buscas (lol.png e tft.png) simultaneamente.
    Se encontrar uma delas, armazena o resultado e finaliza a busca.
    Caso `stop_event` esteja setado, as buscas são interrompidas.
    """
    foundEvent = Event()
    result = [None]

    def search_image(image_path, match_result):
        while not foundEvent.is_set() and not stop_event.is_set():
            if pyautogui.locateOnScreen(image_path, minSearchTime=20000):
                result[0] = match_result
                foundEvent.set()

    threadLol = Thread(target=search_image, args=("imgs/lol.png", "lol"), daemon=True)
    threadTft = Thread(target=search_image, args=("imgs/tft.png", "tft"), daemon=True)

    threadLol.start()
    threadTft.start()

    while not foundEvent.is_set() and not stop_event.is_set():
        time.sleep(0.1)

    return result[0] if not stop_event.is_set() else None


def runScript(stop_event):
    """
    Loop principal do script:
    1. Detecta o modo de jogo (lol ou tft).
    2. Aguarda o usuário estar na fila.
    3. Quando o botão "Aceitar" é encontrado, clica para aceitar a partida.
    4. Repete indefinidamente, a menos que `stop_event` seja setado.
    """
    print("Script rodando")
    imagsDictionary = {"lol": "imgs/NaFilaLol.png", "tft": "imgs/NaFilaTft.png"}

    while not stop_event.is_set():
        matchType = handleMatchType(stop_event)
        if matchType is None:
            break

        print(f"Modo de Jogo: {matchType}")
        pyautogui.locateOnScreen(imagsDictionary[matchType], minSearchTime=20000)
        print("Está na fila")

        sleep(1)

        if stop_event.is_set():
            break

        buttonLocation = pyautogui.locateOnScreen(
            "imgs/Aceitar.png", minSearchTime=960, confidence=0.8
        )
        if buttonLocation is None:
            continue

        print(f"Achou partida {time.strftime('%H:%M:%S', time.localtime())}")
        buttonPoint = pyautogui.center(buttonLocation)
        pyautogui.click(buttonPoint)
        pyautogui.moveTo(0, 0)
        print(
            f"Partida aceita com sucesso {time.strftime('%H:%M:%S', time.localtime())}"
        )

        sleep(5)
        pyautogui.moveTo(0, 0)

    print("Saindo do loop principal...")


def main():
    """
    Função principal:
      - Cria um 'stop_event' para controlar a finalização das threads.
      - Inicia a thread principal de execução (runScript).
      - Fica aguardando uma ação do usuário (Enter) para encerrar.
    """
    stop_event = Event()

    main_thread = Thread(target=runScript, args=(stop_event,))
    main_thread.start()

    input("Pressione ENTER para encerrar o script.\n")

    stop_event.set()

    main_thread.join()

    print("Script finalizado.")


if __name__ == "__main__":
    main()
