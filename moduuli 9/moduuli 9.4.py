import random


class auto:
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
        if self.kuljettu_matka>10000:
            self.kuljettu_matka=10000

autot=[]

for i in range(10):
    rekisteritunnus=f"ABC-{123 + i}"
    huippunopeus=random.randint(100, 200)
    uusi_auto=auto(rekisteritunnus,huippunopeus)
    autot.append(uusi_auto)


def matka_testi(autot):
    for car in autot:
        if car.kuljettu_matka>=10000:
            return True
    return False


def nopeuden_muutos(autot):
    for car in autot:
        car.kiihdytä(random.randint(-10, 15))


def tunnin_ajo(autot):
    for car in autot:
        car.kulje(1)


def peli():
    while not matka_testi(autot):
        nopeuden_muutos(autot)
        tunnin_ajo(autot)


peli()
print("Kilpailu loppui!")
print(f"{'rekisteritunnus':<12} {'huippunopeus km/h':<2} {'nopeus km/h':<15} {'kuljettu matka':<20}")


for car in autot:
    print(f"{car.rekisteritunnus:<18} {car.huippunopeus:<17} "
                f"{car.tämänhetkinen_nopeus:<15} {car.kuljettu_matka:<20.2f}")

