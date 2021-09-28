#In[0]: import, plot
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0, 6, 0.1) # 從0到6, 以0.1間距單位
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin')  #可設定linestyle, color, label
plt.plot(x, y2, linestyle='-.', color='r', label='cos')
plt.xlabel('x')  # 設定x 軸
plt.ylabel('y')  # 設定y 軸
plt.title('sin & cos')  # 顯示標題
plt.legend()  #顯示label
plt.savefig('./sample.png') #儲存影像
plt.show()

#In[1]: read img
img = plt.imread('./sample.png')
plt.imshow(img)
plt.show()