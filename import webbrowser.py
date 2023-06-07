import webbrowser

def main():
    while True:
        url = input('Enter a URL (or "exit" to quit): ')
        if url.lower() == 'exit':
            break
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
