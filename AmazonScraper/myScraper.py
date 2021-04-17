from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

scraper = HTMLSession()

url = "https://www.amazon.fr/s?k=livre+minceur"

#Importing the code of the webpage
def getDataPage(url):
    return BeautifulSoup(scraper.get(url).text, "html.parser")

#Returns the url of the next page if it exists
def getNextPage(soup):
    page = soup.find('ul', {'class': 'a-pagination'})
    if not page.find('li', {'class':'a-disabled a-last'}):
        url = 'https://www.amazon.fr' + str(page.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return

#Returns the list all urls of each next page
def listUrls(url):
    urls = []
    while True:
        soup = getDataPage(url)
        url = getNextPage(soup)
        if not url:
            break
        urls.append(url)
    return urls

####### GET DATA #######

def getItemsTitle(soup):
    h2s = soup.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
    L = []
    for h2 in h2s:
        L.append(h2.text)
    return L

def getItemsPrice(soup):
    prices = soup.find_all('span', {'class': 'a-price-whole'})
    currencies = soup.find_all('span', {'class': 'a-price-symbol'})
    L_prices = []
    for price, currency in zip(prices, currencies):
        L_prices.append(price.text+currency.text)
    return L_prices

def getItemsEvaluations(soup):
    divs = soup.body.find_all('div', {'class': 'a-row a-size-small'})
    L_spans = []
    for div in divs:
        L_spans.append(div.find_all('span'))
    L_evals = []
    for spans in L_spans:
        L=[]
        for span in spans:
            if span.has_attr('aria-label'):
                L.append(span['aria-label'])
        L_evals.append(L)
    L_evaluations = []
    L_num = []
    for i,j in L_evals:
        L_evaluations.append(i[:3])
        if "xa" in j:
            L_num.append(None)
        else:
            L_num.append(j)
    return L_evaluations,L_num

def getItemsUrls(soup):
    urls = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})
    L_test = []
    for url in urls:
        L_test.append(url['href'])
    fparts = ["https://www.amazon.fr/"]*len(L_test)
    L_urls = []
    for i, j in zip(fparts, L_test):
        L_urls.append(i+j)
    return L_urls

####### CREATING THE BOOKS DATABASE #######
list_urls = listUrls(url)
list_titles, list_prices, list_evaluations, list_num, list_urls_items = [], [], [], [], []
table = []
for url in list_urls:
    soup = getDataPage(url)
    list_titles += getItemsTitle(soup)
    list_prices += getItemsPrice(soup)
    list_evaluations += getItemsEvaluations(soup)[0]
    list_num += getItemsEvaluations(soup)[1]
    list_urls_items += getItemsUrls(soup)

table = list(zip(list_titles, list_prices, list_evaluations, list_num, list_urls_items))
books = pd.DataFrame(table, columns=['Titles', 'Prices', 'Evaluations', 'Numbers of evaluators', 'Urls'])
books.to_csv('books.csv')