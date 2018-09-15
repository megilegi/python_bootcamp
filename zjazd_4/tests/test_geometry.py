from zjazd_4.mathematica.geometry import square_area, triangle_area


def test_square_area():
    assert square_area(5) == 25


def test_traingle_area():
    assert triangle_area(5, 4) == 10
