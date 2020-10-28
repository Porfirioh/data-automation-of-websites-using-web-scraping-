from bs4 import BeautifulSoup
import requests

global seed

url = "https://allgovernmentjobs.in/latest-government-jobs"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

links = soup.find_all('a', {'class':'btn btn-sm m-0 btn-outline-primary waves-effect pl-3 pr-3'})

len_url = len(links)

seed_array=[]

for link in links:
    #print("https://allgovernmentjobs.in/"+link.get('href'))
    #print(len_url)
    seed="https://allgovernmentjobs.in/"+link.get('href')
    seed_array.append(seed)
seedlen = len(seed_array)
print (seedlen)
print (seed_array)
    
