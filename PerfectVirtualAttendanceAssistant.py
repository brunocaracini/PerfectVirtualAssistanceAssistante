'''
Description:
This script autoconnects to a Zoom Meeting automatically and reconnects any times as needed after 40 minutes (based on free version meetings duration).
Also, it is possible to set what to do until the meeting starts (f.e, suspend the machine), and it will wake up for the meeting time. 
Finally, you can choose what to do after the call is over, including the amount of reconnections selected (f.e, suspend or shut down the machine).
'''

import webbrowser
import pyautogui as py
import time
import datetime
import os
from datetime import datetime as dt
from datetime import timedelta
from timer import wakeup

#Global Variables
duracion = 42

def calculaMin(month, day, hora, minutos):
    date = str(datetime.datetime(2020, month, day, hora, minutos) - datetime.datetime.now())
    date = date.split(".")
    date = date[0]
    date = date.split(":")
    hours = date[0]
    minutes = date[1]
    seconds = date[2]
    minutes = int(hours) * 60 + int(minutes) - 1
    print(minutes)
    
    return minutes

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    
    return '\n'.join(res)

def reunionURL():
    global duracion
    url = input('Ingrese url de la reunión: ')
    n_reconecciones = input('Ingrese el número de reconecciones: ')
    
    #Gets current date
    today = dt.today()
    
    #Sets meeeting time
    hora = input('Ingrese solamente la hora de la reunión: ')
    minutos = input('Ingrese los minutos de la hora de la reunión: ')
    
    op = False
    op2 = False
    aux2 = False
    aux = False
    
    while aux2 == False:
        print('¿Qué desea hacer hasta el horario de la clase?')
        print('1 - Suspender la computadora y despertarla a la hora de la clase.')
        print('2 - No hacer nada.')
        op2 = input('Elija una opción: ')
        if op2 == '1' or op2 =='2':
            aux2 = True
    os.system('cls')
    
    while aux == False:
        print('¿Qué desea hacer una vez finalizada la clase?')
        print('1 - Suspender la computadora.')
        print('2 - Apagar la computadora.')
        print('3 - No hacer nada.')
        op = input('Elija una opción: ')
        if op == '1' or op =='2' or op == '3':
            aux = True
    os.system('cls')
    if datetime.datetime.now() < datetime.datetime(2020, int(today.month), int(today.day), int(hora), int(minutos)) and op2 == '1':
        minutes = calculaMin(int(today.month), int(today.day), int(hora), int(minutos)) 
        wakeup(minutes)
    i = 0
    
    #Sets meeting time as taget time
    for i in range(0,int(n_reconecciones)+1):
        if i == 0:
            target_time = datetime.datetime(2020, int(today.month), int(today.day), int(hora), int(minutos)) 
        else:
            target_time = target_time + timedelta(minutes=duracion)  
            
        while datetime.datetime.now() < target_time:
            os.system('cls')
            print(bordered(" "*23 + "RESUMEN DE SU CONEXIÓN:" + " "*23))
            print("")
            print("- Lo conectaremos a su clase a las " + str(hora) + ":" + str(minutos) + " hs")
            print("- Lo reconectaremos " + str(n_reconecciones) + " veces cada " + str(duracion + 1) + " minutos")
            #print("")
            
            if op == '1':
                accion = 'se suspenderá su computadora.'
            elif op == '2':
                accion = 'se apagará su computadora.'
            elif op == '3':
                accion = 'no se realizará ninguna acción.'
                
            print("- Una vez finalizada la clase " + accion)
            print("")
            print(bordered("Todo está bajo control. Duerma tranquilo, el descanso es fundamental."))
            time.sleep(10)
        
        #Print Logg
        print('Lo estamos conectando a su clase...')
        time.sleep(5)
        py.press('right')
        webbrowser.open(url, new=2)
        
        #Allows time for webpage to load
        time.sleep(8)
        
        #Set clicks parameter to 2
        py.press('left')
        py.press('enter')
        
        #Allows the meeting to connect
        time.sleep(60)
        
        #Set audio enter by computer
        py.click(x=714, y=310, clicks=1, interval=0.25)
        i+=1
        
        #Print Logg
        print("Lo hemos conectado la vez N°", str(i) + " de " + str(n_reconecciones) +".")
        
    if op == '1':
        time.sleep(duracion*60)
        os.system('Rundll32.exe Powrprof.dll,SetSuspendState Sleep')
        
    elif op == '2':
        time.sleep(duracion*60)
        os.system('shutdown /s')
        
    else:
        pass

def reunionNoURL():
    global duracion
    
    numero = input('Ingrese el número de reunión sin espacios ni guiones: ')
    url = "https://us04web.zoom.us/j/"+ numero
    pwd = input('Ingrese la contraseña de la reunion respetando mayúsculas y minúsculas: ')
    os.system('cls')
    n_reconecciones = input('Ingrese el número de reconecciones: ')
    
    #Gets current date
    today = dt.today()
    
    #Sets meeeting time
    hora = input('Ingrese solamente la hora de la reunión: ')
    minutos = input('Ingrese los minutos de la hora de la reunión: ')
    os.system('cls')
    
    op = False
    op2 = False
    aux2 = False
    aux = False
    
    while aux2 == False:
        print('¿Qué desea hacer hasta el horario de la clase?')
        print('1 - Suspender la computadora.')
        print('2 - No hacer nada.')
        op2 = input('Elija una opción: ')
        if op2 == '1' or op2 =='2':
            aux2 = True
    os.system('cls')
    
    while aux == False:
        print('¿Qué desea hacer una vez finalizada la clase?')
        print('1 - Suspender la computadora.')
        print('2 - Apagar la computadora.')
        print('3 - No hacer nada.')
        op = input('Elija una opción: ')
        if op == '1' or op =='2' or op == '3':
            aux = True
    if datetime.datetime.now() < datetime.datetime(2020, int(today.month), int(today.day), int(hora), int(minutos)) and op2 == '1':
        minutes = calculaMin(int(today.month), int(today.day), int(hora), int(minutos)) 
        wakeup(minutes)
    os.system('cls')
    i = 0
    
    #Sets meeting time as taget time
    for i in range(0,int(n_reconecciones)+1):
        if i == 0:
            target_time = datetime.datetime(2020, int(today.month), int(today.day), int(hora), int(minutos)) 
        else:
            target_time = target_time + timedelta(minutes=duracion)  
            
        while datetime.datetime.now() < target_time:
            os.system('cls')
            print(bordered(" "*23 + "RESUMEN DE SU CONEXIÓN:" + " "*23))
            print("")
            print("- Lo conectaremos a su clase a las " + str(hora) + ":" + str(minutos) + " hs")
            print("- Lo reconectaremos " + str(n_reconecciones) + " veces cada " + str(duracion + 1) + " minutos")
            #print("")
            
            if op == '1':
                accion = 'se suspenderá su computadora.'
            elif op == '2':
                accion = 'se apagará su computadora.'
            elif op == '3':
                accion = 'no se realizará ninguna acción.'
            
            #Print Loggs
            print("- Una vez finalizada la clase " + accion)
            print("")
            print(bordered("Todo está bajo control. Duerma tranquilo, el descanso es fundamental."))
            time.sleep(10)
            
        #Print Logg    
        print('Lo estamos conectando a su clase...')
        time.sleep(5)
        py.press('up')
        webbrowser.open(url, new=2)
        
        #Allows time for webpage to load
        time.sleep(5)
        
        #Set clicks parameter to 2
        py.press('left')
        py.press('enter')
        
        #Allows the meeting to connect
        time.sleep(5)
        
        #Writes password on the textbox
        py.write(pwd)
        
        #Clicks on enter button
        py.press('enter')
        
        #Allows the meeting to connect
        time.sleep(60)
        
        #Set audio enter by computer
        py.click(x=714, y=310, clicks=1, interval=0.25)
        i+=1
        
        #Print Logg
        print("Lo hemos conectado la vez N°", str(i) + " de " + str(n_reconecciones) +".")
        
    if op == '1':
        time.sleep(duracion*60)
        os.system('Rundll32.exe Powrprof.dll,SetSuspendState Sleep')
    elif op == '2':
        time.sleep(duracion*60)
        os.system('shutdown /s')
    else:
        pass

def menu():
    op0 = False
    while True:
        print('Bienvenido a su asistente de asistencia perfecta')
        print('1 - Reunión sin url')
        print('2 - Reunión con url')
        op0 = input('Ingrese la opción deseada: ')
        if op0 == '1':
            os.system('cls')
            reunionNoURL()
            break
        elif op0 == '2':
            os.system('cls')
            reunionURL()
            break

menu()
