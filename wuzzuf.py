import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company = []
skill = []
location = []
links = []
job_type = []


# get the url 
results = requests.get('https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python%20developer')

#save page content
src = results.content

# create soup object to parse content
soup = BeautifulSoup(src, 'lxml')

# find the element containing our needs
job_titles = soup.find_all("h2", {"class" : "css-m604qf"})
companies = soup.find_all("a", {"class" : "css-17s97q8"})
locations = soup.find_all("span", {"class" : "css-5wys0k"})
skills = soup.find_all("div", {"class" : "css-y4udm8"})
job_types = soup.find_all("span", {"class" : "css-1ve4b75 eoyjyou0"})



for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append('https://wuzzuf.net' + job_titles[i].find('a').attrs['href'])
    company.append(companies[i].text)
    location.append(locations[i].text)
    skill.append(skills[i].text)
    job_type.append(job_types[i].text)
    
for link in links:
    result = requests.get(link)
    src = result.content
    soup_link = BeautifulSoup(src, 'lxml')
   
  

cols_list = [job_title, company, location, skill,links, job_type]

exported =zip_longest(*cols_list)
with open('desktop/wuzzuf.csv', 'w') as jobs:
    wr= csv.writer(jobs)
    wr.writerow(['job title', 'company', 'location', 'skills', 'links', 'job_type'])
    wr.writerows(exported)
    print("File Created")


