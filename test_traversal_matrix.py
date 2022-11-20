import pytest
import asyncio


from parss_matrix.traversal_matrix import pars_text_matrix, traverse_matrix, get_matrix


PARSED_MATRIX = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
]

TRAVERSED_MATRIX = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70
]

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/' \
             'python-trainee-assignment/main/matrix.txt'


def test_traversal_matrix():
    with open('test_matrix.txt') as file:
        assert pars_text_matrix(file.read()) == PARSED_MATRIX

    assert pars_text_matrix("") == []
    # assert pars_text_matrix('+-----+\n| 1 | 3 |\n+_____+') == []


def test_traverse_matrix():
    output_matrix = []
    traverse_matrix(PARSED_MATRIX, output_matrix)
    assert output_matrix == TRAVERSED_MATRIX


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSED_MATRIX