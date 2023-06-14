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
