class Foydalanuvchi:
    def __init__(self, ism, username, parol):
        self.ism = ism
        self.username = username
        self.__parol = parol

    def tekshir(self, parol):
        if self.__parol == parol:
            print("Parol to'g'ri")
        else:
            print("Parol noto'g'ri")

    def parolni_ozgartir(self, eski_parol, yangi_parol):
        if self.__parol == eski_parol:
            self.__parol = yangi_parol
            print("Parol o'zgartirildi")
        else:
            print("Eski parol noto'g'ri")


user1 = Foydalanuvchi("Ali", "ali_01", "abc123")
user2 = Foydalanuvchi("Vali", "vali_02", "xyz789")

user1.tekshir("abc123")
user1.parolni_ozgartir("abc123", "new456")
user1.tekshir("new456")

user2.tekshir("xyz789")