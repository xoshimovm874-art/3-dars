from abc import ABC, abstractmethod

class Hayvon(ABC):
    @abstractmethod
    def ovoz_chiqar(self):
        pass


class It(Hayvon):
    def ovoz_chiqar(self):
        print("It: Vov-vov!")


class Mushuk(Hayvon):
    def ovoz_chiqar(self):
        print("Mushuk: Miyov!")


it = It()
mushuk = Mushuk()

it.ovoz_chiqar()
mushuk.ovoz_chiqar()