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
    if answer == 1:
        pirmais = int(input("ievadi pirmo skaitli "))
        otrais = int(input("ievadi otro skaitli "))
        rezultats = pirmais + otrais
        print("Rezultāts: ", rezultats)
        answer = int(input("izvelies darbibu: \n1.saskaitīt \n2.atņemt \n3.reizināt \n4.dalīt \n5.iziet un saglabāt \n"))
    elif answer == 2:
        pirmais = int(input("ievadi pirmo skaitli "))
        otrais = int(input("ievadi otro skaitli "))
        rezultats = pirmais - otrais
        print("Rezultāts: ", rezultats)
        answer = int(input("izvelies darbibu: \n1.saskaitīt \n2.atņemt \n3.reizināt \n4.dalīt \n5.iziet un saglabāt \n"))
    elif answer == 3:
        pirmais = int(input("ievadi pirmo skaitli "))
        otrais = int(input("ievadi otro skaitli "))
        rezultats = pirmais * otrais
        print("Rezultāts: ", rezultats)
        answer = int(input("izvelies darbibu: \n1.saskaitīt \n2.atņemt \n3.reizināt \n4.dalīt \n5.iziet un saglabāt \n"))
    elif answer == 4:
        pirmais = int(input("ievadi pirmo skaitli "))
        otrais = int(input("ievadi otro skaitli "))
        rezultats = pirmais / otrais
        print("Rezultāts: ", rezultats)
        answer = int(input("izvelies darbibu: \n1.saskaitīt \n2.atņemt \n3.reizināt \n4.dalīt \n5.iziet un saglabāt \n"))
print("Lietotājs ir veiksmīgi pievienots \nPaldies par programmas izmantošanu!")