class Julkaisu:
    def __init__(self,nimi,):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulostus(self):
        print(f"Kirjan nimi {self.nimi}, kirjoittaja {self.kirjoittaja} ja sivumäärä {self.sivumäärä}")


class Lehti(Julkaisu):
    def __init__(self,nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja=päätoimittaja

    def tulostus(self):
        print(f"Lehden nimi {self.nimi} ja päätoimittaja {self.päätoimittaja}.")


Julkaisut=[]
Julkaisut.append(Kirja("Hytti no:6","Rosa Liksom","200"))
Julkaisut.append(Lehti("Aku Ankka","Aki Hyyppä"))

for j in Julkaisut:
    j.tulostus()
