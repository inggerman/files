import OPi.GPIO as GPIO
import uinput
import time

# Configura el modo GPIO
GPIO.setmode(GPIO.BOARD)

# Define los pines GPIO para cada botón para los dos jugadores
jugador1 = {
    'BTN_A': 11,
    'BTN_B': 12,
    'BTN_X': 13,
    'BTN_Y': 15,
    'BTN_L': 16,
    'BTN_R': 18,
    'BTN_START': 22,
    'BTN_SELECT': 24,
    'UP': 26,
    'DOWN': 28,
    'LEFT': 32,
    'RIGHT': 36,
}

jugador2 = {
    'BTN_A': 37,
    'BTN_B': 38,
    'BTN_X': 40,
    'BTN_Y': 29,
    'BTN_L': 31,
    'BTN_R': 33,
    'BTN_START': 35,
    'BTN_SELECT': 19,
    'UP': 21,
    'DOWN': 23,
    'LEFT': 7,
    'RIGHT': 5,
}

# Configura uinput
eventos_j1 = {key: uinput.evbit for key in jugador1.keys()}
eventos_j2 = {key: uinput.evbit for key in jugador2.keys()}
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
