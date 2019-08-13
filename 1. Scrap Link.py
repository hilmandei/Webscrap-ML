from bs4 import BeautifulSoup
import requests
import joblib
import numpy as np

jmlhal = 500
listads = []
listid = []


# Scrapping the link
for b in range(1, jmlhal+1):
    page = f'https://www.olx.co.id/mobil/bekas/?page={b}'
    x = requests.get(page)
    y = BeautifulSoup(x.content, 'html.parser')
    ads = y.find_all('a', class_="marginright5 link linkWithHash detailsLink")
    for i in range(len(ads)):
        listads.append(ads[i]['href'])
        print(ads[i]['href'])

# for i in listads:
#     x = requests.get(i)
#     y = BeautifulSoup(x.content, 'html.parser')
#     idads = y.find_all("span", class_="rel inlblk")[0].text
#     listid.append(idads)
#     print(idads)

print(len(listads))
# print(len(listid))
# dict1 = dict(zip(listid, listads))
# print(len(dict1))

# save = np.array(list(dict1.values()))


# Save the list
joblib.dump(listads, 'listads1')


