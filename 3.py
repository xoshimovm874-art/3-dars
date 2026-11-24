class Avtomobil:
    def __init__(self, model):
        self.model = model
        self.__eshik_ochiq = False

    def eshikni_och(self):
        if self.__eshik_ochiq == False:
            self.__eshik_ochiq = True
            print("Eshik ochildi")
        else:
            print("Eshik allaqachon ochiq")

    def eshikni_yop(self):
        if self.__eshik_ochiq == True:
            self.__eshik_ochiq = False
            print("Eshik yopildi")
        else:
            print("Eshik allaqachon yopiq")

    def holat(self):
        if self.__eshik_ochiq:
            print("Eshik ochiq")
        else:
            print("Eshik yopiq")


mashina = Avtomobil("Chevrolet Cobalt")

mashina.eshikni_och()
mashina.holat()
mashina.eshikni_yop()
mashina.holat()