from base64 import b64encode
from _pytest.fixtures import pytest_fixture_setup
import pytest
from flask import Flask, template_rendered

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture
def page(app):
    pass
