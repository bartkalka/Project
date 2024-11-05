import pyautogui
import time
from pynput.mouse import Listener

# Parametry
BEZCZYNNOSC_CZAS = 5  # czas (w sekundach) bez aktywności myszki przed automatycznym ruchem
RUCH_DYSTANS = 100     # dystans (w pikselach) do przesunięcia w przypadku braku aktywności

# Zmienna globalna śledząca ostatni ruch myszy
ostatni_ruch = time.time()

# Funkcja do rejestrowania ruchu myszy
def on_move(x, y):
    global ostatni_ruch
    ostatni_ruch = time.time()  # resetuj czas ostatniego ruchu

# Funkcja do automatycznego poruszania myszką, gdy nie było ruchu przez określony czas
def automatyczny_ruch():
    global ostatni_ruch
    while True:
        czas_bezczynnosci = time.time() - ostatni_ruch
        if czas_bezczynnosci > BEZCZYNNOSC_CZAS:
            # Porusz myszką o ustalony dystans (możesz zmienić wartości x i y)
            pyautogui.move(RUCH_DYSTANS, 0, duration=0.5)
            ostatni_ruch = time.time()  # resetuj czas po automatycznym ruchu
        time.sleep(1)

# Uruchomienie nasłuchiwania ruchu myszy
with Listener(on_move=on_move) as listener:
    automatyczny_ruch()
    listener.join()
