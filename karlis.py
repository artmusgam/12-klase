import datetime
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

    def saglabat(self):
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

produkts = Noma(Produkta_kategorija="a",Produkta_nosaukums="b",Tehniskie_raksturojumi="c",Nomas_cena_diena="15",Produkts_pieejams="jā",Nomnieks_vards="",Nomnieks_uzvards="",Nomnieks_pk="",Nomnieks_tel_numurs="",Nomas_sakuma_datums="",Nomas_beigu_datums="")
produkts.saglabat()

print(datetime.datetime.now())
