"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    if "https://" in url:
        url = url[8:]
    if "http://" in url:
        url = url[7:]
    if "www" in url:
        url = url[4:]
    counter = 0
    index = None
    for idx, char in enumerate(url):
        if char == "." and counter == 0:
            counter =+ 1
            index = idx
    return url[0:index]
