from youtubesearchpython import *

def URL_Search_YT(search_term): #Gibt eine Liste mit dem Link zum Video, dem Namen des Videos und der länge des Videos zurück
    if 'https://' in search_term:
        video = Video.getInfo(search_term, mode = ResultMode.json)
        duration = int(video['duration']['secondsText'])
        duration = f'{duration // 60}:{duration % 60}'
        return([video['link'],video['title'],duration])
    else:
        videosSearch = VideosSearch(search_term, limit = 1)
        result = videosSearch.result()
        return([result['result'][0]['link'],result['result'][0]['title'],result['result'][0]['duration']])

