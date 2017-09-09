import pandas as pd
import numpy as np
import nltk

# df = pd.DataFrame.from_csv('NA_PRELIM_20170829_03p.csv', encoding = "ISO-8859-1")
df = pd.DataFrame.from_csv('NA_ALL_20170901_08a.csv', encoding = "ISO-8859-1")
df.columns
df[df['REPORTING_UNIT'] == 'Administration']['DEPARTMENT'].unique()
df.columns
len(df['Completed_Time'].dropna())
reporting_unit = 'REPORTING_UNIT'
housing_dmg = 'WATER_DAMAGE'
vehicle_dmg = 'VEHICLE_DAMAGE'
finance_ppl = df.loc[df[reporting_unit] == 'Finance']
len(finance_ppl)

finance_housing_dmg = finance_ppl.loc[(finance_ppl[housing_dmg] == 'Yes')]
finance_no_housing_dmg = finance_ppl.loc[(finance_ppl[housing_dmg] == 'No')]
finance_no_answer = finance_ppl.loc[(pd.isnull(finance_ppl[housing_dmg]))]
len(finance_housing_dmg)
len(finance_no_answer)
# 45 / 81 answered about housing
# 16 have housing damage
# Of the people who filled in additional information, 2 people are in temporary housing/evacuated
# lem4, mcc5
has_housing_dmg = df.loc[df[housing_dmg] == 'Yes']
len(has_housing_dmg)
no_housing_dmg = df.loc[df[housing_dmg] == 'No']
no_answer = df[pd.isnull(df[housing_dmg])]
len(no_answer['ADDL_INFORMATION'].dropna())
count = 0
for entry in no_housing_dmg['ADDL_INFORMATION'].dropna().iteritems():
    print (entry)
    if 'displaced' in entry[1] or 'evacuated' in entry[1] or 'evacuation' in entry[1] or 'evacuations' in entry[1]:
        count += 1
        # print (finance_ppl.loc[entry[0]])
        # print ()
count

len(df[pd.isnull(df[vehicle_dmg])])

import re, pprint
string = " ".join(list(df['ADDL_INFORMATION'].dropna().values))
tokens = nltk.word_tokenize(string)

import random
random.sample(list(df['ADDL_INFORMATION'].dropna().values), 50)
# of the 15 people who said additional info about water damage, common trends are roof leaking/damage
# carpets affected by water damage
len(finance_ppl['WATER_DESC'].dropna())
for entry in finance_ppl['WATER_DESC'].dropna().iteritems():
    print (entry)

finance_vehicle_dmg = finance_ppl.loc[finance_ppl[vehicle_dmg] == 'Yes']
len(finance_vehicle_dmg)
