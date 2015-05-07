import keyword
import requests

FLIKR_KEY = '8fe93154747a7fc720dbdeffb3831d81'
FLIKR_ENDPOINT = 'https://api.flickr.com/services/rest/'
FLIKR_IMAGE_KEY = 'url_t'

def clean_code(code):
    cleaned_code = []
    for line_number, line in code:
        split_code = line.split(' ')
        for word in split_code:

            if word.isalpha() and len(word) >= 3 and word not in keyword.kwlist:
                cleaned_code.append((line_number, word))
    return set(cleaned_code)


def parse_code(_file):
    with open(_file) as f:
        code = enumerate(f.readlines())
    cleaned_code = clean_code(code)
    for keyword in cleaned_code:
        yield keyword



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


if __name__ == "__main__":
    for k in parse_code('code_parser.py'):
        image_url = get_image_url(keyword)
        print('<div><pre>%s</pre><img src="%s"/></div>' % (code, image_url))