from distutils.log import error
from bs4 import BeautifulSoup
import logging

try:
    with open("index.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    print(soup)
except:
    logging.error(f'Error occured: {error}')