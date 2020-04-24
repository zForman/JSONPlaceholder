import pytest

payload = {
  "userId": '12',
  "id": 101,
  "title": "My JSON Server",
  "body": "Fake Online REST server for teams"
}


@pytest.mark.parametrize('payload, expected_status', [(payload, 201)])
def test_create_post(call_api, payload, expected_status):
    response = call_api.method_post(path='/posts', data=payload)
    data = response.json()
    assert data == payload
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.status_code == expected_status
