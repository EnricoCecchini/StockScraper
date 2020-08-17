# StockScraper

Python program that uses BeautifulSoup and Requests modules to scrape stock price data from Yahoo FInance

The program displays the current price of each stock and the highest and lowest prices they reach after starting the program.

To add additional stocks, add the URL from the stock page on Yahoo finance, create a new instance of the Price class with the name of the company, the URL an a call to the getPrice() method, passing the URL as a parameter.
Then add the stock in the While loop and set the price to a new call to getPrice(), before calling the printData() method in the class
