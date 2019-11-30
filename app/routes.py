import requests
import json
from app import app
from haversine import haversine

host = "https://bpdts-test-app.herokuapp.com/"

@app.route('/')
@app.route('/index')
def index():
    """
    This is the requested result, when the user hits the index a list of individuals living in or currently within
    50 miles of london will be generated.
    :return: a List of dicts containing the users id, first and last name
    """
    return get_in_radius(50)

@app.route('/health_check')
def health_check():
    return 200, ""

@app.route('/get_in_radius/<radius>')
def get_in_radius(radius):
    """
    Tests to make sure the index page is operational
    :returns String Hello world which is displayed on the landing page
    """
    def _return_values(user):
        """
        :user Dict containing the users information, by keeping this in a nested function if more or less information
        is required to be returned it can be modified in one location rather than multiple locations.
        Returns a predefined dict of values to minimise duplicated code.
        :return: dictionary of user values
        """
        return {"id":user["id"],
                "first_name":user["first_name"],
                "last_name": user["last_name"]
                }

    users_in_range = [] # dictionary to store user information as we only want first name and last name.
    london = (51.30, 0.5) # Create a position point for london using its latitude and longitude

    # ** Note: 'City' is not included in the data returned by the users end point ut it is if you call the
    # users individually i could do this using for loop but that would cause 1000 calls to the API each time
    # the end point is called so instead i've opted to do 2 calls and parsing the data in the API.
    # This should minimise the number of requests being sent to the API.

    # First i will get all the users and compute their current distance from london and checking if that is within
    # the radius specified by the end user (radius component of the url), Then i will get all users listed as being
    # in the city of london and checking if those customers are already in the list by creating a list of ids.

    # If they are in the list they are discarded if they are not then their first name, last name and id are added
    # to the array, since the requirements did not specify what information was to be returned only those three values
    # are returned (This minimises the data protection implications)

    url = "/users"
    response = requests.get(f"{host}{url}")

    for user in json.loads(response.text):
        # Creation location point for the current user and use haversine to compute the distance between the user and
        # london in miles
        user_location = (float(user["latitude"]), float(user["longitude"]))# (lat, lon)
        distance = haversine(london, user_location, unit='mi')

        # if the distance is 50 miles or less then add the users first and last name to the users_in_range dict using
        if distance <= float(radius):
            users_in_range.append(_return_values(user))

    # Get the used defined as 'living in london' this is not clear in the instructions so i have made the 'assumption'
    # That the city value corresponds to their current city of residence.
    url = "/city/London/users"
    response = requests.get(f"{host}{url}")

    # Parse through the list or returned users and filter entries which already exist and append ones that dont to the
    # list to be returned
    for user in json.loads(response.text):
        if not user["id"] in [user["id"] for user in users_in_range]:
            users_in_range.append(_return_values(user))

    # convert the list into a json payload and return using
    return json.dumps(users_in_range)
