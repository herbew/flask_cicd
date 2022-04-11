# from flask_cicd.apps.homes.tests.controls import app


def test_login_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/login' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/login')
        assert res.status_code == 308



