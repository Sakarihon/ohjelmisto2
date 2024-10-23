class auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0,
                 kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
    def kiihdytä(self, kiihdytys):
        uusitämänhetkinen_nopeus=self.tämänhetkinen_nopeus+kiihdytys
        if uusitämänhetkinen_nopeus>140:
            uusitämänhetkinen_nopeus=140
        elif uusitämänhetkinen_nopeus<0:
            uusitämänhetkinen_nopeus=0
        self.tämänhetkinen_nopeus=uusitämänhetkinen_nopeus
        return


auto1=auto("ABC-123", 142)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f"auto1 ominaisuudet: rekisteritunnus on {auto1.rekisteritunnus},"
      f" huippunopeus {auto1.huippunopeus}km/h, tämänhetkinen nopeus {auto1.tämänhetkinen_nopeus}km/h"
      f" ja kuljettu matka {auto1.kuljettu_matka}km")
auto1.kiihdytä(-200)
print(f"auto1 ominaisuudet: rekisteritunnus on {auto1.rekisteritunnus},"
      f" huippunopeus {auto1.huippunopeus}km/h, tämänhetkinen nopeus {auto1.tämänhetkinen_nopeus}km/h"
      f" ja kuljettu matka {auto1.kuljettu_matka}km")