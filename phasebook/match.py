import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1: list, fave_numbers_2:list) -> bool:
    # set to fast track of exisitng numbers for fave_numbers_2
    fave_map1 = set(fave_numbers_1)
    # loop through fave numbers 2
    for num in fave_numbers_2:
        # res is false unless there is always a match
        res = False
        # check if there is a match between fave numbers 1 and 2
        if num in fave_map1:
            # always overwrite the res if there is a match
            # this will make sure that until the end of loop
            # the res will always be true
            res = True
    
    # return the current overall match status
    return res