import re

POST_CODE_PATTERN = re.compile('\d\d-\d\d\d')
DATE_PATTERN = re.compile('(\d\d) (\w\w\w) (\d\d\d\d)')
MAIL_PATTERN = re.compile('user-\d\d@email\S*')


with open("input.txt") as f:
    tekst = f.read()
    kody = POST_CODE_PATTERN.findall(tekst)
    daty = DATE_PATTERN.findall(tekst)
    maile = MAIL_PATTERN.findall(tekst)
    print(kody)
    print(daty)
    print(maile)
