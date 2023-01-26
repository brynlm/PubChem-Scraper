from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

reagents = []

while True:
        x = input("enter compound name. If finished, type 'done'.\n")
        if x != 'done':
                reagents.append(x)
        else:
                break

print('\n')

PATH = Service("/Users/brynleemeyer/Desktop/Desktop/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=PATH)

for i in reagents:
        print('-----------------------------------')
        print(i.capitalize() + ':')
        driver.get("https://pubchem.ncbi.nlm.nih.gov/")
        search = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/div/div[2]/form/div/div[1]/input')
        search.send_keys(i)
        search.send_keys(Keys.RETURN)
        try:
                compound_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="featured-results"]/div/div[2]/div/div[1]/div[2]/div[1]/a')))
                compound_info.click()
        except:
                print("error - element not found")
                continue
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CAS"]/div[2]/div[1]/p')))
        try:
                CAS = driver.find_element(By.XPATH, '//*[@id="CAS"]/div[2]/div[1]/p')
                print("CAS#: " + CAS.text)
        except:
                print('CAS#: error')
        try:
                MW = driver.find_element(By.XPATH, '//*[@id="Computed-Properties"]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]')
                print('MW: ' + MW.text + 'g/mol')
        except:
                print('MW: error')
        try:
                BP = driver.find_element(By.ID, 'Boiling-Point')
                BP_list = BP.find_elements(By.CLASS_NAME, 'section-content-item')
                BP_content = BP_list[len(BP_list)-2].find_element(By.TAG_NAME, 'p')
                print("BP: " + BP_content.text)
        except Exception as e:
                print(e)
                print('BP: error')
        try:
                MP = driver.find_element(By.ID, 'Melting-Point')
                MP_list = MP.find_elements(By.CLASS_NAME, 'section-content-item')
                MP_content = MP_list[len(MP_list)-2].find_element(By.TAG_NAME, 'p')
                print('MP: ' + MP_content.text)
        except:
                print('MP: error')
        try:
                Density = driver.find_element(By.ID, 'Density')
                Densities = Density.find_elements(By.CLASS_NAME, 'section-content-item')
                Density_content = Densities[-1].find_element(By.TAG_NAME, 'p')
                print('Density: ' + Density_content.text)
        except:
                print('Density: error')
        try:
                n = driver.find_element(By.XPATH, '//*[@id="Refractive-Index"]/div[2]/div[1]/p')
                print('Refractive index:' + n.text)
        except:
                print('Refractive index: error')
        try:
                Hazards = driver.find_element(By.XPATH, '//*[@id="GHS-Classification"]/div[2]/div[2]/div[1]/table/tbody/tr[3]/td')
                print('Hazards:' + Hazards.text)
        except:
                print('Hazards: error')
driver.quit()
