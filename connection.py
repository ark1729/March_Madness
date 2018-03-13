import requests

def connection(url):
    r = requests.get(url)
    try:
        r.raise_for_status()
    except Exception as exc:
        print('%s' % (exc))
    print(r)

print('URL?')
uurl = input()
connection(uurl)
