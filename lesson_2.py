# a=int(input('a soni'))
# b=int(input('b soni'))

import time 
 
class NavbatDasturi: 
    def init(self): 
        self.navbat = [] 
 
    def mijoz_qoshish(self, mijoz): 
        self.navbat.append(mijoz) 
 
    def navbatni_korish(self): 
        for index, mijoz in enumerate(self.navbat): 
            print(f"{index + 1}. {mijoz}") 
 
    def navbatdan_olib_tashlash(self): 
        if self.navbat: 
            yangi_mijoz = self.navbat.pop(0) 
            print(f"{yangi_mijoz} navbatdan olib tashlandi.") 
        else: 
            print("Navbat bo'sh.") 
 
# Dasturni sinab ko'rish 
navbat_dasturi = NavbatDasturi() 
navbat_dasturi.mijoz_qoshish("Ali") 
navbat_dasturi.mijoz_qoshish("Vali") 
navbat_dasturi.mijoz_qoshish("Hasan") 
navbat_dasturi.navbatni_korish() 
navbat_dasturi.navbatdan_olib_tashlash() 
navbat_dasturi.navbatni_korish()

