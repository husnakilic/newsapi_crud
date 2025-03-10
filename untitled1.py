# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/133gCix-qq6gq27THXCiRdb-nfgwk2Ojq
"""

# OOP Projesi (Python)

# 1. Class (Sınıf Oluşturma)
class Hayvan:
    def __init__(self, isim, tur):
        self.isim = isim
        self.tur = tur

    def ses_cikar(self):
        return "Ses yok"

# 2. Inheritance (Kalıtım)
class Kopek(Hayvan):
    def __init__(self, isim, cins):
        super().__init__(isim, "Köpek")
        self.cins = cins

    def ses_cikar(self):  # 5. Method Overriding
        return "Hav hav!"

# 3. Polymorphism (Çok Biçimlilik)
class Kedi(Hayvan):
    def __init__(self, isim):
        super().__init__(isim, "Kedi")

    def ses_cikar(self):
        return "Miyav!"

# 4. Encapsulation (Kapsülleme)
class BankaHesabi:
    def __init__(self, sahip, bakiye):
        self.sahip = sahip
        self.__bakiye = bakiye  # Gizli değişken

    def para_yatir(self, miktar):
        self.__bakiye += miktar

    def bakiye_goruntule(self):
        return self.__bakiye

# 6. Abstraction (Soyutlama)
from abc import ABC, abstractmethod
class Arac(ABC):
    @abstractmethod
    def hareket_et(self):
        pass

class Araba(Arac):
    def hareket_et(self):
        return "Araba hareket ediyor"

# 7. Extra init
class Kisi:
    def __init__(self, isim, yas, cinsiyet="Belirtilmemiş"):
        self.isim = isim
        self.yas = yas
        self.cinsiyet = cinsiyet

# Örnek Kullanımlar
kopek = Kopek("Karabaş", "Labrador")
kedi = Kedi("Pamuk")
hesap = BankaHesabi("Mehmet", 2000)
araba = Araba()
kisi = Kisi("Zeynep", 30)

print(kopek.ses_cikar())  # Hav hav!
print(kedi.ses_cikar())  # Miyav!
hesap.para_yatir(1000)
print(hesap.bakiye_goruntule())  # 3000
print(araba.hareket_et())  # Araba hareket ediyor
print(f"{kisi.isim} {kisi.yas} yaşında ve cinsiyeti {kisi.cinsiyet}")