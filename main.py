
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:49:03 2020

@author: john-fante
"""

# İşlevsel dosyalar aynı dizinde olduğuna emin olun
from notice_list import ilan_listesi
from ilan_goruntu_indirme import ilan_goruntu_indirme


driver_path = 'ChromeDriver dizinini yazınız.'

download_link = "Sahibinden kategori linki örneğin https://www.sahibinden.com/audi-a7-2.0-tfsi"

# Çıktı olarak ilanlar adında bir liste öğesi döndürür.
ilanlar = ilan_listesi(download_link, driver_path)
print(ilanlar)

# ilanlar objesininden tek tek görüntülerin aynı dizine indirilmesi.
for i in range(len(ilanlar)):
    ilan_goruntu_indirme(ilanlar[i], driver_path)
