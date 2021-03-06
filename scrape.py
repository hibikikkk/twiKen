import random

import requests
from bs4 import BeautifulSoup

q = "python filter:videos"

lang = "ja"

HEADERS_LIST = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]

HEADER = {'User-Agent': random.choice(HEADERS_LIST)}

# pos = "cm+55m-aDFbsEssJDsasIJEEEs-aDbDIJsXaabvbvJbJIv-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWMCwAACRAAICABDXAQyBIcsDKIuKweBSgAoECCCGoGEkIIQaUSQOgGhhoCAsIwYNBg7DQAYCsS6JgWEMUIAFpEGCRBAgAAUtCYIEAAABYOyqiKEICAUUgEIpqAEABQBKGggCGQFwQH8RIYEQAADkYMUgCQKDEoA0gJGhwkAAS1ABjAhMUCBET+ABoERhBEwiDApwgMCoyMGWBAYAEQACgQDwjZCoKAEckZmApbBEQFLnyDRwBgRDYATEA1wYHCCEAQBIOsIAABqSAMBnKUpMDDxCIywIyAIAVIEEQISVgIBGBghkSHeBAfQKjOaqUANBGCE0YIoSAAAQmoGpDU4cQyiYlQExAA0zSGnAaEAhggxICREgBABu6QARB0gSjTJAkAYYBDCECQpAJQAAQABrAgRQA6kCZQC4kQQAAQEDUA1UBAATwNwAAAATdJcSQ08C9ABYQAgFKEYhAhKQRimRCFJQQigRRSqFAEgABWALIEFuBgQFoQnBUgFWYgAgxQIwSAGZCFIUJIFikCuBQICAJCQAiGiuQJRBEQSAERgANQCMQABIgAyammQiZWAAghMiQqyi8AGA8BIiQUAwGJoCAhhAoMgEMAKAxkQEIShLgDwMgIDHgFIAhlDgVgwGAEiAFmLzYagYUCOEEIQWWBgUBTYIEEwAAEYLgIBYohAiAIgQEVCAMADKDGCCIqISqIIIEkQBgAAhQIkCmIBIOoIAAChFICQUgdUAiWi6GZAkGAgaghEhQJLgBAIygMIsBAgA0AQKAAAvcICQQBAChAgqgFgoYtcCAQiBFiEAByBOAoAMLThFQAAgAAAAAwSRI5/MVUJMtBlAGFQABEVwAIBMSQRIrAAAdEQgApAZMAd1JgjNpEUHoAIAIkEEAYIESDgo2SECAAEYRYdQMiWtMQAaDAQ==-T-0-10"
pos = "cm+55m--aDbDIJJDaXbDEJFXEDD-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWAgoAABQAAACAAAAIBQAAAAAAAAAAAgQAAAAAAQAAEAAAAAAAAAAIAAAAIAgAAAIAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAACAAAAUAABAAAAAAAAAQAAQAAAAAAAAAAAAAAAAgAAAAAAABAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAIAAAAAAABAAAAAQAAAAAAAAgAAAAAAAAAAAgAAAAAAAAIAAAAABAQAAAAAAAAAgAAAAAIAEAAgIQAAAAAAAAAAAAAAAAAAAAAAAIAAAEAAAAAAAAAAIAAAgAAAAAAAAAAAAAAAAAAAAAAAAQAAABAACAAAAAAAAAAAABAAAAAQAIAAEAAAAAAAAAAACAAAAAAAKAAAAFAAAAAAAAAAAAIAAAAAgAAAAAAAABAAIAAAQgAAAAAAAIAAAAAAAAAAAAAAAABAAAABBAAAAAAAAAAAAIAABAAIAIAAAAAAAAEAAAAAIAAAAAAAAAAAAAACAAAAAABSAAAAAAAAEAAAAQACAAAAAAAAAAACAAAAAAIABABAAAgAZAAAAAAAAAAAAAQAEAAAAAAAAAAAAAAIBAAAAAQCBAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAQCAAAAAAAAAAABAAAAAACAAAEAAAAAAAAAAAAAAACACAIAAAAAAAAQAAAAAAAAAAAAAAgBAAKgAAAAAAAQAAAAAAYAAAAICAAAAAAABABAAAAAAAgAAAAAAAAAAAAgAAEAAABAAAAAAAAAAAAAAAAAAABAAAAIAAAAAAQAAAAAAAAAACCIAAAAAAAAAAAAAAAQABAAAAAIAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAIAAEAAAAAAAggAAAAAAAAAAAAAAAAgAAAQAAAAAAAABAAAAAACAgIACACAA==-T-0-0"

base_url = "https://twitter.com/i/search/timeline"

html = requests.get(f'https://twitter.com/search?f=tweets&vertical=default&q={q}&l={lang}', headers=HEADER)
pos = BeautifulSoup(html.text, "html.parser").find_all("div", "stream-container")[0].attrs["data-min-position"]

# soup = BeautifulSoup(html.text,"html.parser").find_all('li', 'js-stream-item')
for retry in range(10):
    html = requests.get(url=base_url, params={"q": q,
                                              "vertical": "default",
                                              "max_position": pos,
                                              "src": "typd",
                                              "include_entities": "2",
                                              "include_available_features": "1",
                                              "lang": lang
                                              }, headers=HEADER)  # .json()["items_html"]
    print(pos)
    print(html)
    pos = html.json()["min_position"]
    # pos = BeautifulSoup(html, "html.parser").find_all("div", "stream-container")[0].attrs["data-min-position"]

# tweets = list(Tweet.from_html(html.text))
#
# for tweet in tweets:
#     print(tweet.icon)
#     print(tweet.text)


# print(json.load(html.text)["items_html"])

#  'https://twitter.com/i/search/'+ user_id +'/timeline/tweets?include_available_features=1&include_entities=1&max_position='+ max_position +'&reset_error_state=false'
