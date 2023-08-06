import pytest

from {{ cookiecutter.project_slug }}.example import example_generator


@pytest.fixture
def list_of_some_primes():
    return [2, 3, 5, 7, 11, 13, 17, 19]


def test_example_generator(list_of_some_primes):
    assert list(example_generator(list_of_some_primes)) == list_of_some_primes
