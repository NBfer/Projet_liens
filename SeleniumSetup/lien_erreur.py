# Importer la library selenium
import time

import requests as requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()
liens_list = driver.find_elements(By.TAG_NAME, 'a')
total_liens = len(liens_list)
print('le nombre de liens dans le site est : ', total_liens)
counter = 0
for link in liens_list:
    url = link.get_attribute('href')
    try:
        response = requests.get(url)
    except:
        None
    response.status_code
    if response.status_code >= 400:
        print(url, ' est un lien Invalide')
        counter += 1
    else:
        print(url, " est un lien valide ")

print('le nombre de lien invalide est : ', counter)

driver.close()




