import shelve, sys, calendar

def body():
    print('*'*90)

def cal():
    body()
    print(calendar.month(2018, 12))

def init():

    body()

    global baza

    try:
        baza = shelve.open('baza_zadan')
    except:
        print ('Błąd krytyczny! Baza danych nie została otwarta!\n')
        sys.exit(0)
    print ('Inicjalizacja udana.\nBaza danych została otwarta!')

def add_task():

    body()

    global baza

    data = input('Podaj date (dd-mm-rrrr): ')[:10]

    if len(data) < 9:
        return
        print('nieprawidlowa data!')

    if data in baza.keys() or data == '' in baza.keys():
        print('Podany termin juz zostal wprowadzony!\n')
        task=input('Dodaj kolejne zadanie do dnia: ')
        mem = baza[data]
        baza[data] = mem+', '+task
    else:
        data
        task =input('Jakie zadania zapamietac: ')

    if data not in baza.keys():
        baza[data]= task
        body()
        print ("Wprowadzono.\n")

def wiev():

    global baza

    body()
    print ('Zadania w terminarzu'.center(90))
    print ('-'*90)
    print ('|'+'DATA'.center(40)+'|'+'ZADANIE'.center(47)+'|')
    print ('-'*90)

    for data,task in baza.items():
        print ('|'+data.center(40)+'|'+task.center(47)+'|')
    print ('-'*90)
    body()

def delete():
    global baza
    data = input('Zadanie z jakiego dnia usunac?: ')
    if data in baza.keys():
        del baza[data]

def menu():
    while True:
        print("*" * 90)
        print("Terminarz".center(90))
        print("*" * 90)
        print("[D]Dodaj zadanie [W]Wyswietl zadania [U]Usun zadanie [C]Kalendarz [K]Koniec".center(90))
        print("*" *90)
        db = input(">:").upper()
        if db == 'D':
            add_task()
        elif db == "W":
            wiev()
        elif db == "U":
            delete()
        elif db == "C":
            cal()
        elif db == "K":
            baza.close()
            print('Wylogowano z bazy.')
            exit(0)

init()
menu()




