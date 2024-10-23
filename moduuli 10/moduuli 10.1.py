class Hissi:
    def __init__(self, alin=0, ylin):
        self.alin=alin
        self.ylin=ylin
    def siirry_kerrokseen(self,kerros, tämänhetkinen_kerros=0):
        while kerros<tämänhetkinen_kerros:
            kerros_alas()
        while kerros>tämänhetkinen_kerros:
            kerros_ylös()
        else:
            tämänhetkinen_kerros=kerros


    def kerros_ylös(ylös):
        uusi_kerros=kerros+1
        kerros=uusi_kerros


    def kerros_alas():
        uusi_kerros = kerros - 1
        kerros = uusi_kerros


h=Hissi(0, 10)
h.siirry_kerrokseen(5)