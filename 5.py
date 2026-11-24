from abc import ABC, abstractmethod

class Xabar(ABC):
    @abstractmethod
    def yuborish(self, matn):
        pass


class Email(Xabar):
    def yuborish(self, matn):
        print(f"Email orqali xabar yuborildi: {matn}")


class SMS(Xabar):
    def yuborish(self, matn):
        print(f"SMS orqali xabar yuborildi: {matn}")


email = Email()
sms = SMS()

email.yuborish("Salom!")
sms.yuborish("Dars boshlandi.")