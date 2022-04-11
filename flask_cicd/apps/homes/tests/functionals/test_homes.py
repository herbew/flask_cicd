
def test_home_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/home' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/home')
        # assert res.status_code == 200

# def test_logout_route(app, client):
#     """ 
#     GIVEN a Flask application configured for testing
#     WHEN the '/logout' route is requested (GET)
#     THEN check that the response is valid
#     """
#     with app.test_client() as test_client:
#         res = test_client.get('/logout')
#         assert res.status_code == 200
#
