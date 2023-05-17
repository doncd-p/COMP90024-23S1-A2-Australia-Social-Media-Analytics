import couchdb
from mastodon import Mastodon, StreamListener
import json
import pandas as pd
from datetime import datetime

# authentication
admin = 'admin'
password = 'password'
url = f'http://{admin}:{password}@172.26.130.136:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name
db_names = ['mastodon_social_politics']

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

# listen on the timeline
class Listener(StreamListener):
    # called when receiving new post or status update
    def on_update(self, status):
        # do sth
        if [keyword for keyword in poli_key_words if f' {keyword} ' in f" {status['content']} "]:

            json_str = json.dumps(status, indent=2, sort_keys=True, default=str)
            #do something json func() 
            doc_id, doc_rev = couch['mastodon_social_politics'].save(json.loads(json_str))
            # with open("output.txt", "a") as f:
            #     f.write(f"Document saved with ID: {doc_id} and revision: {doc_rev} in social, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
        elif any(keyword in status['content'] for keyword in poli_key_words):
            status['key_match'] = 'partial'
            json_str = json.dumps(status, indent=2, sort_keys=True, default=str)
            #do something json func() 
            doc_id, doc_rev = couch['mastodon_social_politics'].save(json.loads(json_str))
            # with open("output.txt", "a") as f:
            #     f.write(f"Document saved with ID: {doc_id} and revision: {doc_rev} in social, partial, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
while True:
    try:
        m.stream_public(Listener())
    except Exception as e:
        continue
