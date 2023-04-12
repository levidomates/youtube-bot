from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.proxy import *
import requests
from bs4 import BeautifulSoup
import random
import sys 

def proxy_scraping(link):

    x = requests.get(link)
    soup = BeautifulSoup(x.text,"html.parser")
    DATA = []
    IP,PORT = "",""

    for td in soup.find_all("td"):
        if td.string == None or td.string == "":
            if len(td.find_all("a")) > 0:
                if td.find_all("a")[0].string != None:
                    PORT = td.find_all("a")[0].string
                    if all_number(IP) and all_number(PORT):
                        proxy = IP + ":" + PORT
                        proxy = proxy.replace("\n","")
                        DATA.append(proxy)
        else:
            IP = td.string
    return DATA

def all_number(value):
    FLAG = True
    for i in value:
        if i.isalpha():
            if i != ".":
                FLAG = False
    return FLAG
                
def watching_video(PROXY,link,duration):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--proxy-server={PROXY}")
    driver = webdriver.Chrome("chromedriver",options=chrome_options)
    
    driver.get(link)
    time.sleep(10)
    player = driver.find_element(By.ID,"player")
    player.click()
    time.sleep(duration)
    driver.close()

if __name__ == "__main__":

    link = sys.argv[1]
    duration = sys.argv[2]
    counter = 0

    while True:
        
        try:
            page = random.randint(1,450)
            DATA = proxy_scraping(f"https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}")
            PROXY = random.choice(DATA)
            TIME = random.randint(0,10)*60
            watching_video(PROXY,link,TIME)
            counter += 1
            print(f"\n[+][{counter}]",end="")
        except:
            pass 
    

