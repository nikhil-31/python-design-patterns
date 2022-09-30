# function to download a file from a url
import urllib.request
import urllib.parse

def download(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except:
        return None

