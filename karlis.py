import datetime
import PySimpleGUI as psg
class Noma():
    def __init__(self,Produkta_kategorija,Produkta_nosaukums,Tehniskie_raksturojumi,Nomas_cena_diena, Produkts_pieejams,Nomnieks_vards,Nomnieks_uzvards,Nomnieks_pk,Nomnieks_tel_numurs,Nomas_sakuma_datums,Nomas_beigu_datums):
        self.Produkta_kategorija = Produkta_kategorija
        self.Produkta_nosaukums = Produkta_nosaukums
        self.Tehniskie_raksturojumi = Tehniskie_raksturojumi
        self.Nomas_cena_diena = Nomas_cena_diena
        self.Produkts_pieejams = Produkts_pieejams
        self.Nomnieks_vards = Nomnieks_vards
        self.Nomnieks_uzvards = Nomnieks_uzvards
        self.Nomnieks_pk = Nomnieks_pk
        self.Nomnieks_tel_numurs = Nomnieks_tel_numurs
        self.Nomas_sakuma_datums = Nomas_sakuma_datums
        self.Nomas_beigu_datums = Nomas_beigu_datums
    
    def izdrukat_produkts(self):
        print("Produkta kategorija:  ", self.Produkta_kategorija)
        print("Produkta nosaukums: ", self.Produkta_nosaukums)
        print("Tehniskie raksturojumi: ", self.Tehniskie_raksturojumi)
        print("Nomas cena diena: ", self.Nomas_cena_diena)
        print("Produkts pieejams: ", self.Produkts_pieejams)
    def izdrukat_nomnieks(self):
        print("Nomnieks vards: ", self.Nomnieks_vards)
        print("Nomnieks uzvards: ", self.Nomnieks_uzvards)
        print("Nomnieks p.k: ", self.Nomnieks_pk)
        print("Nomnieks tel_numurs: ", self.Nomnieks_tel_numurs)
        print("Nomas sakuma datums: ", self.Nomas_sakuma_datums)
        print("Nomas beigu datums: ", self.Nomas_beigu_datums)

    def saglabat_produktu(self):
        with open('noma_produkts.txt', 'w', encoding="utf-8") as fails :
            fails.write("-Produkts-")
            fails.write(" \n")
            fails.write(str(produkts.Produkta_kategorija))
            fails.write(" \n")
            fails.write(str(produkts.Produkta_nosaukums))
            fails.write(" \n")
            fails.write(str(produkts.Tehniskie_raksturojumi))
            fails.write(" \n")
            fails.write(str(produkts.Nomas_cena_diena))
            fails.write(" \n")
            fails.write(str(produkts.Produkts_pieejams))

    def saglabat_nomnieku(self):
        with open('noma_nomnieks.txt', 'w', encoding="utf-8") as fails :
            fails.write("-Nomnieks-")
            fails.write(" \n")
            fails.write(str(produkts.Nomnieks_vards))
            fails.write(" \n")
            fails.write(str(produkts.Nomnieks_uzvards))
            fails.write(" \n")
            fails.write(str(produkts.Nomnieks_pk))
            fails.write(" \n")
            fails.write(str(produkts.Nomnieks_tel_numurs))
            fails.write(" \n")
            fails.write(str(produkts.Nomas_sakuma_datums))
            fails.write(" \n")
            fails.write(str(produkts.Nomas_beigu_datums))

produkts = Noma(Produkta_kategorija="a",Produkta_nosaukums="b",Tehniskie_raksturojumi="c",Nomas_cena_diena="15",Produkts_pieejams="jā",Nomnieks_vards="a",Nomnieks_uzvards="vv",Nomnieks_pk="21312321",Nomnieks_tel_numurs="34543543",Nomas_sakuma_datums="324",Nomas_beigu_datums="2342")
produkts.saglabat_produktu()
produkts.saglabat_nomnieku()
produkts.izdrukat_produkts()
produkts.izdrukat_nomnieks()

print(datetime.datetime.now())

psg.theme('DarkGreen3')
logs = [
        [psg.Text('Produkts')],
        [psg.Text('Kategorija'),psg.InputText()],
        [psg.Text('Nosaukums'),psg.InputText()],
        [psg.Text('Tehniskie raksturojumi'),psg.InputText()],
        [psg.Text('Nomas cena diena'),psg.InputText()],
        [psg.Text('Produkts pieejams')],
        [psg.Radio("jā", "a", default="jā"), psg.Radio("nē", "a", default="nē")],
        [psg.Button('Saglabāt produktu')],
        [psg.Button('Produktu datu apskate')]
]
logs2 = [
    [psg.Text("Nomnieks")],
    [psg.Text('Vards'),psg.InputText()],
    [psg.Text('Uzvards'),psg.InputText()],
    [psg.Text('Personalais kods'),psg.InputText()],
    [psg.Text('Telefona numurs'),psg.InputText()],
    [psg.Text('Sakuma datums'),psg.InputText()],
    [psg.Text('Beiguma datums'),psg.InputText()],
    [psg.Button('Saglabāt kontaktu')],
    [psg.Button('Nomnieks datu apskate')]    
    
]

logugrupa = [[
    psg.TabGroup(
        [
         [
            psg.Tab('Produkts',logs),
            psg.Tab('Nomnieks',logs2)
         ]   
        ]
    ),
    psg.Button('Aizvērt')
]]
window = psg.Window('Produktu noma', logugrupa)
while True:
    event,values = window.read()
    if event == "Saglabāt produktu":
        Produkta_kategorija = values [0]
        Produkta_nosaukums = values [1]
        Tehniskie_raksturojumi = values[2]
        Nomas_cena_diena = values[3]
        Produkts_pieejams = values [4]
        produkts = Noma(Produkta_kategorija,Produkta_nosaukums,Tehniskie_raksturojumi,Nomas_cena_diena,Produkts_pieejams,Nomnieks_vards="",Nomnieks_uzvards="",Nomnieks_pk="",Nomnieks_tel_numurs="",Nomas_sakuma_datums="",Nomas_beigu_datums="")
        produkts.saglabat_produktu()
    if event == "Saglabāt kontaktu":
        Produkta_kategorija = values [6]
        Produkta_nosaukums = values [7]
        Tehniskie_raksturojumi = values[8]
        Nomas_cena_diena = values[10]
        Produkts_pieejams = values [9]
        Nomnieks_vards = values [0]
        Nomnieks_uzvards = values [1]
        Nomnieks_pk = values [2]
        Nomnieks_tel_numurs = values [3]
        Nomas_sakuma_datums = values [4]
        Nomas_beigu_datums = values [5]
        produkts = Noma(Nomnieks_vards,Nomnieks_uzvards,Nomnieks_pk,Nomnieks_tel_numurs,Nomas_sakuma_datums,Nomas_beigu_datums,Produkta_kategorija,Produkta_nosaukums,Tehniskie_raksturojumi,Nomas_cena_diena,Produkts_pieejams)
        produkts.saglabat_nomnieku()
    if event == "Produktu datu apskate":
        if produkts.Produkts_pieejams == True:
            produkts.Produkts_pieejams = "Jā"
        else:
            produkts.Produkts_pieejams = "Nē"
        psg.theme("DarkGreen4")
        layout = [
                  [psg.Text("Produkts")],
                  [psg.Text("Kategorija: " + produkts.Produkta_kategorija)],
                  [psg.Text("Nosaukums: " + produkts.Produkta_nosaukums)],
                  [psg.Text("Tehniskie raksturojumi: " + produkts.Tehniskie_raksturojumi)],
                  [psg.Text("Nomas cena diena: " + produkts.Nomas_cena_diena)],
                  [psg.Text("Produkts pieejams: " + produkts.Produkts_pieejams)],
                  [psg.Button("Iziet")]
                  ]
        window2 = psg.Window('',layout)
        event,values = window2.read()
        if event == "Iziet":
            break 
    if event == "Nomnieks datu apskate":
        if produkts.Produkts_pieejams == True:
            produkts.Produkts_pieejams = "Jā"
        else:
            produkts.Produkts_pieejams = "Nē"
        psg.theme("DarkGreen4")
        layout = [
                  [psg.Text("Nomnieks")],
                  [psg.Text("Vārds: " + produkts.Nomnieks_vards)],
                  [psg.Text("Uzvārds: " + produkts.Nomnieks_uzvards)],
                  [psg.Text("Personalais kods: " + produkts.Nomnieks_pk)],
                  [psg.Text("Tel numurs: " + produkts.Nomnieks_tel_numurs)],
                  [psg.Text("Nomas sakuma datums: " + produkts.Nomas_sakuma_datums)],
                  [psg.Text("Nomas beiguma datums: " + produkts.Nomas_beigu_datums)],
                  [psg.Button("Iziet")]
                  ]
        window2 = psg.Window('',layout)
        event,values = window2.read()
        if event == "Iziet":
            break
    if event in (psg.WIN_CLOSED,'Aizvērt'):
        break