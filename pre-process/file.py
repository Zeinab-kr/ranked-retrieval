import json


def open_json(path):
    file = open(path, 'r')
    data = json.load(file)
    file.close()
    return data


def read_file(path):
    file = open(path, 'r')
    data = file.read()
    file.close()
    return data


def write_file(path, data):
    file = open(path, 'w', encoding='utf-8')
    file.write(data)


def write_json(path, data):
    file = open(path, "w", encoding='utf-8')
    json.dump(data, file)
