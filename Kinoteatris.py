#importē bibliotēku, kurā atbild par programmas interfeisu
import PySimpleGUI as psg
#importe bibliotēku, kurā atbild par programmas kodu savienošanu ar sql datu bāzi
import mysql.connector
#importē bibliotēku, kurā atbild par datu kriptēšanu
from cryptography.fernet import Fernet

#pieškir vertības izveido savienojumu ar datu bāzi
db = mysql.connector.connect(host= "localhost", database = "kinoteatris", user = "root", password = "admin")
#izvada metodi
print(db)
#piešķir vertības
cursor = db.cursor()

#piešķir vertību
karta_1 = 1
#piešķir vertību
karta_2 = 1

#piešķir vertību
atslega = Fernet.generate_key()
#izvada atslegu
print(atslega)
#piešķir vertību
a = Fernet(atslega)
#piešķir vertību
teksts = b'slepeni dati'
#piešķir vertību kriptēšanai
kriptDati = a.encrypt(teksts)
#izvada kriptetos datus
print(kriptDati)
#izvada atšīfrētos datus
print(a.decrypt(kriptDati))

#veidota klasē
class kinoteatris():
    #veidots konstruktors
    def __init__(self, Pircejs_vards, Pircejs_uzvards, Pircejs_tel_num,
                 Bilete_cena, Bilete_filma, Bilete_laiks, Bilete_vieta, Bilete_num):
        #konstruktora elementam self.Pircejs_vards Piešķirta vertība Pircejs_vards
        self.Pircejs_vards = Pircejs_vards
        #konstruktora elementam self.Pircejs_uzvards Piešķirta vertība Pircejs_uzvards
        self.Pircejs_uzvards = Pircejs_uzvards
        #konstruktora elementam self.Pircejs_tel_num Piešķirta vertība Pircejs_tel_num
        self.Pircejs_tel_num = Pircejs_tel_num
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
        #piešķir vertības savienojumam
        self.db = mysql.connector.connect(host= "localhost", database = "kinoteatris", user = "root", password = "admin")
        #piešķir vertības
        self.cursor = self.db.cursor()




    #veidota metode Pircejs_info pircēja datu apskatei
    def Pircejs_info(self):
        #izvada self.Pircejs_vards datus
        print("Pircēja vārds: ", (self.Pircejs_vards))
        #izvada self.Pircejs_uzvards datus
        print("Pircēja uzvārds: ", (self.Pircejs_uzvards))
        #izvada self.Pircejs_tel_num datus
        print("Pircēja telefona numurs: ", (self.Pircejs_tel_num))

    #veidota metode Bilete_info biļetes datu apskatei
    def Bilete_info(self):
        #izvada self.Bilete_num datus
        print("Biļetes numurs: ", (self.Bilete_num))
        #izvada self.Bilete_vieta datus
        print("Biļetes vieta: ", (self.Bilete_vieta))
        #izvada self.Bilete_cena datus
        print("Biļetes cena: ", (self.Bilete_cena))
        #izvada self.Bilete_filma datus
        print("Biļetes filma: ", (self.Bilete_filma))
        #izvada self.Bilete_laiks datus
        print("Biļetes laiks: ", (self.Bilete_laiks))
    
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

    #veidota metode biļetes datu saglābšanai
    def Bilete_saglabat(self):
        #atver Bilete.txt failu un rediģē to, jā faila nav tad izveido to
        with open('Bilete.txt', 'w', encoding="utf-8") as fails :
            self.Bilete_num = karta_1
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

    #veidota pircejam metode datu saglābšanai datu bāze
    def g_p(self):
        #veido karta_2 par globālo elementu
        global karta_2
        #piešķir vertību konnektoru datu bāzei
        db = mysql.connector.connect(host= "localhost", database = "kinoteatris", user = "root", password = "admin")
        #piešķir vertību
        cursor = db.cursor()
        #piešķir vertību uzradot uz datu saglābšanus vietu un principu
        sql = ("""
        insert into pircejs (idPircejs, Vards, Uzvards, Tel_num)
        values (%s,%s,%s,%s);
            """)
        #Veicina darbību ar datiem datu bāze
        self.cursor.execute("SELECT * FROM kinoteatris.pircejs")
        #piešķir vertības
        data = (karta_2,Dati.Pircejs_vards,Dati.Pircejs_uzvards,Dati.Pircejs_tel_num)
        #veicina nepieciešamas iepriekš definētas darbības
        cursor.execute(sql,data)
        #ievada apstiprina datu saglābšanu
        db.commit()
        #aizver datubāzi
        db.close()
        #piešķir vertības
        karta_2 = karta_2 + 1

    #veidota biļetei metode datubāze datus saglābšanai
    def g_b(self):
        #veido karta_1 par globālo elementu
        global karta_1
        #piešķir vertību savienojumam ar datubāzi
        db = mysql.connector.connect(host= "localhost", database = "kinoteatris", user = "root", password = "admin")
        #piešķir vertību
        cursor = db.cursor()
        #piešķir vertību ar saglābšanas vietu un metodi
        sql = ("""
        insert into bilete (idBilete, Cena, Filma, Vieta, Laiks, Numurs)
        values (%s,%s,%s,%s,%s,%s);
            """)
        #veicina darbībus ar datiem datubāze
        self.cursor.execute("SELECT * FROM kinoteatris.bilete")
        #piešķir vertības
        data = (karta_1,Dati.Bilete_cena,Dati.Bilete_filma,Dati.Bilete_vieta,Dati.Bilete_laiks,Dati.Bilete_num)
        #veicina darbības ar metodem
        cursor.execute(sql,data)
        #saglabā apstiprina izmaiņas
        db.commit()
        #aizver datu bāzi
        db.close()
        #piešķir vertības
        karta_1 = karta_1 + 1

#pieverš Dati vertību
Dati = kinoteatris(Pircejs_vards="",Pircejs_uzvards="",Pircejs_tel_num="",Bilete_cena="",
                   Bilete_filma="",Bilete_laiks="",Bilete_vieta="",Bilete_num="")
#saglaba pircēju informāciju
Dati.Pircejs_saglabat()
#saglaba biļetes informāciju
Dati.Bilete_saglabat()
#piešķir vertības
karta_2 = 1
#piešķir vertības
karta_1 = 1



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
        [psg.Text('Telefona numurs'),psg.InputText()],
        #izveido loga tekstu ar pogu
        [psg.Button('Saglabāt pircēja datus')],
        #izveido loga tekstu ar pogu
        [psg.Button('Datu apskate pircējam')]
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
    #izveido loga tekstu ar pogu
    [psg.Button('Saglabāt biļetes datus')],
    #izveido loga tekstu ar pogu
    [psg.Button('Datu apskate biļetei')]    
    
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
]]

#piešķir window vertības
window = psg.Window('Kinoteātris', logugrupa)
#veido ciklu
while True:
    #piešķir vertības
    event,values = window.read()
    #izveido iesacījumu
    if event == "Saglabāt pircēja datus":
        #piešķir vertību
        Pircejs_vards = a.encrypt(bytes(values [0], 'UTF-8'))
        #piešķir vertību
        Pircejs_uzvards = a.encrypt(bytes(values [1],'UTF-8'))
        #piešķir vertību
        Pircejs_tel_num = a.encrypt(bytes(values [2], 'UTF-8'))
        #piešķir vertību
        Dati = kinoteatris(Pircejs_vards,Pircejs_uzvards,Pircejs_tel_num,
                           Bilete_cena="",Bilete_filma="",Bilete_laiks="",Bilete_num="",Bilete_vieta="")
        #Saglabā pircēja datus
        Dati.Pircejs_saglabat()
        #izsauc funkciju
        Dati.g_p()

    #izveido iesacījumu
    if event == "Saglabāt biļetes datus":
        #piešķir vertību
        Pircejs_vards =  a.encrypt(bytes(values [5], 'UTF-8'))
        #piešķir vertību
        Pircejs_uzvards = a.encrypt(bytes(values [6], 'UTF-8'))
        #piešķir vertību
        Pircejs_tel_num = a.encrypt(bytes(values [7], 'UTF-8'))
        #piešķir vertību
        Bilete_cena = a.encrypt(bytes(values [0], 'UTF-8'))
        #piešķir vertību
        Bilete_filma = a.encrypt(bytes(values [1], 'UTF-8'))
        #piešķir vertību
        Bilete_laiks = a.encrypt(bytes(values [2], 'UTF-8'))
        #piešķir vertību
        Bilete_vieta = a.encrypt(bytes(values [3], 'UTF-8'))
        #piešķir vertību
        Bilete_num = a.encrypt(bytes(values [4], 'UTF-8'))
        #piešķir vertību
        Dati = kinoteatris(Bilete_cena,Bilete_filma,Bilete_laiks,Bilete_vieta,Bilete_num,
                           Pircejs_vards,Pircejs_uzvards,Pircejs_tel_num)
        #saglaba biļetes datus
        Dati.Bilete_saglabat()
        #izsauc funkciju
        Dati.g_b()
    
    #izveido iesacījumu
    if event == "Datu apskate pircējam":
        #izveido pop up logu ar tekstu
        psg.popup('Vārds: '+ str(a.decrypt(Dati.Pircejs_vards)),"Uzvārds: " + str(a.decrypt(Dati.Pircejs_uzvards)),
                  "ID: " + str(karta_2), "Tel_num: " + str(a.decrypt(Dati.Pircejs_tel_num)),
                    title= 'Pircēju dati')
    #izveido iesacījumu
    if event == "Datu apskate biļetei":
        #izveido pop up logu ar tekstu
        psg.popup("Numurs: " + str(Dati.Bilete_num), "Cena: " + str(a.decrypt(Dati.Bilete_cena)),
                   "Filma: " + str(a.decrypt(Dati.Bilete_filma)), "Laiks: " + str(a.decrypt(Dati.Bilete_laiks)),
                    "Vieta: " + str(a.decrypt(Dati.Bilete_vieta)), title= 'Biļetes dati')
    #izveido iesacījumu
    if event in (psg.WIN_CLOSED, 'Aizvērt'):
        #pārtrauc darbību
        break