import pytest
import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def method_get(self, path='/', params=None):
        url = self.base_url + path
        return requests.get(url=url, params=params)

    def method_put(self, path='/', data=None):
        url = self.base_url + path
        return requests.put(url=url, data=data)

    def method_post(self, path='/', data=None):
        url = self.base_url + path
        return requests.post(url=url, data=data)

    def method_delete(self, path='/'):
        url = self.base_url + path
        return requests.delete(url=url)


def pytest_addoption(parser):
    parser.addoption('--base_url',
                     default='https://jsonplaceholder.typicode.com')

    parser.addoption('--num_of_post',
                     choices='1',
                     help='Which post should we remove',
                     default=1)


@pytest.fixture
def call_api(request):
    base_url = request.config.getoption('--base_url')
    return APIClient(base_url=base_url)
