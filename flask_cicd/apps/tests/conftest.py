import pytest
from run import app as flask_app

@pytest.fixture(scope='session')
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()