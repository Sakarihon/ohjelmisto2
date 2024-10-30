import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0,
                 kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
    def kiihdytä(self, kiihdytys):

        uusitämänhetkinen_nopeus=self.tämänhetkinen_nopeus+kiihdytys
        if uusitämänhetkinen_nopeus>self.huippunopeus:
            uusitämänhetkinen_nopeus=self.huippunopeus
        elif uusitämänhetkinen_nopeus<0:
            uusitämänhetkinen_nopeus=0
        self.tämänhetkinen_nopeus=uusitämänhetkinen_nopeus
        return
    def kulje(self, tuntimäärä):
        self.kuljettu_matka=self.kuljettu_matka+self.tämänhetkinen_nopeus*tuntimäärä

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.kapasiteetti=kapasiteetti

    def tulostatiedot(self):
        print(f"Reksiteritunnus {self.rekisteritunnus}, akkukapasiteetti {self.kapasiteetti} ja kuljettumatka {self.kuljettu_matka}km")




class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankinkoko=bensatankinkoko

    def tulostatiedot(self):
        print(f"Reksiteritunnus {self.rekisteritunnus}, bensatankinkoko {self.bensatankinkoko} ja kuljettumatka {self.kuljettu_matka}km")

autot = []



autot.append(Sähköauto("ABC-15",180,"52.5kWh"))
autot.append(Polttomoottoriauto("ACD-123",165,"32.3l"))




def nopeuden_muutos(autot):
    for car in autot:
        car.kiihdytä(random.randint(100, 200))

def tunnin_ajo(autot):
    for car in autot:
        car.kulje(3)
        car.tulostatiedot()


nopeuden_muutos(autot)
tunnin_ajo(autot)





