import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def display_links(soup):
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

def main():
    while True:
        url = input('Enter a URL (or "exit" to quit): ')
        if url.lower() == 'exit':
            break
        try:
            html = get_html(url)
            soup = parse_html(html)
            display_links(soup)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
