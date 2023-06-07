import requests
from bs4 import BeautifulSoup

def render_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.get_text())

def main():
    url = input("Enter the URL of the web page: ")
    render_html(url)

if __name__ == '__main__':
    main()
