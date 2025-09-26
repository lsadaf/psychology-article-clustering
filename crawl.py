import requests
from bs4 import BeautifulSoup
import csv




def get_article_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    abstract_tag = soup.find('div', class_='padding_abstract justify rtl')
    if abstract_tag :
        abstract = abstract_tag.text.strip()  
    else :   
        return None , None
    
    keyword_tags1 = soup.find_all('li', class_='padding-3')
    keyword_tags2 = [tag.find_all('a', class_='tag_a') for tag in keyword_tags1]
    
    keywords = [tag.text.strip() for sublist in keyword_tags2 for tag in sublist]
    
    return abstract, keywords


def save_to_csv(url, abstract, keywords):
    with open('D:/Data Mining/project/all_articles300.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([url, abstract, ','.join(keywords)])

def main():
    base_url = 'https://japr.ut.ac.ir/article_'
   # article_numbers = range(52308, 52278, -1) 
    count = 0
    i = 95766
    
    while(count < 300):
        url = f'{base_url}{i}.html'
        i -= 2
        abstract, keywords = get_article_data(url)
        if abstract is not None :
            count += 1
            save_to_csv(url, abstract, keywords)
            print(count)


if __name__ == '__main__':
    main()
