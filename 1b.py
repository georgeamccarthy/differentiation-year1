import numpy as np

# define physical constants and measurements
G = 6.6741 * 10**-11 # gravitation constant in m3kg-1s-2
M = 5.9722*10**24 # mass of the earth in kg
m = 7.3420*10**22 # mass of the moon in kg
R = 3.8440 * 10**8 # earth-moon distance in m
w = 2.6617*10**-6 # angular velocity in radians per second

# this function returns the value of the expression in part 1 a).
def polynomial(x):
    return G*M*(x**-2) - G*m*(R - x)**-2 - x*w**2

# returns the derivitative of a polynomial using the secand method
def secantmethod(x1, x2):
    return x2 - (polynomial(x2)*(x2 - x1))/(polynomial(x2)-polynomial(x1))

precision = 6 # ~ the number of decimal places needed
done = False
# make guesses for x1 and x2. A newton raphson search could be made for the first value
# but using a guess here is simpler and fast.
x1 = 10000
x2 = x1 * 2
x3 = 0

# continually looks for a more precise derivative until 
# one of the required precision is found.
while True:
    x3 = secantmethod(x1, x2)
    if np.abs(polynomial(x3)) < 1/10**precision:
        break
    x1 = x2
    x2 = x3


print('L1: {} m'.format(int(np.round(x3, -4)))) #rounds and prints L1

