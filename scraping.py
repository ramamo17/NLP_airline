# %%
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# %%
session = requests.Session()

# %%
my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
# %%
# url = 'https://communityfoundations.ca/find-a-community-foundation-map/'
url = 'https://www.tripadvisor.fr/Airline_Review-d8728997-Reviews-Air-Botswana'
# url = "https://www.tripadvisor.fr/Airline_Review-d8728984-Reviews-Adria-Airways-No-Longer-Operating"
response = session.get(url, headers=my_headers)
# %%
html_soup = BeautifulSoup(response.text, 'html.parser')
# %%
container = html_soup.find_all(["h2", "h3"], 
                               class_=lambda x: x != 'hidden')
# %%
url = 'https://www.tripadvisor.fr/Airline_Review-d8728997-Reviews-Air-Botswana'
response_ta = session.get(url, headers=my_headers)
soup = BeautifulSoup(response_ta.text, 'html.parser')
# %%
url = 'https://www.tripadvisor.com/Airline_Review-d8728997-Reviews-Air-Botswana'
response_ta = session.get(url, headers=my_headers)
soup = BeautifulSoup(response_ta.text, 'html.parser')
# %%
reviews = soup.find_all('div', class_="lgfjP Gi z pBVnE MD bZHZM")
# reviews = soup.find_all('span', {"class": "QewHA H4 _a"})
# reviews = soup.find_all(["div", "span"], 
#                                class_=lambda x: x != 'hidden')
for review in reviews:
    rating = review.find('div', class_="Hlmiy F1").text
    review_comment = review.find('span', class_='QewHA H4 _a').text
    print(review_comment, '---------------------------')
    review_text = review.find('p', class_='review-text').text
# %%
for lines in reviews:
    print(lines.text)
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