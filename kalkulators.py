import datetime
import json

def kont_add():

    while True:
        vardss = input('ievadiet vardu un uzvardu: ')
        if vardss.isdigit() == False:
            if vardss.strip() == '':
                print('ievadiet atkartoti')
                continue
            else:
                break
        else:
            print('ievadiet atkartoti')
            continue
kont_add()

answer = int(input("izvelies darbibu: \n1.saskaitīt \n2.atņemt \n3.reizināt \n4.dalīt \n5.iziet un saglabāt \n"))
while answer != 5:
    answer = int(input("izvelies darbibu: \n1.saskaitīt \n2.atņemt \n3.reizināt \n4.dalīt \n5.iziet un saglabāt \n"))
    pirmais = int(input("ievadi pirmo skaitli "))
    otrais = int(input("ievadi otro skaitli "))
    if answer == 1:
        rezultats = pirmais + otrais
        print("Rezultāts: ", rezultats)
    elif answer == 2:
        rezultats = pirmais - otrais
        print("Rezultāts: ", rezultats)
    elif answer == 3:
        rezultats = pirmais * otrais
        print("Rezultāts: ", rezultats)
    elif answer == 4:
        rezultats = pirmais / otrais
        print("Rezultāts: ", rezultats)
print("Lietotājs ir veiksmīgi pievienots \nPaldies par programmas izmantošanu!")