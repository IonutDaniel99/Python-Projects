from bs4 import BeautifulSoup
import requests
import os

Link = "https://www.youtube.com/playlist?list=PL6uvCMyxa2PgiL4tXfsfj0Ol-KMD5dy0Z"
response = requests.get(Link)


def SongList(name, author, time):
    with open('backup.txt', 'w', encoding='utf-8') as f:
        f.write(str("%s / %s / %s" % (name, author, time)))


soup = BeautifulSoup(response.content, "html.parser")
Name = soup.find("h1", {"class": "pl-header-title"}).text.strip()
Songs = soup.select("table", {"id": "pl-video-table"})

for tr in soup.findAll("tbody", {"id": "pl-load-more-destination"}):
    for td in tr.findAll("tr", {"class": "pl-video yt-uix-tile"}):
        for a in td.findAll("a", {"class": "pl-video-title-link"})[0]:
            song_name = a
        for b in td.findAll("div", {"class": "pl-video-owner"})[0]:
            song_author = td.findAll("a")[2].get_text()
        for c in td.findAll("td", {"class": "pl-video-time"})[0]:
            song_time = td.findAll("div", {"class": "timestamp"})[0].get_text()
    SongList(song_name, song_author, song_time)
    print(song_name + song_author + song_time)
