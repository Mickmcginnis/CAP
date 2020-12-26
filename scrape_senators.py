from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import html5lib

states_abbr = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def get_senators():
    i=0
    for s in states_abbr:
        driver = webdriver.Firefox()
        driver.get("https://www.senate.gov/general/contact_information/senators_cfm.cfm?State={}".format(states_abbr[i]))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html5lib')
        data=[]
        div = soup.find('main', attrs={'class':'gridcontainer clearfix'})
        print("printing div:",div)
        # tables = div.findAll('div', attrs={'width':'100%'})
        data.append(div)
        i+=1
    print(soup.prettify())
    return soup.prettify()

get_senators()