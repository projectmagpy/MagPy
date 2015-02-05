import requests
from BeautifulSoup import BeautifulSoup


def translate(text, langid=0):
    langs = ["hi", "ml",  "ru"]
    if langid != -1:
        lang = langs[langid]
        base_url = "https://translate.google.co.in/translate_a/single?client=t&sl=auto&tl=" + lang + "&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&rom=0&ssel=0&tsel=4&tk=518745|178722&q="
        r = requests.get(base_url + text.replace(" ", "+"))
        html = r.content
        return html
        result = html.split(",")[0][4:-1]
        return result
    else:
        result = ""
        for lang in langs:
            base_url = "https://translate.google.co.in/translate_a/single?client=t&sl=auto&tl=" + lang + "&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&rom=0&ssel=0&tsel=4&tk=518745|178722&q="
            r = requests.get(base_url + text.replace(" ", "+"))
            html = r.content
            result += html.split(",")[0][4:-1] + "\n"
        return result



if __name__ == '__main__':
    print translate(text=raw_input("enter text "), langid=-1)


