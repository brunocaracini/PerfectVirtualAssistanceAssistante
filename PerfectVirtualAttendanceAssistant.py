import webbrowser
import pyautogui as py
import time
from datetime import datetime as dt
import datetime
from datetime import timedelta
import os



def reunionURL():
    url = input('Ingrese url de la reunión: ')
    n_reconecciones = input('Ingrese el número de reconecciones: ')
    #Gets current date
    today = dt.today()
    #Sets meeeting time
    hora = input('Ingrese solamente la hora de la reunión: ')
    minutos = input('Ingrese los minutos de la hora de la reunión: ')
    os.system('cls')
    i = 0
    #Sets meeting time as taget time
    for i in range(0,int(n_reconecciones)+1):
        if i == 0:
            target_time = datetime.datetime(2020, int(today.month), int(today.day), int(hora), int(minutos)) 
        else:
            target_time = target_time + timedelta(minutes=45)  
        while datetime.datetime.now() < target_time:
            os.system('cls')
            print("")
            print("Lo conectaremos a su clase a las", hora, ":", minutos,"hs. Lo reconectaremos ", n_reconecciones, "veces.")
            print("")
            print("Todo está bajo control. Duerma tranquilo, el descanso es fundamental.")
            time.sleep(10)
        os.system('cls')
        print('Lo estamos conectando a su clase...')
        webbrowser.open(url, new=2)
        #Allows time for webpage to load
        time.sleep(8)
        #Set clicks parameter to 2
        py.click(x=714, y=175, clicks=1, interval=0.25)
        #Allows the meeting to connect
        time.sleep(20)
        #Set audio enter by computer
        py.click(x=714, y=310, clicks=1, interval=0.25)
        i+=1


def menu():
    op = False
    aux = False
    while aux == False:
        print('Bienvenido a su asistente de asistencia perfecta')
        print('1 - Reunión sin url')
        print('2 - Reunión con url')
        op = input('Ingrese la opción deseada: ')
        if op == '1':
            aux = True
        elif op == '2':
            os.system('cls')
            reunionURL()


menu()














































