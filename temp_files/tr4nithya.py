import requests

li = open("dict.txt").read().split("\n")
for text in li:
    text = ''.join([i if ord(i) < 128 else ' ' for i in text]).replace(" ", "").lower()
    base_url = "https://translate.google.co.in/translate_a/single?client=t&sl=auto&tl=ml&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&rom=0&ssel=0&tsel=4&tk=518745|178722&q="
    r = requests.get(base_url + text)
    html = r.content.split(",")[0][4:-1]
    print r.content
    print html
    data = text + " : " + html + "\n"
    print data
    open("result.txt", "a").write(data)
