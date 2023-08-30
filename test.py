from datetime import datetime

def process_iterable(iterable, keys):
    if isinstance(iterable, dict):
        for key in list(iterable.keys()):
            value = iterable[key]
            if isinstance(value, dict):
                process_iterable(value, keys)
            elif isinstance(value, list):
                process_iterable(value, keys)
            elif key in keys and isinstance(value, int):
                try:
                    iterable[key] = datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    pass
    elif isinstance(iterable, list):
        for item in iterable:
            if isinstance(item, dict):
                process_iterable(item, keys)
            elif isinstance(item, list):
                process_iterable(item, keys)
    print(iterable)
    print('-'*100)

# 示例数据
data = {
    'meta': {'version': 1, 'nbTopic': 3},
    'reporter': {'name': 'fc:7f:f1:cd:99:04', 'swBuild': '87765', 'time2': 1693316175},
    'bleData': [
        {'mac': '5a:25:30:71:50:b6', 'frameType': 0},
        {'swBuild': '87765', 'time2': 1693316155, 'birth_date': "1990-05-15"}
    ]
}

keys_to_check = ["time2"]

process_iterable(data, keys_to_check)

print('-'*100)
print(data)