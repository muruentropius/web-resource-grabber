import requests as req
from bs4 import BeautifulSoup as bs


def make_soup_by_url_with_common_headers(self, url):
    raw_html = http_get_response_with_common_headers(url)
    soup = make_parsable_object_with_raw_html(raw_html)
    return soup


def http_get_response_with_common_headers(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"}
    r = req.get(url, headers=headers)

    return r.text


def make_parsable_object_with_raw_html(html):
    return bs(html, 'html.parser')


def download(url, name="cat.png"):
    r = req.get(url)
    with open(name, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
