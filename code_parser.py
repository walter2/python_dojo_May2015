import sys
import keyword
import requests

FLIKR_KEY = '8fe93154747a7fc720dbdeffb3831d81'
FLIKR_ENDPOINT = 'https://api.flickr.com/services/rest/'
FLIKR_IMAGE_KEY = 'url_t'

CODE_TEMPLATE = '''
    <div>
        <pre>{code}</pre>
        <strong>{word}</strong>
        <img src="{image_url}"/>
    </div>
'''


def clean_code(code):
    cleaned_code = []
    for line_number, line in code:
        split_code = line.split(' ')
        for word in split_code:
            if word.isalpha() and len(word) >= 3 and word not in keyword.kwlist:
                cleaned_code.append((line, word))
    return set(cleaned_code)


def parse_code(_file):
    with open(_file) as f:
        code = enumerate(f.readlines())
    cleaned_code = clean_code(code)
    for line, word in cleaned_code:
        yield line, word


def get_image_url(keyword):
    if keyword in _image_url_cache:
        return _image_url_cache[keyword]

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
    _image_url_cache[keyword] = url

    return url
_image_url_cache = {}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = __file__

    with open('temp.html', 'w') as f:
        for code, word in parse_code(source_file):
            print(word)
            image_url = get_image_url(word)
            f.write(CODE_TEMPLATE.format(
                code=code,
                image_url=image_url,
                word=word,
            ))
