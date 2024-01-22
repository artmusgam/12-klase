#importē bibliotēku, kurā atbild par programmas interfeisu
import PySimpleGUI as psg
#importe bibliotēku, kurā atbild par programmas kodu savienošanu ar sql datu bāzi
import mysql.connector
#importē bibliotēku, kurā atbild par datu kriptēšanu
from cryptography.fernet import Fernet

#veidota klasē
class kinoteatris():
    #veidots konstruktors
    def __init__(self, Pircejs_vards, Pircejs_uzvards, Pircejs_tel_num, Pircejs_ID,
                 Bilete_cena, Bilete_filma, Bilete_laiks, Bilete_vieta, Bilete_num):
        #konstruktora elementam self.Pircejs_vards Piešķirta vertība Pircejs_vards
        self.Pircejs_vards = Pircejs_vards
        #konstruktora elementam self.Pircejs_uzvards Piešķirta vertība Pircejs_uzvards
        self.Pircejs_uzvards = Pircejs_uzvards
        #konstruktora elementam self.Pircejs_tel_num Piešķirta vertība Pircejs_tel_num
        self.Pircejs_tel_num = Pircejs_tel_num
        #konstruktora elementam self.Pircejs_ID Piešķirta vertība Pircejs_ID
        self.Pircejs_ID = Pircejs_ID
        #konstruktora elementam self.Bilete_cena Piešķirta vertība Bilete_cena
        self.Bilete_cena = Bilete_cena
        #konstruktora elementam self.Bilete_filma Piešķirta vertība Bilete_filma
        self.Bilete_filma = Bilete_filma
        #konstruktora elementam self.Bilete_laiks Piešķirta vertība Bilete_laiks
        self.Bilete_laiks = Bilete_laiks
        #konstruktora elementam self.Bilete_vieta Piešķirta vertība Bilete_vieta
        self.Bilete_vieta = Bilete_vieta
        #konstruktora elementam self.Bilete_num Piešķirta vertība Bilete_num
        self.Bilete_num = Bilete_num


    #veidota metode Pircejs_info pircēja datu apskatei
    def Pircejs_info(self):
        #izvada self.Pircejs_vards datus
        print("Pircēja vārds: ", self.Pircejs_vards)
        #izvada self.Pircejs_uzvards datus
        print("Pircēja uzvārds: ", self.Pircejs_uzvards)
        #izvada self.Pircejs_tel_num datus
        print("Pircēja telefona numurs: ", self.Pircejs_tel_num)
        #izvada self.Pircejs_ID datus
        print("Pircēja ID", self.Pircejs_ID)

    #veidota metode Bilete_info biļetes datu apskatei
    def Bilete_info(self):
        #izvada self.Bilete_num datus
        print("Biļetes numurs: ", self.Bilete_num)
        #izvada self.Bilete_vieta datus
        print("Biļetes vieta: ", self.Bilete_vieta)
        #izvada self.Bilete_cena datus
        print("Biļetes cena: ", self.Bilete_cena)
        #izvada self.Bilete_filma datus
        print("Biļetes filma: ", self.Bilete_filma)
        #izvada self.Bilete_laiks datus
        print("Biļetes laiks: ", self.Bilete_laiks)
    
    #viedota metode pircēja datu saglābšanai
    def Pircejs_saglabat(self):
        #atver Pircejs.txt failu un rediģē to, jā faila nav tad izveido to
        with open('Pircejs.txt', 'w', encoding="utf-8") as fails :
            #uzraksta faila Pircejs.txt vārdu -Pircējs-
            fails.write("-Pircējs-")
            #jaunas rindas izveide
            fails.write(" \n")
            #uzraksta tekstu dokumenta
            fails.write("Pircēja vārds: ")
            #uzraksta faila Pircejs.txt self.Pircejs_vards vertību
            fails.write(str(self.Pircejs_vards))
            #jaunas rindas izveide
            fails.write(" \n")
            #uzraksta tekstu dokumenta
            fails.write("Pircēja uzvārds: ")
            #uzraksta faila Pircejs.txt self.Pircejs_uzvards vertību
            fails.write(str(self.Pircejs_uzvards))
            #jaunas rindas izveide
            fails.write(" \n")
            #uzraksta tekstu dokumenta
            fails.write("Pircēja tel_numurs: ")
            #uzraksta faila Pircejs.txt self.Pircejs_tel_num vertību
            fails.write(str(self.Pircejs_tel_num))
            #jaunas rindas izveide
            fails.write(" \n")
            #uzraksta tekstu dokumenta
            fails.write("Pircēja ID: ")
            #uzraksta faila Pircejs.txt self.Pircejs_ID vertību
            fails.write(str(self.Pircejs_ID))

    #viedota metode biļetes datu saglābšanai
    def Bilete_saglabat(self):
        #atver Bilete.txt failu un rediģē to, jā faila nav tad izveido to
        with open('Bilete.txt', 'w', encoding="utf-8") as fails :
            #uzraksta tekstu dokumenta
            fails.write("-Biļete-")
            #jaunas rindas izveide
            fails.write("\n")
            #uzraksta tekstu dokumenta
            fails.write("Biļetes numurs: ")
            #uzraksta faila Bilete.txt self.Bilete_num vertību
            fails.write(str(self.Bilete_num))
            #jaunas rindas izveide
            fails.write("\n")
            #uzraksta tekstu dokumenta
            fails.write("Biļetes cena: ")
            #uzraksta faila Bilete.txt self.Bilete_cena vertību
            fails.write(str(self.Bilete_cena))
            #jaunas rindas izveide
            fails.write("\n")
            #uzraksta tekstu dokumenta
            fails.write("Biļetes filma: ")
            #uzraksta faila Bilete.txt self.Bilete_filma vertību
            fails.write(str(self.Bilete_filma))
            #jaunas rindas izveide
            fails.write("\n")
            #uzraksta tekstu dokumenta
            fails.write("Biļetes laiks: ")
            #uzraksta faila Bilete.txt self.Bilete_laiks vertību
            fails.write(str(self.Bilete_laiks))
            #jaunas rindas izveide
            fails.write("\n")
            #uzraksta tekstu dokumenta
            fails.write("Biļetes vieta: ")
            #uzraksta faila Bilete.txt self.Bilete_vieta vertību
            fails.write(str(self.Bilete_vieta))


#pieverš Dati vertību
Dati = kinoteatris(Pircejs_vards="",Pircejs_uzvards="",Pircejs_tel_num="",Pircejs_ID="",Bilete_cena="",
                   Bilete_filma="",Bilete_laiks="",Bilete_vieta="",Bilete_num="")
#saglaba pircēju informāciju
Dati.Pircejs_saglabat()
#saglaba biļetes informāciju
Dati.Bilete_saglabat()

#izvelas krāsas tēmu logiem
psg.theme('DarkGreen3')
#izveido logu
logs = [
        #izveido loga tekstu
        [psg.Text('Pircējs')],
        #izveido loga tekstu ar datu ierakstīšanas laukumu
        [psg.Text('Vārds'),psg.InputText()],
        #izveido loga tekstu ar datu ierakstīšans laukumu
        [psg.Text('Uzvārds'),psg.InputText()],
        #izveido loga tekstu ar datu ierakstīšans laukumu
        [psg.Text('Pircēja ID'),psg.InputText()], #domas par iespēju ievest ID ģēnerēšanu
        #izveido loga tekstu ar datu ierakstīšans laukumu
        [psg.Text('Telefona numurs'),psg.InputText()],
        #izveido loga tekstu ar pogu
        [psg.Button('Saglabāt datus')],
        #izveido loga tekstu ar pogu
        [psg.Button('Datu apskate')]
]
#izveido otro logiu
logs2 = [
    #izveido loga tekstu
    [psg.Text("Biļete")],
    #izveido loga tekstu ar datu ierakstīšans laukumu
    [psg.Text('Filma'),psg.InputText()],
    #izveido loga tekstu ar datu ierakstīšans laukumu
    [psg.Text('Laiks'),psg.InputText()], #iespējams būs iespēja ievadīt cita veida nākotne
    #izveido loga tekstu ar datu ierakstīšans laukumu
    [psg.Text('Vieta'),psg.InputText()],
    #izveido loga tekstu ar datu ierakstīšans laukumu
    [psg.Text('Cena'),psg.InputText()],
    #izveido loga tekstu ar datu ierakstīšans laukumu
    [psg.Text('Pircēja ID'),psg.InputText()],
    #izveido loga tekstu ar pogu
    [psg.Button('Saglabāt datus')],
    #izveido loga tekstu ar pogu
    [psg.Button('Datu apskate')]    
    
]

#izveido logu grupu
logugrupa = [[
    #veido grupu
    psg.TabGroup(
        [
         [
            #veido logu nosaukumu un atvertni
            psg.Tab('Pircējs',logs),
            #veido logu nosaukumu un atvertni
            psg.Tab('Biļete',logs2)
         ]   
        ]
    ),
    #izveido loga tekstu ar pogu
    psg.Button('Aizvērt')
]]

#piešķir window vertības
window = psg.Window('Kinoteātris', logugrupa)
#veido ciklu
while True:
    #piešķir vertības
    event,values = window.read()