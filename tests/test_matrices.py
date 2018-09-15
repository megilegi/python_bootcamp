from mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matrices():
    a = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    b = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    expected = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ]
    assert add_matrices(a, b) == expected


def test_add_matrices_1():
    a = [
        [1, 1, 1],
        [1, 1, 1],

    ]
    b = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    expected = "Matrices not equal!"
    assert add_matrices(a, b) == expected


def test_add_matrices_2():
    a = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1]

    ]
    b = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    expected = "IndexError"
    assert add_matrices(a, b) == expected


def test_sub_matrices():
    a = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    b = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert sub_matrices(a, b) == expected


def test_sub_matrices_1():
    a = [
        [1, 1, 1],
        [1, 1, 1],

    ]
    b = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    expected = "Matrices not equal!"
    assert sub_matrices(a, b) == expected


def test_sub_matrices_2():
    a = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1]

    ]
    b = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]

    ]
    expected = "IndexError"
    assert sub_matrices(a, b) == expected



