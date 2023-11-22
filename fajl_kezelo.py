# fajl_kezelo_py


def fajlbeolvasas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def fajlmentes(file_path, content, encoding='utf-8'):
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(content)

def fuzes(file_path, content, encoding='utf-8'):
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(content)
