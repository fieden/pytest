import os
import pytest

from src import calc

@pytest.fixture
def txt(tmpdir):

    filepath = os.path.join(tmpdir, "numbers.txt")
    with open(filepath, 'w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield filepath


def test_input_numbers(txt):

    assert calc.input_numbers(txt) == [2, 5, 4, 3, 1]


@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True)
])
def test_is_prime(number, expected):

    assert calc.is_prime(number) == expected



# def test_is_prime():
#     assert calc.is_prime(1) is False
#     assert calc.is_prime(2) is True
#     assert calc.is_prime(3) is True
#     assert calc.is_prime(4) is False
#     assert calc.is_prime(5) is True
#     assert calc.is_prime(6) is False
#     assert calc.is_prime(7) is True
#     assert calc.is_prime(8) is False
#     assert calc.is_prime(9) is False
#     assert calc.is_prime(10) is False

# def test_add_num_adn_double():
#     cal = calc.Cal()
#     assert cal.add_num_and_double(1, 1) == 4
