import re

""" 1. Написать функцию email_parse(<email_address>),
    которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
    и возвращает их в виде словаря. 
    Если адрес не валиден, выбросить исключение ValueError
    Например: 
    >>> email_parse('someone@geekbrains.ru') {'username': 'someone', 'domain': 'geekbrains.ru'} """



def email_parse(*args, **kwargs): # можно и предложение в котором имеется email адрес
    try:
        email = re.search("([^@|\s]+@[^@]+\.[^@|\s]+)", *args, **kwargs)
        email = email.group()
        pattern = re.search(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}", email) # регулярка для email адреса

    except AttributeError as e:
        print(f'email адреса не обнаружено!:   AttributeError: {e}')
    else:
        email_parse_dict ={}
        email_parse_dict.setdefault('username', pattern.group(0).split('@')[0])
        email_parse_dict.setdefault('domain', (pattern.group(0).split('@')[1]).split('.')[1])
        return email_parse_dict



print(email_parse('aaaa@xxxxx.com'))
print(email_parse('Hello ABCD, here is my mail id examp@leme.com'))

# {'username': 'aaaa', 'domain': 'com'}
# {'username': 'examp', 'domain': 'com'}