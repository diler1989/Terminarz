import shelve
import os
import datetime

mydate = datetime.datetime.now()
now = mydate.strftime("%B")
days_in_month_dict = {"January": 31, "February": 28,
                      "March": 31, "April": 30,
                      "May": 31, "June": 30,
                      "July": 31, "August": 31,
                      "September": 30, "October": 31,
                      "November": 30, "December": 31}
monts = ["January", "February", "March",  "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def init():

    global baza
    print('*' * 90)
    print('|'+'Terminarz'.center(90))
    print('*' * 90)
    print('|'+'Miesiące do wyboru'.center(90))
    print("*" * 90)
    print('|'+"[0]January [1]February [2]March [3]April [4]May [5]June\n|[6]July [7]August [8]September [9]October [10]November [11]December".center(90))
    print("*" *90)
    try:
        tab = input('Jaki miesiąc wybrać:')
        x = monts[int(tab)]
        baza = shelve.open(x)
    except:
        print('Błąd krytyczny! Baza danych nie została otwarta!\n')
        exit(0)
    print('\nInicjalizacja udana.\nBaza danych została otwarta!\n')
    crate_data(int(tab))
    menu(int(tab))
def crate_data(x):
    d = monts[x]
    m = days_in_month_dict[d]
    m = int(m) +1
    for day in range(1, m):
        data = str(day)
        task = ' '
        if data not in baza.keys():
            baza[data] = task
    print ("Wprowadzono.\n")
    os.system("sleep 1 && clear")

def mieciace(tab):
    m = days_in_month_dict[monts[tab]]
    m = int(m) +1
    print ("Miesiąc:", monts[tab])
    for d in range(1, m ):
        data = str(d)
        if data in baza.keys() and baza[data] == ' ':
            print ('[',d,']')
        else:
            print ('[',d,']*')
    print ('* - zaplanowane zadanie')
def add_task():

    global baza, data, task

    data = input('Podaj date: ')

    if data in baza.keys() and baza[data] != ' ':
        task = input('Jakie kolejne zadanie dodac do dnia: ')
        mem = baza[data]
        baza[data] = mem+', '+task
        print('Poprawnie dodano zadanie do dnia: ', data)
    else:
        task = input('Jakie zadanie dodac do dnia: ')
        baza[data] = task
        print('Poprawnie dodano zadanie do dnia: ', data)

def delete():
    global baza
    data = input('Zadanie z jakiego dnia usunac?: ')
    if data in baza.keys():
        baza[data] = ' '

def wiev(tab):
    global baza, data, task
    print("*" * 90)
    print ('Zadania w terminarzu'.center(90))
    print ('-'*90)
    print ('|'+'DATA'.center(40)+'|'+'ZADANIE'.center(47)+'|')
    print ('-'*90)
    for data,task in baza.items():
        if data in baza.keys() and baza[data] != ' ' and data != 'January':
            print ('| ',data.center(10), monts[tab].center(15), task.center(37))
    print ('-'*90)

def menu(tab):
    while True:
        print('*' * 90)
        print('|'+'Terminarz'.center(90))
        print("*" * 90)
        print('|'+"[D]odaj zadanie  [W]yświetl zadania  [U]suń zadanie  [M]iesiąc  [K]oniec".center(90))
        print("*" *90)
        db = input(">:").upper()
        if db == 'D':
            add_task()
        elif db == "W":
            wiev(tab)
        elif db == "U":
            delete()
        elif db == "M":
            mieciace(tab)
        elif db == "K":
            step = input("Zmienić [M]iesiac, Zamknać baz[Z]e?: ").upper()
            if step == "M":
                init()
            else:
                baza.close()
                os.system("clear")
                print('Wylogowano z bazy.')
                exit(0)
init()
