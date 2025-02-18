# Already tested and implemented the scrapping process on jupyter notebook, copy paste it here. 67k entries were scrapped
# I still need to examine the data to make sure it is up to date and no discrepancies
import pandas as pd
import requests

vscodeDataSet = pd.DataFrame(columns = ['Extension Name','Publisher','Downloads','Rating','Verified','Published','Last Update']) # I might need more cols later

url = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery" # scrapping from this url
headers = {
        "Accept": "application/json;api-version=3.0-preview.1",
        "Content-Type": "application/json"
    }

to_add = {
    "Extension Name":[],
    "Publisher":[],
    "Downloads":[],
    "Rating":[],
    "Verified":[],
    "Published":[],
    "Last Update":[]
}
# 88 was found through trial and error. This is the maximum number of pages that can be scrapped 
for i in range(1,88):
    payload = {
            "filters": [
                {
                    "criteria": [
                        {"filterType": 8, "value": "Microsoft.VisualStudio.Code"}],
                    'pageNumber':i,
                    'pageSize':1000,
                    
                }
            ],
            "flags": 870
        }
    make_request = requests.post(url,headers=headers,json=payload)
    database = make_request.json()

    for x in range(0,1000):
        name = database['results'][0]['extensions'][x]['extensionName']
        publisher = database['results'][0]['extensions'][x]['publisher']['publisherName']
        downloads = database['results'][0]['extensions'][x]['statistics'][0]['value']
        rating = database['results'][0]['extensions'][x]['statistics'][-2]['value']
        verified = database['results'][0]['extensions'][x]['publisher']['isDomainVerified']
        published = database['results'][0]['extensions'][x]['releaseDate']
        lastUpdate = database['results'][0]['extensions'][x]['lastUpdated']
            
        new_row = pd.DataFrame([[name,publisher,downloads,rating,verified,published,lastUpdate]], columns=['Extension Name', 'Publisher', 'Downloads','Rating','Verified','Published','Last Update'])
        updated_VscodeDataSet = pd.concat([vscodeDataSet,new_row])

