import json


def load_data(filepath):
    with open(filepath, 'r') as reader:
        data = reader.read()
    return json.loads(data)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    data = load_data(input('Input path to json file: '))
    pretty_print_json(data)
