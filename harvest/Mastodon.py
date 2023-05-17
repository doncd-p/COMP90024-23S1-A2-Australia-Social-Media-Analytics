import couchdb
from mastodon import Mastodon, StreamListener
import json
import pandas as pd
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
import numpy as np
import re
import subprocess

#http://172.26.133.251:5984/test_running_toot_db


# authentication
# admin = 'admin'
# password = 'password'
admin = 'group9_admin'
password = 'group9_H1'
# url = f'http://{admin}:{password}@172.26.130.136:5984/'
url = 'http://172.26.133.251:5984/'
database = 'test_running_toot_db'

# get couchdb instance
couch = couchdb.Server(f'http://{admin}:{password}@172.26.133.251:5984/')

# indicate the db name
db_names = ['test_running_toot_db']

# if not exist, create one
for db_name in db_names:
    if db_name not in couch:
        couch.create(db_name)

token = '2UqOce-h-VscNrEnWll30zPvmhyp0VfD4Vrv8Ks25h8'
m = Mastodon(
    # your server here
    api_base_url=f'https://mastodon.social',
    access_token=token
)

poli_key_words = pd.read_excel('Copy of Voting Keyword.xlsx')
poli_key_words = poli_key_words['keywords'].tolist()


def get_sentiment(x):
    """ Helper to extract sentiment """

    sia = SentimentIntensityAnalyzer()

    sia_out = sia.polarity_scores(x)

    neg = sia_out['neg']
    pos = sia_out['pos']
    neu = sia_out['neu']
    compound = sia_out['compound']

    sentiment = np.argmax([sia_out['neg'], sia_out['neu'], sia_out['pos']]) - 1

    return neg, pos, neu, compound, sentiment

def extract(input):
    """ Helper to extract text in betweein paragraph tags """
    
    # Use regular expression to extract the first text between <p> and </p > tags
    match = re.search('<p>(.*?)</p>', input)
    if match:
        # Extract the matched text group
        text = match.group(1)
        # Remove any HTML tags within the matched text
        clean_text = re.sub('<.*?>', '', text)

        return clean_text
    return input

def process_mastadon(toot):
    """ Process Mastadon data: input - a list of dictionaries, representing mastadon documents """

    # skip non english
    if toot['language'] != 'en':
        return None
    
    document = {}

    # add in the columns we are interested in
    document['_id'] = str(toot['id'])
    document['author_id'] = str(toot['account']['id'])
    if 'key_match' in toot:
        document['partial_match'] = 1
    else:
        document['partial_match'] = 0
    document['date'] = str(toot['created_at'])[:10]
    document['text'] = extract(toot['content'])

    # get the sentiment output
    neg, pos, neu, compound, sentiment = get_sentiment(document['text'])

    document['neg_score'] = neg
    document['neu_score'] = neu
    document['pos_score'] = pos
    document['compound_score'] = compound
    document['sentiment'] = sentiment

    return document


# listen on the timeline
class Listener(StreamListener):
    # called when receiving new post or status update
    def on_update(self, status):

        if [keyword for keyword in poli_key_words if f' {keyword} ' in f" {status['content']} "]:
            
            status_processed = process_mastadon(status)

            json_str = json.dumps(status_processed, indent=2, sort_keys=True, default=str)
            
            if status_processed:
                print(status_processed)
                status_processed = eval(str(status_processed))
                out = {'docs': [status_processed]}
                json_data = json.dumps(out).encode('utf-8')
                subprocess.run(['curl', '-X', 'POST', f'{url}/{database}/_bulk_docs', '--header', 'Content-Type: application/json', '--data-binary', '@-', '-u', f'{admin}:{password}'], input=json_data)

        elif any(keyword in status['content'] for keyword in poli_key_words):
            status['key_match'] = 'partial'
            status_processed = process_mastadon(status)
            
            if status_processed:
                print(status_processed)
                status_processed = eval(str(status_processed))
                out = {'docs': [status_processed]}
                json_data = json.dumps(out).encode('utf-8')
                subprocess.run(['curl', '-X', 'POST', f'{url}/{database}/_bulk_docs', '--header', 'Content-Type: application/json', '--data-binary', '@-', '-u', f'{admin}:{password}'], input=json_data)


            # with open("output.txt", "a") as f:
            #     f.write(f"Document saved with ID: {doc_id} and revision: {doc_rev} in social, partial, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        
# while True:
#     try:
#         m.stream_public(Listener())
#     except Exception as e:
#         continue

m.stream_public(Listener())
