
import urllib.request
import csv
import json
import pandas as pd
import requests
import urllib3
from bs4 import BeautifulSoup
import lxml
csv_file = 'data3.csv'
dt1 = ['mux','vulcun-2','blissfully','stypi','flirtey','rimeto','tetra','hush','subdream-studios','stedi','magnar','princeton-ventures',
      'hulu','kylie-ai','distributed-systems','bridge','keyme','educents','movewith','fountain','bluecrew','phil','solugen','govpredict',
      'ring','techmate','optimus-ride','mantl','the-hustle','meta','ramen-ventures','joymode','fullcontact','quartzy',
      'trendmd','salido','shift','plastiq','mapbox','shippo','moment','wonolo','gravity-group','pilot','leo','radiopublic','windfall-data',
      'simpleprints','homelight','techstars','voxy','zeus','designer-fund','good-co','merchbar','zendrive','rubikloud','arthena','txn',
      'datawire','airfox','terminal-49','onemove','loom','nautilus-labs','workstep','fieldwire','carbon','real-ventures','compass',
      'routific','survata','truevault','radiusagent','maven','pingpad','eden','fitbod','returnbase','bizly','upcall','focal-systems',
       'pinterest','500-startups','sickweather','chewse','particle','scalyr','pixlee','superhuman','alloy','truebill','winnie','kite',
       'imgix','stripe','memsql','careguide','ngdata','sensor-tower','equidate','kinetic','wrapify','revcascade','studio','akido-labs',
       'dv01','starcity','republic','amitree','onfleet']

data_col = {'website':{},'phone_number':{},'twitter':{},'facebook':{},'contact_email':{},'linkedin':{}}
key = data_col.keys()
csv_columns = key

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()

for d in dt1:
        req = urllib.request.Request('https://www.crunchbase.com/v4/data/entities/organizations/'+d+'?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,'
                             '%22title%22,%22short_description%22,%22is_locked%22%5D&layout_mode=view',  headers={
    'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        df = pd.read_json(html)
        data1 = json.loads(html)
        key = data1['cards']['overview_fields2'].keys()
        dict_data = data1['cards']['overview_fields2']


        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writerow(data1['cards']['overview_fields2'])

csv_input = pd.read_csv('data3.csv')
csv_input['Name'] = csv_input['website']
csv_input.to_csv('data3.csv', index=False)


r = csv.reader(open('data3.csv'))
lines = list(r)

i = 1
for d in dt1:
    lines[i][6] = d
    i = i + 1
j = 1

writer = csv.writer(open('data3.csv', 'w'))
writer.writerows(lines)