import pytest


def get_title():
    return ['et ea vero quia laudantium autem', 'in quibusdam tempore odit est dolorem',
                       'dolorum ut in voluptas mollitia et saepe quo animi', 'voluptatem eligendi optio',
                       'eveniet quod temporibus',
                       'sint suscipit perspiciatis velit dolorum rerum ipsa laboriosam odio',
                       'fugit voluptas sed molestias voluptatem provident',
                       'voluptate et itaque vero tempora molestiae',
                       'adipisci placeat illum aut reiciendis qui',
                       'doloribus ad provident suscipit at']


@pytest.mark.parametrize('title', get_title())
def test_get_resource(call_api, title):
    response = call_api.method_get(path='/posts')
    data = response.json()
    res_id2 = []
    for i in data:
        if i['userId'] == 2:
            res_id2.append(i['title'])
    assert title in res_id2
