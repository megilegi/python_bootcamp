def add_matrices(a, b):
    try:
        if len(a) == len(b):
            result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
            final_result = []
            for r in result:
                final_result.append(r)
            return final_result
        else:
            return "Matrices not equal!"
    except IndexError:
        e = "IndexError"
        return e


def sub_matrices(a, b):
    try:
        if len(a) == len(b):
            result = [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
            final_result = []
            for r in result:
                final_result.append(r)
            return final_result
        else:
            return "Matrices not equal!"
    except IndexError:
        e = "IndexError"
        return e
