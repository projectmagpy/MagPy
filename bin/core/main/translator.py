import mechanize
import requests
from BeautifulSoup import BeautifulSoup
langs = ["hi", "ml"]
x = raw_input("Enter the word to translate ")
for lang in langs:
    base_url = "https://translate.google.co.in/translate_a/single?client=t&sl=auto&tl=" + lang + "&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&rom=0&ssel=0&tsel=4&tk=518745|178722&q="
    r = requests.get(base_url+x)
    html = r.content

    print html.split(",")[0][4:-1]
