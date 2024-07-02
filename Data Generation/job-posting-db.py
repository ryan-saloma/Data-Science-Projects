
import requests
import pandas as pd
import json

search_terms = ['data', 'analyst', 'District-of-Columbia']

# date_posted = 3days
# employment_type = FULLTIME
# query = data analyst in District-of-Columbia

base_url = "https://jsearch.p.rapidapi.com/search" 
query = "?query=" + "%".join(search_terms) +\
"&employment_type=FULLTIME&date_posted=week&num_pages=1&page_num="

payload = {}
headers = {
  'x-rapidapi-host': 'jsearch.p.rapidapi.com',
  'x-rapidapi-key': 'XXXXX'
}

url = base_url + query
df = pd.DataFrame()
for i in range(50):
    tmp_url = url + str(i)
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    tmp_df = pd.DataFrame(data["data"])
    if df.empty: 
        df = tmp_df.copy()
    else:
        df = pd.concat([df,tmp_df], ignore_index=True)
        df.reset_index()

df.to_csv('job_postings_2024-07-02.csv')
