
text = """add1 http://mit.edu.com abc
add2 https://facebook.jp.com.2. abc
add3 www.google.be. uvw
add4 https://www.google.be. 123
add5 www.website.gov.us test2
Hey bob on www.test.com. 
another test with ipv4 http://192.168.1.1/test.jpg. toto2
website with different port number www.test.com:8080/test.jpg not port 80
www.website.gov.us/login.html
test with ipv4 192.168.1.1/test.jpg.
search at google.co.jp/maps.
test with ipv6 2001:0db8:0000:85a3:0000:0000:ac1f:8001/test.jpg.
aah gdrive link https://drive.google.com/file/d/1xd-K4cz6e5tdP353P8U-ZFYiQuDkWfVw/view?usp=sharing
https://drive.google.com/file/d/1MUp3ZN4EG1TnGogIeydymBMhkSg5tizP/view?usp=sharing"""

regex= r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"

import re
from furl import furl

matches = re.findall(regex, text)
IDs = [furl(url).path.segments[furl(url).path.segments.index("d")+1] for url in matches \
            if furl(url).host == "drive.google.com"]