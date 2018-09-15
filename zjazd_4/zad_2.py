import sys

file = sys.argv[1]
assert file == r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4\logs.txt', 'Zły plik!'

users = {}
with open(file, 'r') as f:
    for line in f:
        user = line.split(';')[0]
        time = int(line.split(';')[2])
        log = line.split(';')[1]

        if user in users:
            if log == 'LOGOUT':
                users[user] += time
            if log == 'LOGIN':
                users[user] -= time
        else:
            users.update({user: -time})


s_dict = sorted(users.items(), key=lambda x: x[1], reverse= True)
# users = list(users)
#s_dict = users.sort(key=lambda x: x[1])

for k, v in s_dict:
    print(f'{k}:{v} s')
