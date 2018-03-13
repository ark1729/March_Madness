import requests

def connection(url):
    user_agent='python-requests/4.8.2 (Compatible; Animus Silica; mailto: silicaanimus@gmail.com)'
    r = requests.get(url, headers={'User-Agent': user_agent}, timeout=10)
    try:
        r.raise_for_status()
    except Exception as exc:
        print('%s' % (exc))
    print(r)

print('URL?')
uurl = input()
connection(uurl)
