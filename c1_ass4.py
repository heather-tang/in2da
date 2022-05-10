#### Q1
import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def clear_data(string1):
    if re.search(r'\[[a-z]* [0-9]+\]', string1) is None:
        return string1
    else:
        return string1.replace(re.search(r'\[[a-z]* [0-9]+\]', string1).group(), '')


def get_area(team):
    for each in list(nhl_cities.index.values):
        if team in each:
            return nhl_cities.at[each, 'Metropolitan area']


def get_nhl_data():
    return out_df


population_by_region = []  # pass in metropolitan area population from cities
win_loss_by_region = []  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
nhl_df = pd.read_csv("assets/nhl.csv")
cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
nhl_df = nhl_df[nhl_df['year'] == 2018].drop([0, 9, 18, 26], axis=0) # get only 2018 stats
population = cities[['Metropolitan area', 'Population (2016 est.)[8]']]
population = population.set_index('Metropolitan area')
cities['NHL'] = cities['NHL'].apply(lambda x: clear_data(x))
nhl_cities = cities[['Metropolitan area', 'NHL']].set_index('NHL')
nhl_cities = nhl_cities.drop(['—', ''], axis=0)
nhl_df['team'] = nhl_df['team'].apply(lambda x: x[:-1].strip() if x.endswith("*") else x.strip())
nhl_df['area'] = nhl_df['team'].apply(lambda x: x.split(" ")[-1])
nhl_df['area'] = nhl_df['area'].apply(lambda x: get_area(x))
out = []
for group, frame in nhl_df.groupby('area'):
    total_wins = np.sum(pd.to_numeric(frame['W']))
    total_losses = np.sum(pd.to_numeric(frame['L']))
    total_matches = total_wins + total_losses
    ratio = (total_wins / total_matches)
    out_dict = {
        'Area': group,
        'Ratio': ratio
    }
    out.append(out_dict)
new_df = pd.DataFrame(out)
new_df = new_df.set_index('Area')
out_df = pd.merge(new_df, population, how="inner", left_index=True, right_index=True)
out_df['Population (2016 est.)[8]'] = pd.to_numeric(out_df['Population (2016 est.)[8]'])
population_by_region = out_df['Population (2016 est.)[8]']
win_loss_by_region = out_df['Ratio']
corr = stats.pearsonr(population_by_region, win_loss_by_region)[0]


#### Q2
import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def clear_data(string1):
    if re.search(r'\[[a-z]* [0-9]+\]', string1) is None:
        return string1
    else:
        return string1.replace(re.search(r'\[[a-z]* [0-9]+\]', string1).group(), '')


def clear_nba_data(string1):
    if re.search(r'\* \([0-9]*\)| \([0-9]*\)', string1) is None:
        return string1
    else:
        return string1.replace(re.search(r'\* \([0-9]*\)| \([0-9]*\)', string1).group(), '')


def get_area(team):
    for each in list(nba_cities.index.values):
        if team in each:
            return nba_cities.at[each, 'Metropolitan area']


def get_nba_data():
    return out_df


population_by_region = []  # pass in metropolitan area population from cities
win_loss_by_region = []  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
nba_df = pd.read_csv("assets/nba.csv")
cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
nba_df = nba_df[nba_df['year'] == 2018]  # get only 2018 stats no need of dropping rows
population = cities[['Metropolitan area', 'Population (2016 est.)[8]']]
population = population.set_index('Metropolitan area')
cities['NBA'] = cities['NBA'].apply(lambda x: clear_data(x))
nba_cities = cities[['Metropolitan area', 'NBA']].set_index('NBA')
nba_cities = nba_cities.drop(['—', ''], axis=0)
nba_df['team'] = nba_df['team'].apply(lambda x: clear_nba_data(x))
nba_df['area'] = nba_df['team'].apply(lambda x: x.split(" ")[-1])
nba_df['area'] = nba_df['area'].apply(lambda x: get_area(x))
out = []
for group, frame in nba_df.groupby('area'):
    total_wins = np.sum(pd.to_numeric(frame['W']))
    total_losses = np.sum(pd.to_numeric(frame['L']))
    total_matches = total_wins + total_losses
    ratio = (total_wins / total_matches)
    out_dict = {
        'Area': group,
        'Ratio': ratio
    }
    out.append(out_dict)
new_df = pd.DataFrame(out)
new_df = new_df.set_index('Area')
out_df = pd.merge(new_df, population, how="inner", left_index=True, right_index=True)
out_df['Population (2016 est.)[8]'] = pd.to_numeric(out_df['Population (2016 est.)[8]'])
population_by_region = out_df['Population (2016 est.)[8]'].to_list()
win_loss_by_region = out_df['Ratio'].to_list()
corr = stats.pearsonr(population_by_region, win_loss_by_region)[0]


#### Q3
import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def clear_data(string1):
    if re.search(r'\[[a-z]* [0-9]+\]', string1) is None:
        return string1
    else:
        return string1.replace(re.search(r'\[[a-z]* [0-9]+\]', string1).group(), '')


def get_area(team):
    for each in list(mlb_cities.index.values):
        if team in each:
            return mlb_cities.at[each, 'Metropolitan area']


def get_mlb_data():
    return out_df


population_by_region = []  # pass in metropolitan area population from cities
win_loss_by_region = []  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
mlb_df = pd.read_csv("assets/mlb.csv")
cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1,[0,3,5,6,7,8]]
mlb_df = mlb_df[mlb_df['year'] == 2018]  # get only 2018 stats no need of dropping rows
population = cities[['Metropolitan area', 'Population (2016 est.)[8]']]
population = population.set_index('Metropolitan area')
cities['MLB'] = cities['MLB'].apply(lambda x: clear_data(x))
mlb_cities = cities[['Metropolitan area', 'MLB']].set_index('MLB')
mlb_cities = mlb_cities.drop(['—', ''], axis=0)
mlb_df['area'] = mlb_df['team'].apply(lambda x: x.split(" ")[-1])
mlb_df['area'] = mlb_df['area'].apply(lambda x: get_area(x))
mlb_df.at[0, 'area'] = 'Boston'
out = []
for group, frame in mlb_df.groupby('area'):
    total_wins = np.sum(pd.to_numeric(frame['W']))
    total_losses = np.sum(pd.to_numeric(frame['L']))
    total_matches = total_wins + total_losses
    ratio = (total_wins / total_matches)
    out_dict = {
        'Area': group,
        'Ratio': ratio
    }
    out.append(out_dict)
new_df = pd.DataFrame(out)
new_df = new_df.set_index('Area')
out_df = pd.merge(new_df, population, how="inner", left_index=True, right_index=True)
out_df['Population (2016 est.)[8]'] = pd.to_numeric(out_df['Population (2016 est.)[8]'])
population_by_region = out_df['Population (2016 est.)[8]'].to_list()
win_loss_by_region = out_df['Ratio'].to_list()
corr = stats.pearsonr(population_by_region, win_loss_by_region)[0]


#### Q4
import pandas as pd
import numpy as np
import scipy.stats as stats
import re


def clear_data(string1):
    if re.search(r'\[[a-z]* [0-9]+\]', string1) is None:
        return string1
    else:
        return string1.replace(re.search(r'\[[a-z]* [0-9]+\]', string1).group(), '')


def clear_nba_data(string1):
    if re.search(r'\*|\+', string1) is None:
        return string1
    else:
        return string1.replace(re.search(r'\*|\+', string1).group(), '')


def get_area(team):
    for each in list(nfl_cities.index.values):
        if team in each:
            return nfl_cities.at[each, 'Metropolitan area']


def get_nfl_data():
    return out_df


population_by_region = []  # pass in metropolitan area population from cities
win_loss_by_region = []  # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
nfl_df = pd.read_csv("assets/nfl.csv")
cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1,[0,3,5,6,7,8]]
nfl_df = nfl_df[nfl_df['year'] == 2018].drop([0, 5, 10, 15, 20, 25, 30, 35])  # get only 2018 stats
population = cities[['Metropolitan area', 'Population (2016 est.)[8]']]
population = population.set_index('Metropolitan area')
cities['NFL'] = cities['NFL'].apply(lambda x: clear_data(x))
nfl_cities = cities[['Metropolitan area', 'NFL']].set_index('NFL')
nfl_cities = nfl_cities.drop(['—', ''], axis=0)
nfl_df['team'] = nfl_df['team'].apply(lambda x: clear_nba_data(x))
nfl_df['area'] = nfl_df['team'].apply(lambda x: x.split(" ")[-1])
nfl_df['area'] = nfl_df['area'].apply(lambda x: get_area(x))
out = []
for group, frame in nfl_df.groupby('area'):
    total_wins = np.sum(pd.to_numeric(frame['W']))
    total_losses = np.sum(pd.to_numeric(frame['L']))
    total_matches = total_wins + total_losses
    ratio = (total_wins / total_matches)
    out_dict = {
        'Area': group,
        'Ratio': ratio
    }
    out.append(out_dict)
new_df = pd.DataFrame(out)
new_df = new_df.set_index('Area')
out_df = pd.merge(new_df, population, how="inner", left_index=True, right_index=True)
out_df['Population (2016 est.)[8]'] = pd.to_numeric(out_df['Population (2016 est.)[8]'])
population_by_region = out_df['Population (2016 est.)[8]'].to_list()
win_loss_by_region = out_df['Ratio'].to_list()
corr = stats.pearsonr(population_by_region, win_loss_by_region)[0]
