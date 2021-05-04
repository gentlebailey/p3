
from math import pi, exp
from time import time

start = time()
TE=[0,0,0,0]
rho,c,D,TS,TI,V,h = 1.164,1007,0.25,10,50,7,85
L = [3,12,25,50]
m = (rho * pi * D**2 * V)/4
for i in range(0,4):
    A = pi * D * L[i]
    TE[i] = TS - (TS- TI)*(exp((-h*A)/(m*c)))

end = time()
elapsed = end - start
for i in range(0,4):
    print(TE[i])
print('Seconds taken to calculate:', elapsed)
