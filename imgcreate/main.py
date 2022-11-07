def openloader(what):
    import openai
    import requests
    # Enter ur Api Key Here
    openai.api_key = ''


    var = openai.Image.create(
        prompt=what,
        n=3,
        size='512x512'
    )


    var1 = var['data'][0]
    var2 = var['data'][1]
    var3 = var['data'][2]
    url1 = var1['url']
    url2 = var2['url']
    url3 = var3['url']
    
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    r3 = requests.get(url3)

    with open('static/image1.png',"wb") as f:
        f.write(r1.content)

    r = requests.get(url2)
    with open('static/image2.png',"wb") as f:
        f.write(r2.content)

    r = requests.get(url3)
    with open('static/image3.png',"wb") as f:
        f.write(r3.content)


    