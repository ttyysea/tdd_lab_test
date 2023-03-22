from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "World"}

def test_GET_hello_Phet():
    name = "Phet"
    url = f"/callname/{name}"
    expected_result = {"hello": name}
    actual_result = client.get(url)
    assert actual_result.status_code == 200
    assert actual_result.json() == expected_result

def test_POST_hello_Jack():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == {"hello": "Jack"}
