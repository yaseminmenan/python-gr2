# web scraper
import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.halopedia.org'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


def read_file():
    with open('Did_You_Know.txt', 'r') as file:
        print(file.read())


def write_text(text):
    with open('Did_You_Know.txt', 'w') as file:
        file.write('Did you know?\n')
        for line in text:
            file.write(line)
            file.write('\n')


def get_list_lines(ul_list):
    did_you_know = set()
    for ul in ul_list:
        for li in ul.find_all("li"):
            did_you_know.add(li.text)
    return did_you_know


def get_left_container():
    left_container = soup.find(class_='bottom-left-nav-container')
    uls = left_container.find_all('ul')
    did_you_know = get_list_lines(uls)
    write_text(did_you_know)
    return did_you_know


def get_bottom_container():
    bottom_container = soup.find('div', title=re.compile('^Did you know?'))
    uls = bottom_container.find_all('ul')
    did_you_know = get_list_lines(uls)
    write_text(did_you_know)
    return did_you_know


def get_both():
    dyk_left = get_left_container()
    dyk_bottom = get_bottom_container()
    dyk_left.update(dyk_bottom)
    write_text(dyk_left)


stdin_input = input('Read data from left container, bottom container, or both? ')
if stdin_input == 'left':
    get_left_container()
elif stdin_input == 'bottom':
    get_bottom_container()
else:
    get_both()
read_file()
