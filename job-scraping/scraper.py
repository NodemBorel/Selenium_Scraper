from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

PATH = 'C:\Program Files (x86)\chromedriver.exe'

l=list()
o={}

target_url = "https://api.scrapingdog.com/scrape?api_key=xxxxxxxxxxxxxxxxxxxxxxxx&url=https://www.glassdoor.com/Job/new-york-python-jobs-SRCH_IL.0,8_IC1132348_KO9,15_IP3.htm?includeNoSalaryJobs=true&pgc=AB4AAoEAPAAAAAAAAAAAAAAAAfkQ90AAdwEBAQtEzo8VunEQLF8uBoWr%2BRnCsnMFj0JNOLbRUXIkLkFAzjjZlKDW1axVwiTVV%2BbXo8%2BX471WNF8IEWPMdAwCPhbzQe1T1HHMEVPYFwQLM8h1NnGMDPcEwo7tpQ7XL65R7DMDR26n0NhBU7lFGCODAwxNTsJRAAA%3D&dynamic=false"

driver=webdriver.Chrome(PATH)

driver.get(target_url)

driver.maximize_window()
time.sleep(2)

resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')

allJobsContainer = soup.find("ul",{"class":"css-7ry9k1"})

allJobs = allJobsContainer.find_all("li")

for job in allJobs:
    try:
        o["name-of-company"]=job.find("div",{"class":"d-flex justify-content-between align-items-start"}).text
    except:
        o["name-of-company"]=None

    try:
        o["name-of-job"]=job.find("a",{"class":"jobLink css-1rd3saf eigr9kq2"}).text
    except:
        o["name-of-job"]=None

    try:
        o["location"]=job.find("div",{"class":"d-flex flex-wrap css-11d3uq0 e1rrn5ka2"}).text
    except:
        o["location"]=None

    try:
        o["salary"]=job.find("div",{"class":"css-3g3psg pr-xxsm"}).text
    except:
        o["salary"]=None

    l.append(o)

    o={}

print(l)

df = pd.DataFrame(l)
df.to_csv('jobs.csv', index=False, encoding='utf-8')