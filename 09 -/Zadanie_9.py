import webbrowser


def ensure_correct(url):
    return url.startswith()


def get_url():
    url = input("Podaj url do otwarcia: ")
    if url.startswith('https://') or url.startswith('http://'):
        return url
    else:
        print("Błąd")


def main():
    try:
        url = get_url()
        webbrowser.open(f'https://{url}')
    except:
        print()



if __name__ == '__main__':
    main()
