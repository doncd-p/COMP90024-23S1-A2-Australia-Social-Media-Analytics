import pandas as pd
import subprocess
import json


data = pd.read_parquet('../data/curated/twitter_with_sent.parquet')

data['neu_score'] = 1-data['pos_score']-data['neg_score']
data = data.drop('sentiment', axis = 1)

data['p>n'] = data['pos_score']>data['neg_score']
data['p>nu'] = data['pos_score']>data['neu_score']
data['nu>n'] = data['neu_score']>data['neg_score']

import geopandas as gpd
from shapely.geometry import Point

# Load the GeoPandas polygon data
polygon_gdf = gpd.read_file("../data/raw/Geography/2021_ELB_region.shp")


def get_Electorate(coord):
    for idx, polygon in polygon_gdf.iterrows():
        if polygon.geometry.contains(coord):
            return polygon['Elect_div']
    
    return None


for id, row in data.iterrows():

    # coord
    coord = Point(row["x_cent"], row["y_cent"])
    electorate = get_Electorate(coord)
    print(electorate)

    if row['p>n']:
        if row['p>nu']:
            sentiment = 1
        else:
            sentiment = 0
    elif row['p>nu']:
        if row['p>n']:
            sentiment = 1
        else:
            sentiment = -1
    elif row['nu>n']:
        if row['p>nu']:
            sentiment = 1
        else:
            sentiment = 0


    text = row['text']
    text = text.replace("'", "\\'")

    
    row_json = {"id": f"{row['_id']}", "author_id": f"{row['author_id']}", "date": f"{row['date']}", "text": text, 
            "is_political": f"{row['is_political']}", "neg_score": f"{row['neg_score']}", "neu_score": f"{row['neu_score']}", 
            "pos_score": f"{row['pos_score']}", "compound_score": f"{row['compound_score']}", "sentiment": f"{sentiment}", 
            "electorate": f"{electorate}"}
    
    json_data = json.dumps(row_json).encode('utf-8')

    subprocess.run(['curl', '-X', 'POST', 'http://172.26.131.22:5984/socialmediadatabase', '--header', 'Content-Type: application/json', '--data-binary', '@-', '-u', 'admin:password'], input=json_data)