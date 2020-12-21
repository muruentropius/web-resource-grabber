from http_modules import http_get_response, parse_html, download
from save_lyrics import save_lyrics

def get_maxpage_num(artist_songs_url):
    html = http_get_response(artist_songs_url)
    soup = parse_html(html)
    print(soup)
    save_lyrics(data=html)
    # return len(soup.find_all(attrs={'class': 'page_num'}))
    soup.find
