import requests
import base64

url = "https://www.oebp.org/solve.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
    "Sec-Ch-UA": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-UA-Mobile": "?0",
    "Sec-Ch-UA-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

params = {"bp": "1", "referrer": "https://www.oebp.org/solve.php?bp=1246"}

response = requests.get(url, headers=headers, params=params)

page = response.text

s_img_idx = page.find('<img src=') + 10
e_img_idx = page.find('\" /><')

encoded_image = page[s_img_idx:e_img_idx]
