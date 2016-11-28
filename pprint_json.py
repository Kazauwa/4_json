import json


def load_data(filepath):
    with open(filepath, 'r') as reader:
        raw_data = reader.read()
    return json.loads(raw_data)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    raw_json = load_data(input('Input path to json file: '))
    pretty_print_json(raw_json)
