"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)
    

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, *rest = each_wagons_id
    return [rest[0], *missing_wagons, *rest[1:], a, b]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return route | {'stops': list(stops.values())}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return route | more_route_information


def fix_wagon_depot(*wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[tuple] - the list of rows of wagons.
    :return: list[tuple] - list of rows of wagons.
    """
    row_one, *_ = wagons_rows
    return [list(i) for i in zip(*row_one)]
