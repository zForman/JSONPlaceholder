import pytest

payload = {
  "id": 1,
  "title": "My JSON Server",
  "body": "Fake Online REST server for teams",
  "userId": '12'
}


@pytest.mark.parametrize('payload, expected_status', [(payload, 200)])
def test_put_post(call_api, payload, request, expected_status):
    num_of_post = request.config.getoption('--num_of_post')
    response = call_api.method_put(path=f'/posts/{num_of_post}', data=payload)
    data = response.json()

    assert data == payload
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.status_code == expected_status


def test_delete_post(call_api, request):
    num_of_post = request.config.getoption('--num_of_post')
    response = call_api.method_delete(path=f'/posts/{num_of_post}')
    assert response.request.method == 'DELETE'
