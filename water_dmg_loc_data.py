import googlemaps
import pandas as pd
import numpy as np

df = pd.DataFrame.from_csv('NA_ALL_20170831_08a.csv', encoding = "ISO-8859-1")

gmaps = googlemaps.Client(key="AIzaSyAaIRcGMd7kFPi9i250ckS_8MEhnA_7QQA")
# gmaps.geocode(address)[0]['geometry']['location']
df.columns
# take only completed
df = df[df["Completed_Time"].notnull()]
housing_dmg = 'WATER_DAMAGE'
vehicle_dmg = 'VEHICLE_DAMAGE'

df[(df['WATER_DAMAGE'] == 'Yes') & (df['PRIMARY_ROLE'] != 'Student')]
df['NA_Address'].values

def generate_geocodes(addresses):
    columns = ['lng', 'lat']
    for address in addresses:
        try:
            location = gmaps.geocode(address)[0]['geometry']['location']
            lat.append(location['lat'])
            lng.append(location['lng'])
        except:
            print ('invalid address', address)
    data = np.array(lng, lat).T
    lng_lat = DataFrame(data, columns=columns)
    print (lng_lat)
    # lng_lat.to_csv()
# df.to_csv()
