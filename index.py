# importing the requests library
import requests
import json
import os, errno
from urllib.parse import urlparse

# Change to necessary url
URL = "https://yoursite.com/wp-json/wp/v2/[pages, posts, custom post type]?_embed"

print("Creating images folder")
try:
    original_umask = os.umask(0)
    os.makedirs("./images", 0o755)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
finally:
    os.umask(original_umask)

print("Folder was created")
print("Sending requests...")
res = requests.get(URL)
print(res.status_code)
if res.status_code == 200:
    print("Ok...")
    pages = res.headers["x-wp-totalpages"]
    print("Total pages: " + pages)
    page = 1
    def loadImages(url):
        res = requests.get(url)
        if res.status_code == 200:
            dataFormated =  res.content.decode("utf-8")
            symbol =dataFormated.find("[")
            allData = json.loads(dataFormated[symbol:])
            for data in allData:
                if 'wp:featuredmedia' in data['_embedded']:
                    url = data['_embedded']['wp:featuredmedia'][0]['source_url']
                    urlData = urlparse(url)
                    imageName = os.path.basename(urlData.path)
                    imageData = requests.get(url)
                    open("images/" + imageName, "wb").write(imageData.content)
                    print(imageName)
        else:
            print("Can't make request: " + url)

    while page <= int(pages):
        print("Page #: " + str(page))
        loadImages(URL + "&page=" + str(page))
        page+=1
     print("Done!")
else:
     print("Can't make request: " + URL)