import requests

FLIKR_KEY = '8fe93154747a7fc720dbdeffb3831d81'
FLIKR_ENDPOINT = 'https://api.flickr.com/services/rest/'
FLIKR_IMAGE_KEY = 'url_t'


def get_image_url(keyword):
    params = {
        'api_key': FLIKR_KEY,
        'extras': FLIKR_IMAGE_KEY,
        'format': 'json',
        'method': 'flickr.photos.search',
        'nojsoncallback': 1,
        'per_page': 1,
        'sort': 'interestingness-desc',
        'text': keyword}
    response = requests.get(FLIKR_ENDPOINT, params)
    url = response.json()['photos']['photo'][0][FLIKR_IMAGE_KEY]
    return url


def parse_code():
    keywords = [('def hello():', 'hello'), ('   python =1 ', 'python'), ('   world = 2', 'world')]
    for keyword in keywords:
        yield keyword


if __name__ == "__main__":
    for code, keyword in parse_code():
        image_url = get_image_url(keyword)
        print('<div><pre>%s</pre><img src="%s"/></div>' % (code, image_url))
