from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import re
import pandas as pd
import json
import math 



options = webdriver.FirefoxOptions()
# options.headless = True
driver = webdriver.Firefox(options=options)

site = "https://www.ensonhaber.com";spor = "/spor";ekonomi = "/ekonomi";teknoloji = "/politika";saglik = "/saglik"; kadin="/kadin"

kategoriler = [spor,ekonomi,teknoloji,saglik,kadin]
saglikhaberleri, ekonomihaberleri, teknolojihaberleri, sporhaberleri,kadinhaberleri = [],[],[],[],[]

for i in kategoriler:
    for sayfa in range(2): 
        driver.get(site+str(i)+"/"+str(sayfa))
        time.sleep(3)
            
        baslik = driver.find_elements(By.CLASS_NAME,"news-container")
        linkler = []
        for l in baslik:
            print("BAŞLIK :",l.text)
            a = l.find_elements(By.TAG_NAME,"a")
            for k in a:
                print("LİNKLER")
                
                if i == spor:
                    sporhaberleri.append(k.get_attribute("href"))

                elif i == ekonomi:
                    ekonomihaberleri.append(k.get_attribute("href"))

                elif i==teknoloji:
                    teknolojihaberleri.append(k.get_attribute("href"))

                elif i==saglik:
                    saglikhaberleri.append(k.get_attribute("href"))

                elif i==kadin:
                    kadinhaberleri.append(k.get_attribute("href"))  

              

print("saglikhaberleri",saglikhaberleri)
print("ekonomihaberleri",ekonomihaberleri)
print("sporhaberleri",sporhaberleri)
print("teknolojihaberleri",teknolojihaberleri)
print("kadinhaberleri",kadinhaberleri)

saglikicerik,ekonomiicerik,sporicerik,teknolojiicerik,kadinicerik = [],[],[],[],[]
sayac = 0
for i in saglikhaberleri:
    driver.get(i)
    makale = driver.find_elements(By.CLASS_NAME,"body")
    for o in makale:
        
        saglikicerik.append(o)
        open(r"C:\Users"+str(sayac)+".txt", "w",encoding="utf-8").write(o.text)
        sayac = sayac+1
for i in sporhaberleri:
    driver.get(i)
    makale = driver.find_elements(By.CLASS_NAME,"body")
    for o in makale:
        
        sporicerik.append(o)
        open(r"C:\Users\alper\OneDrive\Masaüstü\haberler\spor\spor"+str(sayac)+".txt", "w",encoding="utf-8").write(o.text)
        sayac = sayac+1

for i in teknolojihaberleri:
    driver.get(i)
    makale = driver.find_elements(By.CLASS_NAME,"body")
    for o in makale:
        
        teknolojiicerik.append(o)
        open(r"C:\Users\alper\OneDrive\Masaüstü\haberler\siyaset\siyaset"+str(sayac)+".txt", "w",encoding="utf-8").write(o.text)
        sayac = sayac+1

for i in ekonomihaberleri:
    driver.get(i)
    makale = driver.find_elements(By.CLASS_NAME,"body")
    for o in makale:
        
        ekonomiicerik.append(o)
        open(r"C:\Users\alper\OneDrive\Masaüstü\haberler\ekonomi\ekonomi"+str(sayac)+".txt", "w",encoding="utf-8").write(o.text)
        sayac = sayac+1


for i in kadinhaberleri:
    driver.get(i)
    makale = driver.find_elements(By.CLASS_NAME,"body")
    for o in makale:     
        kadinicerik.append(o)
        open(r"C:\Users\alper\OneDrive\Masaüstü\haberler\magazin\magazin"+str(sayac)+".txt", "w",encoding="utf-8").write(o.text)
        sayac = sayac+1


import csv
 
fields = ['Teknoloji', 'Saglik', 'Ekonomi', 'Spor',"Kadin"] 
    
rows = [ teknolojiicerik,saglikicerik,ekonomiicerik,sporicerik,kadinicerik] 
  
with open('haberler.csv', 'w') as f:
      
    
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(rows)





driver.close()