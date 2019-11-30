import requests
import json
from app import app

# Unit Tests to ensure that the API is reachable and that the App is returning data correctly
# because this is a test it assumes that the data in the test environment will not change.
# In production where the database changes over time specific tests would be created with a fixed dataset

bpdts_host = "https://bpdts-test-app.herokuapp.com/"
dwp_api_host = "http://0.0.0.0:5000/"

def test_bpdts_api_available():
    """Tests that the bpdts-test-app is available and the api can communicate with it."""

    url = "/users"
    response = requests.get(f"{bpdts_host}{url}")
    assert response.status_code == 200

def tests_dwp_api_is_available():
    """Tests that the dwp_api is available and we can call the health check end point"""
    url = "/health_check"
    response = requests.get(f"{dwp_api_host}{url}")
    assert response.status_code == 200

def tests_dwp_api_returns_correct_individuals():
    """Again making an assumption that the number of individuals will not change and that this is the expected result"""

    response = requests.get(f"{dwp_api_host}")
    assert response.status_code == 200
    users = json.loads(response.text)
    assert len(users) == 9

def tests_that_radius_and_index_return_same_user_count():
    """The Index landing page should get all users in 50 miles of london so response from both endpoints should be the same"""
    response = requests.get(f"{dwp_api_host}")
    assert response.status_code == 200
    index_users = json.loads(response.text)

    response = requests.get(f"{dwp_api_host}get_in_radius/50")
    radius_users = json.loads(response.text)
    assert len(radius_users) == len(index_users)

if __name__ == '__main__':
    """Main Initializer"""
    app.run(host='0.0.0.0', port=5000)
