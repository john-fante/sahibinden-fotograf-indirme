
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:36:44 2020

@author: john-fante
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import math


# Kategorik link ve ChromeDriver dizini giriş olarak kullanarak tüm ilan listesini döndüren fonksiyon.
def ilan_listesi(ana_link, driver_path):

    chromeOption = Options()
    chromeOption.add_argument("--kiosk")
    chromeOption.add_argument("--headless")

    driver = webdriver.Chrome(driver_path, options=chromeOption)

    driver.get(ana_link)
    page_source_overview = driver.page_source
    soup = BeautifulSoup(page_source_overview, 'lxml')
    notice_code = soup.find_all("a", class_="classifiedTitle")

    notice_number_find = soup.find_all("div", class_="result-text")

    for title in notice_number_find:
        a1 = title.span.text
        a2 = title.text
        a3 = "aramanızda"
        a4 = "ilan"
        try:
            notice_number = int(a2[a2.index(a3) + 11:a2.index(a4)])
        except:
            notice_number_str = a2[a2.index(a3) + 11:a2.index(a4)]
            notice_number = int(notice_number_str.replace(".", ""))

    notice_page_number = math.ceil(notice_number / 20)
    print("-" * 30)
    print(
        f"Toplam ilan sayısı:{notice_number}, toplam sayfa sayısı:{notice_page_number}")
    print("-" * 30)

    notice_pages = [ana_link]

    for i in range(notice_page_number - 1):
        notice_pages.append(ana_link + "?pagingOffset=" + str(20 * (i + 1)))

    driver.quit()

    notice_link_list = []

    for page_link in notice_pages:
        chromeOption = Options()
        chromeOption.add_argument("--kiosk")
        chromeOption.add_argument("--headless")
        driver = webdriver.Chrome(driver_path, options=chromeOption)

        ana_link = page_link
        driver.get(ana_link)
        page_source_overview = driver.page_source
        soup = BeautifulSoup(page_source_overview, 'lxml')
        notice_code = soup.find_all("a", class_="classifiedTitle")

        notice_number_find = soup.find_all("div", class_="result-text")

        for href in notice_code:
            m = "https://www.sahibinden.com" + href.get('href')
            notice_link_list.append(m)

        driver.quit()

    return notice_link_list
