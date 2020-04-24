import pytest
from cerberus import Validator

schema = {
    'userId': {'type': 'integer'},
    'id': {'type': 'integer'},
    'title': {'type': 'string'},
    'body': {'type': 'string'}
  }
v = Validator(schema)


@pytest.mark.parametrize('params', [{'userId': '1'},
                                    {'userId': '2'},
                                    {'userId': '3'}])
def test_get_filtering_resources(call_api, params):
    response = call_api.method_get(path='/posts', params=params)
    data = response.json()
    for post in data:
        assert v.validate(post)
