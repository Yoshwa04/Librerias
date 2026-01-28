import time

def countdown(seconds: int):
    while seconds > 0:
        print(f"Tiempo restante: {seconds} segundos")
        time.sleep(1)
        seconds -= 1
    print("⏰ Tiempo terminado!")
    

def countdown_silent(seconds: int):
    time.sleep(seconds)
