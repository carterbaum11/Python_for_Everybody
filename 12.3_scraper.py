import re
import ssl
import urllib.request

from bs4 import BeautifulSoup

lst1 = list()
name_lst = list()
url_lst = list()
url1 = input('http://py4e-data.dr-chuck.net/known_by_Kira.html')
url_lst.append(url1)
repeat = input('enter no of repeats:')
position = int(input('enter url position:')) - 1
count = 0

while count < int(repeat):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url_lst[int(count)], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
