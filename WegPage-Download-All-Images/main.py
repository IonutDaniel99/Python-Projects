import requests
import sys
import re
import threading
from bs4 import BeautifulSoup as soup


def Get_Source(link):
    r = requests.get(link)
    if r.status_code == 200:
        return soup(r.text, "html.parser")
    else:
        sys.exit("[~] Invalid Response Received.")


def Get_Images(html):
    imgs = html.findAll("img")
    if imgs:
        return imgs
    else:
        sys.exit("[~] No images detected on the page.")


def Download_Images(link, name):
    try:
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            f = open(name, "wb")
            f.close()
            print("[*] Downloaded Image: %s" % name)
    except Exception as error:
        print("[~] Error Occured with %s : %s" % (name, error))


def main():
    print("Link(https://www.yyy.zzz): \n")
    link_input = input()
    html = Get_Source(link_input)
    tags = Get_Images(html)
    i = 1
    for tag in tags:
        src = tag.get("src")
        if src:
            src = re.match(r"((?:https?:\/\/.*)?\/(.*\.(?:png|jpg)))", src)
            if src:
                (link, name) = src.groups()
                Download_Images(link,  "Downloaded/" +
                              str(i) + name.split("/")[-1])
                i += 1


if __name__ == "__main__":
    main()
