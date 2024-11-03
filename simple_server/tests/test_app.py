def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"


def test_get_home_1(web_client):
    response = web_client.get("/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"

