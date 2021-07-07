# web scraper
import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

stage_table = soup.find(class_='clasament_general white-shadow etape_meciuri')
# print(stage_table.prettify())
team_rows = stage_table.find_all(class_='echipa-etapa-1')
# print(team_rows)
# print()

teams = []
for team in team_rows:
    team_cell = team.find('a')
    team_name = team_cell.find(class_='hiddenMobile').text.strip()
    # print(team_name)
    teams.append(team_name)

print(teams)
