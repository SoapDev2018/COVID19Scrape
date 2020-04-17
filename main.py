import requests
from bs4 import BeautifulSoup
from color import Color

def national():
    url = "https://api.covid19india.org/data.json"
    response = requests.get(url).json()
    daily_stat = response['statewise'][0]
    active = daily_stat['active']
    confirmed = daily_stat['confirmed']
    deaths = daily_stat['deaths']
    recovered = daily_stat['recovered']
    last_update = daily_stat['lastupdatedtime']
    deltaconfirmed = int(daily_stat['deltaconfirmed'])
    deltadeaths = int(daily_stat['deltadeaths'])
    deltarecovered = int(daily_stat['deltarecovered'])
    print("Last Updated On: {}".format(last_update))
    print("Confirmed: {} ({})".format(confirmed, "+" + str(deltaconfirmed) if deltaconfirmed > 0 else "-" + str(deltaconfirmed)))
    print("Active: {}".format(active))
    print("Deaths: {} ({})".format(deaths, "+" + str(deltadeaths) if deltadeaths > 0 else "-" + str(deltadeaths)))
    print("Recovered: {} ({})".format(recovered, "+" + str(deltarecovered) if deltarecovered > 0 else "-" + str(deltarecovered)))

def statewise():
    url = "https://www.mohfw.gov.in/"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    state_table = soup.find('tbody').find_all('tr')
    state_table_len = len(state_table)
    state_table = state_table[:state_table_len - 3]
    print("+-------------------------------------------------------------------------+")
    print("+            State            |   Confirmed    |   Cured    |   Deaths    +")
    print("+-------------------------------------------------------------------------+")
    for state in state_table:
        state_name = state.find('td').find_next_sibling()
        state_name_text = state_name.text
        confirmed = state_name.find_next_sibling()
        confirmed_text = str(confirmed.text)
        cured = confirmed.find_next_sibling()
        cured_text = str(cured.text)
        death = cured.find_next_sibling()
        death_text = str(death.text)
        print("+",end="")
        
        # Formatting State Names
        state_name_len_diff = 29 - len(state_name_text)
        if state_name_len_diff % 2 == 0:
            diff = int(state_name_len_diff / 2)
            for i in range(diff):
                state_name_text = " " + state_name_text + " "
        else:
            for i in range(state_name_len_diff//2):
                state_name_text = " " + state_name_text + " "
            state_name_text = state_name_text + " "
        print(state_name_text + "|",end="")

        # Formatting Confirmed Cases
        confirmed_len_diff = 16 - len(confirmed_text)
        if confirmed_len_diff % 2 == 0:
            diff = int(confirmed_len_diff / 2)
            for i in range(diff):
                confirmed_text = " " + confirmed_text + " "
        else:
            for i in range(confirmed_len_diff//2):
                confirmed_text = " " + confirmed_text + " "
            confirmed_text = confirmed_text + " "
        print(confirmed_text + "|", end="")

        # Formatting Cured Cases
        cured_len_diff = 12 - len(cured_text)
        if cured_len_diff % 2 == 0:
            diff = int(cured_len_diff / 2)
            for i in range(diff):
                cured_text = " " + cured_text + " "
        else:
            for i in range(cured_len_diff//2):
                cured_text = " " + cured_text + " "
            cured_text = cured_text + " "
        print(cured_text + "|",end="")
        
        # Formatting Deaths
        death_len_diff = 13 - len(death_text)
        if death_len_diff % 2 == 0:
            diff = int(death_len_diff / 2)
            for i in range(diff):
                death_text = " " + death_text + " "
        else:
            for i in range(death_len_diff//2):
                death_text = " " + death_text + " "
            death_text = death_text + " "
        print(death_text+"+")
    print("+-------------------------------------------------------------------------+")

if __name__ == '__main__':
    print(Color.BOLD + "National Statistics" + Color.END)
    national()
    print()
    print(Color.BOLD + "State Wise Statistics" + Color.END)
    statewise()