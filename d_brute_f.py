from urllib.request import urlopen
from urllib.request import HTTPError
from time import sleep
from urllib.request import Request
import csv
import ssl


# 'wordlists/directory-list-2.3-small.txt'
with open('wordlists/directory-list-custom.txt', "r") as File:
    data = [line.strip() for line in File.readlines()]

founded_urls = []
for i in data:
    url = "http://127.0.0.1/community_site/"
    url += i.strip()
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')

    try:
        sleep(0.05)
        print(f"Testing {url}...")

        context = ssl._create_unverified_context()
        a = urlopen(req, context=context)

        if a.getcode() in [301, 302]:
            print(f"[+] Redirected: {url} -> {a.geturl()}")
        elif a.getcode() == 403:
            print(f"[+] Forbidden but Exists: {url}")
        else:
            print(f"[+] Found: {url}")
            founded_urls.append(url)
    except HTTPError as e:
        if e.code == 429:  # Too Many Requests
            print(f"[-] Rate limit hit. Slowing down...")
            sleep(5)
        # print(f"[-] Error {e.code}: {e.reason}")
        continue

print("----------------------------------------------------------------------------------")
print("[+] Found URLs")

for j in founded_urls:
    print(j)

with open('found_urls.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Found URLs"])
    for url in founded_urls:
        writer.writerow([url])

File.close()
