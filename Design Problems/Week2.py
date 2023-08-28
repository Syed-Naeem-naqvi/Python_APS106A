import math
# Robo-Arm Question: CORRECT


def dual_arm_system_coordinate_conversion(l_1, theta_1, l_2, theta_2):
    """
        (number, number, number, number) -> tuple(number, number)
        Given a robotic arm with two position polar coordinates,
        a set of cartesian coordinates is returned.
    """
    l_1x = l_1 * math.cos(theta_1)
    l_1y = l_1 * math.sin(theta_1)
    l_2x = l_2 * math.cos(theta_1 + theta_2)
    l_2y = l_2 * math.sin(theta_1 + theta_2)
    lx = round((l_1x + l_2x), 10)
    ly = round((l_1y + l_2y), 10)
    coordinates = (lx, ly)
    return coordinates


print(dual_arm_system_coordinate_conversion(1, math.pi/4, 1, math.pi/4))
print(dual_arm_system_coordinate_conversion(1, 0, 1, 0))
print(dual_arm_system_coordinate_conversion(1, math.pi/2, 1, 0))
print(dual_arm_system_coordinate_conversion(0, 0, 0, 0))
print(dual_arm_system_coordinate_conversion(0, math.pi/2, 0, math.pi/2))
print(dual_arm_system_coordinate_conversion(1, 3*math.pi/4, 1, math.pi/2))

ref_th = math.pi/2 - 2*math.pi
# Is the math for reflex angles valid?

print(dual_arm_system_coordinate_conversion(1, math.pi/2, 1, math.pi/2))
print(dual_arm_system_coordinate_conversion(1, ref_th, 1, ref_th))

# Another one1
ref_th2 = math.pi/4 - 2*math.pi

print(dual_arm_system_coordinate_conversion(1, math.pi/3, 1, math.pi/6))
print(dual_arm_system_coordinate_conversion(1, ref_th2, 1, ref_th2))

# Doesn't work for complex numbers of the for a + jb

