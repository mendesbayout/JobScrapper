import requests
from bs4 import BeautifulSoup
import pandas as pd




def extract(year):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
    url = f'https://www.indeed.com/jobs?q=Rov&start={page}'
    r = requests.get(url, headers)
    # return r.status_code > Check response
    # print(extract(0)) check response
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding = 'windows-1252')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', {'class':'summary'}).text.strip().replace('\n', '')

        job = {'title':title, 'company':company, 'salary':salary, 'summary':summary}
        joblist.append(job)
    return


joblist = []

for i in range(0, 10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

newfile = 'C:/Users/dev/PycharmProjects/pythonProject5/output_file.pdf'
html = 'C:/Users/dev/PycharmProjects/pythonProject5/html.html'

df = pd.DataFrame(joblist)
df.to_html(html)

pdf.from_file('html.html', newfile)


print(df.head())

##ensure encoding
with open('jobs.json', 'w', encoding = 'utf-8') as file:
    df.to_json('jobs.json', indent = 4, orient = "records", force_ascii = False)

with open('jobs.json') as f:
    print(f)



