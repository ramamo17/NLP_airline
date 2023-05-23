# %%
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

key_api_google="AIzaSyDcZIgjyoPZ5suy-zT6BbsnsjVf_Lt6eRk"
# %%
session = requests.Session()

# %%
my_headers = {"User-Agent": "Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
# %%
# url = 'https://communityfoundations.ca/find-a-community-foundation-map/'
url = 'https://www.google.com/search?gs_ssp=eJzj4tTP1TcwzDE1MjVgtFI1qDAxTzUzN00yTEs0SzROMkyxMqiwTDG3SElNMTcxTkmyMDEy8uLJL8qpVEjMLCrILyoBAClAEpk&q=orly+airport&oq=orly&aqs=chrome.1.69i57j46i67i175i199i433i650j0i512j0i433i512j46i131i175i199i433i512l2j0i433i512j0i131i433i512j0i433i512j0i271.2999j0j7&sourceid=chrome&ie=UTF-8#lrd=0x47e675b1fa6a3b1d:0x9d78ded743db8422,1,,,,'
# url = 'https://www.tripadvisor.fr/Airline_Review-d8728997-Reviews-Air-Botswana'
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