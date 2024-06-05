import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories(hnlist):   # Sort by points in descending order
    return sorted(hnlist, key=lambda k: k['Points'], reverse=True)  

def create_custom_hn(links, subtext):
    hn = []
    for item, sub in zip(links, subtext):
        title = item.getText()
        href = item.find('a').get('href')
        vote = sub.select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points > 420:
                hn.append({'Title': title, 'Link': href, 'Points': points})
    return sort_stories(hn)

hn_combined = []
for page in range(1, 6):  # Iterate over pages 1 to 5
    res = requests.get(f'https://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    hn_combined.extend(create_custom_hn(links, subtext))

hn_combined = sort_stories(hn_combined)
pprint.pprint(hn_combined)