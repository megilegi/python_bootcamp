lista = [1, 2, 3, [4, 5, [6]], 7]

def splaszcz(lista):
    flat_list = []
    for element in lista:
        if type(element) == list:
            for a in element:
                flat_list.append(a)
        else:
            flat_list.append(element)
    return flat_list

print(splaszcz(lista))


# def test_splaszcz():
#     assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == ([1, 2, 3, 4, 5, 6, 7])
jupyter