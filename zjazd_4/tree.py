import os

dir_content = list(os.scandir(r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4'))


def walk_through_folders(dir_content):
    lista =[]
    for item in dir_content:
        if str(item).count('.') >= 1:
            print(str(item).split('\'')[1])
        else:

    #         lista.append(item)
    # for item in lista:
    #     if str(item).count('.') >= 1:
    #         print(str(item).split('\'')[1])
    #     walk_through_folders(r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4' + '\\' + str(item).split('\'')[1])



