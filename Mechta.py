import time
import webbrowser
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.mechta.kz/section/telefony-eed/')
time.sleep(3)



data=[]
for p in range(33):
    print(p)
    soup = BeautifulSoup(driver.page_source, 'lxml')


    sps=soup.findAll('div', class_='tw-h-[499px]')

    for sp in sps:
        name=sp.find('div', class_='tw-mt-[15px]').text
        price=sp.find('div', class_='tw-text-xl').text.strip().replace('\xa0', ' ')[:-1]
        link=sp.find('div', class_='tw-bg-bgColor').find('a')['href']
        data.append([name, price, link])

    print(len(data))

    driver.find_element('class name', 'block')
    sleep(10)

print(data)

df = pd.DataFrame(data, columns=['Name', 'Price', 'Link'])
df.to_csv('mechta_phones.csv', index=False, encoding='utf-8-sig')

