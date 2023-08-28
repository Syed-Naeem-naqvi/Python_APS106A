import math as m


def nuclear_reactor_protocol(quake_magnitude, grid_on, reactor_temp, rad_lvl, t_height, reactor_water_lvl, explosion):
    """ (float, bool, float, str, float, str, bool, str) -> str

    : param quake_magnitude: float
    : param grid_on: bool
    : param reactor_temp: float
    : param rad_lvl: str (none, low, high)
    : param t_height: float
    : param reactor_water_lvl: str (low, normal, high)
    : param explosion: bool
    : return status: str (green, yellow, orange, red)
     """
    status = ''

    if quake_magnitude > 8.5 or explosion or reactor_water_lvl == 'low' or reactor_temp >= 1000 or t_height >= 5:
        status = 'red'
    elif 6 < quake_magnitude <= 8.5 or reactor_water_lvl == 'high' or 500 < reactor_temp <= 1000 or 0 < t_height < 5:
        status = 'orange'
    elif 4 <= quake_magnitude <= 6 or not grid_on or 300 <= reactor_temp <= 500 or rad_lvl == 'low':
        status = 'yellow'
    else:
        status = 'green'

    return status


print(nuclear_reactor_protocol(2, False, 250, 'none', 5, 'high', False))
print(nuclear_reactor_protocol(8, True, 500, 'none', 4, 'high', False))

# Try the decision tree (Hard)
























