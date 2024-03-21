import numpy as np
a,b=np.array([[3,1],[1,0]]),np.array([[2,2],[1,2]])
c=np.dot(a,b)
print(c)
print(c==np.matmul(a,b))