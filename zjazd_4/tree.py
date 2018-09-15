import os

dir_content = list(os.scandir(r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4'))

for item in dir_content:
    if str(item).count('.') >= 1:
        print(str(item).split('\'')[1])
    else:
        dir_content = list(os.scandir(r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4' + '\\' + str(item).split('\'')[1]))
        for x in dir_content:
            print(x)