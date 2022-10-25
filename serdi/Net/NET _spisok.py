import requests
import shutil
import os

s = 'robots.txt'
z = 'sitemap.xml'
with open('site.txt', 'r', encoding='UTF-8') as file:
    site = file.read()
    words = site.split()
for x in words:
    n = x + s
    c = x + z
    print (n, '\n', c)
dirname, filename = os.path.split(c)
r = requests.get(c, stream=True, verify=False)
if r.status_code == 200:
    print(str(r) + str(c))
elif r.status_code != 200:
        print (str(r) + str(c))
        
        with open (filename, 'wb') as f:
            r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


