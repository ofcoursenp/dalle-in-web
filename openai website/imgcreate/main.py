def openloader(what):
    import openai
    import requests
    # Enter ur Api Key Here
    openai.api_key = ''


    var = openai.Image.create(
        prompt=what,
        n=1,
        size='512x512'
    )

    vard = var['data'][0]
    url = vard['url']

    r = requests.get(url)
    with open('static/image.png',"wb") as f:
        f.write(r.content)

