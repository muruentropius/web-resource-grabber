import requests as req
import numpy as np
import sys


from bs4 import BeautifulSoup as bs
from pprint import pprint


from http_modules import make_soup_by_url_with_common_headers, http_get_response, make_parsable_object_with_raw_html, download
from get_input import get_input
from save_lyrics import save_lyrics
from make_url import make_artist_songs_url
from slicing_html import get_maxpage_num

if __name__ == "__main__":
    artistId = int(input("Please Enter the artistId of which artist you want."))
    lyrics_grabber = MelonLyricsGrabber(artistId)

    
class MelonLyricsGrabber():
    def __init__(self, artist_id):
        self.artist_id = artist_id
        self.artist_page_html = 'https://www.melon.com/artist/song.htm?artistId={}'.format(self.artist_id)
        self.song_list_without_startindex = "https://www.melon.com/artist" +
        "/song.htm?artistId={}#params%5BlistType%5D=A&params%5BorderBy" +
        "%5D=ISSUE_DATE&params%5BartistId%5D={}&po=pageObj&startIndex={}".format(self.artist_id, self.artist_id, 1)
        
        self.song_id_list = __get_all_song_id_list(artist_id)
        
    def __get_all_song_id_list(self, artist_id):
        total_song_num = __get_total_song_number()
        total_song_pages = (total_song_num + 49) // 50
        for song_index in range(total_song_pages):
            start_song_num = 50 * song_index + 1
            end_song_num = min(50 * (song_index + 1), total_song_num
            song_list_url_banded = __make_song_list_url_by_song_num_band(start_song_num, end_song_num)
            soup = make_soup_by_url_with_common_headers(song_list_url_banded).find_all('button', attrs={'data-song-no': True})
            for tag in soup:
                print(tag['data-song-no'])
            


    def __get_max_song_number(self):
        soup = make_parsable_object_with_raw_html(self.artist_page_html).find("참여 보기")
        for possible_string in soup.find("참여 보기").strings:
            if possible_string != "발매":
                total_song_num = int(possible_string[1:-1])
                break

        return total_song_num
    def __make_song_list_url_by_song_num_band(start_song_num, end_song_num):
        return "https://www.melon.com/artist" +
        "/song.htm?artistId={}#params%5BlistType%5D=A&params%5BorderBy" +
        "%5D=ISSUE_DATE&params%5BartistId%5D={}&po=pageObj&startIndex={}".format(start_song_num, end_song_num)
    def down_all_lyrics(self):
        
    def down_one_lyrics_with_songid(self, songid):
        
        
    
    
    
music = music_lyrics_grabber_melon()
music.download_with_artistid(108363)
# Shell code(SGWANNABE): python main.py 108363