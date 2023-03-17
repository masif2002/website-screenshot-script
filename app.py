import requests
import img2pdf

ACCESS_KEY = 'YOUR_ACCESS_KEY'
URLS = ['github.com/masif2002', 'mohamedasif.web.app']

path = './screenshots.pdf'
screenshots = []

for url in URLS:
    print("\nstart", url)
    API_ENDPOINT = f'https://api.screenshotone.com/take?access_key={ACCESS_KEY}&url=https%3A%2F%2F{url}&device_scale_factor=1&format=jpg&block_ads=true&block_cookie_banners=true&block_trackers=true&cache=false'

    res = requests.get(API_ENDPOINT, stream=True)

    if res.status_code == 200:
        screenshots.append(res.content)
        print("done", url)
    else:
        print("failed", url)

# Saving it as pdf
file = open(path, 'wb')

pdf = img2pdf.convert(*screenshots)

file.write(pdf)

file.close()
    