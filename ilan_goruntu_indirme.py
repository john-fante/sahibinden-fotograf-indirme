# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:57:57 2020

@author: john-fante
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request

# Kategorik link ve ChromeDriver dizini giriş olarak kullanarak tüm ilanda bulunan
# tüm fotoğrafları indiren fonksiyon.


def ilan_goruntu_indirme(link, driver_path):

    chromeOption = Options()
    chromeOption.add_argument("--kiosk")
    chromeOption.add_argument("--headless")

    driver = webdriver.Chrome(driver_path, options=chromeOption)
    driver.get(link)
    page_source_overview = driver.page_source
    soup = BeautifulSoup(page_source_overview, 'lxml')

    notice_number_find = soup.find_all("span", class_="classifiedId")

    for value in notice_number_find:
        notice_id = value.text

    img = driver.find_elements_by_tag_name('img')

    img_list = []

    for link in img:
        img_list.append(link.get_attribute('src'))

    final_img_list = []

    for m in range(len(img_list)):
        try:
            img_list[m].index("thmb")
            final_img_list.append(img_list[m])
        except ValueError:
            pass

    final_img_list2 = final_img_list[:int(len(final_img_list) / 2)]

    final_img_list3 = []

    for mm in range(len(final_img_list2)):
        final_img_list3.append(final_img_list2[mm].replace("thmb", "x5"))

    driver.quit()

    print("-" * 30)
    print(f"{notice_id} numaralı ilan görselleri indiriliyor...")
    for img in range(len(final_img_list3)):
        img_name = notice_id + "_" + str(img) + ".jpg"
        urllib.request.urlretrieve(final_img_list3[img], img_name)
