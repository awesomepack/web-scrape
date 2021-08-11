'''
Scrape.py contains functions used in the completion of Homework 12 Mission_To_Mars: Web Scraping
'''

# Defining the scrape function
def Scrape():
    '''
    Scrape retreives data from various mars mission websites and returns:
    * Recent news headlline and summary
    * Featured space image
    * A table of Mars facts
    * Titles and images of the mars hemispheres
    '''

# Importing Dependencies
# importing dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd