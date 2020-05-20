import numpy as np
import matplotlib.pyplot as plt

# set N
N = 10000

# the function to be integrated
def integrand(theta, m, x):
    return np.cos(m*theta - x*np.sin(theta))

# this function returns an integral using the trapezium rule
def trapezium(a, b, m, x):
    area = 0
    h = (b-a)/N
    for n in range(0, N):
        area = area + (h * ((integrand(h*n, m, x) + integrand(h*(n+1), m, x)) / 2))
    return area

# the bessel function for a specified m and x value
def J(m, x):
    return 1/np.pi * trapezium(0, np.pi, m, x)

# define empty arrays to contain bessel function at various x-values later
J0 = [0]*21
J1 = [0]*21
J2 = [0]*21

#m = 0
for x in range(0, 20+1): # 20+1 because range is not inclusive at the upper end
    J0[x] = J(0, x) # fills the array with the bessel function at each x-value between 0 and 20

#m = 1
for x in range(0, 20+1):
    J1[x] = J(1, x)

#m = 2
for x in range(0, 20+1):
    J2[x] = J(2, x)

# plot each bessel function on the same graph
plt.plot(np.linspace(0, 20, num=21), J0, 'ro-', label='m = 0')
plt.plot(np.linspace(0, 20, num=21), J1, 'go-', label='m = 1')
plt.plot(np.linspace(0, 20, num=21), J2, 'bo-', label='m = 2')

plt.axhline(y=0, color='k', linewidth=1) # x-axis line
plt.xlim(0, 20)
plt.xlabel('$x$')
plt.ylabel('$J_m(x)$')
plt.legend()

