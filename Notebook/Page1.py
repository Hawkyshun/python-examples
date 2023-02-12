#Python - Class
class Hub():
    print("This is a Hub")

#Class Attributes
class Data():
    part = ''
    sql = 'yes'
    exp_year = 0
    langs = []
    
Data.part
print(Data.sql)

#Change Attributes
Data.sql = 'no'
print(Data.sql)

#Instantiation
John = Data()
print(John.exp_year)
John.langs.append("Python")
print(John.langs)

Ken = Data()
print(Ken.langs)

class Data():
    langs = ["Python", "C#"]
    part = ''
    sql = 'yes'
    exp_year = 0
    def __init__(self):
        self.langs = []

John = Data()
print(John.langs)

Ken = Data()
print(Ken.langs)

John.langs.append("Python")
Ken.langs.append("C#")

print(John.langs)
print(Ken.langs)

print(Data.langs)
print(John.part)

print(Data.part)
John.part = "Statistics"
print(Data.part)
print(Ken.part)
Ken.part = "Computer"
print(Ken.part)
print(John.part)

class VeriBilimci():
    calisanlar = []
    bildigi_diller = []
    bolum = []
    def _init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()
print("ali.bildigi_diller", ali.bildigi_diller)
print(ali.bolum)

veli = VeriBilimci()
print("veli.bildigi_diller", veli.bildigi_diller)
print(veli.bolum)

dir(VeriBilimci)

VeriBilimci.dil_ekle

ali.dil_ekle("C#")
print("ali.bildigi_diller", ali.bildigi_diller)

#Inheritance

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

person1 = DataScience()
person1.FirstName = "John"

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()

class Employee_new():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
person2 = Employee_new("Ken", "Doe", "c")
print(person2.FirstName)

