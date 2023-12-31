##############################
# APS106 Winter 2022 - Lab 2 #
##############################

###########################################
# PART 1 - Cartesian to Polar Coordinates #
###########################################
import math


def magnitude(x, y):
    """
    (float,float) -> float
    
    Function calculate the magnitude of a 2D vector. The x-and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the magnitude of the vector as a float.
    
    >>> magnitude(10.0,25.5)
    27.391
    
    >>> magnitude(0.0,0.0)
    0.0
    
    >>> magnitude(10.2,63.2)
    64.018
    
    >>> magnitude(-11.3, -3.9)
    11.954
    
    """
    mag = math.sqrt(x**2 + y**2)
    mag = round(mag, 3)
    return mag

    # TODO: YOUR CODE HERE


# TODO: Write your test code for magnitude here - MAKE SURE YOU DELETE THESE LINES BEFORE SUBMITTING


# Write test cases above this line, DELETE EVERYTHING UP TO THIS LINE BEFORE SUBMITTING

def phase(x, y):
    """
    (float,float) -> float
    
    Function calculates the phase angle of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the phase angle in radians as a float.   
    
    >>> phase(10.0,25.5)
    1.197
    
    >>> phase(0.0,0.0)
    0.0
    
    >>> phase(10.2,63.2)
    1.411
    
    >>> phase(-11.3, -3.9)
    -2.809
    
    """
    
    # TODO: YOUR CODE HERE
    theta = math.atan2(y, x)
    theta = round(theta, 3)
    return theta


print(phase(-25.1, -30.712))

# TODO: Write your test code for phase here - MAKE SURE YOU DELETE THESE LINES BEFORE SUBMITTING

# Write test cases above this line, DELETE EVERYTHING UP TO THIS LINE BEFORE SUBMITTING


###########################################
# PART 2 - Particle Position Calculation  #
###########################################


def particle_position(q, E, m, t, L):
    """
    (float,float,float,float,float) -> float
    
    Function calculates the horizontal position of a charged particle
    within a electrostatic precipitator.
    Input parameters:
        q - charge of the particle in nanocoulombs
        E - electric field strength in kilonewtons/coulomb
        m - mass of particle in nanograms
        t - time since the particle entered the precipitator in microseconds
        L - the distance between the parallel plate electrodes in centimetres
        
    Returns the height of the particle in centimetres
    
    >>> particle_position(0,150,9.2,3.6,5.0)
    2.5
    
    >>> particle_position(2.3,150,9.2,26.8,5.0)
    3.847
    
    >>> particle_position(-2.3,160,9.2,36.8,5.0)
    0.0
    
    """

    # TODO: Write your solution here
    p_init = L/2
    p_t = (1/20000)*((q*E)/m)*t**2 + p_init
    p_t = round(p_t, 3)
    true_p_t = float(max(p_t, 0)) and float(min(p_t, 5))
    return true_p_t

# TODO: Write your test code for particle_height here - MAKE SURE YOU DELETE THESE LINES BEFORE SUBMITTING


# Write test cases above this line, DELETE EVERYTHING UP TO THIS LINE BEFORE SUBMITTING


if __name__ == '__main__':
    import doctest
    doctest.testmod()


