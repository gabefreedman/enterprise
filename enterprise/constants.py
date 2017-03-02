#constants.py
"""Declares physical constants for use in enterprise.
Depends on numpy for base mathematical constants, and
scipy.constants for physical constants.
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import numpy as np
import scipy.constants as sc


# mathematical constants from numpy
# the log constants are useful for converting between log base 10 and e
pi = np.pi
e = np.e
log10e = np.log10(np.e)
ln10 = np.log(10.)

# physical constancts in mks
c = sc.speed_of_light
G = sc.gravitational_constant
h = sc.Planck

# astronomical times in sec (and frequencies in Hz)
yr = sc.Julian_year
fyr = 1. / yr

# astronomical distances in meters
AU = sc.astronomical_unit
ly = sc.light_year
pc = sc.parsec
kpc = pc * 1.e3
Mpc = pc * 1.e6
Gpc = pc * 1.e9

# other useful conversions in mks
erg = sc.erg
