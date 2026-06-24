import urllib.request
import re

req = urllib.request.Request('https://commons.wikimedia.org/wiki/File:Poiuyt.svg', headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    links = re.findall('https://upload.wikimedia.org/wikipedia/commons/[^\"]+Poiuyt.svg', html)
    print("Found links:")
    for link in set(links):
        print(link)
except Exception as e:
    print("Error:", e)
