import pandas as pd



data = pd.read_parquet('../data/curated/twitter_sentiment.parquet')

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

sentiment_list = []
text_list = []
electorate_list = []

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

    
    sentiment_list.append(sentiment)
    text_list.append(text)
    electorate_list.append(electorate)


data['sentiment'] = sentiment_list
data['text'] = text_list
data['electorate'] = electorate_list

data.to_parquet('./fully_cleaned_tweets.parquet')