import numpy as np
import matplotlib.pyplot as plt
print("Vvedite const 'r'")
r=float(input())
print("Vvedite const 'y'")
y=float(input())
def Pervoe(c,r):
    return c*r
def Vtoroe(c,r,y):
    return c*np.power(r,y)
x=np.arange(10)
plt.subplot(3,1,1)
plt.plot(x,Pervoe(x,r),color='green')
plt.title('Логарифмическое')
plt.xlabel('c')
plt.ylabel("s")
plt.grid()
plt.subplot(3,1,3)
plt.plot(x,Vtoroe(x,r,y),color='red')
plt.title('Степенное')
plt.xlabel('c')
plt.ylabel("s")
plt.grid()
print('Готово')
plt.show()