from urllib.request import urlopen
from urllib.request import HTTPError
from time import sleep

# File = open('wordlists/directory-list-2.3-small.txt', "r")
File = open('wordlists/directory-list-custom.txt', "r")
data = File.readlines()

founded_urls = []
for j in data:
    url = "http://127.0.0.1/community_site/"
    url += j.strip() 

    try:
        sleep(0.05)
        print(f"Testing {url}...")
        a = urlopen(url)
    except HTTPError as e:
        # print(f"[-] Error {e.code}: {e.reason}")
        continue
    else:
        print(f"[+] Found: {url}")
        founded_urls.append(url)

print("----------------------------------------------------------------------------------")
print("[+] Founded URLs")

for i in founded_urls:
    print(i)

File.close()
