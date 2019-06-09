import requests
import json
import xmltodict
import configparser
import goodreads_api_client as gr

config = configparser.ConfigParser()
config.read("config.ini")

googleAPI = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
goodreadsAPI = "https://www.goodreads.com/book/isbn/"
goodreadskey = "?key=" + config['GoodreadsAPI']['Key']

def handleGoogleRequest(url):
    request = googleAPI + url
    response = requests.get(request)
    obj = response.json()

    return obj

def handleGoodReadsRequest(url):
    request = goodreadsAPI + url + goodreadskey
    response = requests.get(request)
    book = xmltodict.parse(response.text)['GoodreadsResponse']['book']
    keys_wanted = ['id', 'title', 'isbn']
    reduced_book = {k:v for k, v in book.items() if k in keys_wanted}

    return reduced_book

def main():
    isbn = input("Enter ISBN: ").strip()
    result = handleGoogleRequest(isbn)
    grResult = handleGoodReadsRequest(isbn)
    
    print("Google API: ", result)
    print("Goodreads API: ", grResult)

main() 