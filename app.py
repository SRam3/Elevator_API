from flask import Flask, jsonify
from db import elevator as db
from request import in_request, out_request, delete_request
from helpers import movement

app = Flask(__name__)

# Begin
@app.route("/")
def welcome():
    """Initial route"""
    return jsonify({"message": "Welcome to the elevator"})


# State of elevator
@app.route("/elevator")
def get_floors():
    """Obtain the number of floors and prints where's the elevator"""
    if movement():
        return movement()
    return jsonify({"elevator": db, "message": "Number of floors beginning from 0"})


# Move the elevator between floors from inside
@app.route("/elevator/<int:floor_number>", methods=["PUT"])
def in_elevator(floor_number):
    """
    Input:
    floor_number - desired floor to move from inside the elevator

    Returns:
    Message to confirm the movement or reject the action
    """
    return in_request(floor_number)


# Request the elevator from outside
@app.route("/elevator/<int:floor_number>", methods=["POST"])
def out_elevator(floor_number):
    """
    Input:
    floor_number - desired floor to move from outside the elevator

    Returns:
    Message to confirm the movement or reject the action
    """
    return out_request(floor_number)


# Using stairs
@app.route("/elevator/<int:floor_number>", methods=["DELETE"])
def use_stairs(floor_number):
    """
    Input:
    floor_number - delete a request to prevent movement of the elevator

    Output:
    Message to confirm the request deleted
    """
    return delete_request(floor_number)


if __name__ == "__main__":
    app.run(debug=True)