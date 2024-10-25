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



class Kilpailu:
    def __init__(self,kilpailun_nimi, kisa_pituus, autot):
        self.kilpailun_nimi=kilpailun_nimi
        self.kisa_pituus=kisa_pituus
        self.autot=autot


    def tunti_kuluu(self):
        for car in self.autot:
            car.kiihdytä(random.randint(-10, 15))
            car.kulje(1)


    def tulosta_tilanne(self):
        print(f"{'rekisteritunnus':<12} {'huippunopeus km/h':<2} {'nopeus km/h':<15} {'kuljettu matka':<20}")

        for car in self.autot:
            print(f"{car.rekisteritunnus:<18} {car.huippunopeus:<17} "
                  f"{car.tämänhetkinen_nopeus:<15} {car.kuljettu_matka:<20.2f}")


    def kilpailu_ohi(self):
        for car in self.autot:
            if car.kuljettu_matka >= self.kisa_pituus:
                if car.kuljettu_matka > self.kisa_pituus:
                    car.kuljettu_matka = self.kisa_pituus
                    return True
        return False

autot=[]

for i in range(10):
    rekisteritunnus=f"ABC-{123 + i}"
    huippunopeus=random.randint(100, 200)
    uusi_auto=auto(rekisteritunnus,huippunopeus)
    autot.append(uusi_auto)

K=Kilpailu("Suuri romuralli", 8000,autot)

def peli():
    print("Tervetuloa Suureen romuralliin!")
    K.tulosta_tilanne()
    Kesto=1
    while not K.kilpailu_ohi():
        K.tunti_kuluu()
        if Kesto%10==0:
            print("10 tuntia on kulunut.")
            K.tulosta_tilanne()
        Kesto+=1


    print("Kilpailu on päättynyt!")
    K.tulosta_tilanne()


peli()
