from urllib.request import urlopen
import requests


def download_photo(image_url: str, image_name: str):
    resource = urlopen(image_url)
    out = open(f"data/images/{image_name}", 'wb')
    out.write(resource.read())
    out.close()


def get_proxy_request(proxy):
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    return session


def get_response(url: str, headers=None):
    if not headers:
        headers = {'Content-Type': 'text/html', }

        return requests.get(url, headers)
    else:
        return requests.get(url)

