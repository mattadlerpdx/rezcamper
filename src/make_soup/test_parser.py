from bs4 import BeautifulSoup
import logging
import requests

try:
    with open('index.html', 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    print(soup)
except:
    logging.error(f'Error occured: {error}')

try:
    home_page = requests.get('https://www.mountainproject.com/', stream=True)
    if home_page.status_code == 200:
        with open('mountain_project.html', 'w') as fp:
            for line in home_page.text:
                fp.write(line)
except:
    logging.error(f'Error occured: {error}')

try: 
    with open('mountain_project.html', 'r') as fp:
        for line in fp:
            print(line)
except:
    logging.debug(f'Unsuccessfull Wrote to mountain project file {debug}')