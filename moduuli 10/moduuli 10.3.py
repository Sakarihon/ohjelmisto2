class Talo:
    def __init__(self, alin,ylin,määrä):
        self.alin = alin
        self.ylin = ylin
        self.määrä=määrä
        self.hissit = [Hissi(alin,ylin) for _ in range(määrä)]


    def hissi_ajo(self, hissin_numero, kerros):
        if hissin_numero <= self.määrä>0:
            print(f"Hissi numero {hissin_numero} liikkuu.")
            self.hissit[hissin_numero-1].siirry_kerrokseen(kerros)
        else:
            print(f"Talossa ei ole hissiä numero {hissin_numero}")

    def palohälytys(self):
        print("Palohälytys!")
        for i in range(self.määrä):
            self.hissit[self.määrä - 1-i].siirry_kerrokseen(0)
            print("Hissi alhaalla!")


class Hissi:
    def __init__(self, alin=0, ylin=10):
        self.alin=alin
        self.ylin=ylin
        self.tämänhetkinen_kerros=alin

    def siirry_kerrokseen(self,kerros):
        if self.alin<=kerros<=self.ylin:

            while kerros<self.tämänhetkinen_kerros:
                self.kerros_alas()
            while kerros>self.tämänhetkinen_kerros:
                self.kerros_ylös()

        else:
            print("Ei ole tämmöistä kerrosta")

    def kerros_ylös(self):
        self.tämänhetkinen_kerros+=1
        print(f"1 kerros ylös. Olet kerroksessa {self.tämänhetkinen_kerros}")

    def kerros_alas(self):
        self.tämänhetkinen_kerros-=1
        print(f"1 kerros alas. Olet kerroksessa {self.tämänhetkinen_kerros}")





t=Talo(0,10,3)
h=Hissi(0, 10)
Talo.hissi_ajo(t,3,10)
Talo.hissi_ajo(t,2,4)
Talo.hissi_ajo(t,1,8)
Talo.palohälytys(t)