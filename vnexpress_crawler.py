from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
from underthesea import word_tokenize

# url =  'https://vnexpress.net'
urls= [
    'https://vnexpress.net',
    'https://vnexpress.net/thoi-su',
    'https://vnexpress.net/the-gioi',
    'https://vnexpress.net/kinh-doanh',
    'https://vnexpress.net/giai-tri',
    'https://vnexpress.net/the-thao',
    'https://vnexpress.net/suc-khoe'   
]


def crawl():
    output = set()

    for url in urls: 
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        new_feeds = soup.find_all('h3', class_='title-news')
        
        for feed in tqdm(new_feeds):
            article = feed.find('a')
            title = str(article.get('title')).strip()
            output.add(title)
            
        new_feeds = soup.find_all('h4', class_='title-news')
        
        for feed in tqdm(new_feeds):
            article = feed.find('a')
            title = str(article.get('title')).strip()
            output.add(title)

    return output

if __name__ == '__main__':
    output = crawl()
    
    with open('vnexpress_271_titles.txt', 'w') as f, \
        open('vnexpress_271_titles_segmented.txt', 'w') as f_seg: 
        for title in output:
            f.write(title + '\n')
            title = word_tokenize(title, format="text")
            f_seg.write(title + '\n')

    
    
