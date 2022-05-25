from config import config
import json
import pytest
from flask import Blueprint
from faker import Faker
from admin_lead_management.api.app import create_app
from tests.v1.fake_data import fake_data_obj
import io

fake = Faker()

v1_blueprint = Blueprint(name='v1', import_name=__name__)

data_dict = {}

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjUyOTQ1MzQxLCJqdGkiOiJlMmIwOTcxYy1hNmVhLTRlYzEtYjU3MC03Nzc4NTU3NzBlYmYiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiNmU2NDMxMDItMDdhNi00MmVlLThhMDgtYTc0Y2U1ZTkyODNkIiwibmJmIjoxNjUyOTQ1MzQxLCJleHAiOjE2NTI5NDg5NDEsIndvcmtmbG93IjoibG9naW4ifQ.080S4t_rXQ4pWh_h7ghJ9QvCGZwSRnKFeqnh1OvUKeQ"

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.testing = True
    app.config["TEST_DB_URL"] = config.TEST_DB_URL

    with app.test_client() as client:
        yield client


def test_get_all_lead_sources(client):
    """
        List all lead sources
    """
    response = client.get(f"v1/lead-sources/?name=lead-source", headers={"access-token": token})
    assert response.status_code == 200


def test_create_lead_sources(client):
    """
        List all lead sources
    """
    data = {
        "name": fake_data_obj.name[0]
    }
    response = client.post(f"v1/lead-sources/", data=data, headers={"access-token": token})
    assert response.status_code == 200


def test_get_all_lead_statuses(client):
    """
        List all lead statuses
    """
    response = client.get(f"v1/statuses/", headers={"access-token": token})
    assert response.status_code == 200


def test_create_status(client):
    """
        Create a status
    """
    data = {
        "name": fake_data_obj.name[0],
        "role": "admin"
    }
    response = client.post(f"v1/statuses/", data=data, headers={"access-token": token})
    print(response.data, '------------------------')
    assert response.status_code == 200