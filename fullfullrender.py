import requests
from bs4 import BeautifulSoup
import webbrowser

def render_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.get_text())

    links = soup.find_all('a')
    num_links = len(links)
    print(f"\nFound {num_links} link(s):\n")
    for i, link in enumerate(links):
        print(f"{i+1}. {link.get('href')}")

    while True:
        try:
            choice = int(input("\nEnter the number of the link you want to open (or 0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= num_links:
                selected_link = links[choice - 1]
                selected_url = selected_link.get('href')
                if selected_url.startswith('http://') or selected_url.startswith('https://'):
                    webbrowser.open(selected_url)
                    break
                else:
                    selected_url = url + selected_url
                    webbrowser.open(selected_url)
                    break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    while True:
        user_url = input("Enter the URL of the page you want to render (or 'exit' to quit): ")
        if user_url.lower() == 'exit':
            break
        else:
            render_html(user_url)
