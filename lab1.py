import math
s=0
x=0.1
eps=0.01
fakt=1
i=1
z1=1
z=1
while math.fabs(z)>eps:
    s=s+z
    fakt=fakt*i
    z1=z1*x
    z=z1/fakt
    i=i+1
print('S=',s)