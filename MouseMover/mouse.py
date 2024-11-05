import pyautogui
import time
from pynput.mouse import Listener

# Parametry
BEZCZYNNOSC_CZAS = 5  # czas (w sekundach) bez aktywności myszki przed automatycznym ruchem
RUCH_DYSTANS = 50     # dystans (w pikselach) do przesunięcia w przypadku braku aktywności

# Zmienna globalna śledząca ostatni ruch myszy
ostatni_ruch = time.time()

# Ustawienie początkowego kierunku ruchu myszy
kierunek_x = RUCH_DYSTANS
kierunek_y = RUCH_DYSTANS

# Pobranie wymiarów ekranu
szerokosc_ekranu, wysokosc_ekranu = pyautogui.size()

# Funkcja do rejestrowania ruchu myszy
def on_move(x, y):
    global ostatni_ruch
    ostatni_ruch = time.time()  # resetuj czas ostatniego ruchu

# Funkcja do automatycznego poruszania myszką, gdy nie było ruchu przez określony czas
def automatyczny_ruch():
    global ostatni_ruch, kierunek_x, kierunek_y
    while True:
        czas_bezczynnosci = time.time() - ostatni_ruch
        if czas_bezczynnosci > BEZCZYNNOSC_CZAS:
            # Pobierz aktualną pozycję kursora
            x, y = pyautogui.position()

            # Sprawdzenie krawędzi ekranu i zmiana kierunku ruchu
            if x <= 0 or x >= szerokosc_ekranu - 1:
                kierunek_x = -kierunek_x  # zmiana kierunku w poziomie
            if y <= 0 or y >= wysokosc_ekranu - 1:
                kierunek_y = -kierunek_y  # zmiana kierunku w pionie

            # Przesuń myszkę w określonym kierunku
            pyautogui.move(kierunek_x, kierunek_y, duration=0.5)
            
            # Zaktualizuj czas po automatycznym ruchu
            ostatni_ruch = time.time()
        
        # Poczekaj sekundę przed kolejnym sprawdzeniem
        time.sleep(1)

# Uruchomienie nasłuchiwania ruchu myszy
with Listener(on_move=on_move) as listener:
    automatyczny_ruch()
    listener.join()
