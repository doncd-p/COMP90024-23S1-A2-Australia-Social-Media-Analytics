

if don't have geolocation:
    don't use

if not english: 
    don't use



1. electorate which it belongs to: 'Elect_div'
    -how to do it:
        -the state which coordinates belong to
            if have geolocation data:
            -geolocation detail: long lat
                -long = avg of two long points in bbox; lat = avg of two lat points in bbox; 
                    -1st and third are longitude; 2nd and 4th are latitude.
            
            geopandas: use coordinate in polygon to find which electorate area this tweet belongs to

2. does it contain keywords: bool

3. time of posting: yyyy-mm-dd  (datetime)
    -granularity to be checked

4. authorid

5. tweet id (unique identifier on our database)

6. text of the tweet




7. sentiment: compound score
8. sentiment: neg (round to 4 digits)
9. sentiment: pos (round to 4 digits)
10.sentiment: -1/0/1  (argmax of neg, pos and neu)






from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores(dict['doc']['data']['text'])

sia.polarity_scores("If hypothetically an ancient 700 year's or so Jewish temple was found in another country, say Spain or ??, Zionist's would claim that country as an ancient sister homeland of Israel then probably find some ancient text in 1 of their vault's saying that God gave them that land too")
