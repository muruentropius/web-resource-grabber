def save_lyrics(filename='New_Lyrics.txt', data=""):
    with open(filename, 'w') as f:
        f.write(data)
