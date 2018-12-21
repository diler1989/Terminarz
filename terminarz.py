import shelve
import datetime

mydate = datetime.datetime.now()
now = mydate.strftime("%B")
days_in_month_dict = {"January": 31, "February": 28,
                      "March": 31, "April": 30,
                      "May": 31, "June": 30,
                      "July": 31, "August": 31,
                      "September": 30, "October": 31,
                      "November": 30, "December": 31}
def init():

    global baza

    try:
        baza = shelve.open('_zadan')
    except:
        print('Błąd krytyczny! Baza danych nie została otwarta!\n')
        exit(0)
    print('Inicjalizacja udana.\nBaza danych została otwarta!\n')
    tab = input('Utworzyc kalendarz? [T][N]: ')
    if tab == 'T':
        crate_data()
    elif tab == 'N':
        menu()
def crate_data():
    for day in range(1, 32):
        data = str(day)
        task = ' '
        if data not in baza.keys():
            baza[data] = task
    print ("Wprowadzono.\n")

def add_task():

    global baza, data, task

    data = input('Podaj date: ')

    if data in baza.keys():
        task = input('Jakie kolejne zadanie dodac do dnia: ')
        mem = baza[data]
        baza[data] = mem+', '+task
        print('Poprawnie dodano zadanie do dnia: ', data, now)

def delete():
    global baza
    data = input('Zadanie z jakiego dnia usunac?: ')
    if data in baza.keys():
        baza[data] = ' '

def wiev():

    global baza, data, task
    print("*" * 90)
    print ('Zadania w terminarzu'.center(90))
    print ('-'*90)
    print ('|'+'DATA'.center(40)+'|'+'ZADANIE'.center(47)+'|')
    print ('-'*90)

    for data,task in baza.items():
        print ('| '+data.center(10),now.center(28)+'|'+task.center(47)+'|')
    print ('-'*90)

def menu():
    while True:
        print('*' * 90)
        print('|'+'Terminarz'.center(90))
        print("*" * 90)
        print('|'+"[D]Dodaj zadanie   [W]Wyswietl zadania   [U]Usun zadanie   [K]Koniec".center(90))
        print("*" *90)
        db = input(">:").upper()
        if db == 'D':
            add_task()
        elif db == "W":
            wiev()
        elif db == "U":
            delete()
        elif db == "K":
            baza.close()
            print('Wylogowano z bazy.')
            exit(0)
init()
menu()
baza.close()