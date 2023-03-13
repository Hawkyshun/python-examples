import csv
from datetime import datetime

# Menu.txt dosyasını oluşturma
with open('Menu.txt', 'w') as file:
    file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n"
               "1: Klasik\n"
               "2: Margarita\n"
               "3: TürkPizza\n"
               "4: Sade Pizza\n"
               "* ve seçeceğiniz sos:\n"
               "11: Zeytin\n"
               "12: Mantarlar\n"
               "13: Keçi Peyniri\n"
               "14: Et\n"
               "15: Soğan\n"
               "16: Mısır\n"
               "* Teşekkür ederiz!")

# Pizza sınıfı oluşturma


class Pizza:
    def __init__(self):
        self.description = "Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Alt sınıf olarak pizza çeşitlerini oluşturma
class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Klasik pizza"
        self._cost = 10.0

    def get_cost(self):
        return self._cost


class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Margarita pizza"
        self._cost = 12.0

    def get_cost(self):
        return self._cost


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Türk pizzası"
        self._cost = 15.0

    def get_cost(self):
        return self._cost


class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Sade pizza"
        self._cost = 8.0

    def get_cost(self):
        return self._cost


# Decorator sınıfını oluşturma
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            ' ' + Pizza.get_description(self)
            

# Pizza soslarını oluşturma


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Zeytin"
        self._cost = 1.5


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Mantar"
        self._cost = 2.0


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Keçi peyniri"
        self._cost = 3.0


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Et"
        self._cost = 4.0


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Soğan"
        self._cost = 1.0


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Mısır"
        self._cost = 1.0


def main():
    # Menüyü ekrana yazdırma
    with open('Menu.txt', 'r') as file:
        menu = file.read()
        print(menu)

    # Pizza seçimini isteme
    pizza_choice = input("Lütfen bir pizza seçin (1-4): ")
    while pizza_choice not in ['1', '2', '3', '4']:
        pizza_choice = input("Geçersiz seçim. Lütfen bir pizza seçin (1-4): ")

    # Seçilen pizza türüne göre nesne oluşturma
    if pizza_choice == '1':
        pizza = Klasik()
    elif pizza_choice == '2':
        pizza = Margarita()
    elif pizza_choice == '3':
        pizza = TurkPizza()
    else:
        pizza = SadePizza()

    # Sos seçimini isteme
    sos_choice = input("Lütfen bir sos seçin (11-16): ")
    while sos_choice not in ['11', '12', '13', '14', '15', '16']:
        sos_choice = input("Geçersiz seçim. Lütfen bir sos seçin (11-16): ")

    # Seçilen sos türüne göre nesne oluşturma
    if sos_choice == '11':
        pizza = Zeytin(pizza)
    elif sos_choice == '12':
        pizza = Mantar(pizza)
    elif sos_choice == '13':
        pizza = KeciPeyniri(pizza)
    elif sos_choice == '14':
        pizza = Et(pizza)
    elif sos_choice == '15':
        pizza = Sogan(pizza)
    else:
        pizza = Misir(pizza)

    # Toplam fiyatı hesaplama ve ekrana yazdırma
    total_cost = pizza.get_cost()
    print("Toplam tutar: {:.2f} TL".format(total_cost))

    # Sipariş bilgilerini isteme
    name = input("İsim: ")
    tc = input("TC Kimlik Numarası: ")
    cc_num = input("Kredi Kartı Numarası: ")
    cc_cvv = input("Kredi Kartı Şifresi: ")

    # Sipariş zamanını kaydetme
    order_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Veritabanına sipariş bilgilerini yazma
    with open('Orders_Database.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pizza.get_description(), name, tc, cc_num, "Pizza ve {} soslu pizza".format(
            pizza.get_description()), order_time, cc_cvv])


if __name__ == '__main__':
    main()
