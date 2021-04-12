import numpy as np 
import math
from lec_3_constants import g
from lec_3_constants import e
from lec_3_constants import k
from lec_3_constants import h
V1=g*100*(np.tan(30))**2
V2=2*(np.cos(60))**2*(1-np.tan(60)*np.tan(30))
V=(V1/V2)**(1/2)
print(V)
E=300.0
T=200.0
N=2*h*pow(e,-E/(k*T))*E**(T/2)/((3.14)**(1/2)*(k*T)**(3/2))
print(N)