# Python program to obtain current, lowest and highest prices for stocks I follow
# This program uses BeautifulSoup to scrape data from yahoo Finance to obtain
# the current, highest and lowest price of individual stocks

# Import Modules
import bs4
import requests
from bs4 import BeautifulSoup
import time
import datetime

# Price class for program
class Price():

    # Constructor method for program
    def __init__(self, name, url, price):
        self.name = name
        self.url = url
        self.price = price
        self.highest = 0.0
        self.lowest = 0.0
    
    # Method to obtain the highest price the stock reached that day
    def getHighest(self):
        
        return max(self.price, self.highest)

    # Method to obtain the lowest price the stock reached that day
    def getLowest(self):
        
        return min(self.price, self.highest)
    
    # Method to print the data obtained
    def printData(self):
        # Get lowest and highest price of Stock
        self.lowest = self.getLowest()
        self.highest = self.getHighest()

        # Print Data
        print(f'{self.name} Price: {self.price}')
        print(f'{self.name} Lowest Price: {self.lowest}')
        print(f'{self.name} Highest Price: {self.highest}')

# Method to obtain the current price of the stock
def getPrice(url):
        # Obtain reference to webpage
        r = requests.get(url)

        # Create soupt to work with HTML code
        soup = bs4.BeautifulSoup(r.text, 'lxml')

        # Obtain price from HTML code
        priceSTR = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        # Turn price into float type
        price = float(priceSTR.replace(',',''))

        return price


# URL of stocks the program will track and creates object instances of each stock
# Price('Company Name', url, price)
tslaURL = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'
tsla = Price('TESLA', tslaURL, getPrice(tslaURL))

zoomURL = 'https://finance.yahoo.com/quote/ZM?p=ZM'
zoom = Price('ZOOM', zoomURL, getPrice(zoomURL))

msftURL = 'https://finance.yahoo.com/quote/MSFT?p=MSFT'
msft = Price('Microsoft', msftURL, getPrice(msftURL))

mrnaURL = 'https://finance.yahoo.com/quote/MRNA?p=MRNA'
mrna = Price('Moderna', mrnaURL, getPrice(mrnaURL))

rclURL = 'https://finance.yahoo.com/quote/RCL?p=RCL'
rcl = Price('Royal Caribbean Group', rclURL, getPrice(rclURL))

# Infinite Loop to run program
while True:

    # Calls getPrice() method to obtain current price of each stock and stores the new 
    # value, before printing stock data
    tsla.price = getPrice(tslaURL)
    tsla.printData()
    print('')

    zoom.price = getPrice(zoomURL)
    zoom.printData()
    print('')

    msft.price = getPrice(msftURL)
    msft.printData()
    print('')

    mrna.price = getPrice(mrnaURL)
    mrna.printData()
    print('')

    rcl.price = getPrice(rclURL)
    rcl.printData()
    print('')

    # Prints current Date and Time during loop run
    print('\nTime: ' + str(datetime.datetime.now()))

    # Prints separation between each loop run and makes program wait 1s before running loop again
    print('*******************************************')
    time.sleep(1)
