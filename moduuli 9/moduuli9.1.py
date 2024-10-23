class auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
auto1=auto("ABC-123", 142)
print(f"auto1 ominaisuudet: rekisteritunnus on {auto1.rekisteritunnus},"
      f" huippunopeus {auto1.huippunopeus}km/h, tämänhetkinen nopeus {auto1.tämänhetkinen_nopeus}km/h"
      f" ja kuljettu matka {auto1.kuljettu_matka}km")
