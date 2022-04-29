from flask import jsonify
from db import elevator as db
from helpers import elevator_range


def in_request(floor_number):
    """
    Inputs:
    floor_number - denotates the desired floor to get

    Returns:
    Confirmation if the desired floor is valid to move
    due to restrictions of the elevator.
    Change in the state of the current floor.
    """
    if elevator_range(floor_number):
        return elevator_range(floor_number)

    db["elevator_position"] = floor_number
    return jsonify({"message": "Moving", "elevator": db})


def out_request(floor_number):
    """
    Inputs:
    floor_number - denotates the desired floor to get from outside

    Returns:
    Confirmation if the desired floor is valid to move
    due to restrictions of the elevator.
    Change in the state of the current floor.
    """
    if elevator_range(floor_number):
        return elevator_range(floor_number)

    elif len(db["pending_floors"]) == 0 or floor_number not in db["pending_floors"]:
        db["pending_floors"].append(floor_number)
        return jsonify({"message": "Wait the elevator"})

    elif floor_number in db["pending_floors"]:
        return jsonify({"message": "Already requested, hold your horses"})


def delete_request(floor_number):
    """
    Input: floor number desired to deleted the request

    Output:
    Validation if the floor has been requested and
    elimination of the user request.
    """
    if floor_number in db["pendingFloors"]:
        db["pendingFloors"].remove(floor_number)
        return jsonify({"message": "Use the stairs bitch"})
    else:
        return jsonify({"message": "This floor has not been requested"})
