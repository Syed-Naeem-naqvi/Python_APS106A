def beam_deflection(P, a, E, I, l):
    """
        (number, number, number, number, number) => (number) <- type contract
        Given force, distance to force, young's modulus, 2nd moment of area, and length,
        calculates the maximum deflection of the beam.
    """
    del_max = ((P*a**2)/(6*E*I))*(3*l-a)
    return del_max


deflection = beam_deflection(100, 6, 2.0685e11, 0.005208, 13)
print(deflection)

