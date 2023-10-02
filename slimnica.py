#importējam bibliotēku
import PySimpleGUI as psg

#veidota klasē
class Slimnica():
    #veidots konstruktors
    def __init__(self,Pacients_vards,Pacients_uzvards,Pacients_pk,Pacients_tel_numurs,Pacients_nozare,Dakteris_vards,Dakteris_uzvards,Dakteris_tel_numurs,Dakteris_nozare):
            self.Pacients_vards = Pacients_vards
            self.Pacients_uzvards = Pacients_uzvards
            self.Pacients_pk = Pacients_pk
            self.Pacients_tel_numurs = Pacients_tel_numurs
            self.Pacients_nozare = Pacients_nozare
            self.Dakteris_vards = Dakteris_vards
            self.Dakteris_uzvards = Dakteris_uzvards
            self.Dakteris_tel_numurs = Dakteris_tel_numurs
            self.Dakteris_nozare = Dakteris_nozare
    #veidotas metodes datu apskātei pacientam un dakterim
    def Pacients_info(self):
        print("Pacienta vārds: ", self.Pacients_vards)
        print("Pacienta uzvārds: ", self.Pacients_uzvards)
        print("Pacienta p.k.: ", self.Pacients_pk)
        print("Pacienta tel numurs: ", self.Pacients_tel_numurs)
        print("Pacienta nozare: ", self.Pacients_nozare)
    def Dakteris_info(self):
        print("Daktera vārds: ", self.Dakteris_vards)
        print("Daktera uzvārds: ", self.Dakteris_uzvards)
        print("Daktera tel numurs: ", self.Dakteris_tel_numurs)
        print("Daktera nozare: ", self.Dakteris_nozare)

    #veidotas metodes datu saglābšanai pacientam un dakterim

    def Pacients_saglabat(self):
        with open('Pacients.txt', 'w', encoding="utf-8") as fails :
            fails.write("-Pacients-")
            fails.write(" \n")
            fails.write(str(Dati.Pacients_vards))
            fails.write(" \n")
            fails.write(str(Dati.Pacients_uzvards))
            fails.write(" \n")
            fails.write(str(Dati.Pacients_pk))
            fails.write(" \n")
            fails.write(str(Dati.Pacients_tel_numurs))
            fails.write(" \n")
            fails.write(str(Dati.Pacients_nozare))

    def Dakteris_saglabat(self):
        with open('Dakteris.txt', 'w', encoding="utf-8") as fails :
            fails.write("-Dakteris-")
            fails.write(" \n")
            fails.write(str(Dati.Dakteris_vards))
            fails.write(" \n")
            fails.write(str(Dati.Dakteris_uzvards))
            fails.write(" \n")
            fails.write(str(Dati.Dakteris_tel_numurs))
            fails.write(" \n")
            fails.write(str(Dati.Dakteris_nozare))

Dati = Slimnica(Pacients_vards="a",Pacients_uzvards="b",Pacients_pk="c",Pacients_tel_numurs="d",Pacients_nozare="e",Dakteris_vards="f",Dakteris_uzvards="g",Dakteris_tel_numurs="h",Dakteris_nozare="i")
Dati.Pacients_saglabat()
Dati.Dakteris_saglabat()
Dati.Pacients_info()
Dati.Dakteris_info()

psg.theme('DarkGreen3')
logs = [
        [psg.Text('Pacients')],
        [psg.Text('Vārds'),psg.InputText()],
        [psg.Text('Uzvārds'),psg.InputText()],
        [psg.Text('Personas kods'),psg.InputText()],
        [psg.Text('Telefona numurs'),psg.InputText()],
        [psg.Text('Nozare'),psg.InputText()],
        [psg.Button('Saglabāt pacienta datus')],
        [psg.Button('Pacienta datu apskate')]
]
logs2 = [
    [psg.Text("Dakteris")],
    [psg.Text('Vārds'),psg.InputText()],
    [psg.Text('Uzvārds'),psg.InputText()],
    [psg.Text('Telefona numurs'),psg.InputText()],
    [psg.Text('Nozare'),psg.InputText()],
    [psg.Button('Saglabāt daktera datus')],
    [psg.Button('Daktera datu apskate')]    
    
]

logugrupa = [[
    psg.TabGroup(
        [
         [
            psg.Tab('Pacients',logs),
            psg.Tab('Dakteris',logs2)
         ]   
        ]
    ),
    psg.Button('Aizvērt')
]]
window = psg.Window('Slimnīca', logugrupa)
while True:
    event,values = window.read()
    if event == "Saglabāt pacienta datus":
        Pacients_vards = values [0]
        Pacients_uzvards = values [1]
        Pacients_pk = values [2]
        Pacients_tel_numurs = values [3]
        Pacients_nozare = values[4]
        Dati = Slimnica(Pacients_vards,Pacients_uzvards,Pacients_pk,Pacients_tel_numurs,Pacients_nozare,Dakteris_vards="",Dakteris_uzvards="",Dakteris_tel_numurs="",Dakteris_nozare="")
        Dati.Pacients_saglabat()
    if event == "Saglabāt daktera datus":
        Pacients_vards = values [4]
        Pacients_uzvards = values [5]
        Pacients_pk = values [6]
        Pacients_tel_numurs = values [7]
        Pacients_nozare = values[8]
        Dakteris_vards = values [0]
        Dakteris_uzvards = values [1]
        Dakteris_tel_numurs = values [2]
        Dakteris_nozare = values [3]
        Dati = Slimnica(Dakteris_vards,Dakteris_uzvards,Dakteris_tel_numurs,Dakteris_nozare,Pacients_vards,Pacients_uzvards,Pacients_pk,Pacients_tel_numurs,Pacients_nozare)
        Dati.Dakteris_saglabat()
    if event == "Pacienta datu apskate":
        psg.theme("DarkGreen4")
        layout = [
                  [psg.Text("Pacients")],
                  [psg.Text("Vārds: " + Dati.Pacients_vards)],
                  [psg.Text("Uzvārds: " + Dati.Pacients_uzvards)],
                  [psg.Text("Personalais kods: " + Dati.Pacients_pk)],
                  [psg.Text("Telefona numurs: " + Dati.Pacients_tel_numurs)],
                  [psg.Text("Nozare: " + Dati.Pacients_nozare)],
                  [psg.Button("Iziet")]
                  ]
        window2 = psg.Window('',layout)
        event,values = window2.read()
        if event == "Iziet":
            break 
    if event == "Daktera datu apskate":
        psg.theme("DarkGreen4")
        layout = [
                  [psg.Text("Dakteris")],
                  [psg.Text("Vārds: " + Dati.Dakteris_vards)],
                  [psg.Text("Uzvārds: " + Dati.Dakteris_uzvards)],
                  [psg.Text("Telefona numurs: " + Dati.Dakteris_tel_numurs)],
                  [psg.Text("Nozare: " + Dati.Dakteris_nozare)],
                  [psg.Button("Iziet")]
                  ]
        window2 = psg.Window('',layout)
        event,values = window2.read()
        if event == "Iziet":
            break
    if event in (psg.WIN_CLOSED,'Aizvērt'):
        break