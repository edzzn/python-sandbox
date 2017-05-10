import requests
import os
# FB_TOKEN = os.environ['FB_ACCESS_TOKEN']
FB_TOKEN ='EAACEdEose0cBAPJEPKret1iySK8r6SNyZAr9ZAeofhR2VQ5l3qyUAqZCbTPbyW4QLNFMM56QhrJ9DaHgRKtlVe6eYdQabzmfW' \
          'GcKYYy1vIDnZCZCnAoRT20dUlRW2YdnpEJ4FRwK5qPAPbwtzhYLF7XfCaQP1IZB7BxAm9ZB6VXX7ZCeg05m1LL4PSZBLUFGVJOEZD'

def setSearchIdsUrl(topic):
    # -2.900771, -79.010230 UCuenca location
    lat = '-2.900771'
    lon = '-79.010230'
    radio = '5000' # en metros
    url = "https://graph.facebook.com/v2.8/search?q=" + topic + "&type=place&center=" + lat + "%2C" + lon + "&" \
          "distance=" + radio + "&access_token=" + FB_TOKEN
    return url

# returns Json given an url
def getData(url):
    webURL = requests.get(url)
    return webURL.json()

def getFirstPage(query):
    # print setSearchIdsUrl(query)
    requests = getData(setSearchIdsUrl(query))
    print(requests)
    if 'error' in requests:
        print(requests['error']['message'])
        return None
    if 'data' not in requests:
        print('No data')
        return None
    # print(requests['data'][0]['name'])
    return(requests['data'][0]['name'])


def getDataPage(query):
    requests = getData(setSearchIdsUrl(query))
    # print(requests)
    if 'data' in requests:
        print('FB.py sent data')
        return(requests['data'])
    elif 'error' in requests and len(requests['data']) > 0:
        print(requests['error']['message'])
        return None
    else:
        print('No data')
        return None

# Gets a page information
# name, location, Overall_star_rationg
def searchPage(pageId):
    url = "https://graph.facebook.com/v2.8/%s?fields=name%2" \
          "Clocation%2Coverall_star_rating&access_token=%s" %(pageId, FB_TOKEN)
    requests = getData(url)
    print(requests)
    if 'name' in requests:
        print('FB.py sent data')
        return(requests)
    elif 'error' in requests:
        print(requests['error']['message'])
        return None
    else:
        print('No data')
        return None


print 'Get FirstPage'
print (getFirstPage('pizza'))
print 'Get DataPage'
print (getDataPage('pizza'))
