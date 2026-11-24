class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif
        self.__ijarada = False

    def ijaraga_ber(self):
        if self.__ijarada == False:
            self.__ijarada = True
            print("Kitob ijaraga berildi")
        else:
            print("Kitob allaqachon ijarada")

    def qaytarish(self):
        if self.__ijarada == True:
            self.__ijarada = False
            print("Kitob qaytarildi")
        else:
            print("Kitob ijarada emas")

    def holat(self):
        if self.__ijarada:
            print("Kitob ijarada")
        else:
            print("Kitob kutubxonada")


kitob = Kitob("O'tkan kunlar", "Abdulla Qodiriy")

kitob.ijaraga_ber()
kitob.holat()
kitob.qaytarish()
kitob.holat()