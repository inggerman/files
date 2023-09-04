import OPi.GPIO as GPIO
import uinput
import time

# Configura el modo GPIO
GPIO.setmode(GPIO.BOARD)

# Define los pines GPIO para cada botón para los dos jugadores
jugador1 = {
    uinput.BTN_A: 11,
    uinput.BTN_B: 12,
    uinput.BTN_X: 13,
    uinput.BTN_Y: 15,
    uinput.BTN_TL: 16,
    uinput.BTN_TR: 18,
    uinput.BTN_START: 22,
    uinput.BTN_SELECT: 24,
    uinput.KEY_UP: 26,
    uinput.KEY_DOWN: 28,
    uinput.KEY_LEFT: 32,
    uinput.KEY_RIGHT: 36,
}

jugador2 = {
    uinput.BTN_A: 37,
    uinput.BTN_B: 38,
    uinput.BTN_X: 40,
    uinput.BTN_Y: 29,
    uinput.BTN_TL: 31,
    uinput.BTN_TR: 33,
    uinput.BTN_START: 35,
    uinput.BTN_SELECT: 19,
    uinput.KEY_UP: 21,
    uinput.KEY_DOWN: 23,
    uinput.KEY_LEFT: 7,
    uinput.KEY_RIGHT: 5,
}

# Configura uinput
eventos_j1 = list(jugador1.keys())
eventos_j2 = list(jugador2.keys())
dispositivo_j1 = uinput.Device(eventos_j1)
dispositivo_j2 = uinput.Device(eventos_j2)

# Configura los pines como entrada
for pin in jugador1.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for pin in jugador2.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Bucle principal para leer los botones y emitir eventos
while True:
    for evento, pin in jugador1.items():
        if GPIO.input(pin) == GPIO.LOW:
            dispositivo_j1.emit(evento, 1)
        else:
            dispositivo_j1.emit(evento, 0)

    for evento, pin in jugador2.items():
        if GPIO.input(pin) == GPIO.LOW:
            dispositivo_j2.emit(evento, 1)
        else:
            dispositivo_j2.emit(evento, 0)

    time.sleep(0.1)
