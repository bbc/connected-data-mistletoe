import base64
import json
import os
import pytest

import rubus

@pytest.fixture
def client():
    rubus.app.testing = True
    return rubus.app.test_client()

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200
