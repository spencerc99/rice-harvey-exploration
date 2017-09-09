
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[5]:

df = pd.DataFrame.from_csv('housing_2017-08-30-1308.csv')
df


# In[8]:

df.columns


# In[10]:

df['Housing option'].unique()


# In[17]:

needs = df.loc[df['Housing option'] == 'I need temporary housing']
offers = df.loc[df['Housing option'] == 'I can offer temporary housing']


# In[20]:
new_needs = needs[-3:]
for need in new_needs.iterrows():
    print (need)
    # find_nearest(need)
needs.iloc[-4]
needs.loc[needs['Rice Role'] != 'Undergraduate Student'].iloc[-1]

needs['Number of adults'] + needs['Number of children']
needs['Number of children']
address_key_needs = 'What is your usual home address?'
address_key = 'What is the address where you can provide temporary housing?'
role_key = 'Rice Role'
num_adults = 'Number of adults'
num_children = 'Number of children'
num_adults_offer = 'Number of adults.1'
num_children_offer = 'Number of children.1'
pets = 'Can you accommodate pets?'
# have_capacity = offers.loc[(offers['Number of adults.1'] >= 2) & (offers['Number of children.1'] >= 1) &(offers['Can you accommodate pets?'] == 'Yes')]
have_capacity = offers.loc[(offers['Number of adults.1'] >= 3) & (offers['Number of children.1'] >= 2)]
# have_capacity = offers.loc[(offers['Number of adults.1'] >= 2)  & (offers['Can you accommodate pets?'] == 'Yes')]

have_capacity[address_key]
staff_faculty = have_capacity.loc[(have_capacity[role_key] == 'Staff') | (have_capacity[role_key] == 'Faculty')]
staff_faculty[address_key]
students = have_capacity.loc[(have_capacity[role_key] == 'Undergradute Student') | (have_capacity[role_key] == 'Graduate Student')]
students[address_key]

other_info = 'Other information we need to know about your family.1'
staff_faculty.loc[126]

import googlemaps
from datetime import datetime
import configparser
config = configparser.ConfigParser()
gmaps = googlemaps.Client(key=config['google']['token'])
# df.iloc[0][address_key]
# df.iloc[1][address_key]
# dir = gmaps.directions("2630 Bissonnet street Apt 5133", "1311 woodhead", mode='driving', departure_time=datetime.now())
# dir[0]['legs'][0]['distance']['value']

def sort_df(df, column_idx, key):
    '''Takes dataframe, column index and custom function for sorting,
    returns dataframe sorted by this column using this function'''
    col = df.ix[:,column_idx]
    temp = pd.DataFrame([])
    temp[0] = col
    temp[1] = df.index
    temp = temp.values.tolist()
    df = df.ix[[i[1] for i in sorted(temp, key=key)]]
    return df

from math import radians, cos, sin, asin, sqrt
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

def find_nearest(need_person):
    predicate = (offers['Number of adults.1'] >= need_person[num_adults])
    if not pd.isnull(need_person[num_children]) and need_person[num_children] > 0:
        predicate = predicate & (offers[num_children_offer] >= need_person[num_children])
    if not pd.isnull(need_person[pets]) and need_person[pets] == 'Yes':
        predicate = predicate & (offers['Can you accommodate pets?'] == 'Yes')
    have_capacity = offers.loc[predicate]
    needs_address = need_person[address_key_needs]
    needs_geocode = gmaps.geocode(needs_address)[0]['geometry']['location']
    def distance_func(temp):
        # offer_address = temp[0]
        # needs_address = need_person[address_key_needs]
        # try:
        #     dir = gmaps.directions(needs_address, offer_address, mode='driving', departure_time=datetime.now())
        #     return dir[0]['legs'][0]['distance']['value']
        # except:
        #     print ('invalid address:', offer_address)
        #     return float('inf')
        offer_address = temp[0]
        try:
            offers_code = gmaps.geocode(offer_address)[0]['geometry']['location']
            return haversine(needs_geocode['lat'], needs_geocode['lng'], offers_code['lat'], offers_code['lng'])
        except:
            print ('invalid address:', offer_address)
            return float('inf')

    print (sort_df(have_capacity, address_key, distance_func)[address_key].head(15))

needs_address = needs.iloc[-6][address_key_needs]
needs_address
# needs_geocode = gmaps.geocode(needs_address)
# needs_geocode[0]['geometry']['location']['lng']
find_nearest(needs.iloc[-6])
