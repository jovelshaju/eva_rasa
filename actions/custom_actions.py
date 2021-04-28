import os
import webbrowser

# url='https://www.google.com'
# path="C:\Program Files\Mozilla Firefox\firefox.exe"
# webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(path))
# #webbrowser.get('firefox').open_new_tab(urL)
# webbrowser.open_new_tab(url)

site_links = {
    "google" : "https://www.google.com",
    "wikipedia" : "www.wikipedia.org",
    "youtube" : "www.youtube.com",
}

firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe"

def OpenSite(url):
    webbrowser.open(url)
    print('Hello World')