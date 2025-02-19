import urllib.request
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
request = urllib.request.Request(url, headers=headers)

try:
    html = urllib.request.urlopen(request)

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")

soup = BeautifulSoup(html, "html.parser")

# getting text
text = soup.get_text("", strip=True)    
with open("page_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

# getting links
links = soup.find_all('link')

# getting images
images = soup.find_all('img')
print(images)
  