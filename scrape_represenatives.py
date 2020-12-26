from bs4 import BeautifulSoup
import requests
import html5lib


url = "https://www.house.gov/representatives"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

def get_states():
    data=[]
    section = soup.find('section', attrs={'id':'by-state'})
    tables = section.findAll('table', attrs={'class':'table'})
    states=[]
    t=0
    for i in tables:
        state_data=[]
        table = tables[t]
        table_captions = table.find('caption')
        state_name = table_captions.text.strip()
        state_data.append([state_name])
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            state_data.append([ele for ele in cols if ele])
        data.append(state_data)
        t=t+1

    print(data[1])
    return data

all_states = get_states()

def individual_states(all_states):
    t=0
    states=[]
    for i in all_states:
        state = all_states[t]
        states.append(state[1])
        reps = state[1::]

get_states()

# '<td class="views-field views-field-text-3 views-field-text-11" headers="view-text-3-table-column">'
