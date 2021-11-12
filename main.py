from urllib.request import urlopen
from bs4 import BeautifulSoup
#url of the website we want to scrap
urlOneBeingScrapped = ""
#this will open the url that we requested above. A header will need to be added to scrap bigger web app likes
#Amazon
RequestPage = urlopen(urlOneBeingScrapped)
#reading
page_html = RequestPage.read()
#clolsing the request
RequestPage.close
#This will let us pick through the html elements of a website, and its requested
SoupHtml = BeautifulSoup(page_html, "html.parser")

