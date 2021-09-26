"""
 Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
 — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
"""
from collections import Counter
import requests

# url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# r = requests.get(url)

# with open('logs.txt', 'w') as f:
#     f.writelines(r.text)

list_result = []
list_id = []
with open('logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        content = f.readline().split()
        list_id.append(content[0])
        list_result.append((content[0], content[5][1:], content[6]))
print(*Counter(list_result).most_common(3), sep='\n')
print('-' * 20)
print(Counter(list_id).most_common(1))
# print(*list_result, sep='\n')
# print(*list_id, sep='\n')
print('-' * 20)

my_dict = {i: list_id.count(i) for i in list_id}
for key, values in my_dict.items():
    if values == max(my_dict.values()):
        print(f'{key}: {values}')



