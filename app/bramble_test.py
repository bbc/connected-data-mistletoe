import base64
import json
import os
import pytest

import bramble

@pytest.fixture
def client():
    bramble.app.testing = True
    return bramble.app.test_client()

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200
