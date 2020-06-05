import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from tabulate import tabulate

h = float(input("enter the step size=", ))
x = np.arange(0,1+h,h)
n = len(x)
def solution(t): return np.exp(2)*(np.exp(4)-1)**(-1)*(np.exp(2*t)-np.exp(-2*t))+t

def func(t,y): return np.vstack((y[1], 4*(y[0]-t)))

def bc(ya,yb): return np.array([ya[0],yb[0]-2])

y = np.zeros((2,n))

y[0]=0



sol=solve_bvp(func,bc,x,y)



y_numeric = sol.sol(x)[0]
y_true = solution(x)
percent_error = []
for i in range(n):
    e = ((y_true[i]-y_numeric[i])/(y_numeric[i]))*100
    percent_error.append(abs(e))
index = range(1, len(x)+1)
headers = ['index','x','y_true','y_numeric','percent_error']    
table = zip(index,x,y_true,y_numeric,percent_error)
print(tabulate(table, headers=headers))

plt.plot(x, y_numeric,label="From scipy.integrate solve_bvp ")
plt.plot(x,y_true,"+k",label="Analytic Solution")
plt.title(r'$y=e^{2}(e^{4}-1)^{-1}(e^{2x}-e^{-2x})+x$')
plt.xlabel("$x$")
plt.ylabel("y(x)")
plt.legend()
plt.show()
          




