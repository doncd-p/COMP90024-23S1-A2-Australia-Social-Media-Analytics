import subprocess
import json

import sys

file_location = sys.argv[1]
ip = sys.argv[2]
database = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]

# load the data
with open(file_location, 'r') as f:
    twitter_cdb_bulk = json.load(f)

# create the database
subprocess.run(f'curl -X PUT http://{ip}:5984/{database} -u {username}:{password}', shell=True)

# uplaod 10000 at a time
for i in range(len(twitter_cdb_bulk['docs'])//10000):
    out = {'docs': twitter_cdb_bulk['docs'][i*10000:(i+1)*10000]}
    json_data = json.dumps(out).encode('utf-8')
    subprocess.run(['curl', '-X', 'POST', f'http://{ip}:5984/{database}/_bulk_docs', '--header', 'Content-Type: application/json', '--data-binary', '@-', '-u', f'{username}:{password}'], input=json_data)

out = {'docs': twitter_cdb_bulk['docs'][(i+1)*10000:len(twitter_cdb_bulk['docs'])]}
json_data = json.dumps(out).encode('utf-8')
subprocess.run(['curl', '-X', 'POST', f'http://{ip}:5984/{database}/_bulk_docs', '--header', 'Content-Type: application/json', '--data-binary', '@-', '-u', f'{username}:{password}'], input=json_data)
