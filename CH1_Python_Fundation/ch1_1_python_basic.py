#In[0]: Arithmetic operation +-*/
print(1-2) # -1
print(4*5) # 20
print(7/5) # 1.4
print(3**2) # 次方 9
print(9%5) # 餘數 4

#In[1]: data type
print(type(10))   # int
print(type(2.14)) # float
print(type('hello world'))  # str
print(type(int(2.14)))  # data type transformer, int

#In[2]: variable
x = 10
y = 1.23
print(x, y)  # 10, 1.23
print(x*y)   # 12.3

#In[3]: list
a = [1,2,3,4,5]
print(a)   # [1,2,3,4,5]
print(len(a))  # List長度, 5
print(a[1])   # 指定index從0開始, 2
print(a[2:])  # index從2開始往後取, [3,4,5]
print(a[-2])  # circle index, 負index從後面開始數, 4

#In[4]: Dictionary
dict = {'height':178, 'wight':65}  # 格式為:'label':data
print(dict)  
print(dict['height'])   # call data

#In[5]: bool type
Happy = [True, True]
Sad = [True, False]
print(type(Happy))
print(Happy and Sad)  # and operation
print(Happy or Sad) # or operation
print(Happy[0]|Sad[0])  # |,& only used for single operation

#In[6]: if/else, 依序條列順序判斷
Happy = True
Sad = True
if Happy:
    print("I am Happy !")
elif Sad:
    print('I am Sad !')
else:
    print('I am confused !')

#In[7]: for loop
for i, data in enumerate(['a','b','c']):  # enumerate 可記錄index並回傳content
    print(i, data)  

#In[8]: function
def add(a, b):    # 輸入值 變數a,b
    return a + b  # 回傳結果
print(add(1,2))  # 3

#In[9]: Script
# 可在終端機進行cammad, cd ~/code_path/
# python ch1_script_temp.py  即可執行

#In[10]: class
class people:
    def __init__(self, height, wight):
        self.h = height
        self.w = wight
    def eat(self, kg):
        self.w += kg
    def jump(self, times):
        self.w -= times
        self.h += times
Sam = people(170, 50)  # init define
print(Sam.w, Sam.h)    # call item, 50, 170
Sam.eat(10)            # call def 
print(Sam.w, Sam.h)    # call item, 60, 170

# %%
