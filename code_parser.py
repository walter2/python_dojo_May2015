import keyword


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


if __name__ == "__main__":
    for k in parse_code('code_parser.py'):
        print(k)