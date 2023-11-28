import pyautogui as pag
import time
import secrets


while True:
    x = secrets.SystemRandom().randint(600, 700)
    y = secrets.SystemRandom().randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(0.2)
