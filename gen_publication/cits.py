import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept-language': 'en-US,en;q=0.9',
    'x-requested-with': 'XHR',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

s = requests.Session()
s.headers.update(headers)
url = f'https://scholar.google.com/citations?hl=en&user=lPTdGRMAAAAJ'
r = s.post(url)
soup = bs(r.text, 'html.parser')
cit = str(soup.find("div", {"id": "gsc_rsb_cit"}))

filename = "./_includes/gs_citations.html"

with open(filename, "w+") as f:
    f.write(cit)
    print("Saved citations to", filename)
