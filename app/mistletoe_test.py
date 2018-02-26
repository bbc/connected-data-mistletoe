import base64
import json
import os
import pytest

import mistletoe

@pytest.fixture
def client():
    mistletoe.app.testing = True
    return mistletoe.app.test_client()

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200
