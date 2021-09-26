from itertools import zip_longest

with open('users.csv', 'r') as f:
    users = f.read().split(',')

with open('hobby.csv', 'r') as f:
    hobby = f.read().split(',')


# if len(users) >= len(hobby):
#     dict_users_hobby = zip_longest(users, hobby, fillvalue='No hoddy')
# else:
#     dict_users_hobby = '1'
#
# with open('users_hobby.txt', 'w') as f:
#     f.write(f'{list(dict_users_hobby)}\n')

with open('users_hobby.txt', 'w') as f:
    for users, hobby in zip_longest(users, hobby):
        if users == None:
            f.write('1')
            break
        else:
            f.write(f'{users} : {hobby}\n')
