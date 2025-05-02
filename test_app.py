from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to my Flask app!" in response.data

def test_get_data():
    tester = app.test_client()
    response = tester.get('/api/data')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["name"] == "Nishika"
    assert json_data["language"] == "Python"
