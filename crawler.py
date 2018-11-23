from bs4 import BeautifulSoup
from selenium import webdriver
import requests

page_link = 'https://austin.craigslist.com/d/computers/search/sya?query=macbook+pro'
page_response = requests.get(page_link, timeout=5)
#page_content = BeautifulSoup(page_response.content, 'html.parser')

class MBPFinder(BeautifulSoup):
  content = page_response.content  

  MBPofInterest = []
  print(content)


