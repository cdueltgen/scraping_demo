from pyquery import PyQuery
import requests

def readfile(filename):
    html = open(filename, 'r').read()
    jquery = PyQuery(html)
    return jquery

def readsite(address):
    jquery = PyQuery(url=address)
    return jquery

def get_link_text(html):
    for addr in html('a'):
        print html(addr).text()

def print_tweets(twitter_html):
    for tweet in twitter_html('p'):
        print twitter_html(tweet).text()

twitter_url = "https://twitter.com/lizthedeveloper"
twitter = PyQuery(url=twitter_url)

cl_url = "http://sfbay.craigslist.org/"
moto_url = "http://sfbay.craigslist.org/search/?areaID=1&subAreaID=&query=suzuki+sv650&catAbb=sss"

local = readfile("index.html")
cl = readsite(cl_url)
moto = readsite(moto_url)