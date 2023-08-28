import math


def fluid_flow(v, l, n, situation):
    """ (float), (float), (float), (string) -> (string)

    Given the fluid speed (v), characteristic length (l),
    kinematic viscosity (n) and situation, returns the flow type
    """
    flow_condition = ''
    plate_turbulence_value = 5 * 10 ** 5
    rey_num = (v * l)/n
    if situation == "pipe":
        if rey_num < 2000:
            flow_condition = 'laminar'
        elif 2000 <= rey_num <= 4000:
            flow_condition = 'translational'
        elif rey_num > 4000:
            flow_condition = 'turbulent'
        else:
            print('Invalid Input')
            flow_condition = 'NA'
    elif situation == 'plate':
        if rey_num < plate_turbulence_value:
            flow_condition = 'laminar'
        elif rey_num >= plate_turbulence_value:
            flow_condition = 'turbulent'

    else:
        print('Invalid input')
        flow_condition = 'NA'
    return flow_condition


print(fluid_flow(1000, 30, 10, 'pipe'))

