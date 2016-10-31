import webbrowser
import lxml
from bs4 import BeautfulSoup
import requests
r=requests.open("www.google.com")
soup=BeautifulSoup("r.text","lxml") #soup=BeautifulSoup("r.text")
print soup.head.title



import time
webbrowser.visit('www.cloud.google.com/speech')
webbrowser.find_by_name('speech_demo_record_icon').click()
time.sleep(60)
copied_text = webbrowser.find_by_id('results')[0].text

