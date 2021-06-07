from .. import app

def test_add():  

    response = app.test_client().get('/')
    assert response.status_code == 200


def test_data():
    response = app.test_client().get('/data')
    print(response.__dict__ )
    assert response.status_code == 200 and \
    response.json == {
                        "age": 30, 
                        "name": "Toto"
                    }
