import requests
import os
import re
from bs4 import BeautifulSoup
from datetime import datetime

print("\n==================================================================================================================")
print("This script Saves Your First 100 songs from a playlist into a .txt file with the same name of it(name of playlist)")
print("==================================================================================================================\n")

print(
    "PlayList Link: ( Example: https://www.youtube.com/playlist?list=PL6uvCzzzzzzzzzztXfsfj0Ol-zzzzzzzz )")
response = requests.get(input("Link: "))

SongList = []
current_time = datetime.now().strftime("%H:%M:%S / %d-%m-%Y")


def Output(PlayList_Name, SongsNumber):
    with open(PlayList_Name + ' - PlayList.txt', 'w', encoding='utf-8') as f:
        f.write("Backup Date:   " + current_time + "\n\n")
        for line in SongList:
            f.write(line.replace("dela", " / ")
                    [:-4] + " / " + line.replace("dela", " / ")[-4:] + "\n")
        f.write("\nTotal Songs: " + str(SongsNumber - 1))
    print("\nPlaylist " + PlayList_Name + " has been updated!")


def main():
    i = 1
    soup = BeautifulSoup(response.content, "html.parser")
    Name = soup.find("h1", {"class": "pl-header-title"}).text.strip()
    for tr in soup.findAll("table", {"id": "pl-video-table"}):
        for tr in soup.findAll("tr", {"class": "pl-video"}):
            SongList.append(str(i)+"." + tr.get_text().translate(
                {ord(c): None for c in ' \n'}))
            i += 1
    Output(Name, i)


if __name__ == "__main__":
    main()
