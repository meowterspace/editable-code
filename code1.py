# IMPORTS
import webbrowser
import lxml
import requests
import time
from bs4 import BeautfulSoup

# PARSER FUNCTIONS
def parser(website):
  r=requests.open(website)
  soup=BeautifulSoup("r.text","lxml") #soup=BeautifulSoup("r.text")
  print soup.head.title

  webbrowser.visit('www.cloud.google.com/speech')
  webbrowser.find_by_name('speech_demo_record_icon').click()
  time.sleep(60)
  copied_text = webbrowser.find_by_id('results')[0].text
# MAIN CODE
parser("http://google.co.uk")
