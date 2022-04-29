from db import elevator as db
from flask import jsonify


def elevator_range(floor_number):
    """
    Check if the input floor is valid to the elevator's range
    """
    if floor_number > db["number_of_floors"]:
        return jsonify({"message": "Use helicopter"})
    elif floor_number == db["elevator_position"]:
        return jsonify({"message": "You are there"})


def movement():
    """
    Input:
    Current position of the elevator
    Current floors waiting to go
    Check if the elevator has arrived to the pending floor

    Output:
    Return an update of pendingFloors list if the elevator has
    already visited the floor.
    """
    elevator_position = db["elevator_position"]
    pending_floors = db["pending_floors"]

    condition = elevator_position in pending_floors
    if condition:
        return pending_floors.remove(elevator_position)
    print(pending_floors)
