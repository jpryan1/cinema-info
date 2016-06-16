
#This program was written for scraping wikipedia for articles on movies and actors
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import html2text
driver=webdriver.Firefox()
driver.get('en.wikipedia.org')
f = open('patch.txt')
s=f.read()
s=s.split('\n')
f=open('MLINKS2.txt','w')
l=len(s)
for x in range(l):
    string = s[x]+'pedia'
    driver.get(string)
    f.write(driver.current_url)
    f.write('\n')
    time.sleep(5)
f.close()
    
