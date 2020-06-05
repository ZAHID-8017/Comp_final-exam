import numpy as np
import matplotlib.pyplot as plt
h = float(input("enter the step size=", ))
n = int(1/h)+1
def f1(y1,y2,t):return (32*y1 + 66*y2 + (2/3)*t + (2/3))
	
def f2(y1,y2,t):return (-66*y1 -133*y2 - (2/3)*t - (1/3))


x = np.linspace(0,1,n)
#print('t=', t)
y1 = np.zeros(n)
y2 = np.zeros(n)
y1[0] = 1/3
y2[0] = 1/3

for i in range(0,n-1,1):
    
	k0=h*f1(y1[i],y2[i],x[i])
	l0=h*f2(y1[i],y2[i],x[i])
	
	k1=h*f1(y1[i]+h/2,y2[i]+k0/2,x[i]+l0/2)
	l1=h*f2(y1[i]+h/2,y2[i]+k0/2,x[i]+l0/2)
	
	k2=h*f1(y1[i]+h/2,y2[i]+k1/2,x[i]+l1/2)
	l2=h*f2(y1[i]+h/2,y2[i]+k1/2,x[i]+l1/2)
	
	k3=h*f1(y1[i]+h/2,y2[i]+k2/2,x[i]+l2/2)
	l3=h*f1(y1[i]+h/2,y2[i]+k2/2,x[i]+l2/2)
	
	y1[i+1]=y1[i]+(k0+2*k1+2*k2+k3)/6
	y2[i+1]=y2[i]+(l0+2*l1+2*l2+l3)/6
	
	
	
plt.plot(x,y1,label="y1(t)")
plt.plot(x,y2,label="y2(t)")

plt.xlabel("$t$",)
plt.legend()
plt.show()
