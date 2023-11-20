import urllib.request
import json


def get_all_video_in_channel(channel_id):
    api_key = "AIzaSyBd9-w1yBcoTsE0y30_Olikk4zCPe8SZ-Q"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url, timeout=1)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links

huberman_channel_id = "UC2D2CMWXMOVWx7giW1n3LIg"

links = get_all_video_in_channel(huberman_channel_id)

with open("Hubrman video links.txt", "w", encoding='utf-8') as file:
    for link in links[::-1]:
        file.write(link + '\n')
print(links)
