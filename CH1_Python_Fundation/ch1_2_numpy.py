#In[0]: import, define
import numpy as np
x = np.array([1.0, 2.0, 3.0])
print(x)  # [1. 2. 3.]
print(type(x)) # <class 'numpy.ndarray'>

#In[1]: operation
y = np.array([2.0, 4.0, 6.0])
print( x + y )  # [3. 6. 9.]
print( x - y )  # [-1. -2. -3.]
print( x * y )  # element-wise product, [ 2.  8. 18.]
print( x / y )  # [0.5 0.5 0.5]

#In[2]: N-dim array
A = np.array([[1,2],[3,4]])
print(A) 
# [[1 2]
# [3 4]]
print(A.shape)  # (2, 2)
print(A.dtype)  # int64

#In[3]: Broadcast, 針對不同shape會自動補齊數字
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*10) # 10 變成 [[10,10],[10,10]]
# [[10 20]
#  [30 40]]
print(A*B) # Ｂ變成[[10,20],[10,20]]
# [[10 40]
#  [30 80]]

#In[4]: index
X = np.array([[1,2],[1,2]])
X[1][0] = 3
X[1][1] = 4
print(X)  
# [[1 2]
#  [3 4]]
for row in X:  #依序row回傳
    print(row)
# [1 2]
# [3 4]

#In[5]: flatten
X = X.flatten()
print(X)  # [1 2 3 4]

#In[6]: condition
print(X>2) # [False False  True  True]

#In[7]: function
print(X.sum())  # 10
print(X.mean()) # 2.5
print(X.var())  # 1.25
# %%
