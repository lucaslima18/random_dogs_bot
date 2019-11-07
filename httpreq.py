import requests, re

def get_url():
    '''
    Get an url of a random image of a dog 
    '''
    contents = requests.get('https://random.dog/woof.json').json()

    url = contents['url']

    return url