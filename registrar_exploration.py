import pandas as pd
import numpy as np
import nltk
time = '20170901_08a'
key_words = ['registration', 'transcript', 'verification', 'diploma', 'graduation', 'degree', 'record', 'waitlist', 'wait-list', 'wait list', 'schedule', 'drop', 'add']
df = pd.DataFrame.from_csv('NA_ALL_' + time + '.csv', encoding = "ISO-8859-1")
registrar_df = pd.DataFrame.from_csv('active_students_' + time + '.csv')

len(df)
df.columns
registrar_df['Matriculation Term'].unique()
# Number respondents to survey
len(df['Completed_Time'].dropna())

# Number of students responded to survey and number of students in registrar
students = df[df['PRIMARY_ROLE'] == 'Student']
len(students[students['Completed_Time'].notnull()])
len(registrar_df)

# break out students with multiple majors to different rows
len(registrar_df['Major 3'].dropna())
registrar_df[registrar_df['Major 4'].notnull()].head()
registrar_df[registrar_df['Major 2'].notnull()].head()

merge_df = df.merge(registrar_df, how='inner', right_index=True, left_on='NetID')
len(merge_df)


# only one student not in common

housing_dmg = 'WATER_DAMAGE'
vehicle_dmg = 'VEHICLE_DAMAGE'
has_wifi = "INTERNET_AVAIL"
has_phone = 'PHONE_AVAIL'
road_access = 'ROAD_STATUS'
road_access_mapping = {'Passable': 0, 'Continuous Standing Water': 1, 'Periodic Standing Water': 2}
students[[housing_dmg,vehicle_dmg,has_wifi,has_phone,road_access]]

import matplotlib.pyplot as plt

def generate_plots():
    mapping = {'Yes': 1, 'No': 0}
    mapped_df = df.replace({housing_dmg: mapping, vehicle_dmg: mapping, has_phone: mapping, has_wifi: mapping})
    mapped_df[has_wifi]
