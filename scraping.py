# %%
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
# %%
session = requests.Session()

# %%
my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS          X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko)          Chrome/71.0.3578.98 Safari/537.36",           "Accept":"text/html,application/xhtml+xml,application/xml;          q=0.9,image/webp,image/apng,*/*;q=0.8"}
# %%
url = 'https://communityfoundations.ca/find-a-community-foundation/'
response = session.get(url, headers=my_headers)
# %%
html_soup = BeautifulSoup(response.text, 'html.parser')
# %%
container = html_soup.find_all(["h2", "h3"], 
                               class_=lambda x: x != 'hidden')
# %%
url = 'https://www.tripadvisor.fr/Airline_Review-d8728997-Reviews-Air-Botswana'
response_ta = session.get(url, headers=my_headers)
soup = BeautifulSoup()
reviews = soup.find_all('span')
# %%
for lines in reviews:
    if lines.name == 'h2': 
        province = lines.text
        print('In', province, "\n")
    if lines.name == 'h3':
        foundation = lines.text
        print('Foundation name:', foundation)   
        print('Foundation url:', lines.find_all("a", 
            href=re.compile("cfc_locations"))[0].get('href'), "\n")
# %%
subresponse = []
for lines in container:
    if lines.name == 'h3': 
        url_fou = lines.find_all("a", href=re.compile("cfc_locations"))[0].get('href')
        subresponse.append(session.get(url_fou, 
                                       headers=my_headers))
        time.sleep(2)
# %%
df = pd.DataFrame({'Organization': organization,
                   'Title': gender_title,
                   'Addressee': person,
                   'Addressee Job Title': person_title,
                   'Civic Address 1 (Street Address)': street,
                   'Civic Address 2 (PO Box)': pobox,
                   'Municipality': municipality,
                   'Province or Territory': provinces, 
                   'Postal Code': postalCode,
                   'Phone': phone,
                   'Website': org_url
                   })
cols = ['Organization', 'Title', {add in here the others}]
df.to_csv('data/cfcMailingAddresses.csv', encoding='utf-8',
          index=False, columns=cols)