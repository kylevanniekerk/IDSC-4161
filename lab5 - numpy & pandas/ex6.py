import pandas as pd
from bs4 import BeautifulSoup as bs

def total_votes(file):
    with open(file) as f:
        soup = bs(f)
        
    names = soup.find_all('tr')
    labels = []
    data = []
    
    for h in names[0].find_all('td'):
        labels.append(h.get_text().strip())
        
    for i in names[1:]:
        i_list = []
        
        for x in i.find_all('td'):
            x_str = x.get_text().strip()
            if x_str.isnumeric():
                i_list.append(int(x_str))
            else:
                i_list.append(x_str)
        data.append(i_list)
    df = pd.DataFrame(data,columns = labels)
    
    yes_votes = df['vote_yes'].sum()
    no_votes = df['vote_no'].sum()
    return yes_votes, no_votes

def num_states_passed(file):
    with open(file) as f:
        soup = bs(f)
        
    names = soup.find_all('tr')
    labels = []
    data = []
    
    for h in names[0].find_all('td'):
        labels.append(h.get_text().strip())
        
    for i in names[1:]:
        i_list = []
        
        for x in i.find_all('td'):
            x_str = x.get_text().strip()
            if x_str.isnumeric():
                i_list.append(int(x_str))
            else:
                i_list.append(x_str)
        data.append(i_list)
    df = pd.DataFrame(data,columns = labels)
    
    passed = (df['state'][df['vote_yes'] > df['vote_no']].drop_duplicates()).count()
        
    return passed

def highest_pct(file):
    with open(file) as f:
        soup = bs(f)
        
    names = soup.find_all('tr')
    labels = []
    data = []
    
    for h in names[0].find_all('td'):
        labels.append(h.get_text().strip())
        
    for i in names[1:]:
        i_list = []
        
        for x in i.find_all('td'):
            x_str = x.get_text().strip()
            if x_str.isnumeric():
                i_list.append(int(x_str))
            else:
                i_list.append(x_str)
        data.append(i_list)
    df = pd.DataFrame(data,columns = labels)
    
    df['pct'] = df['vote_yes'] / df['population']
    maxpct = df['state'][df['pct'].max()]
    minpct = df['state'][df['pct'].min()]
    
    return maxpct, minpct
    
def potential_fraud(file):
    with open(file) as f:
        soup = bs(f)
        
    names = soup.find_all('tr')
    labels = []
    data = []
    
    for h in names[0].find_all('td'):
        labels.append(h.get_text().strip())
        
    for i in names[1:]:
        i_list = []
        
        for x in i.find_all('td'):
            x_str = x.get_text().strip()
            if x_str.isnumeric():
                i_list.append(int(x_str))
            else:
                i_list.append(x_str)
        data.append(i_list)
    df = pd.DataFrame(data,columns = labels)
    
    df['tot'] = df['vote_yes'] + df['vote_no']
    fruad = df['city'][df['tot']>df['population']].array
    return fruad