def parse_code():
    keywords = ['hello', 'python', 'world']
    for keyword in keywords:
        yield keyword


if __name__ == "__main__":
    for k in parse_code():
        print(k)