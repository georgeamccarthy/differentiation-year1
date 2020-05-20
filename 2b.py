import numpy as np
import matplotlib.pyplot as plt

# set N
N = 10000
m = 1 # we only need J1(x) in the program, so it can be defined globally.
wavelength = 600 * 10**-9 # approximately the wavelength of visible light

def integrand(theta, x):
    return np.cos(m*theta - x*np.sin(theta))

# integrates the integrand using the trapezium rule
def trapezium(a, b, x):
    area = 0
    h = (b-a)/N
    for n in range(0, N):
        area = area + (h * ((integrand(h*n, x) + integrand(h*(n+1), x)) / 2))
    return area

#bessel function for m = 1 at x
def J(x):
    return 1/np.pi * trapezium(0, np.pi, x)

# calculates intensity at r in terms of I0
def intensity(r):
    I0 = 1
    x = (1/10 *np.pi * (1/wavelength) * (r*10**-6))
    return I0 * (2*J(x)/x)**2

J1 = [0]*26
I = [0]*26

# loops through i values from r = 0 to r = 25 micrometers
for r in range(0, 25+1):
    if r == 0:
        I[r] = 1 # the sinc function is 1 and x = 0, 
        # doing it manually aboids a division by zero error.
    else:
        I[r] = intensity(r)

# plots intensity against r
plt.plot(np.linspace(0, 25, 25+1), I)
plt.ylabel('Intensity(r)')
plt.xlabel('r (um)')
plt.xlim(0, 25)
plt.ylim(0,1)
plt.axhline(y=0, color='k', linewidth=1)
plt.axvline(x=0, color='k', linewidth=1)