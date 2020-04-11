import pytest
import os


@pytest.fixture(scope='session')
def get_file():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    def _get_file(fn):
        return '{}/tests/data/{}'.format(test_dir, fn)
    return _get_file


@pytest.fixture(scope="function", autouse=True)
def output_cleanup(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('-----------------')