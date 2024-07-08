from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args: dict) -> list[dict]:
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
 
    # Implement search here!
    search_results = [] # empty list
    
    # check if the query has age
    # if it does then change change the type to int
    if args.get('age'):
        args['age'] = int(args['age'])
    
    # loop through each users
    for user in USERS:
        # loop through each query
        for key in args.keys():
            if user not in search_results:
                append_to_list(key, args, user, search_results)

    if search_results:
        return sort_search(args, search_results)

    # if none of check are passed, return all users
    return USERS

def sort_search(args: dict, search_results: list[dict]) -> list[dict]:
    """Bonus Challenge
    
    sorting method is linear and loops through the arguments
    where the args' positioning (e.g {'id': '5', 'name': 'Joe', 'age': 30, 'occupation': 'Arc'})
    will be the basis of sorting priority.
    
    [1] anything that matches 'id 5' will be appended first, 
    [2] then next those who have substring of 'Joe'
    [3] then those who have age in between/tolerance of -1 and 1 
    [4] then lastly, check the substring occurence of 'Arc'
    """
    sort_result = []
    
    for key in args.keys():
        for user in search_results:
            if user not in sort_result:
                append_to_list(key, args, user, sort_result)
    
    return sort_result

def append_to_list(key, args: dict, user: dict, target_list: list) -> None:
    """Function to catch exception and append the user to target list
        under specific circumstances.
    """
    try:
        if args[key] in user[key]:
            target_list.append(user)
    except TypeError:
        if args['age'] - 1 <= user['age'] <= args['age'] + 1:
            target_list.append(user)